#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.

import random

# Ask user for inputs
num_dice = int(input("How many dice are being rolled? "))
hit_target = int(input("What is the hit target? (e.g., 3 means 3+ to hit): "))

print("\nRolling dice...\n")

hits = 0

for i in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Die {i + 1}: {roll}")
    
    if roll >= hit_target:
        hits += 1

print(f"\nTotal Hits: {hits} out of {num_dice}")