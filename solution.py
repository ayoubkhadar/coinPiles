def coinPiles(n,arr):
    return list(range(n,n*len(arr)+1,n)) == arr

def coinPiles(n,arr):
    newArr = []
    for num in arr:
        if num == n:
            continue
        newArr.append(num-n)
    newArr.append((len(arr)*n))
    return newArr == arr