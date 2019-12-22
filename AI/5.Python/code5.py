a=[i**3+j**3+k**2 for i in range(1,10) for j in range(0,10) for k in range(0,10) if i*100+j*10+k==i**3+j**3+k**3]
print(a)
print("red\tyellow\tgreen\t")
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(0,7):
            if 8==red+yellow+green:
                print(red,'\t',yellow,'\t',green)