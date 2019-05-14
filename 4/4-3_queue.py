def enqueue(x):
  global tail
  que.append(x)
  tail = (tail + 1) % N

def dequeue():
  head_v = que.pop(0)
  return head_v


N, Q = map(int, input().split())
list = [input().split() for _ in range(N)]
que = []
elaps = 0

for i in range(N):
  que.append([list[i][0], int(list[i][1])])
tail = N

while que:
  target = dequeue()
  c = min(Q, target[1])
  target[1] -= c
  elaps += c
  if target[1] > 0:
    enqueue(target)
  else:
    print(target[0], elaps)

