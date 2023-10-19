#3
def sort_books_by_field(book, field):
    return sorted(book, key=lambda x: x[field])

#6
def sort_by_count(list):

    max_val = max(list)
    min_val = min(list)

    counter = [0] * (max_val - min_val + 1)

    for num in list:
        counter[num - min_val] += 1

    list_sort = []
    for i in range(len(counter)):
        list_sort.extend([i + min_val] * counter[i])

    return list_sort

#8
def merge_sort(list):
    if len(list) > 1:
        
        half = len(list) // 2
        half_left = list[:half]
        half_right = list[half:]

        merge_sort(half_left)
        merge_sort(half_right)

        i = j = k = 0

        while i < len(half_left) and j < len(half_right):
            if half_left[i] < half_right[j]:
                list[k] = half_left[i]
                i += 1
            else:
                list[k] = half_right[j]
                j += 1
            k += 1

        while i < len(half_left):
            list[k] = half_left[i]
            i += 1
            k += 1

        while j < len(half_right):
            list[k] = half_right[j]
            j += 1
            k += 1