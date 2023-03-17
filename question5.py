l = ["apple", "banana", "orange", "grape"]              
sorted_list = [''.join(sorted(i)) for i in l]
print("1: ",sorted_list)


l.sort()
print("2: ",l)

for i in l:
    print("3: ",i)

print("4: ",sorted(l))
