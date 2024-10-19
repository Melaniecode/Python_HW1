import ast

def add_n(lst, n):
  n = n if n else '0'
  return [str(item) + n for item in lst]

lst = ast.literal_eval(input("請輸入一串列（如 ['a', 'b', 123]）： "))
n = input("請輸入一字串： ")
print(add_n(lst, n))
