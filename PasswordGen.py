
import random
import string


#def pwd():
pwd = ""
count = 0
length = int(input("How many characters would you like in your password? "))

while count != length:

     upper = [random.choice(string.ascii_uppercase)]
     lower = [random.choice(string.ascii_lowercase)]
     num = [random.choice(string.digits)]
     symbol = [random.choice(string.punctuation)]
     everything = upper + lower + num + symbol

     pwd += random.choice(everything)
     count += 1

     if count == length:
        print(pwd)

#print(pwd())