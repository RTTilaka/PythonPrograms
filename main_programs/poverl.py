class test:
        def Hello(self,Name=None,Age=None):
                self.Name=Name
                self.Age=Age
                if(self.Name==None and self.Age==None):
                        print("Hello")
                elif(self.Name!=None and self.Age==None):
                        print("Hello",self.Name)
                elif(self.Name!=None and self.Age!=None):
                        print("Hello",self.Name,self.Age)
while(True):
        print("Enter the details")
        Name=input("Enter your name ")
        Age=int(input("Enter your Age "))
        obj1=test()
        obj1.Hello()
        obj1.Hello(Name)
        obj1.Hello(Name,Age)
        break
