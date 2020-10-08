print("Weight in Planet Calculations")
def calc_weight_on_planet(weight, gravity=23.1):
    mass = float(weight)/9.8
    q = float(mass)*float(gravity)
    return q

#input the numbers in the calc_weight_on_planet(), the gravity is optional
print("Your weight in this planet ", calc_weight_on_planet(120))
print("(If you didn't input any gravity, by default it's Jupiter)")