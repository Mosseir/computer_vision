import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret,im = cap.read()
im_resized = cv2.resize(im, (640,360))
im_flipped = cv2.flip(im_resized, 1)
im0 = im1 = im2 = im3 = im_flipped

while(True):
    im0 = im1 #im0 = t - 4
    im1 = im2 #im1 =  t - 3
    im2 = im3 #im2 = t - 2
    im3 = im_flipped #im3 = t - 1 , im_flipped = t
    
    ret,im = cap.read()
    im_resized = cv2.resize(im, (640,360))
    im_flipped = cv2.flip(im_resized, 1)

    # im_out = (0.2*im0 + 0.2*im1 + 0.2*im2 + 0.2*im3 + 0.2*im_flipped).astype(np.uint8) #no astype(np.uint8) รันได้แต่ไม่ตรงตามต้องการแน่ๆ
    # im_out = ((im0 + im1 + im2 + im3 + im_flipped) / 5).astype(np.uint8) #Overflow example
    im_out = (im_flipped*2).astype(np.uint8) #Overflow example
    cv2.imshow('camera',im_out)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
