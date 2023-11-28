#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i:02d}, {j:02d}", end=", " if (i != 8 or j != 9) else "\n")
        
