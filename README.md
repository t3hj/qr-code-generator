# QR Code Generator 🖼️

Welcome to the QR Code Generator! This project allows you to create customized QR codes with optional logos and frames. It's a handy tool for generating QR codes for URLs with various customization options.

## Features ✨

- **Customizable Colors**: Choose your own fill and background colors for the QR code.
- **Logo Integration**: Add a logo to the center of your QR code.
- **Frame Text**: Add a custom text frame around your QR code.
- **Error Correction Levels**: Supports different error correction levels (L, M, Q, H).
- **Multiple Formats**: Save your QR code in various formats like PNG, JPEG, etc.

## Installation 📦

To use this project, you'll need to have Python installed along with the following libraries:

```bash
pip install qrcode[pil]
pip install pillow
```

## Usage 🚀

Run the `main.py` script to generate your QR code. You'll be prompted to enter various customization options:

```python
python main.py
```

### Example

Here's an example of how to use the script:

```python
Enter the URL to encode in the QR code: https://example.com
Enter the fill color (default is black): blue
Enter the background color (default is white): yellow
Enter the filename to save the QR code image (default is qr_code.png): my_qr_code.png
Enter the QR code version (1-40, default is 1): 2
Enter the error correction level (L, M, Q, H, default is L): H
Enter the path to a logo image (optional): path/to/logo.png
Enter the output format (PNG, JPEG, etc., default is PNG): PNG
Enter the text to display on the frame (optional): Scan Me!
```

## Contributing 🤝

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License 📄

This project is licensed under the MIT License.
