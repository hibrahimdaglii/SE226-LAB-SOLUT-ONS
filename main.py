from abc import ABC
import os

path = 'C:\\Users\\ibrahim\\Desktop\\strange.txt'
class Address(ABC):
    def __init__(self, path):
        self.path = path

    def calculateFreqs(self):
        pass

class ListCount(Address):
    def calculateFreqs(self):
        file = open('strange.txt', 'r')
        list = []
        for line in file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list.append(line_list)
        file.close()

class DictCount(Address):
    def calculateFreqs(self):
        file = open('strange.txt','r')

x = Address(path)
x.calculateFreqs()