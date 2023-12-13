import pyqrcode
import png

link = "www.linkedin.com/in/ervikasyadav"
qr_code = pyqrcode.create(link)
qr_code.png("qrcode.png", scale=5)
