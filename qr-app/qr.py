#python qr.py

#pip install qrcode


import qrcode

img = qrcode.make('www.google.com')
img.save("qrcode.png")



