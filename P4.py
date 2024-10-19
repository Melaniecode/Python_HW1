import ast

lst_input = ast.literal_eval(input("請輸入一整數串列（如 [-3,6,100,300]）： "))

lst = list(filter(lambda x: 0 <= x <= 255, lst_input))

print(lst)
