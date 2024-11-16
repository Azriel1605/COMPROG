word = input().lower()

target = "halo dunia"
benar = 0

for i, j in zip(target, word):
    if i == j:
        benar +=1
        
print(benar)