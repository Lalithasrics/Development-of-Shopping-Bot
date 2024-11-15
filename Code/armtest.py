import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time
from qreader import QReader
import cv2
from pyzbar.pyzbar import decode
import serial

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2)
rotm1=37
rotm2=35
upm1=31
upm2=29
m1=40
m2=38
m3=36
m4=32
irr=13
irm=12
irl=11
hm1=12
hm2=3
am1=33
am2=26
irc=5
GPIO.setup(rotm1,GPIO.OUT)
GPIO.setup(rotm2,GPIO.OUT)
GPIO.setup(hm1,GPIO.OUT)
GPIO.setup(hm2,GPIO.OUT)
GPIO.setup(am1,GPIO.OUT)
GPIO.setup(am2,GPIO.OUT)
GPIO.setup(upm1,GPIO.OUT)
GPIO.setup(upm2,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(m3,GPIO.OUT)
GPIO.setup(m4,GPIO.OUT)
GPIO.setup(irr,GPIO.IN)
GPIO.setup(irl,GPIO.IN)
#GPIO.setup(irm,GPIO.IN)
GPIO.setup(irc,GPIO.IN)
GPIO.output(m1,0)
GPIO.output(m2,0)
GPIO.output(m3,0)
GPIO.output(m4,0)
GPIO.output(rotm1,0)
GPIO.output(rotm2,0)
GPIO.output(hm1,0)
GPIO.output(hm2,0)
GPIO.output(am1,0)
GPIO.output(am2,0)
GPIO.output(upm1,0)
GPIO.output(upm2,0)

def rot():
    GPIO.output(rotm1,1)
    GPIO.output(rotm2,0)
    time.sleep(0.7)
    GPIO.output(rotm1,0)
    GPIO.output(rotm2,0)
def rota():
    GPIO.output(rotm1,0)
    GPIO.output(rotm2,1)
    time.sleep(0.7)
    GPIO.output(rotm1,0)
    GPIO.output(rotm2,0)

def upms1():
    GPIO.output(upm1,1)
    GPIO.output(upm2,0)
    time.sleep(1.5)
    GPIO.output(upm1,0)
    GPIO.output(upm2,0)
def downms1():
    GPIO.output(upm1,0)
    GPIO.output(upm2,1)
    time.sleep(1.3)
    GPIO.output(upm1,0)
    GPIO.output(upm2,0)

def upms2():
    GPIO.output(upm1,1)
    GPIO.output(upm2,0)
    time.sleep(2.8)
    GPIO.output(upm1,0)
    GPIO.output(upm2,0)
def downms2():
    GPIO.output(upm1,0)
    GPIO.output(upm2,1)
    time.sleep(2.2)
    GPIO.output(upm1,0)
    GPIO.output(upm2,0)
def upm():
    GPIO.output(upm1,1)
    GPIO.output(upm2,0)
    time.sleep(0.3)
    GPIO.output(upm1,0)
    GPIO.output(upm2,0)
def downm():
    GPIO.output(upm1,0)
    GPIO.output(upm2,1)
    time.sleep(0.3)
    GPIO.output(upm1,0)
    GPIO.output(upm2,0)

def hms1():
    GPIO.output(hm1,1)
    GPIO.output(hm2,0)
    time.sleep(1)
    GPIO.output(hm1,0)
    GPIO.output(hm2,0)
def ihms1():
    GPIO.output(hm1,0)
    GPIO.output(hm2,1)
    time.sleep(1)
    GPIO.output(hm1,0)
    GPIO.output(hm2,0)
def aopen():
    GPIO.output(am1,1)
    GPIO.output(am2,0)
    time.sleep(2.3)
    GPIO.output(am1,0)
    GPIO.output(am2,0)
def aclose():
    GPIO.output(am1,0)
    GPIO.output(am2,1)
    time.sleep(2.3)
    GPIO.output(am1,0)
    GPIO.output(am2,0)

def BarcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
    bartext=""
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:  
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using 
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10), 
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
            # Print the barcode data
                print(barcode.data)
                print(barcode.type)
                bartext=barcode.data
    return(bartext)
def qrread():

    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    #print(check) #prints true as long as the webcam is running
    #print(frame) #prints matrix values of each framecd
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    cv2.imwrite(filename='saved_img.png', img=frame)
    webcam.release()
    #img_new = cv2.imread('saved_img.png', cv2.IMREAD_GRAYSCALE)
    #img_new = cv2.imshow("Captured Image", img_new)
    cv2.waitKey(1650)
    cv2.destroyAllWindows()
    qr=BarcodeReader('saved_img.png')
    return(qr)

def pickpro():
    hms1()
    aclose()
    ihms1()
    rota()
    aopen()
    rot()

SerialPort = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
time.sleep(3)
print("data")
SerialPort.write(str.encode('a\r'))

print("rotation")