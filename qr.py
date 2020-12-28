# barcodes QR codes testing

import qrcode # QRCODE 6.1
# from qrcode.image.pure import PymagingImage

def qr_creator(item_num, item_name):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(item_num)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")

    img.save('{}.png'.format(item_name))
    img.show()

# qr_creator('123 Yeti 121','testing')
 
for i in range(10):
    qr_creator('123 Yeti 121{}'.format(i),'testing{}'.format(i))