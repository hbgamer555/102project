import cv2

def snapshot_create():
    captureobject=cv2.VideoCapture(0)
    ret,frame=captureobject.read()
    cv2.imwrite("firstsnap.jpg",frame)
    captureobject.release()
    cv2.destroyAllWindows()



snapshot_create()    
  