import cv2 as cv
##### Reading Images
# img = cv.imread('C:/Users/DELL/Downloads/Projects/Kenyan_Sign_language/Images/ImageID_00AVE728.jpg')

# cv.imshow('Sign',img)

###What i have learnt
 #    * Take note of the file path while using "\" always replace it with a "/".
    
###Reading videos
capture = cv.VideoCapture("C:/Users/DELL/Videos/20190731_175127.mp4")

while True:
    isTrue,frame = capture.read() 
    cv.imshow("Video", frame) 
    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows() 
## Error messages are common such as the the listed below show up as a result of the video coming to an end.
##cv2.error: OpenCV(4.5.5) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'

# cv.waitKey(0)