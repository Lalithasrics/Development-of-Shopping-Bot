from pyzbar import pyzbar
import cv2


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:",obj.data)
        print()

    return image
def capimage():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    print(check) #prints true as long as the webcam is running
    print(frame) #prints matrix values of each framecd
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    decoded_objects = decode(frame)
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    webcam.release()
    cv2.waitKey(1650)
    cv2.destroyAllWindows()
    #return(decoded_objects)


capimage()