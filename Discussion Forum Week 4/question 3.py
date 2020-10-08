print("Number of atoms counter")
def num_atoms(grams, atomic_weight=196.97):
    element = float(grams/atomic_weight)*(6.022*10**23)
    return element

#input the numbers in the num_atpms(), the atomic weight is optional
print("The number of atoms is ", num_atoms(10))
print("(If you didn't input any atomic weight, by default it's gold(Au))")