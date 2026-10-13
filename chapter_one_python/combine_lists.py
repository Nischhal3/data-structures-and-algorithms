
# Exercise: Combine Two Sorted Lists
#
# Write a function that combines two already-sorted lists
# into one sorted list without using a sorting function.

def combine_lists(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Add any remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result