""" ------- PYTHON DSA ------- """

"""
1.arrays

from array import *
arr = array("i", [1, 2, 3, 4])
# insering
arr.insert(0, 5)
# deleting
arr.pop(1)
# accesing and searching
for i in range(0, len(arr)):
    if arr[i] == 4:
        print(i)
print(arr)

2. Searching (main concept traversing and finding the element) 

from array import *

a = int(input("Enter your element to search: "))
arr = array("i", [1, 2, 3, 4])
for i in range(0, len(arr)):
    if arr[i] == a:
        print(f"We found the element {a} at position {i}")
        break
else:
    print(f"{a} not found")
    
3. Recursion ()

n = int(input())
def fact(n):
    if n <= 1:
        return 1 
    else:
        return n * fact(n-1). #check each fact of other n-1 element
print(fact(n))        

4. binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0  # left boundary of the search
        r = len(nums) - 1  # right boundary of the search
        while l <= r:
            m = (l + r) // 2  # middle index
            if target == nums[m]:  # target found
                return m
            elif target > nums[m]:  # target is in the right half
                l = m + 1
            elif target < nums[m]:  # target is in the left half
                r = m - 1
        return 'target cant be found'  # target not found
        
5. Bubble sort 

arr = [1,5,10,2,11]
for i in range(0, len(arr) - 1):
    for j in range(0, len(arr) - 1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
print(arr)

6. Selection sort

arr = [4,5,1,3,2]
for pos in range(len(arr) -1):
    min = pos
    for i in range(pos+1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    arr[min],arr[pos] = arr[pos],arr[min]
print(arr)
 
7. Insertion sort

arr = [7, 1, 4, 5, 3, 2]
for i in range(1, len(arr)):
    cur = arr[i]
    j = i - 1
    while j >= 0 and cur < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = cur    
print(arr)

8. Merge sort

def merge_sort(arr):
    # Base case: an array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    # Merge elements from left and right arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # Append any remaining elements from left or right
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Example usage
arr = [4, 5, 1, 3, 2]
sorted_arr = merge_sort(arr)
print(sorted_arr)

9. quick sort

import random
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]
    return quicksort(left) + middle + quicksort(right)
    
arr = [3,2,5,7,6,9,1,4,8]    
print(arr)

quicksort(arr)
print(quicksort(arr))

10. 2 pointer algorithm        

arr  = [1,2,3,4,5,6] #O(n)
Target = 10
print(f"target: {Target}")
l = 0
r = len(arr) - 1
while(l < r):
    act = arr[l] + arr[r]
    if act == Target:
        print(f"index : [{l},{r}]")
        print(f"value : [{arr[l]},{arr[r]}]")
        break
    if act < Target:
        l = l+1
    if act > Target:
        r = r-1
print(f"sorted : {arr}")        
    
11. Stack

# Initialize an empty stack
stack = []
# Push items onto the stack
stack.append(10)  # push 10
stack.append(20)  # push 20
stack.append(30)  # push 30
# Check if the stack is empty
is_empty = len(stack) == 0
print("Is stack empty?", is_empty)  # False
# Peek at the top item
top_item = stack[-1] if not is_empty else None
print("Top item is:", top_item)  # 30
# Get the size of the stack
stack_size = len(stack)
print("Stack size is:", stack_size)  # 3
# Pop items from the stack
popped_item = stack.pop() if not is_empty else None
print("Popped item:", popped_item)  # 30
popped_item = stack.pop() if len(stack) > 0 else None
print("Popped item:", popped_item)  # 20
# Peek at the new top item
top_item = stack[-1] if len(stack) > 0 else None
print("Top item is:", top_item)  # 10
# Final size of the stack
stack_size = len(stack)
print("Final stack size:", stack_size)  # 1

12.queue

from queue import Queue
q = Queue()
q.put("hi") #adding an element
x = q.get() #accesing the object
print(x)

13. linked list

# lst = [1,2,3,4,5]
# print(id(lst[0]))
# print(id(lst[1]))
# #131928978030832
# #131928978030864

class Student:
    def __init__(self, name, age):
        self.name = name  # Student's name
        self.age = age    # Student's age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

class Node:
    def __init__(self, student):
        self.student = student  # The student object stored in the node
        self.next = None        # Initially, the next node is None

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the linked list is empty

    def append(self, student):
        new_node = Node(student)
        
        if not self.head:  # If the list is empty, the new node becomes the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse the list until the last node
                current = current.next
            current.next = new_node  # Link the last node to the new node

    def display(self):
        current = self.head
        while current:
            print(current.student)  # Print the student object (via __str__ method)
            current = current.next
        print("End of list")

# Example usage
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 21)

ll = LinkedList()
ll.append(student1)
ll.append(student2)
ll.append(student3)

ll.display()  # Output: Alice (20 years old), Bob (22 years old), Charlie (21 years old)

14. Dynamic programming

# n = int(input())
# lst = []
# a, b = 0, 1
# for _ in range(n):
#     lst.append(a)
#     a, b = b, a+b
# print(lst)

# bottom up approach 

# def fact(n):
#     lst = [0] * n
#     lst[0] = 0
#     lst[1] = 1
#     for i in range(2, n):
#         lst[i] = lst[i-1] + lst[i-2]
#     print(lst)    
# fact(int(input()))

# top down approach 

# def fibo(n, memory):
#     if n in memory:
#         return memory[n]
#     if n <= 2:
#         return 1
#     memory[n] = fibo(n-1, memory) + fibo(n-2, memory)
#     return memory[n]
        
# print(fibo(9, {}))        
        
15. backtracking(nqueen)
"""      
# N = int(input())
# for i in range(N):
#     for j in range(N):
#         print("0", end = " ")
#     print()

# def count(days):
#     return (days -2) // 7 +1
# print(count(28))    
# things needed board, size, start, 
def safe(board, row, col, size):
    # Check the same row to the left
    i = col
    while i >= 0:
        if board[row][i] == 1:
            return False
        i -= 1

    # Check the upper diagonal to the left
    i, j = col, row
    while i >= 0 and j >= 0:
        if board[j][i] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal to the left
    i, j = col, row
    while i >= 0 and j < size:
        if board[j][i] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(board, col, size):
    # Base case: If all queens are placed, print the board
    if col >= size:
        print_board(board, size)
        return True

    # Try placing a queen in all rows for the current column
    for row in range(size):
        if safe(board, row, col, size):
            board[row][col] = 1  # Place the queen

            # Recur for the next column
            if solve(board, col + 1, size):
                return True

            # Backtrack if placing the queen doesn't lead to a solution
            board[row][col] = 0

    return False

def print_board(board, size):
    for row in range(size):
        for col in range(size):
            print("Q" if board[row][col] == 1 else ".", end=" ")
        print()
    print("\n")

# Input board size and solve the problem
size = int(input("Enter the size of the board: "))
board = [[0 for _ in range(size)] for _ in range(size)]

if not solve(board, 0, size):
    print("No solution exists!")




   






















































































































































































































































































