#Import OpenCV
import cv2
# Read the image
img = cv2.imread('P:\Sea.jpg')
# initialize counter
i = 0
while True:
    # Display the image
    cv2.imshow('Sea',img)
    # wait for keypress
    k = cv2.waitKey(0)
    # specify the font and draw the key using puttext
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "fish",(250+i,350), font, 2,(0,255,255),5,cv2.LINE_AA)
    i+=10
    if k == ord('q'):
        break
cv2.destroyAllWindows()