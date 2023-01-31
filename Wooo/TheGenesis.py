import csv
import datetime
# In the beginning programmer created the SQL Database and Python Program.
# Programme made by Anshumaan Vikram Singh, Dron Pande, Shivansh Singh from Study Hall School

def register():
    while True:
        name = input("Enter candidate's name: ")
        rollno = int(input("Enter roll number: "))
        dob = input("Enter date of birth (YYYY/MM/DD): ")
        school = input("Enter School Name: ")
        while True:
            print("Please pick a center of your choice: \n1.Mumbai\n2.Delhi\n3.Kanpur\n4.Lucknow")
            choice = int(input("Enter your selection: (1,2,3,4): "))
            if choice == 1:
                centername = "Mumbai"
                break
            elif choice == 2:
                centername = "Delhi"
                break
            elif choice == 3:
                centername = "Kanpur"
                break
            elif choice == 4:
                centername = "Lucknow"
                break
            else:
                print("That is not an option. Try again.")
        
        with open("regis.csv",'a') as f:
            pen = csv.writer(f)
            pen.writerow([name,rollno,dob,school,centername])
            print("Data Added")
        choice2 = int(input("Add more data ?\n1.Yes\n2.No\n == "))
        if choice2 == 2:
            break

print("Current Date and Time(YYYY-MM-DD H:MIN:SEC): ", datetime.datetime.now(),"\n\n")
register()
