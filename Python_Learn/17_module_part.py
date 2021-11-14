import random
from datetime import date
import emojis
emojified = emojis.encode("There is a :dog: in my boot !")
print(emojified)
today = date.today()

# dd/mm/YY
d1 = today.strftime("%b/%d/%Y")
print("d1 =", d1)

random_number = random.randint(1, 100)
print(random_number)
print(random.randint(100, 200))

rand=random.random()*100
print(rand)


list1=["jaymin","abc","def","hij"]
choice=random.choice(list1)
print(choice)
