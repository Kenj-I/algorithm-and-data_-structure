def _main():
  text = list(input())

  S1 = []
  S2 = []
  area = 0

  for i in range(len(text)):
    if text[i] == '\\':
      S1.append(i)
    elif text[i] == '/' and len(S1) > 0:
      j = S1.pop()
      section_area = i - j
      area += section_area
      while len(S2) > 0 and S2[-1][0] > j:
        print(S2[-1][0], j)
        section_area += S2[-1][1]
        S2.pop()
      S2.append([j, section_area])
    print('S1', S1)
    print('S2',S2)
    print('------------')

  print(area)
  print(len(S2), *[n[1] for n in S2])




if __name__ == '__main__':
  _main()