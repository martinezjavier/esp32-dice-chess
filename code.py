"""
This module allows to show random chess pieces on an ST7789V display, when
driven by an T-Display-S3 board. The goal is to be used instead of a dice
in a dice chess game.
"""

# Copyright (c) 2025 Javier Martinez Canillas
# SPDX-License-Identifier: MIT

import random
import time

# pylint: disable=E0401

import board
import digitalio
import displayio

import adafruit_imageload

WIDTH = 320
HEIGHT = 170

button0 = digitalio.DigitalInOut(board.BUTTON0)
button0.direction = digitalio.Direction.INPUT
button0.pull = digitalio.Pull.UP

button1 = digitalio.DigitalInOut(board.BUTTON1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

display = board.DISPLAY

chess_pieces = {
    0: "data/bishop.jpg",
    1: "data/king.jpg",
    2: "data/knight.jpg",
    3: "data/pawn.jpg",
    4: "data/queen.jpg",
    5: "data/rook.jpg"
}

def create_background():
    """
    Creates and returns a background display group.

    Returns:
        displayio.Group: A group containing the background sprite.
    """
    bg_group = displayio.Group()
    display.root_group = bg_group

    background = displayio.Bitmap(WIDTH, HEIGHT, 1)
    background_palette = displayio.Palette(1)
    background_palette[0] = 0xFFFFFF
    background_sprite = displayio.TileGrid(background, pixel_shader=background_palette)

    bg_group.append(background_sprite)

    return bg_group

def show_random_piece(display_group):
    """
    Displays random chess pieces on the given display group.

    Args:
        display_group (displayio.Group): The group to which the chess piece images will be added.
    """
    for i in range(30):
        number = random.randint(0, len(chess_pieces) - 1)
        file = chess_pieces[number]

        try:
            image, palette = adafruit_imageload.load(file)
        except Exception as e:
            raise SystemExit(f'Could not load image "{file}": {str(e)}') from e

        tile_grid = displayio.TileGrid(image, pixel_shader=palette)

        x = (display.width - image.width) // 2
        y = (display.height - image.height) // 2

        image_group = displayio.Group(x=x, y=y)
        image_group.append(tile_grid)

        display_group.append(image_group)

        display.refresh()
        time.sleep(0.0001 * i)

if __name__ == "__main__":

    group = create_background()
    show_random_piece(group)

    while True:
        if button0.value is False:
            group = create_background()
            show_random_piece(group)
        else:
            time.sleep(0.1)

        if button1.value is False:
            display.brightness = not display.brightness
            time.sleep(0.5)
