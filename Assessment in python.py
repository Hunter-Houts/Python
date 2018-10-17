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
    new_arr = []
    for name in arr:
        new_arr.append(name.title())
    return " ".join(new_arr)


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
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(analyze_word(arr[i]))
    return new_arr


def pad_array(arr, length, fill):
    return arr[:length] + [fill] * (length - len(arr))


def main():
    print(remove9s([1, 2, 3, 9, 9, 9]))
    print(is_ten(10))
    print(is_ten(9))
    print(double(2))
    print(capitalize_name("hunter"))
    print(capitalize_all_names(["hunter", "houts"]))
    print(count_vowels("aeiouu"))
    print(analyze_word("hunter"))
    print(analyze_all_words(["hunter", "houts"]))
    print(pad_array(["a", "b", "c"], 9, "Filler"))


if __name__ == "__main__":
    main()
