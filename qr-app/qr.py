#python qr.py


import qrcode

img = qrcode.make('www.google.com')
img.save("qrcode.png")



