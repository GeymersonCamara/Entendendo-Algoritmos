def soma(arr):
    if arr == []:
        return 0
    return arr[0] + soma(arr[1:])
    
print(soma([2, 4, 6]))