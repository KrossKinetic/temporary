import mysql.connector as sqltor
import numpy as np
import cv2 as cv

mycon = sqltor.connect(host="localhost",user="root",passwd="MyPass",database="registration")
if mycon.is_connected() == False:
    print('Error connecting to database')
cursor = mycon.cursor()

def searchcandidate(rollnum):
    data= cursor.execute("select * from nta where 'rollno' =", rollnum)
    print("data of student", data)


    choice = int(input("Do you wish to open the video recording of the exam hall ? (1.Yes/2. No"))
    if choice == 1:
        cap = cv.VideoCapture('')#FILE NAME / SOURCE FROM CURSOR
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


print("Accessing Candidate Database")
while True:
    rollnum = int(input("Enter the student's roll number: "))
    searchcandidate(rollnum)
    choice2 = int(input("Look for more candidates ?(1.Yes/2.No): "))
    if choice2 == 1:
        continue
    else:
        break