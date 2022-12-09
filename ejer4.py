def fibonacci(num):
  if num < 0: return (-1)**(num % 2 + 1) * fibonacci(-num)
  a = b = x = 1
  c = y = 0
  while num:
    if num % 2 == 0:
      (a, b, c) = (a**2 + b**2, a * b + b * c, b**2 + c**2)
      num /= 2
    else:
      (x, y) = (a * x + b * y, b * x + c * y)
      num -= 1
  return y

print(fibonacci(1000))