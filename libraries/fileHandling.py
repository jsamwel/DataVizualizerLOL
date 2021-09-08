
# library to handle textfiles for storage of data
# expects the data in the following format in the file:
# name=value

import os

class dataFile:
    def __init__(self, fileName):
        self.data = {}
        self.fileName = fileName
        
    def getData(self):
        file = open(self.fileName, 'r')
        
        name = 0
        value = 1
        
        # split data received from file.read to a name and a value. This is then put in 
        # a dictionary
        
        for row in file.read().split('\n'):
            splitText = row.split('=')
            if len(splitText) > 1:
                # check what type of data the value is and converts it to that type
                
                if splitText[value].isdigit():
                    self.data[splitText[name]] = int(splitText[value])
                elif '.' in splitText[value]:
                    isString = 0
                    
                    for i in splitText[value].split('.'):
                        if not i.isdigit():
                            isString = 1
                    
                    if isString:
                        self.data[splitText[name]] = splitText[value]
                    else:
                        self.data[splitText[name]] = float(splitText[value])
                else:
                    self.data[splitText[name]] = splitText[value]
                
        file.close()
        return self.data
        
    def writeData(self, data):
        file = open(self.fileName, 'w')
        
        # joins the data from a dictionary into a single string
        text = '\n'.join((row + '=' + str(data[row]) for row in data))
        
        # write data and close file
        file.write(text)
        file.close()
    
    def createFile(self):
        try:
            file = open(self.fileName, 'x')
            file.close()
            
            return 1
        except:
            return 0
            
    def checkExists(self):
        return os.path.exists(self.fileName)