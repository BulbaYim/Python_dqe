import random

def main():
    #TASK 1: create list of 100 random numbers from 0 to 1000

    #random.randint(0, 1000) - returns random integer from 0 to 1000
    #for i in range(0,100) - 100 iterations of the loop

    array_random = array_random_2 = [random.randint(0, 1000) for i in range(0,100)]

    print(f'Created array:\n{array_random}\n')


    #TASK 2: sort list from min to max (without using sort())

    for i in range(len(array_random)):
            #select index of start min element
            min = i
            
            for j in range(i + 1, len(array_random)):
                # select index of the smallest element by comparing j element with current min element
                
                if array_random[j] < array_random[min]:
                    min = j

            # swap i element with the min element
            array_random[min], array_random[i] = array_random[i], array_random[min]

    print(f'Sorted array:\n{array_random}\n')

    #TASK 3: calculate average for even and odd numbers
    #TASK 4: print both average result in console 

    #1 method

    #get arrays of odd and even elements by comparing remainder of division 
    odd_array_1 = [i for i in array_random if i % 2 == 1]
    even_array_1 = [i for i in array_random if i % 2 == 0]

    # use sum() and len() functions to find average value of array, round() is used to round value
    avg_odd_1 = round(sum(odd_array_1) / len(odd_array_1), 2)
    avg_even_1 = round(sum(even_array_1) / len(even_array_1), 2)

    print(f'The first method:\nThe average of odd: {avg_odd_1} \nThe average of even: {avg_even_1}\n')

    #2 method

    even_sum = even_count = odd_sum = odd_count = 0

    for i in range(0, len(array_random)):
        
        #if remainder of division == 0, then even numeral, else odd
        if array_random[i] % 2 == 0:
            even_count += 1                 #use as counter of elements
            even_sum += array_random[i] #use as sum of elemetns
        else: 
            odd_count += 1
            odd_sum += array_random[i]

    print(f'The second method:\nThe average of odd: {round((odd_sum/odd_count), 2)} \nThe average of even: {round((even_sum/even_count), 2)}')


if __name__ == "__main__":
    main()