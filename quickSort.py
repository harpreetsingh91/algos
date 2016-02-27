#Author: Harpreet Singh
# A simple python implementation of quickSort

def quickSort(A,start,end):
    if(start<end):
        pIndex = partition(A,start,end)
        quickSort(A,start,pIndex-1)
        quickSort(A,pIndex+1,end)


def partition(A,start,end):
    pivot = A[end]
    pIndex = start
    for i in range(start,end):
        if (A[i]<=pivot):
            #swap A[i] and A[pIndex]
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
        #swap A[pIndex] and A[end]
    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex

#testing the algorithm
import random

A = []

for i in range (0,30):
    A.append(random.randint(0,100))

print "This is unsorted array \n"
print A

quickSort(A,0,len(A)-1)

print "This is sorted array \n"
print A
