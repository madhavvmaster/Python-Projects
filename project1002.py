import qrcode

url = input("Enter the URL to generate QR code: ").strip()
file_path = input("Enter the absolute file path to save the QR code with file name and extension: ").strip()

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print(f"QR code generated and saved to {file_path}")
