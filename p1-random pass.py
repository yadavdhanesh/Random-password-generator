# PROJECT 1 - Use a Python script to generate a random password of 8 characters.
# 2 uppercase letters from A to Z,
# 2 lowercase letters from a to z,
# 2 digits from 0 to 9,
# 2 punctuation signs such as !, ?, “, # etc.

import random

u1=chr(random.randint(65,90))
u2=chr(random.randint(65,90))

l1=chr(random.randint(97,122))
l2=chr(random.randint(97,122))

d1=str(random.randint(0,9))
d2=str(random.randint(0,9))

lst=[chr(random.randint(33,40)),chr(random.randint(58,64)),chr(random.randint(41,47)),chr(random.randint(33,40))]
pun1=random.choice(lst)
pun2=random.choice(lst)

pas=u1+u2+l1+l2+d1+d2+pun1+pun2

pass_lst=list(pas)
random.shuffle(pass_lst)

password="".join(pass_lst)
print(password)