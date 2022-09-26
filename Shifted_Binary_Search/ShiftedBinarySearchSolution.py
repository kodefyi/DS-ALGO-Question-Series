#time complexity-O(n) | space complexity-O(1)

def shiftedBinarySearch(array, target):
    return shiftedhelp(array,target,0,len(array)-1)

def shiftedhelp(array,target,leftindex,rightindex):
    while leftindex <= rightindex:
        middleindex=(leftindex+rightindex)//2
        leftelement=array[leftindex]
        rightelement=array[rightindex]
        midelement=array[middleindex]
        if midelement == target:
            return middleindex
        elif leftelement <= midelement :
            if target < midelement and target >=leftelement:
                rightindex=middleindex-1
            else:
                leftindex=middleindex+1
        else:
            if target > midelement and target <=rightelement:
                leftindex=middleindex+1
            else:
                rightindex=middleindex-1

    return -1