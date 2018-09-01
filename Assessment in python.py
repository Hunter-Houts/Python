def isTen(num):
    if(num == 10):
        return True
    else:
        return False
def double(num):
    return num + num
def remove9s(arr):
    newArr = []
    for i in range(len(arr)):
        if arr[i] != 9:
            newArr.append(arr[i])
    return newArr
        
def capitalizeName(str):
    return str.title()
def capitalizeAllNames(arr):
    for i in range(len(arr)):
        if i < len(arr):
            print(arr[i].title())
            i += 1

        

def countVowels(str):
    str.lower()
    a = str.count("a")
    e = str.count("e")
    i = str.count("i")
    o = str.count("o")
    u = str.count("u")
    totalCount = a+e+i+o+u
    return totalCount
def averageSales(arr):
    lenth = len(arr)
    sales = 0
    i = 0
    for i in length:
        sales += arr[i].sales
        i += 1
    return sales/length
def analyzeWord(str):
    class obj:
        name = str
        numberOfLetters = len(str)
        numberOfVowels = countVowels(str.lower())
    
    return [obj.name, obj.numberOfLetters, obj.numberOfVowels]
def analyzeAllWords(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(analyzeWord(arr[i]))
        i += 1
    return newArr
def padArray(arr, length, fill):
    for i in range(len(arr)):
        if i <= length and i >= length == False:
            arr = arr.append(fill)
            i += 1
        return arr
        
        
        
    
    
