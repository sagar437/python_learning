def end_other(a, b):
  for i in range(len(a)):
    if a[-len(b):].lower() == b.lower():
      print("True")
  print("False")
str1= 'HiAbC'
str2 = 'abc'
