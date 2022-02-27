array = list(map(int, input('Введите числа (через пробел): ').split()))
any_number = int(input('Введите любое число: '))

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, any_number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == any_number:
        return middle
    elif any_number < array[middle]:
        return binary_search(array, any_number, left, middle - 1)
    else:
        return binary_search(array, any_number, middle + 1, right)


while True:
    try:
        any_number = int(any_number)
        break
    except ValueError:
        print('Введите только целое число!')
        any_number = input('Введите число повторно: ')

if any_number in array:
    print(array)
else:
    array.append(any_number)
print(array)

sort_array = merge_sort(array)
print(*sort_array)


print('Индекс введеного числа:', binary_search(sort_array, any_number, 0, len(sort_array)))
