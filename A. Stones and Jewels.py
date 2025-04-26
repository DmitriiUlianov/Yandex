"""
You are given two strings of lowercase Latin letters: string J and string S.
The characters in string J represent "jewels", and the characters in string S represent "stones".
You need to determine how many characters from S are also "jewels".
In simpler terms, you need to check how many characters from S are present in J.
"""
jewels = set(input())
stones = input()
count = 0
for i in jewels:
	count += stones.count(i)
            
print(count)
