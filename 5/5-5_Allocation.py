import sys
input = sys.stdin.readline

max_n = 100000
max_k = 100000
max_w = 10000


def check(p):
  global N, K, T

  i = 0
  for k in range(K):
    s = 0
    while s + T[i] <= p:
      s += T[i]
      i += 1
      if i == N: return N
  return i

def solve():
  left = 0
  right = max_k * max_w

  while right - left > 1:
    mid = (left + right) // 2
    v = check(mid)
    if (v >= N):
      right = mid
    else:
      left = mid
  return right


if __name__ == '__main__':
  N, K = map(int, input().split())
  T = [int(input()) for _ in range(N)]

  ans = solve()
  print(ans)
