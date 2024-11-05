import random

namelist = ['Sarah', 'Jackson', 'John', 'Emily', 'Arben', 'Molly', 'Joe']
print('Names already in rotation:')# This shows the user what names are already in use so there are no doubles
print(namelist)
namelist.append(input('Enter a name:'))
namelist.append(input('Enter a name:'))
namelist.append(input('Enter a name:'))
# There are seven names already in the list, and 3 others will be inputted

agelist = [34, 88, 42, 12, 7, 19, 23]
print('Ages already in rotation:')
print(agelist)
agelist.append(input('Enter an age:'))
agelist.append(input('Enter an age:'))
agelist.append(input('Enter an age:'))
# Same for the Age
print("\033[H\033[J", end="")
#This is a little copy-paste I found on stack overflow that just clears the console. It's pretty helpful for keeping things organized while running the code.

haircolor = ['Blonde', 'Red', 'Brown', 'Gray', 'Black']
random_hair_color = random.choice(haircolor)
#This chooses a random hair color

def height():
    return str(random.randint(4,7)) + " foot " +   str(random.randint(1,11)) + " inches"
#This chooses a random height

def IQ():
    return random.randint(50,170)
    
COD_KD_ratio = []
for i in range(1,11):
    COD_KD_ratio.append(random.randint(1000, 2000)/random.randint(500, 2000))
#unique little characteristic for the funzies


NPC1 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC2 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC3 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC4 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC5 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC6 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC7 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC8 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC9 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]

NPC10 = [random.choice(namelist), random.choice(agelist), random_hair_color, height(), IQ(), random.choice(COD_KD_ratio)]
#these are all the different NPCs

NPCs = [NPC1, NPC2, NPC3, NPC4, NPC5, NPC6, NPC7, NPC8, NPC9, NPC10]
#this variable compiles them all
def info(n):
    print()
    print("------------------------ \n")#this little line separates the NPCs so you can actually read them
    print('Name: ' + n[0] + '\n')
    print('Age: ' + str(n[1]) + '\n')
    print('Hair color: ' + n[2] + '\n')
    print('Height: ' + n[3] + '\n')
    print('IQ: ' + str(n[4])+ '\n')
    print('K/D ratio in Call of Duty: ' + str(n[5]))
#this is a function that actually prints out the data stored in the different NPCs

for i in NPCs:
    info(i)
#this loops the command so that each NPC's data gets shown
