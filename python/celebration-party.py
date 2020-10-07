def getGroups(children):
    lastChild=len(children)
    currentChild=1
    startingPoint=0
    groups=0
    while(currentChild<lastChild):
        if(children[currentChild]-children[startingPoint]>1):
            startingPoint=currentChild
            groups+=1
        if(currentChild==lastChild-1):
            groups+=1
        currentChild+=1
    return groups

if __name__ == '__main__':
    input_n = int(input())
    l=list(map(float,input().split()))
    print(getGroups(sorted(l)))
