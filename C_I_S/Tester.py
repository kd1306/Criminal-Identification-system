#!C:/Users/Kushang Darbar/AppData/Local/Programs/Python/Python38-32/python 
#print("Content-Type:text/html; charset=utf-8\n\n")
print()
import cgi
#!/usr/bin/env python
# coding: utf-8
import cv2
import os
import numpy as np
import FaceRecognition as fr
import retrieve as rt
import cgitb

cgitb.enable()
form = cgi.FieldStorage()
photo=form['Photo']
if photo.filename:
    fn=os.path.basename(photo.filename)
    open('C:/xampp/htdocs/Criminal_Identification_System/tmp/'+fn,'wb').write(photo.file.read())
    #print('\nFile'+fn+'was uploaded')
else:
    print('\nNo file uploaded')
#print(photo)

#print(test_img)
#This module takes images  stored in diskand performs face recognition
test_img=cv2.imread('C:/xampp/htdocs/Criminal_Identification_System/tmp/'+fn)#test_img path
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)


#Comment belows lines when running this program second time.Since it saves training.yml file in directory
#faces,faceID=fr.labels_for_training_data(r'C:\Users\Kushang Darbar\PROJECT\trainingImages')
#face_recognizer = fr.train_classifier(faces,faceID)
#face_recognizer.save(r'C:\Users\Kushang Darbar\PROJECT\trainingData.yml')

#Uncomment below line for subsequent runs
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\Kushang Darbar\PROJECT\trainingData.yml')#use this to load training data for subsequent runs

name={0:"Kushang",1:"Milind"}#creating dictionary containing names for each label

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence<35):#If confidence more than 30 then don't print predicted face text on screen
        fr.put_text(test_img,predicted_name,x,y)
        rt.retrieveData(predicted_name)
    else:
        print("No data found in database")

resized_img=cv2.resize(test_img,(800,800))
cv2.imshow("face recognition",resized_img)
#Waits indefinitely until a key is pressed
cv2.waitKey(0)                       
cv2.destroyAllWindows()