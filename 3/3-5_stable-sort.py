import re
import copy

N = int(input())
list = list(input().split())
pattern = '[DHSC]'

def bubble_sort(N, cards):
  flag = 1
  while flag == 1:
    flag = 0
    for i in range(N - 1, 0, -1):
      if int(re.sub(pattern, '', cards[i])) < int(re.sub(pattern, '', cards[ i - 1])):
        cards[i], cards[i - 1] = cards[i - 1], cards[i]
        flag = 1
  print(' '.join(cards))
  print('Stable')
  return cards

def selection_sort(N, cards):
  for i in range(N):
    minj = i
    for j in range(i, N):
      # print(j)
      if int(re.sub(pattern, '', cards[j])) < int(re.sub(pattern, '', cards[minj])):
        minj = j

    cards[i], cards[minj] = cards[minj], cards[i]

  print(' '.join(cards))
  return cards

bubblelist = bubble_sort(N, copy.deepcopy(list))
selectionlist = selection_sort(N, copy.deepcopy(list))

print('Not stable') if bubblelist != selectionlist else print('Stable')