# F1 = (x ∨ ¬y) → (w ≡ z)
# F2 = (x ∨ ¬y) ≡ (w → z)
'''

print("x,y,w,z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f1 = (x or not(y)) <= (w ==z)
                f2 = (x or not(y)) == (w <= z)
                print(x,y,w,z,int(f1),int(f2))
'''
print('ywxz')