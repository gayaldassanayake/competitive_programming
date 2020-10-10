n, h, d = map(int, input().strip().split())

tot = []
floor = []
for k in range(n):
    lst = list(map(int, input().strip().split()))
    tot.append(lst[0])
    floor.append([x-1 for x in lst[1:]])

count = [[0]*n for x in range(h)]

for i in range(n):
    for j in range(tot[i]):
        count[floor[i][j]][i]+=1

# print(count)
maxi = [[0]*n for x in range(h)]

maxi[h-1] = count[h-1]

best_val = [0]*h
best_val[h-1] = max(count[h-1])

for i in range(h-2,-1,-1):
    best_val[i] = 0
    for j in range(n):
        if i+d < h:
            maxi[i][j] = maxi[i+1][j] + count[i][j]
            if maxi[i][j]< best_val[i+d]+ count[i][j]:
                maxi[i][j] = best_val[i+d]+ count[i][j]
                
        else:
            maxi[i][j] = maxi[i+1][j]+ count[i][j]
        
        if maxi[i][j] > best_val[i]:
            best_val[i] = maxi[i][j]

print(max(maxi[0]))
        


