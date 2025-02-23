# Chess Piece Randomizer for ESP32-S2 Mini

## Description

This project implements a chess piece randomizer using an ESP32-S2 Mini board and an ST7735R display. It's designed to replace a traditional dice in a dice chess game, randomly displaying chess pieces on the screen when activated.

## Features

- Displays random chess pieces on an ST7735R 128x128 pixel display
- Uses a button input to trigger new random piece selection
- Smooth animation effect when changing pieces
- Configurable for different chess pieces

## Hardware Requirements

- ESP32-S2 Mini board
- ST7735R display (128x128 pixels)
- Push button connected to IO0
- Appropriate connections for SPI communication

## Software Dependencies

- CircuitPython
- Adafruit CircuitPython libraries:
  - adafruit_imageload
  - adafruit_st7735r

## Installation

1. Install CircuitPython on your ESP32-S2 Mini board.
2. Copy the following files to your board:
   - `code.py` (main script)
   - `data/` directory containing chess piece images:
     - pawn.jpg
     - rook.jpg
     - knight.jpg
     - bishop.jpg
     - queen.jpg
     - king.jpg

## Usage

1. Power on the ESP32-S2 Mini board.
2. The display will show a random chess piece on startup.
3. Press the button connected to IO0 to display a new random chess piece.

## Customization

- Modify the `chess_pieces` dictionary in `code.py` to change the available pieces or their corresponding image files.
- Adjust the `WIDTH` and `HEIGHT` constants if using a different size display.

## Pin Configuration

- SPI Clock: IO7
- SPI MOSI: IO11
- TFT CS: IO5
- TFT DC: IO3
- TFT Reset: IO9
- Button: IO0

## Troubleshooting

- Ensure all image files are present in the `data/` directory.
- Check that all required libraries are installed and up to date.
- Verify hardware connections, especially for the display and button.

## Contributing

Contributions to improve the project are welcome. Please feel free to submit issues or pull requests on the project's repository.

## Image Attributions

The chess piece images used in this project are derived from Wikimedia Commons. These images have been modified to fit the resolution of the ST7735R display used in this project. Detailed attribution information for each image, including original creators, sources, and licenses, can be found in the [ATTRIBUTIONS.md](./ATTRIBUTIONS.md) file in this repository.

Please note that the images are licensed under Creative Commons Attribution-Share Alike licenses (CC BY-SA 3.0 and CC BY-SA 4.0). As per the terms of these licenses, any distribution of this project must be under the same or compatible license terms. For more details on how this affects the overall project licensing, please refer to the [LICENSE](./LICENSE) file.

## License

This project is licensed under the MIT License. The full license text can be found in the [LICENSE](./LICENSE) file.
