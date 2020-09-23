print("To find acceleration using Newton's Second Law")
mass, force = [mass for mass in input("Enter the mass in kg and the force in N, separated by comma: ").split(",")]
print("The acceleration is ", float(force) / float(mass))