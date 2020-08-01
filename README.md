# Write-Text-on-images-in-real-time-using-OpenCV-Python

In this project, we will see how to write text on image. Firstly, import libraries and read the image then initialize the counter that will be used for changing the position of the text. Inside an infinite while loop, Display the image and use cv2.waitKey() for a keypress. Specify the font and draw the text using cv2.putText().

cv2.putText(img, position, font, fontScale, color, thickness, lineType, bottomLeftOrigin)

Next, increase the counter and provide the termination conditionwhere key ‘q’ break the loop.
Lastly, we call cv2.destroyAllWindows() function for destroys all the windows we created.
