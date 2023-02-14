import random


def main():
    # TASK 1: create list of 100 random numbers from 0 to 1000
    array_random = [random.randint(0, 1000) for _ in range(0, 100)]
    print(f'Created array:\n{array_random}\n')

    # TASK 2: sort list from min to max (without using sort())
    for i in range(len(array_random)):
        min = i # index of start min element
        for j in range(i + 1, len(array_random)):
            # select index of the smallest element by comparing j element with current min element
            if array_random[j] < array_random[min]:
                min = j
            # swap i element with the min element
        array_random[min], array_random[i] = array_random[i], array_random[min]

    print(f'Sorted array:\n{array_random}\n')

    '''TASK 3: calculate average for even and odd numbers
    TASK 4: print both average result in console 
    '''
    #use comparing remainder of division 
    odd_array = [i for i in array_random if i % 2]
    even_array = [i for i in array_random if i % 2 == 0]

    # use sum() and len() functions to find average value of array
    avg_odd = round(sum(odd_array) / len(odd_array), 2)
    avg_even = round(sum(even_array) / len(even_array), 2)

    print(f'The average of odd: {avg_odd}\nThe average of even: {avg_even}\n')

if __name__ == "__main__":
    main()