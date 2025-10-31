#Function to perform bubble sort on a given list
def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] < arr[j+1]:   # Swap if the element found is greater
                temp = arr[j]       # Swap operation
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

if __name__ == "__main__":
    print("Enter the number of elements: ")
    n = int(input())
    arr = []
    print("Enter the elements: ")
    for i in range(n):
        element = int(input())
        arr.append(element)

    sorted_arr = bubble_sort(arr)
    print("Sorted array is: "+str(sorted_arr))
    