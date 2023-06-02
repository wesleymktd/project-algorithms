def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)

    return array


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def count_chars(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def compar_anagrams(str1_ord, str2_ord):
    count1 = count_chars(str1_ord)
    count2 = count_chars(str2_ord)

    return count1 == count2


def is_anagram(first_string, second_string):

    first = list(first_string.lower())
    second = list(second_string.lower())

    list1_ord = quicksort(first)
    list2_ord = quicksort(second)

    str1_ord = "".join(list1_ord)
    str2_ord = "".join(list2_ord)

    result = compar_anagrams(str1_ord, str2_ord)

    if len(first) == 0 or len(second) == 0:
        return (str1_ord, str2_ord, False)

    return (str1_ord, str2_ord, result)
