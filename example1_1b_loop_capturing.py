import cv2

cap = cv2.VideoCapture(0)

# CAP_SIZE = (1280,720) ### (h x w while w is x-axis , h is y-axis)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_SIZE[0])
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_SIZE[1])

print("Press q to quit")

while(True):
    ret,im = cap.read()

    cv2.imshow('camera',im) 
    cv2.imshow('blue channel',im[:,:,0])
    cv2.imshow('green channel',im[:,:,1])
    cv2.imshow('red channel',im[:,:,2])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
