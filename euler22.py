__author__ = 'WillyLampert'

with open("euler22.txt") as file:
    names = file.readline()

names2 = names.replace("\"", "")

nameslist = names2.split(",")
nameslist.sort()

def search(dic, searchfor):
    temp1 = []
    for m in dic:
        if m in searchfor:
            y = searchfor.count(m)
            for z in range(1,y+1):
                temp1.append(m)
    return temp1

def alphabeticalscore(list1):
    scores = {"A":1, "B":2, "C":3, "D":4, "E":5, "F": 6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
    ascores = []
    temp2 = []
    for name in list1:
        temp2 = []
        temp1 = search(scores,name)
        for x in range(0,len(temp1)):
            temp2.append(scores[temp1[x]])
            if len(temp2) == len(temp1):
                ascores.append(sum(temp2))
    return ascores

def namescore(list2, ascores):
    nscores = []
    for name in list2:
        nscores.append((list2.index(name)+1) * ascores[list2.index(name)])
    return sum(nscores)







print namescore(nameslist, alphabeticalscore(nameslist))