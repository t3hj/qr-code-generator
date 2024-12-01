import qrcode
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk

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

def generate_qr_code():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Input Error", "URL cannot be empty.")
        return
    
    fill_color = fill_color_entry.get().strip() or 'black'
    back_color = back_color_entry.get().strip() or 'white'
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    if not filename:
        return
    version = int(version_entry.get().strip() or 1)
    error_correction = error_correction_entry.get().strip().upper() or 'L'
    logo_path = logo_path_entry.get().strip() or None
    output_format = output_format_entry.get().strip().upper() or 'PNG'
    
    # Ensure default format is 'PNG' if not specified
    if not output_format:
        output_format = 'PNG'
    
    frame_text = frame_text_entry.get().strip() or None
    
    create_qr_code(url, filename, fill_color=fill_color, back_color=back_color, version=version, error_correction=error_correction, logo_path=logo_path, output_format=output_format, frame_text=frame_text)
    messagebox.showinfo("Success", f"QR code saved as '{filename}'")

def browse_logo():
    logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if logo_path:
        logo_path_entry.delete(0, tk.END)
        logo_path_entry.insert(0, logo_path)

def choose_fill_color():
    color = colorchooser.askcolor()[1]
    if color:
        fill_color_entry.delete(0, tk.END)
        fill_color_entry.insert(0, color)

def choose_back_color():
    color = colorchooser.askcolor()[1]
    if color:
        back_color_entry.delete(0, tk.END)
        back_color_entry.insert(0, color)

root = tk.Tk()
root.title("QR Code Generator")

tk.Label(root, text="URL (*):").grid(row=0, column=0, sticky=tk.W)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
url_entry.insert(0, "https://example.com")

tk.Label(root, text="Fill Color (*):").grid(row=1, column=0, sticky=tk.W)
fill_color_entry = tk.Entry(root)
fill_color_entry.grid(row=1, column=1, padx=5, pady=5)
fill_color_entry.insert(0, "black")
tk.Button(root, text="Choose", command=choose_fill_color).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Background Color (*):").grid(row=2, column=0, sticky=tk.W)
back_color_entry = tk.Entry(root)
back_color_entry.grid(row=2, column=1, padx=5, pady=5)
back_color_entry.insert(0, "white")
tk.Button(root, text="Choose", command=choose_back_color).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="Filename (*):").grid(row=3, column=0, sticky=tk.W)
filename_entry = tk.Entry(root)
filename_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
filename_entry.insert(0, "qr_code.png")

tk.Label(root, text="Version:").grid(row=4, column=0, sticky=tk.W)
version_entry = tk.Entry(root)
version_entry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
version_entry.insert(0, "1")

tk.Label(root, text="Error Correction Level:").grid(row=5, column=0, sticky=tk.W)
error_correction_entry = ttk.Combobox(root, values=["L", "M", "Q", "H"])
error_correction_entry.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
error_correction_entry.set("L")

tk.Label(root, text="Logo Path:").grid(row=6, column=0, sticky=tk.W)
logo_path_entry = tk.Entry(root)
logo_path_entry.grid(row=6, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_logo).grid(row=6, column=2, padx=5, pady=5)

tk.Label(root, text="Output Format:").grid(row=7, column=0, sticky=tk.W)
output_format_entry = ttk.Combobox(root, values=["PNG", "JPEG"])
output_format_entry.grid(row=7, column=1, columnspan=2, padx=5, pady=5)
output_format_entry.set("PNG")

tk.Label(root, text="Frame Text:").grid(row=8, column=0, sticky=tk.W)
frame_text_entry = tk.Entry(root)
frame_text_entry.grid(row=8, column=1, columnspan=2, padx=5, pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr_code).grid(row=9, column=0, columnspan=3, pady=10)

root.mainloop()
