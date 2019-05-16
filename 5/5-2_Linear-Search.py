def _main():
  N = int(input())
  lst = list(map(int, input().split()))
  K = int(input())
  key_lst = list(map(int, input().split()))

  ans = 0
  for k in range(K):
    if search(lst, key_lst[k]): ans += 1

  print(ans)

def search(lst, key):
  lst.append(key)
  i = 0
  while lst[i] != key:
    i += 1
  lst.pop()
  return len(lst) != i

if __name__ == '__main__':
  _main()