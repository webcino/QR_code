import qrcode

data = 'Don\'t forget to subscribe'

img = qrcode.make(data)

img.save('myqr.png')

