from collections import Counter


def repeat_major_one(dictionary):
    filtered_keys = [key for key, value in dictionary.items() if value >= 2]
    return not len(filtered_keys) <= 1 or filtered_keys == []


def find_duplicate(nums=[]):

    if len(nums) <= 1 or not isinstance(nums, list):
        return False

    counter = Counter(nums)

    if repeat_major_one(counter):
        return False

    for num in nums:
        if num < 0:
            return False

    filtered_keys = [key for key, value in counter.items() if value >= 2]

    return filtered_keys[0]
