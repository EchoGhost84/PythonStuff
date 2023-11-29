# this file is just for where i can test things without effecting the actual project

import random

ammount = ['1','2','3','4','5']

password_list_ammount = []

for int in range(1, ammount + 1):
    password_list_ammount.append(random.choice(ammount))

while ammount:
    print("you will print" + ammount + "passwords")



