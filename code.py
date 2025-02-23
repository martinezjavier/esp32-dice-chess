"""
This module allows to show random chess pieces on an ST7735R display, when
driven by an ESP2 S2 Mini board. The goal is to be used instead of a dice
in a dice chess game.
"""

# Copyright (c) 2025 Javier Martinez Canillas
# SPDX-License-Identifier: MIT

import random
import time

# pylint: disable=E0401

import board
import busio
import digitalio
import displayio
import fourwire

import adafruit_imageload
import adafruit_st7735r

WIDTH = 128
HEIGHT = 128

button = digitalio.DigitalInOut(board.IO0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(board.IO7, MOSI=board.IO11)

tft_cs = board.IO5
tft_dc = board.IO3

display_bus = fourwire.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.IO9)

display = adafruit_st7735r.ST7735R(display_bus, width=WIDTH, height=HEIGHT, colstart=2, rowstart=1)

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
        if button.value is False:
            group = create_background()
            show_random_piece(group)
        else:
            time.sleep(0.1)
