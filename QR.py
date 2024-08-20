import pyqrcode

qr_code = pyqrcode.create('https://www.github.com/')
qr_code.png('QRCode.png', scale=8)