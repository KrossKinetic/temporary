import mysql.connector as sqltor
import numpy as np
import cv2 as cv

mycon = sqltor.connect(host="localhost",user="root",passwd="",database="registration")
if mycon.is_connected() == False:
    print('Error connecting to database')
cursor = mycon.cursor()
print("Accessing Candidate Database")
var = str(input("Enter roll number you want searched:"))
sql = "select * from nta where rollno = " + var + ";"
data = cursor.execute(sql)
myresult = cursor.fetchall()
print("data of student", myresult)

choice = int(input("Do you wish to open the video recording of the exam hall ? (1.Yes/2. No)"))
if choice == 1:
    cap = cv.VideoCapture("file.mp4")#FILE NAME / SOURCE FROM CURSOR
    while cap.isOpened():
        ret, frame = cap.read()
            # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

else:
        print("Not showing the video.")
