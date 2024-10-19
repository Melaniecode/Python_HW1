import ast

def make_dict(keys, values):
    if not values:
        values = [0] * len(keys) 
    return dict(zip(keys, values))

keys = ast.literal_eval(input("請輸入第一個串列如[0,1,2]： "))
values_input = input("請輸入第二個串列如[32,43,55]： ")

values = ast.literal_eval(values_input) if values_input else None

print(make_dict(keys, values))
