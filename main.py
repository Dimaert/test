import random

geg= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pas_len= int(input("введите длину пароля"))
pasworde= ""

for i in range(pas_len):
    pasworde += random.choice(geg)

print("Пароль:", pasworde)    
