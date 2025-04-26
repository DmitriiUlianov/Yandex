"""
Legend
You are given a sorted array of 32-bit integers in non-decreasing order. The task is to remove all duplicates from the array.
It is desirable to obtain a solution that does not read the entire input file into memory, i.e., it should use only constant memory during execution.

Input Format
The first line of the input file contains a single integer n, where n ≤ 1,000,000.
The next n lines contain integers — elements of the array, one per line. The integers are sorted in non-decreasing order.

Output Format
The output file should contain the unique elements of the input array in ascending order.
"""

num = int(input())
const = -2**31 - 1
while num > 0:
    digit = int(input())
    if const < digit:
        print(digit)
        const = digit
    num -= 1

