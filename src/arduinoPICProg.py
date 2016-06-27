import serial
import os
import subprocess
import time

class HexFile:
    def __init__(self,x):
        self.x=x
    def Read(self,filename): #Reads a specific hex file
        self.filename=filename
        filept=open(self.filename,'r')
        self.file_contents=filept.read()
        filept.close()
    def printHex(self):
        print(self.file_contents)
    def splitContents(self):
        #Hex File Format
        # :BBAAAARRDDDD...DDCC
        # : -start 
        # BB: Number of Bytes in Data Field
        # AAAA: 16 bit (2bytes) address
        # DDDD: Data
        # CC  : 2 bytes checksum
        lines=self.file_contents.splitlines()
        i=-1
        self.elements=[]
        for line in lines:
            i=i+1
            self.elements.append([]) #new array of list inside                                    existing array
            data_end_i= 9+String2Int(line[1:3])*2 #data end index
            self.elements[i]=[line[1:3],line[3:7],line[7:9],line[9:data_end_i],line[data_end_i:]]
            print self.elements[i]
    def SendData(self):
        index_dict={'NDataBytes':0,'Address':1,'Record':2,'Data':3,'Checksum':4}
        ser=serial.Serial('/dev/tty.usbmodem1421',9600,timeout=3.0)
        ser.flush()
        n=ser.inWaiting()
        print n
        time.sleep(1)
        b=ser.write('C')
        print "b:",b
        time.sleep(1)
        a=ser.read(100)
        print a
        ser.close()
    
   
        
def String2Int(str_hex):
    hexdict={'A':10,
             'B':11,'C':12,'D':13,'E':14,'F':15}
    value=0;
    index=len(str_hex)-1;
    for i in str_hex:
        if ord(i)>64:
            temp=hexdict[i]
        else:
            temp=int(i)
        value=value+temp*(16**index)
        index-=1
    return value
        








#a=bytes(bytearray([i for i in range(0,256)]))

hex1=HexFile(10)
hex1.Read('test.hex')
hex1.splitContents()
#hex1.SendData()
    




