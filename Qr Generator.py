import os
import qrcode

def generate_qr(qr_name, qr_data):
    # Define the name of the QR code file
    qr_file = f"{qr_name}.png"

    # Check if the QR code file already exists
    if os.path.isfile(qr_file):
        # If the file exists, generate a new name for the QR code
        i = 1
        while os.path.isfile(f"{qr_name}_{i}.png"):
            i += 1
        qr_name = f"{qr_name}_{i}"
        qr_file = f"{qr_name}.png"

    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(qr_file)

    # Return the name of the QR code file
    return qr_name

# Generate a QR code with the name "myqr" and the data "https://www.blackboxai.io"
qr_name = generate_qr("myqr", "https://www.blackboxai.io")
print(f"QR code saved as {qr_name}")
