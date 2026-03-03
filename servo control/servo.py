import cv2
import mediapipe as mp
import numpy as np
import pyfirmata2

#SETTING UP MEDIAPIPE DETECTION
mpHand = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHand.Hands(min_detection_confidence=0.8)

#SETTING UP CAMERA CAPTURE
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

#SETTING UP ARDUINO
port = "COM9"
board = pyfirmata2.Arduino(port)
servo_pinX = board.get_pin('d:9:s') #pin 9 Arduino
servo_pinY = board.get_pin('d:10:s') #pin 10 Arduino

#SETTING SERVO ORIGINAL POSITION
servo_pinX.write(90)
servo_pinY.write(90)


while cap.isOpened():
    success, img = cap.read()
    #img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    multiHandDetection = results.multi_hand_landmarks #Hand Detection
    lmList = []

    if multiHandDetection:
        #Hand Visualization
        for id, lm in enumerate(multiHandDetection):
            mpDraw.draw_landmarks(img, lm, mpHand.HAND_CONNECTIONS,
                                  mpDraw.DrawingSpec(color=(0, 255,255), thickness=4, circle_radius=7),
                                  mpDraw.DrawingSpec(color=(0, 0, 0), thickness = 4))

        #Hand Tracking
        singleHandDetection = multiHandDetection[0]
        for lm in singleHandDetection.landmark:
            h, w, c = img.shape
            lm_x, lm_y = int(lm.x*w), int(lm.y*h)
            lmList.append([lm_x, lm_y])

        #print(lmList)

        # draw point
        myLP1 = lmList[9] #which landmark from the hand
        myLP2 = lmList[0]
        px1, py1 = myLP1[0], myLP1[1]
        px2, py2 = myLP2[0], myLP2[1]
        px = (px1+px2)/2
        py = (py1+py2)/2

        #point = cv2.circle(img, (px, py), 15, (255, 0, 255), cv2.FILLED)
        #cv2.putText(img, str((px, py)), (px + 10, py - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        #cv2.line(img, (0, py), (ws, py), (0, 0, 0), 2)  # x line
        #cv2.line(img, (px, hs), (px, 0), (0, 0, 0), 2)  # y line


        # convert position to degree value
        servoX = int(np.interp(px, [0, ws], [180, 0])) #the 2nd are the ranges
        servoY = int(np.interp(py, [0, hs], [0, 180]))
        #cv2.rectangle(img, (40, 20), (350, 110), (0, 255, 255), cv2.FILLED)
        #cv2.putText(img, f'Servo X: {servoX} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        #cv2.putText(img, f'Servo Y: {servoY} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        # write to servo
        errorPan=px-ws/2
        errorTilt=py-hs/2
        if errorPan>30:
            servoX=servoX-1
            if servoX>180:
                servo=180
        if errorPan<30:
            servoX=servoX+1
            if servoX<0:
                servoX=1
        if errorTilt>30:
            servoY=servoY-1
            if servoY>120:
                servoY=120
        if errorTilt<30:
            servoY=servoY+1
            if servoY<60:
                servoY=60

        servo_pinX.write(servoX)
        servo_pinY.write(servoY)

        print(f'Hand Position x: {px} y: {py}')
        print(f'Servo Value x: {servoX} y: {servoY}')




    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()