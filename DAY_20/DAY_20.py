import qrcode

def create_qr_code(url, fill_color, back_color, box_size, border):
    # Create QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    # Add data
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR Code image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    return img

# Get user input
url = input("Please enter the URL: ")
fill_color = input("Fill color (e.g., 'black'): ")
back_color = input("Background color (e.g., 'white'): ")
box_size = int(input("Box size (e.g., 10): "))
border = int(input("Border thickness (e.g., 4): "))

# Create QR Code
img = create_qr_code(url, fill_color, back_color, box_size, border)

# Save image as PNG file
img.save("custom_qr_code.png")

print("QR Code has been successfully created and saved as 'custom_qr_code.png'.")