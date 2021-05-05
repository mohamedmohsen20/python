class Member:
    def __init__(self,fname,lname):
        
        self.fname=fname
        self.lname=lname


    def getfullname(self):
        #full=self.fname+" "+self.lname
        #return full
        return f"hi {self.fname} {self.lname}"

m1=Member("mohamed","mohsen")

print("Full name is : {}".format(m1.getfullname()))
