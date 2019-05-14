def push(x):
  S.append(x)

def pop():
  return int(S.pop())

list = list(input().split())
S = []

for i in range(len(list)):
  if list[i] == '+':
    a = pop()
    b = pop()
    push(a + b)
  elif list[i] == '-':
    b = pop()
    a = pop()
    push(a - b)
  elif list[i] == '*':
    a = pop()
    b = pop()
    push(a * b)
  else :
    push(list[i])

print(S.pop())
