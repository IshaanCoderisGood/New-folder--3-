def non(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res
arr = []
n = int(input("Size of Array: "))
while (n):
    m = int(input("Enter numbers: "))
    arr.append(m)
    n = n-1
print("Odd Occuring number is: ", non(arr))
