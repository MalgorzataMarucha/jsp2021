x = list(range(3,100,3))
print(x)
del x[4::3]
print (x)
print("len:",len(x))
print("sum:",sum(x))
print(sum(x)/len(x))