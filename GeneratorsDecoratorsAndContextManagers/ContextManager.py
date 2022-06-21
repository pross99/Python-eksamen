#with open ("sample.txt", "w") as f:
   # f.write("Det er godt vejr, jubi!")

class Open_file():

    def __init__(self,fileName, mode):
        self.fileName= fileName
        self.mode = mode


    def __enter__(self):
        self.file = open(self.fileName, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

    
with Open_file("sample.txt", "w") as f:
    f.write("Det er godtg vejr, jubi!")

print(f.closed)