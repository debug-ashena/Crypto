import random
from hashlib import sha256
import hashlib
import numpy
#usname=input('Username: ')
#uspass=input('Password:')
# sha256(data).hexdigest()

#print(hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest())

#print(hashlib.sha256(b"Your Desire String here").hexdigest())
#print(uspass.__hash__())
#print(hash(uspass))
class User:
    def __init__(self , name , password):
        self.name=name
        self.password= password
    def __eq__(self, other):
        return self.name== other.name \
        and self.password==other.password
    def __hash__(self):
        return hash((self.name , self.password))
    def __str__(self):
        return f'{self.name} {self.password}'

user1=User(input('Please Insert your name:'),input('Please insert your pass:'))
user2=User('Elnaz Azizi' , 'E@13999q')
users={user1,user2}
print(len(users))

print("Hash of user1: ")
print(hash(user1))
print("Hash of user2: ")
print(hash(user2))
print('-------------%%%-------------')
#user1.password=input('Change your pass:')
if (user1==user2):
    print('same user')
    print('f{user1} == {user2}')
else:
    print('Different Users')