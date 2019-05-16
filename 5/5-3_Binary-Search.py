def _main():
  N = int(input())
  lst = list(map(int, input().split()))
  K = int(input())
  key_lst = list(map(int, input().split()))

  ans = 0
  for k in range(K):
    if binary_search(N, lst, key_lst[k]): ans += 1
  print(ans)

def binary_search(N ,lst, key):
  left = 0
  right = N
  while left < right:
    mid = (left + right) // 2
    if lst[mid] == key:
      return True
    elif key < lst[mid]:
      right = mid
    else:
      left = mid + 1
  return False

if __name__ == '__main__':
  _main()