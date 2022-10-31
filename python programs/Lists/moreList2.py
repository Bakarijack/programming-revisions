import random

names = ['Bakari','Mtua','Kilu','Jack']

current_name = random.choice(names)
print(current_name)

current_name2 = random.sample(names, 2)

print(current_name2)

s= ' abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*() '

for i in range(10):
    print(random.choice(s),end=" ")
    
players = ['ibrahim','Jamal','Saumu','Rehema','Mariam','Bakari']
random.shuffle(players)

for p in players:
    print(p," is your turn now")
    
random.shuffle(players)
teams = []
for i in range(0,len(players),2):
    teams.append([players[i],players[i+1]])
    print(teams)