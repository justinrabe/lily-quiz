qaTotal = {'A': [1, 2, 3],
            'B': [4,5,6],
            'C': [7,8,9]
}
print(qaTotal)
k = 'D'
if k in qaTotal.keys():
    qaTotal[k].append(4)
    print(qaTotal)
else:
    qaTotal[k] = [10]
    print(qaTotal)