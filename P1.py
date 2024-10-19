import ast

def combine(t1, t2):
    return t1 + t2

t1 = ast.literal_eval(input("請輸入第一個序對如(2,4,6)： "))
t2 = ast.literal_eval(input("請輸入第二個序對如(1,2,3)： "))

print(combine(t1, t2))