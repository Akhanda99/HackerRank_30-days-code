# 30 Days of Code
# Day 20: Sorting

def sorting(element_number, listOFnumber):
    count = 0
    for i in range(element_number - 1):
        for j in range(0, element_number - i - 1):
            if listOFnumber[j] > listOFnumber[j + 1]:
                listOFnumber[j], listOFnumber[j + 1] = listOFnumber[j + 1], listOFnumber[j]
                count += 1
    return count



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    numberOfSwap= sorting(n,a)
    print("Array is sorted in " + str(numberOfSwap) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n - 1]))

