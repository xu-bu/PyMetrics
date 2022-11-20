import os

def calculateSLOC(path):
    sum=0
    for i,j,k in os.walk(path):
        for each in k:
            if (each.endswith(".java")):
                try:
                    with open(path + each) as file:
                        SLOC = 0
                        for line in file:
                            if line in ['\n', '\r\n'] or line.strip() == "":
                                pass
                            else:
                                SLOC += 1
                        print(each, SLOC)
                        sum += SLOC
                except:
                    print("illegal path for "+path)


    return sum

# remember to add \\ at the end of the path
print(calculateSLOC("before\\src\\main\\java\\comp5911m\\cwk2\\"))
print(calculateSLOC("before\\src\\test\\java\\comp5911m\\cwk2\\"))
print(calculateSLOC("after\\src\\main\\java\\comp5911m\\cwk2\\"))
print(calculateSLOC("after\\src\\test\\java\\comp5911m\\cwk2\\"))


