 # coding: utf-8
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



def isPointinPolygon(point, rangelist):  #[[0,0],[1,1],[0,1],[0,0]] [1,0.8]
     # 判断是否在外包矩形内，如果不在，直接返回false
    lnglist = []
    latlist = []
    for i in range(len(rangelist)-1):
        lnglist.append(rangelist[i][0])
        latlist.append(rangelist[i][1])
    print(lnglist, latlist)
    maxlng = max(lnglist)
    minlng = min(lnglist)
    maxlat = max(latlist)
    minlat = min(latlist)
    print(maxlng, minlng, maxlat, minlat)
    if (point[0] > maxlng or point[0] < minlng or point[1] > maxlat or point[1] < minlat):
        return False
    count = 0
    point1 = rangelist[0]
    for i in range(1, len(rangelist)):
        point2 = rangelist[i]
        # 点与多边形顶点重合
        if (point[0] == point1[0] and point[1] == point1[1]) or (point[0] == point2[0] and point[1] == point2[1]):
            print("在顶点上")
            return False
        # 判断线段两端点是否在射线两侧 不在肯定不相交 射线（-∞，lat）（lng,lat）
        if (point1[1] < point[1] and point2[1] >= point[1]) or (point1[1] >= point[1] and point2[1] < point[1]):
            # 求线段与射线交点 再和lat比较
            point12lng = point2[0] - (point2[1] - point[1]) * (point2[0] - point1[0])/(point2[1] - point1[1])
            print(point12lng)
            # 点在多边形边上
            if (point12lng == point[0]):
                print("点在多边形边上")
                return False
                if (point12lng < point[0]):
                    count +=1
                    point1 = point2
            print(count)
            if count%2 == 0:
                 return False
            else:
                  return True

if __name__ == '__main__':
    name="D:\wuhan.txt"

    new="D:\wuHanNew.txt"

    fileList=readFileBylines(name,"r")
    newList=[]
    for item in fileList:
        itemList=item.split(",")
        itemList[1]=itemList[1].replace("\n","")
        itemList[0]=float(itemList[0])
        itemList[1]=float(itemList[1])
        newList.append(itemList)
print(isPointinPolygon([114.317984,30.595931], newList))