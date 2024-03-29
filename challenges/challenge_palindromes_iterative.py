def is_palindrome_iterative(word):
    low_index = 0
    high_index = len(word) - 1

    if not word:
        return False

    while low_index <= high_index:
        if word[low_index] != word[high_index]:
            return False
        else:
            low_index += 1
            high_index -= 1

    return True
