#!/bin/python3
# 30 Days of Code
# Day 11: 2D Arrays


def get_hourglass_sum(matrix,row,col):
    sum=0
    sum+=matrix[row-1][col-1]
    sum+=matrix[row-1][col]
    sum+=matrix[row-1][col+1]
    sum+=matrix[row][col]
    sum+=matrix[row+1][col-1]
    sum += matrix[row + 1][col]
    sum += matrix[row + 1][col + 1]
    return sum


arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

max_hourglass_sum=-100
for i in range(1,5):
    for j in range(1,5):
        current_hourglass_sum= get_hourglass_sum(arr,i,j)
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum= current_hourglass_sum

print(max_hourglass_sum)

