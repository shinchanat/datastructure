
def triangle_sum(array):

    if len(array) == 1:
        print(array)
        return
    
    triangle_sum(addConElements(array))
    print(array)
    

def addConElements(array,index = 0):

    if index == len(array) - 2:
        return [array[index]+array[index+1]]

    return [array[index] + array[index+1]] + addConElements(array,index+1)


def minElement(array,_min,index = 0):

    if index == len(array) -1 :
        print(_min)
        return

    if _min > array[index+1]:
        minElement(array,array[index+1],index+1)
    else:
        minElement(array,_min,index+1)

def maxElement(array,_max,index = 0):

    if index == len(array) - 1:
        print(_max)
        return

    if _max < array[index+1]:
        maxElement(array,array[index+1],index+1)
    else:
        maxElement(array,_max,index+1)

def minElementItr(array):

    length = len(array)

    _min  = array[0]

    for idx in range(1,length):
        if _min > array[idx]:
            _min = array[idx]
    print(_min)

def maxElementItr(array):

    length = len(array)

    _max = array[0]

    for idx in range(1,length):
        if _max < array[idx]:
            _max = array[idx]
    print(_max)

def firstUpperCaseLetter(string):

    if not string:
        return None

    if string[0].isupper():
        return string[0]
    else:
        return firstUpperCaseLetter(string[1:])

def firstUpperCaseLetterItr(string):

    length = len(string)
    char = ''
    for idx in range(length):
        if string[idx].isupper():
            char = string[idx]
            break

    return char

def binarySearch(array,target):


    index = len(array) // 2

    if array[index] == target:

        return "Found"
    
    elif len(array) == 1:
        
        return "Not found"

    elif array[index] > target:
        
        return binarySearch(array[:index],target)
    else:
        return binarySearch(array[index:],target)

    
def reverse_string(string):

    if len(string) == 1:
        return string

    return reverse_string(string[1:]) + string[0]

def palindrome(string):

    return reverse_string(string) == string


def palindrome2(string,length,index = 0):

    if index == len(string)//2:
        return True

    return  string[index] == string[length - index - 1] and palindrome2(string,length,index + 1 )

def palindrome_itr(string):

    length = len(string)

    for idx in range(length):

        if string[idx] != string[length - idx - 1]:
            return False
    return True

def pattern(row , column):

    if row < 0:
        return

    if column < row:
        pattern(row,column+1)
        print("*",end = ' ')
    else:
        pattern(row-1,0)
        print()


def SortedOrNot(array,index = 0):

    if index == len(array) - 1:
        return True

    return array[index] < array[index+1] and SortedOrNot(array,index+1)

def power(number,base,result = 1):

    if base == 0:
        return result

    return power(number,base-1,result*number)


def powerOf2(power,result = 1):

    if power == 0:
        return result

    return powerOf2(power-1,result*2)

def powerOf3(power,result = 1):
    if power == 0:
        return result
    return powerOf3(power-1,result*3)

def findItr(string,word):

    for idx in range(len(string)):
        if string[idx:].startswith(word):
            return True
    return False

def find(string,word):

    if not string:
        return False

    if string[0:].startswith(word):
        return True
    else:
        return find(string[1:],word)

def removeWord(string,word,new_string = ''):

    if not string:
        return new_string


    if string[0:].startswith(word):
        return removeWord(string[len(word):],word,new_string)
    else:
        return removeWord(string[1:],word,new_string+string[0])

def removeWordItr(string,word):

    new_string = ''
    idx = 0
    while idx < len(string):
        if string[idx:].startswith(word):
            idx += len(word)
        else:
            new_string += string[idx]
        idx += 1

    return new_string

def removeWordForItr(string,word):

    index = 0
    new_string = ''
    for idx in range(len(string)):

        if len(string)<=index:
            break
        
        if string[index:].startswith(word):
            index += len(word)
        else:
            new_string += string[index]
        index += 1
    return new_string


def  isFloat(string,point_count = 0):

    if not string and point_count == 1:
        return True
    elif not string and point_count != 1:
        return False

    if string[0] == '.' or not string[idx].isdigit():
       return isFloat(string[1:],point_count+1)
    else:
        return isFloat(string[1:],point_count)

def isFloatItr(string):

    point_count = 0

    for idx in range(len(string)):
        if string[idx] == '.' or not string[idx].isdigit():
            point_count += 1

    return True if point_count == 1 else False

def isInt(string):

    if not string:
        return True
    
    if string[0] == '.' or not string.isdigit():
        return False
    else:
        return isInt(string[1:])
            

def replace(string,word,new_word,new_string=''):

    if not string:
        return new_string
    

    if string[0:].startswith(word) and string[2] ==' ':
        return replace(string[len(word):],word,new_word,new_string+new_word)
    else:
        return replace(string[1:],word,new_word,new_string+string[0])

def wordLength(string,count=0):

    if not string:
        return count

    return wordLength(string[1:],count+1)

def isBinary(string):

    if not string:
        return True

    if string[0] == '1' or string[0] == '0':
        return isBinary(string[1:])
    else:
        return False

def isIntItr(string):

    for idx in range(len(string)):

        if string[idx] == '.' or not string[idx].isdigit():
            return False
    return True

def isBinaryItr(string):

    for idx in range(len(string)):

        if string[idx] != '1' and string[idx] != '0':
            return False
    return True

def isSameWord(string,other,idx = 0):

    if len(string) != len(other):
        return False

    if idx == len(string):
        return True

    return string[idx] == other[idx] and isSameWord(string[1:],other[1:],idx+1)

def isSameWordItr(string,other):

    if len(string) != len(other):
        return False

    for idx in range(len(string)):
        if string[idx] != other[idx]:
            return False
    return True
        

    
print(replace("harish is keerthana","is","loves"))
print(wordLength("harish"))
print(removeWordForItr("shinchan is a japanese cartoon , shinchan is my cartoon","cartoon"))
print(isInt('13456'))
print(isBinary('1011011'))
print(isIntItr("1236"))
print(isBinaryItr("1123"))
print(isSameWord("harish","harih"))
print(isSameWordItr("harish","har5sh"))
