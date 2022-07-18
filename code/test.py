id_num = "970103-1234567"
num_list = list(id_num)
num_list[-6:] = "******"
id_num1 = ''.join(num_list)
print(id_num1)
