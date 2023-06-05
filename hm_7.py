def binary_search(element, lst):
    lst = sorted(lst)
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == element:
            return mid
        elif guess > element:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


my_list = [5, 2, 3, 9, 1, 7]
target_element = 1

sorted_list = bubble_sort(my_list)
print("Отсортированный список:", sorted_list)

result = binary_search(target_element, sorted_list)
if result != -1:
    print("Число", target_element, "найден в списке на позиции", result)
else:
    print("Число", target_element, "не найден в списке.")
