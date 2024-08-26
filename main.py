import cv2
from cvzone.HandTrackingModule import HandDetector

# Abrir webcam
video = cv2.VideoCapture(0, cv2.CAP_DSHOW) 

# criar resolução HD
video.set(propId=3, value=1280)
video.set(propId=4, value=720)

dectector = HandDetector()

desenho = []
while True:
    check, img = video.read()

    resultado = dectector.findHands(img, draw=True)
    hand = resultado[0]
    
    if hand:
        lmList = hand[0]['lmList']
        dedos = dectector.fingersUp(hand[0])
        dedos_lev = dedos.count(1)

        if dedos_lev == 1 : # Se aparecer 1 dedos, começe a desenhar
            x,y = lmList[8][0], lmList[8][1]
            cv2.circle(img,(x,y), 15, (255, 0, 0), cv2.FILLED)
            desenho.append((x,y))

        elif dedos_lev !=1 and dedos_lev !=3:
            desenho.append((0,0))

        elif dedos_lev ==3:
            desenho = []

        for id, ponto in enumerate(desenho):
            x,y = ponto[0], ponto[1]
            cv2.circle(img,(x,y), 10, (255, 0, 0), cv2.FILLED)
            if id >=1:
                ax, ay = desenho[id-1][0], desenho[id-1][1]
                if x !=0 and ax !=0:
                    cv2.line(img, (x,y), (ax, ay), (255,0,0), 20)

    # inverter imagem
    imgFlip = cv2.flip(img, 1)
    cv2.imshow("Img", imgFlip)
    if cv2.waitKey(1)==27:
        break