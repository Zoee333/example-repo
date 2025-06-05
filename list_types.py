# Code written by Zoe - started 23/04/2025

# Create a list of 3 friend's names
friends_names = ["Aasiyah", "Erin", "Shallum"]

# Print the first name, last name, and list length
print(f"The first friend's name is {friends_names[0]}.")
print(f"The last friend's name is {friends_names[-1]}.")
print(f"The length of the friend's list is {len(friends_names)}.")

# Create a list storing the friend's ages relatively
friends_ages = [24, 21, 19]

# Print each friend's name and age in a sentence
for friend in range(0, 3):
    print(f"{friends_names[friend]} is {friends_ages[friend]} years old.")
