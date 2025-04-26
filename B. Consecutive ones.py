"""
You are required to find the longest sequence of consecutive ones in a binary vector and output its length.

The solution should ideally work in linear time and pass through the input array only once.

Input format:
The first line of the input file contains a single number n, where n ≤ 10000. Each of the following n lines contains exactly one number — an element of the array.

Output format:
The output file should contain a single number — the length of the longest sequence of consecutive ones in the input array.
"""

num = int(input())
count = 0
ones =[]
while num > 0:
    digit = int(input())
    if digit == 1:
        count += 1
    elif count > 0:
        ones.append(count)
        count = 0
    num -= 1

ones.append(count)

print(max(ones)) if ones else print(0)
