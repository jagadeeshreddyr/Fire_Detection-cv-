# 
import cv2
import time
import requests
import json

fire_cascade = cv2.CascadeClassifier('xml/fire_detection.xml')

cap = cv2.VideoCapture(0)

def notification():
        print("sending notification")
        url = 'http://blynk-cloud.com/KGS493YUW2tgHp3XGyFEasVEA1aSc_cw/notify'   # paste ur token here and add notification widget in the blynk app
        body = {'body': 'Alert Fire Detected\nImage Processing'}    #msg u want as notification
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(body), headers=headers)

# def sms():
#     url = "https://www.fast2sms.com/dev/bulk"

#     querystring = {"authorization":"Jbk0F1YhvZtHoEqIWm6OnX93iurNxGUKL8zsMTVeydgARQ4PB5FCg5coKtGSkJA6vOuiRhQm4XsqljpT","sender_id":"FSTSMS","message":"Alert! Fire Detected","language":"english","route":"p","numbers":"7760565855,8197639481,9663391291"}

#     headers = {
#         'cache-control': "no-cache"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     print(response.text)
#     notification()
#     time.sleep(5)
#     val = requests.get("http://blynk-cloud.com/KGS493YUW2tgHp3XGyFEasVEA1aSc_cw/update/V3?value=0")

while True:
    ret, img = cap.read()
    #cv2.imshow('imgorignal',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img, 1.2, 5)
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print ('Fire is detected..!')
        val = requests.get("http://blynk-cloud.com/KGS493YUW2tgHp3XGyFEasVEA1aSc_cw/update/V3?value=1")
        # sms()
        time.sleep(0.1)
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
