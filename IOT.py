import cv2
import mediapipe as mp
import pyautogui as p
import RPi.GPIO as GPIO
import time

def count_fingers(lst):
    cnt=0
    thresh=(lst.landmark[0].y*100-lst.landmark[9].y*100)/2

    if (lst.landmark[5].y*100-lst.landmark[8].y*100)>thresh:
        cnt+=1
    if (lst.landmark[9].y*100-lst.landmark[12].y*100)>thresh:
        cnt+=1
    if (lst.landmark[13].y*100-lst.landmark[16].y*100)>thresh:
        cnt+=1
    if (lst.landmark[17].y*100-lst.landmark[20].y*100)>thresh:
        cnt+=1
    if (lst.landmark[5].x*100-lst.landmark[4].x*100)>5:
        cnt+=1
    return cnt

def LED(x):
    LED_PIN = x
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()


def SW_control():
    cap=cv2.VideoCapture(0)
    cap.set(600,850)
    drawing=mp.solutions.drawing_utils
    
    hands=mp.solutions.hands
    hand_obj=hands.Hands(max_num_hands=1)
    
    while(True):
        _,frm=cap.read()
        frm=cv2.flip(frm,1)
        res=hand_obj.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:
            hand_keyPoints=res.multi_hand_landmarks[0]
            # print(count_fingers(hand_keyPoints))
            op=count_fingers(hand_keyPoints)
            if(op==0):
                cv2.putText(frm,str(op)+': Idle',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            if(op==1):
                p.press('space')
                cv2.putText(frm,str(op)+': Play/Pause',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==2):
                p.press('up')
                cv2.putText(frm,str(op)+': Volum Up',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==3):
                p.press('down')
                cv2.putText(frm,str(op)+': Volum Down',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==4):
                p.press('right')
                cv2.putText(frm,str(op)+': Forward',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==5):
                p.press('left')
                cv2.putText(frm,str(op)+': Backward',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            drawing.draw_landmarks(frm,hand_keyPoints,hands.HAND_CONNECTIONS)
            
        cv2.imshow('Aniket',frm)
        
        if cv2.waitKey(1)==27:
            cv2.destroyAllWindows()
            cap.release()
            break

def HW_control():
    cap=cv2.VideoCapture(0)
    drawing=mp.solutions.drawing_utils
    
    hands=mp.solutions.hands
    hand_obj=hands.Hands(max_num_hands=1)
    
    while(True):
        _,frm=cap.read()
        frm=cv2.flip(frm,1)
        res=hand_obj.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:
            hand_keyPoints=res.multi_hand_landmarks[0]
            op=count_fingers(hand_keyPoints)
            if(op==0):
                cv2.putText(frm,str(op)+': Idle',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            if(op==1):
                LED(17)
                cv2.putText(frm,str(op)+': Play/Pause',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==2):
                LED(22)
                cv2.putText(frm,str(op)+': Volum Up',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==3):
                LED(27)
                cv2.putText(frm,str(op)+': Volum Down',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==4):
                LED(23)
                cv2.putText(frm,str(op)+': Forward',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            elif(op==5):
                LED(25)
                cv2.putText(frm,str(op)+': Backward',(150,150),cv2.FONT_HERSHEY_PLAIN,5,(225,140,35),12)
            drawing.draw_landmarks(frm,hand_keyPoints,hands.HAND_CONNECTIONS)
            
        cv2.imshow('Aniket',frm)
        
        if cv2.waitKey(1)==27:
            cv2.destroyAllWindows()
            cap.release()
            break     
