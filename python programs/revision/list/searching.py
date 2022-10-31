#linear Search
def linearSearch(list, key):
    for i in range(len(list)):
        if key == list[i]:
            return i
    
    return -1 #not found

def main():
    mylist = [1,4,56,6,5,4,6,0,8,7,6,5,4,43,3,22,44]

    print(linearSearch(mylist, 4))
    print(binarySearch(mylist, 4))
    print(mylist[3])


def binarySearch(list, key):
    list.sort()
    low = 0
    high = len(list) - 1
   

    while high >= low:
        mid = (low + high) // 2

        if key < list[mid]:
            high = mid - 1
        elif key == list[mid]:
            return mid    
        else:
            low = mid + 1
    
    return -1 #not found 


main() #calling the main function
