def count_hi(str):
  count = 0
  for i in range(len(str) - 1):
    print(str[i:i+2])
    if str[i:i+2] == 'hi':
      print(str[i:i+1])
      count += 1
  return count
str = 'iamhisa'
count_hi(str)
