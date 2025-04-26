'''
Time limit: 1 second
Memory limit: 64 MB
Input: standard input or input.txt
Output: standard output or output.txt

It's no secret that some programmers love to travel. The well-known programmer Petya also loves traveling, visiting museums, and sightseeing in different cities.
For traveling between cities, he prefers to use a car. However, he can only refuel at gas stations located inside cities, not at stations along the road.
Therefore, he must carefully choose his routes so that his car doesn't run out of fuel on the way.
Moreover, Petya is an important member of his team, so he cannot afford to spend too much time traveling.
He decided to write a program to help him choose his next trip.
But since he's currently overwhelmed with tasks, he asked you to help him.

The distance between two cities is calculated as the sum of the absolute differences of their coordinates (i.e., Manhattan distance).
There are roads between every pair of cities.

Input format
The first line contains a single integer n — the number of cities (2 ≤ n ≤ 10,000).
The next n lines each contain two integers — the coordinates of each city (each coordinate's absolute value does not exceed one billion).
The cities are numbered from 1 to n in the order they appear in the input.
The next line contains a positive integer k — the maximum distance Petya's car can travel without refueling (k does not exceed 2 billion).
The last line contains two different integers — the starting city number and the destination city number.

Output format
If there exists a path satisfying the described conditions, output the minimum number of roads Petya must travel to reach the destination city.
If no such path exists, output -1.

I used Breadth-First Search (BFS), which is a fundamental graph traversal algorithm. It begins with a node and first traverses all of its adjacent nodes. 
Once all adjacent nodes have been visited, it then traverses the adjacent nodes of those nodes.
'''

import sys
with open("input.txt", "r") as file:
    content = [line.strip() for line in file]

numberOfCities = int(content[0])
allCities = []
for cityCoord in content[1 : numberOfCities + 1]:
    allCities.append([int(i) for i in cityCoord.split()])
    
dist = int(content[numberOfCities + 1])
tripCities = content[-1].split()
firstCity = allCities[int(tripCities[0]) - 1]
lastCity = allCities[int(tripCities[1]) - 1]


citiesWithoutFirst = allCities.copy()
citiesWithoutFirst.remove(firstCity)

roads = 0
nextLayerOfCities = citiesWithoutFirst
currentLayerOfCities = [firstCity]

while currentLayerOfCities:
    visited = False
    visitedCities = []
    for fromCity in currentLayerOfCities:
        for toCity in nextLayerOfCities.copy():
            if abs(toCity[0] - fromCity[0]) + abs(toCity[1] - fromCity[1]) <= dist:
                if toCity == lastCity:
                    roads += 1
                    print(roads)
                    sys.exit()
                else:
                    visitedCities.append(toCity)
                    nextLayerOfCities.remove(toCity)
                visited = True
    
    if visited:       
        currentLayerOfCities = visitedCities.copy()
        roads += 1
    else:
        print(-1)
        sys.exit()
        
        
