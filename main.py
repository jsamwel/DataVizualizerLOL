
# See the following websites for more information
# https://developer.riotgames.com/apis
# https://github.com/Canisback/pantheon

import sys
import PyQt5.QtWidgets as Qt
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor

from libraries import dataFile, retrieveDataLOL

class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

class AppDemo(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Recent League of Legends Matches')
        self.resize(500, 700)

        treeView = Qt.QTreeView()
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        #get data latest matches 
        dataRetriever = retrieveDataLOL()
        
        #get configuration LOL api and write to class
        configFile = dataFile("config.txt")
        dataRetriever.setServerConfig(configFile.getData())
        
        dataRetriever.startServerConnection()
        #dataMatches = dataRetriever.getDataLatestMatches(3)
        dataMatches = dataRetriever.getTimelinesMatches(2)
        
        #visualize data
        self.__addRows(rootNode, dataMatches)

        treeView.setModel(treeModel)

        self.setCentralWidget(treeView)

    def __addRows(self, currentRow, data):
        if isinstance(data, list):
            for i in range(len(data)):
                var = data[i]
                
                if isinstance(var, list) or isinstance(var, dict):
                    row = StandardItem(str(i + 1) + ": " + type(var).__name__)
                    currentRow.appendRow(row)
                    self.__addRows(row, var)
                    
        elif isinstance(data, dict):
            for var in data:
                if isinstance(data[var], list) or isinstance(data[var], dict):
                    row = StandardItem(var + ": " + type(data[var]).__name__)
                    currentRow.appendRow(row)
                    self.__addRows(row, data[var])
                else:
                    row = StandardItem(var + ": " + str(data[var]))
                    currentRow.appendRow(row)
                    
app = Qt.QApplication(sys.argv)        

demo = AppDemo()
demo.show()

sys.exit(app.exec_())