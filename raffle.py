import random

volunteer = ["Index", "xsquared", "elizabot", "Yeungx", "Carolina", "t.he.art", "Tamara_VA7ETR", "lionello", "omkar", "TankGuy"]

seeding = {}
seed_list = []

print("Generating Randomized ticket 1000-9999 for each volunteer")

for v in volunteer:		
	seed = random.randint(1, 9999)
	seeding[v] = seed
	seed_list.append(seed)

print(seeding)

# defines winning seed
print("drawing winning number between 1 and 9999")

winning_seed = random.randint(1, 9999)

print("winning number is " + str(winning_seed))

def closest(seed_list, winning_seed):
	return (seed_list[min(range(len(seed_list)), key = lambda i: abs(seed_list[i]-winning_seed))])

winner = closest(seed_list, winning_seed)

for s in seeding:
	if seeding[s] == winner:
		print("the winning number belongs to: " + s)
