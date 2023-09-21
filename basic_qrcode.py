import segno

# create QR code object that encode the text "Hello, World"
# this will greet user with that text, and it might also offer the option of searching for "hello, World" on the internet
qrcode = segno.make_qr("Hello, World")
# save QR code object as PNG file
qrcode.save("basic_qrcode.png")
