import pyqrcode
import png
from pyqrcode import QRCode

QRstring = "https://en.wikipedia.org/wiki/Independent_Order_of_Odd_Fellows"
url = pyqrcode.create(QRstring)
url.png("Desktop\\qr.png", scale=8)
