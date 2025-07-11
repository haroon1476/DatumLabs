def printFibonacciSeries(num1, num2):
    fibonacciSeries = [num1, num2]  

    for i in range(10): 
        nextValue = num1 + num2
        fibonacciSeries.append(nextValue)    
        num1 = num2
        num2 = nextValue

    for element in fibonacciSeries:
        print(element)


printFibonacciSeries(0,1)      


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j 

        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


myArr = [12,22,3,23,54,23,12,2]
sortedArr = selection_sort(myArr)
for elem in sortedArr:
    print(elem)



def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str 
    return reversed_str


print(reverse_string('This is a sentence'))

def printTable(num) :
    for i in range (1,11,1):
        print(f"{num}*{i} = {num*i}")


printTable(7)