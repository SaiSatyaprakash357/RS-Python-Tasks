# Finger Counter using OpenCV and CVZone.

# Uses cv2 for webcam feed and cvzone.HandTrackingModule for hand detection.
# Counts raised fingers on one or two hands in real-time.
# Displays total finger count with styled text on the screen.
# Press 'Esc' to exit the live feed.


from cvzone.HandTrackingModule import HandDetector
from cvzone.Utils import putTextRect
import cv2

cap = cv2.VideoCapture(0)

detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (960, 720))
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        center1 = hand1['center']
        handType1 = hand1["type"]  

        fingers1 = detector.fingersUp(hand1)
        fingers2 = []

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

            fingers2 = detector.fingersUp(hand2)

        img, bbox = putTextRect(
            img, 
            f"Total Fingers: {fingers1.count(1)+fingers2.count(1)}", 
            (420, 100), 
            scale=1, 
            thickness=2, 
            colorT=(255, 0, 0), 
            colorR=(0, 255, 0),
            colorB=(0, 0, 255),
            font=cv2.FONT_HERSHEY_SIMPLEX, 
            offset=10, 
            border=3
        )
             

    cv2.imshow("Finger Counter", img)
    if cv2.waitKey(1) & 0xFF == 27:
            break
    
cap.release()  
cv2.destroyAllWindows()