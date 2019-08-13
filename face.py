import cv2
import numpy as np
import dlib
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("faceLuyen.mp4")

detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

dem = 0
while cap.isOpened():
    _, frame = cap.read()
    # frame = cv2.resize(frame, (480,360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        crop_img = gray[y1:y2, x1:x2]
        dem = dem + 1

        cv2.imwrite('C:\\Users\\gvc\\Desktop\\FACE\\DATA\\TRAIN\\Luyen\\'+str(dem)+'.png',crop_img)
    cv2.imshow("Frame", frame)
        # landmarks = predictor(gray, face)

        # for n in range(0, 68):
        #     x = landmarks.part(n).x
        #     y = landmarks.part(n).y
        #     cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)


    

    key = cv2.waitKey(1)
    if key == 27:
        break