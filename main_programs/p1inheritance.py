#hierarchial inheritance
d={}
class STUDENT:
        def __init__(self):
                self.USN=input("Enter the USN Number")
                self.Name=input("Enter the Name")
                self.Age=int(input("Enter the Age"))
        def display(self):
                print("USN : ", self.USN)
                print("Name: ", self.Name)
                print("Age : ", self.Age)
class Derived1(STUDENT):
        def __init__(self):
                super().__init__()
                self.semester=int(input("Enter the semester"))
                self.sub1=int(input("Enter Marks in Sub1"))
                self.sub2=int(input("Enter Marks in Sub2"))
                self.sub3=int(input("Enter Marks in Sub3"))
                self.sub4=int(input("Enter Marks in Sub4"))
                self.sub5=int(input("Enter Marks in Sub5"))
                self.percentage=((self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5)/5)
                self.jkl=self.update()
        def update(self):
                d.update({self.Name:{
                        "USN":self.USN,
                        "Name":self.Name,
                        "Age":self.Age,
                        "Semester":self.semester,
                        "Sub1":self.sub1,
                        "sub2":self.sub2,
                        "Sub3":self.sub3,
                        "Sub4":self.sub4,
                        "Sub5":self.sub5,
                        "Percentage":self.percentage}})

class Derived2(Derived1):
        def show(self):
                for key in d:
                        print(key,d[key])
while(True):
        print("choose from following option")
        print("1.Add an Student")
        print("2.Display the Student")
        print("3.exit")
        ch=int(input("Enter the choice number"))
        if(ch==1):
                obj1=Derived2()
        elif(ch==2):
                obj1.show()
        elif(ch==3):
                break
        else:
                print("wrong choice")
