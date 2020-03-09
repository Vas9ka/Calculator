class Storage:
    Log = open("log.txt","w")
    def Write(self,string):
        self.Log.write(string)
    def Clear(self):
        self.Log.truncate(0)
    def ShowLastOperations(self):
        self.Log.close()
        self.Log = open("log.txt","r")
        print(self.Log.read())
        self.Log.close()
        self.Log = open("log.txt","a+")

    def Close(self):
        self.Log.close()