N = int(input())

minv = int(input())
maxv = -20000000000
for i in range(N - 1):
  v = int(input())
  maxv = max(maxv, v - minv)
  minv = min(minv, v)
print(maxv)
