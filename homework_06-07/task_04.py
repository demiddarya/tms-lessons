from functools import reduce
user = input().split()
s = input()
def my_join():
    for i in user:
        return [(i + s) for i in user]
agard= reduce(lambda x,y: x+y , my_join())
print(agard)
