class Verify_Password:
    def __init__(self, password):
        self.password = password
        self.password_strength = 0
        
    def checklength(self,password):
        if len(password) > 6 and len(password) < 10 :
            self.password_strength += 1
        elif len(password) > 10:
            self.password_strength += 1
        else:
            self.password_strength = 0
    
    def checkalpha(self,password):
        if password.isalpha() == True:
            self.password_strength += 1
        elif password.isnumeric() == True:
            self.password_strength += 1
        elif password.isalnum() == True:
            self.password_strength += 1
        elif password.isascii() == True:
            self.password_strength += 1
        else:
            self.password_strength += 0
    
    def checkcase(self,password):
        if password.islower():
            self.password_strength += 1
        elif password.isupper():
            self.password_strength += 1
        #elif password.islower() and password.isupper():
        #    self.password_strength += 1
        else:
            self.password_strength = 0

    def standardpasswords(self,password):
        standardlist=["password","test","password1","password2","tester",1234567,"qwerty","@@@@@@"]
        for passwords in standardlist:
            if password == standardlist:
                print (f"matched password is : {password}")
                self.password_strength = 0
        else:
            self.password_strength +=1
        
    def rating(self,password_strength):
        if self.password_strength < 1:
            status = "Weak password"
            return status
        elif self.password_strength < 2:
            status = "Medium password"
            return status
        elif self.password_strength < 3:
            status = "Strong password"
            return status
        elif self.password_strength < 4:
            status = "Very Strong password"
            return status

while True:
    userpassword= input("Enter Password: ")
    if len(userpassword) > 0:
        check1=Verify_Password(userpassword)
        check1.checklength(userpassword)
        #print (f"Counter for checklength : {check1.password_strength}")
        check1.checkalpha(userpassword)
        #print (f"Counter for checkalpha : {check1.password_strength}")
        check1.checkalpha(userpassword)
        #print (f"Counter for checkcase : {check1.password_strength}")
        check1.standardpasswords(userpassword)
        #print (f"Counter for standardpasswords : {check1.password_strength}")
        y = check1.rating(check1.password_strength)
        print (f"Counter for standardpasswords :{check1.password_strength} so rating is : {y}")
    else:
        print("invalid Input")
    break