n, h, i = map(int, input().split())
buildings = []
for b in range(n):
    people = list(map(int, input().split()))
    u = people.pop(0)
    building = [0 for j in range(h)]
    for p in range(u):
        building[people[p]-1] += 1
    buildings.append(building)
dp = [[0 for j in range(n)] for k in range(h)]
max_height = [0]*h
for b in range(n):
    dp[h-1][b] = buildings[b][h-1]
    max_height[h-1] = max(max_height[h-1], dp[h-1][b])
max_people = 0
for _h in range(h-2, -1, -1):
    for b in range(n):
        dp[_h][b] = max(dp[_h][b], dp[_h+1][b] + buildings[b][_h])
        if(_h+i < h):
            dp[_h][b] = max(dp[_h][b], max_height[_h+i] + buildings[b][_h])
        max_height[_h] = max(max_height[_h], dp[_h][b])  
print(max(dp[0]))