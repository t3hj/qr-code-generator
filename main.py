import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_qr_code(url, filename='qr_code.png', box_size=10, border=4, fill_color='black', back_color='white', version=1, error_correction='L', logo_path=None, output_format='PNG', frame_text=None):
    try:
        # Map error correction level
        error_correction_levels = {
            'L': qrcode.constants.ERROR_CORRECT_L,
            'M': qrcode.constants.ERROR_CORRECT_M,
            'Q': qrcode.constants.ERROR_CORRECT_Q,
            'H': qrcode.constants.ERROR_CORRECT_H
        }
        
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction_levels.get(error_correction, qrcode.constants.ERROR_CORRECT_L),
            box_size=box_size,
            border=border,
        )
        
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

        # Add logo if provided
        if logo_path:
            logo = Image.open(logo_path)
            logo_size = min(img.size) // 5
            logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            img.paste(logo, pos, mask=logo)

        # Add a frame around the QR code
        if frame_text:
            # Create a new image with extra space for the frame
            frame_width = img.size[0] + 40
            frame_height = img.size[1] + 80
            framed_img = Image.new('RGB', (frame_width, frame_height), back_color)
            draw = ImageDraw.Draw(framed_img)

            # Paste the QR code onto the framed image
            qr_x = (frame_width - img.size[0]) // 2
            qr_y = 40
            framed_img.paste(img, (qr_x, qr_y))

            # Add text to the frame
            font = ImageFont.load_default()
            text_bbox = draw.textbbox((0, 0), frame_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = (frame_width - text_width) // 2
            text_y = frame_height - text_height - 20
            draw.text((text_x, text_y), frame_text, fill=fill_color, font=font)

            img = framed_img

        # Save the image in the specified format
        img.save(filename, format=output_format)
        print(f"QR code saved as '{filename}' for URL: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the QR Code Generator!")
    
    # Prompt for URL
    url = input("Enter the URL to encode in the QR code: ")
    
    # Prompt for colors
    fill_color = input("Enter the fill color (default is black): ") or 'black'
    back_color = input("Enter the background color (default is white): ") or 'white'
    
    # Prompt for filename
    filename = input("Enter the filename to save the QR code image (default is qr_code.png): ") or 'qr_code.png'
    
    # Prompt for version
    version = int(input("Enter the QR code version (1-40, default is 1): ") or 1)
    
    # Prompt for error correction level
    error_correction = input("Enter the error correction level (L, M, Q, H, default is L): ") or 'L'
    
    # Prompt for logo path
    logo_path = input("Enter the path to a logo image (optional): ") or None
    
    # Prompt for output format
    output_format = input("Enter the output format (PNG, JPEG, etc., default is PNG): ") or 'PNG'
    
    # Prompt for frame text
    frame_text = input("Enter the text to display on the frame (optional): ") or None
    
    # Generate the QR code
    create_qr_code(url, filename, fill_color=fill_color, back_color=back_color, version=version, error_correction=error_correction, logo_path=logo_path, output_format=output_format, frame_text=frame_text)

if __name__ == "__main__":
    main()
