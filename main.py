import pyqrcode
import png
from pyqrcode import QRCode

# String which represent the QR code
my_str = "https://github.com/klcheung1100"

# Generate the QR Code
url = pyqrcode.create(my_str)

# create and save the png file naming "myqr.png"
url.png("myqr.png", scale=6)

