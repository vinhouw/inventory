############################################################################
# Author: Vinh Florentin
# Trinity Fl
# December 30th, 2020
############################################################################
# .\barvenv\Scripts\activate

# Dependencies
# barcodes QR codes testing
# pip install qrtools 0.0.2 decoder
# pip install qrcode[pil]  encoder
# pip install opencv-python
# pip install pillow
# pip install PyZbar
# pip install python-qrtools /????/?

############################################################################

# from segno import helpers

# qr = helpers.make_mecard(name='Florentin,Vinh', email='vflorentin@fastmd.com', phone='8139473252')
# qr.designator
# Some params accept multiple values, like email, phone, url
# qr = helpers.make_mecard(name='Florentin,Vinh', email=('vflorentin@fastmd.com', 'another@example.org'), url=['http://www.example.org', 'https://example.org/~joe'])
# qr.save('my-mecardVinhFlorentin.svg', scale=4)

import segno
import cv2
from pyzbar import pyzbar


barcodes_read = []

# def qr_creator(name, sku, mf, MinQty):
def qr_creator(sku, item_name):
    """ qr help func to create new QR codes 
    """
    qr = segno.make_qr(sku +' '+ item_name)
    qr.save('{}.png'.format(item_name), scale=3)
    qr.show()


def read_barcodes(frame):
    """ Read QR codes and copy content in txt file but overwrite item
        Press SPACEBAR to capture QR code info into list
     """
    barcodes = pyzbar.decode(frame)
    # barcodes_read = []
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8') # data in barcode_info
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        print(barcode_info)
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 5, y - 5), font, 1.0, (0, 0, 255), 2)
        #3
        with open("barcode_result.txt", mode ='w') as file:
            # file.write("Barcodes:" + barcode_info)
            file.write(barcode_info)
        #4
        # if cv2.waitKey(1) == ord("q"):
        if cv2.waitKey(1) == 32: # spacebar
            barcodes_read.append(barcode_info)
    return frame


def scanner():
    """ Opens camera to scan and close when ESC is pressed  """
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
  
        if cv2.waitKey(1) & 0xFF == 27: 
            break
        # elif cv2.waitKey(1) == ord("q"):
        #     barcodes_read.append(barcode_info)
        
    print(barcodes_read)
    #3
    camera.release()
    cv2.destroyAllWindows()


def add_scanned_items(barcodes_read):
    """" function that grab item_numbers and add them to database """
    for barcode in barcodes_read:
        print("barcodes: {} ".format(barcode))
    
    print("{} barcodes scanned!!".format(len(barcodes_read)))



qr_creator('0409-1159-02','Bupivacaine') # create the QR code
scanner() # scan the QR code
add_scanned_items(barcodes_read)


# dump barcodes_read[] into a text file?