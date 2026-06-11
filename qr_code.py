import qrcode
from datetime import datetime

print("===== QR Code Generator =====")

text = input("Enter Text or URL: ")

img = qrcode.make(text)

time = datetime.now().strftime("%d%m%Y_%H%M%S")

file_name = f"qr_{time}.png"

img.save(file_name)

print(f"\nQR Code Saved As {file_name}")