print("x,y,w,z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f1 = bool((w or not(y)) <= (z == x))
                f2 = bool((w or not(y)) == (x <= z))
                print(x,y,w,z,int(f1),int(f2))
