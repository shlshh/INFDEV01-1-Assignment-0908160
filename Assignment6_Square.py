size = int(raw_input("Size: "))

vierkant = ""
for i in range(0, size):
    for j in range(0, size):
        vierkant += "*"
    vierkant += "\n"

print vierkant