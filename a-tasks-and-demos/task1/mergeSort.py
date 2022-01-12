# This code is contributed by Mayank Khanna
# Found on https://www.geeksforgeeks.org/merge-sort/
# and modified to introduce a bug 

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        

        # Dividing the array elements
        left_arr = arr[:mid]


        # into 2 halves
        right_arr = arr[mid:]

        # Sorting the first half
        mergeSort(left_arr)

        # Sorting the second half
        mergeSort(right_arr)
        i = 0
        j = 0 
        k = 0

        # Copy data to temp arrays left_arr[] and right_arr[]
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = right_arr[i]
                i += 1
            else:
                arr[k] = left_arr[j]
                j += 1
            k += 1


        # Checking if any element was left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)


