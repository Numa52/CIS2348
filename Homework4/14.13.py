#Ryan Nguyen PSID: 1805277

#creating a simple class
def selection_sort_descend_trace(lst):
    #going through the range of numbers
    for i in range(len(lst) - 1):
        largest_value_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[largest_value_index]:
                largest_value_index = j
        lst[i], lst[largest_value_index] = lst[largest_value_index], lst[i]
        #creating an array of numbers
        for x in lst:
            print(x, end=' ')
        print()
    return lst

#if statement
if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
