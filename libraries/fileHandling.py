
import os

class dataFile:
    def __init__(self, fileName):
        self.data = {}
        self.fileName = fileName + '.txt'
        
    def getData(self):
        file = open(self.fileName, 'r')
        for row in file.read().split('\n'):
            splitText = row.split('=')
            if len(splitText) > 1:
                if splitText[1].isdigit():
                    self.data[splitText[0]] = int(splitText[1])
                elif '.' in splitText[1]:
                    isString = 0
                    
                    for i in splitText[1].split('.'):
                        if not i.isdigit():
                            isString = 1
                    
                    if isString:
                        self.data[splitText[0]] = splitText[1]
                    else:
                        self.data[splitText[0]] = float(splitText[1])
                else:
                    self.data[splitText[0]] = splitText[1]
                
        file.close()
        return self.data
        
    def writeData(self, data):
        file = open(self.fileName, 'w')
        
        text = '\n'.join((row + '=' + str(data[row]) for row in data))
        
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