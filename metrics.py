import collections
import inspect
import os
import sys


map=dict()

# eval(exec) may print string, disable it
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def main(path):
    # recursively traverse all directories
    def importFiles():
        files = []
        for i, j, k in os.walk(path):
            # sys.path.append(i)
            sys.path.insert(1,i)
            for each in k:
                if os.path.isdir(each):
                    files+=importFiles()
                elif each.endswith(".py"):
                    files.append(i+'\\'+each)
        return files

    files=importFiles()

    classes=[]
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                if line.startswith("class"):
                    line=line.split(' ')[1][:-2]
                    line=line.split('(')[0]
                    classes.append(line)
    classObjList=[]
    blockPrint()
    for each in classes:
        s = f"from {each} import *"
        eval(f'exec("{s}")')
        classObjList.append(eval(each))
    enablePrint()
    print("the instability of each class is:")
    print(instability(classObjList))
    print("the abstractness of this project is:")
    print(abstractness(classObjList))


def instability(classList):
    global map
    for classObj in classList:
        dep=set()
        for each in classObj.__dict__.items():
            tmp=eval(f'classObj.{each[0]}')
            if (inspect.isfunction(tmp)):
                dic = tmp.__annotations__
                if (dic != None):
                    for kv in dic.items():
                        dep.add(tmp.__annotations__[kv[0]].__name__)
        map[classObj.__name__]=dep
    dic={}
    for each in map.keys():
        dic[each]=0
    for key,val in map.items():
        for each in val:
            dic[each] += 1
    for key, val in dic.items():
        dic[key]=len(map[key])/(dic[key]+len(map[key]))
    return dic


def abstractness(classList):
    abstract=sum(1 for each in classList if inspect.isabstract(each))
    return abstract/len(classList)

if __name__ == '__main__':
    main(sys.argv[1])
