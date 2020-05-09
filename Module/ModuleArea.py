#We are creating a Module named ModuleArea

#creating func
def triangleCal(b,h):
    area=.05*(b*h)
    return area



def ractangleCal(b, h):
    area = b * h
    return area


def compareArea(a,b):
    if a>b:
        return a
    else:return b


#Now we can use above functions from other file just after importing