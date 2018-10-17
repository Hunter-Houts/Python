def is_ten(num):
    if num == 10:
        return True
    else:
        return False


def double(num):
    return num + num


def remove9s(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] != 9:
            new_arr.append(arr[i])
    return new_arr


def capitalize_name(s):
    return s.title()


def capitalize_all_names(arr):
    for i in range(len(arr)):
        if i < len(arr):
            print(arr[i].title())
            i += 1


def count_vowels(s):
    s.lower()
    a = s.count("a")
    e = s.count("e")
    i = s.count("i")
    o = s.count("o")
    u = s.count("u")
    total_count = a + e + i + o + u
    return total_count


def average_sales(arr):
    sales = 0
    for i in range(len(arr)):
        sales += arr[i].sales

    return sales / len(arr)


def analyze_word(s):
    class Obj:
        name = s
        numberOfLetters = len(s)
        numberOfVowels = count_vowels(s.lower())

    return [Obj.name, Obj.numberOfLetters, Obj.numberOfVowels]


def analyze_all_words(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(analyze_word(arr[i]))
    return newArr


def pad_array(arr, length, fill):
    for i in range(len(arr)):
        if i <= length and not i >= length:
            arr = arr.append(fill)
        return arr
