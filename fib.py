# Rough fibonacci numbers generation program
n = 5
a, b = 0, 1
count = 0
print a
while count < n-1:
  a, b = b, a+b
  count += 1
  print b

