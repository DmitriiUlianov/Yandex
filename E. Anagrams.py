'''
Time limit: 1 second
Memory limit: 20 MB
Input: standard input or input.txt
Output: standard output or output.txt

You are given two strings consisting of lowercase Latin letters.
You need to determine whether these two strings are anagrams of each other, meaning they differ only in the order of their characters.

Input format
The input file contains two strings of lowercase Latin letters, each no longer than 100,000 characters.
The strings are separated by a newline character.

Output format
The output file should contain 1 if the strings are anagrams, and 0 otherwise.
'''

str1 = input()
str2 = input()
s_str1 = sorted(str1)
s_str2 = sorted(str2)

if s_str1 == s_str2:
  print(1)
else:
  print(0)
