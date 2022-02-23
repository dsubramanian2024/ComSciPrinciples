'''
Mergesort
Author: Divya Subramanian
Time Complexity: O(nlogn)
    The function continuously divides the arry by 2 until all the elements are separated
which contributes to the logn, and merging and comparing the elements in the correct order
contributes to the N, so the big O notation is O(nlogn)
'''

def merge(arr, first, second):
    '''This function takes in an array and two segment of the array. It then arranges th elements in both segments in order in the arr. The function returns the merged arr'''
    count1 = count2 = c = 0

    while (count1 < len(first) and count2 < len(second)):
        if first[count1] < second[count2]:
            arr[c] = first[count1]
            count1 += 1
        else:
            arr[c] = second[count2]
            count2 += 1
        c += 1
    #checks to see if any elements were not included
    while count1 < len(first):
        arr[c] = first[count1]
        count1 += 1
        c += 1
    while count2 < len(second):
        arr[c] = second[count2]
        count2 += 1
        c += 1

def mergeSort(arr):
    '''This function recursively calls itslef until each element in the array is separated. Then, it merges them back together in the proper order.'''
    if len(arr) > 1:
        m = len(arr)//2 # Finding the middle of the array
        first = arr[:m]
        second = arr[m:]

        mergeSort(first) # Sorts the first half
        mergeSort(second) # Sorts the second half
        merge(arr, first, second)


'''
  Selection Sort
  Author: Laura Liu
  run time: O(n^2)
  Each time, the code runs through the whole list to find the minimum and move it to the front.
  It does this repeatedly for each term in the list, so the time complexity is O(n^2)
 '''

def selection_sort(nList):
  '''returns nList sorted from least to greatest using selection sort'''
  l = len(nList)
  if l < 2:
    return nList

  minIndex = 0
  for i in range(l):
    if nList[i] < nList[minIndex]:
      minIndex = i

  nList[0], nList[minIndex] = nList[minIndex], nList[0]
  return [nList[0]] + selection_sort(nList[1:])


def callfunc(arr):
  print("The starting array is: ")
  print(arr)
  print("\nAfter selection sort: ")
  print(selection_sort(arr))
  print("\nAfter mergesort: ")
  mergeSort(arr)
  print(arr)
  print("\n\n")


callfunc([1, 7, 3, 8, 3, 6, 1, 34, 9, 5])
callfunc([])
callfunc([1])
callfunc([1, 2, 1, 1, 1, 4, 1, 1,])
