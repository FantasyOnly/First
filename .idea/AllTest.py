# coding=UTF-8
import time
import datetime

def readFile(name,operation):
    file = open(name,operation)
    str=file.read()
    file.close()
    return str


def readFileBylines(name,operation):
    file=open(name,operation)
    list1=file.readlines()
    return list1


def writeFile(name,data,operation):
    file = open(name,operation)
    file.write(data)
    file.close()


def getTimeStamp(offset):
    the_time=time.time()
    return str(int(round(the_time * 1000))+offset) #毫秒级时间戳

if __name__ == "__main__":
    name="D:\wuhan.txt"

    new="D:\wuHanNew.txt"

    originData=readFile(name,'r')
    new_str=originData.replace(";","\n")
    writeFile(name,new_str,"w")
    fileList=readFileBylines(name,"r")
    for index in range(len(fileList)):
        new_item=getTimeStamp(index*1000*100)+" "+fileList[index]
        new_item=new_item.replace(","," ")
        new_item=new_item.replace("\n",",")
        writeFile(new,new_item,"a")

