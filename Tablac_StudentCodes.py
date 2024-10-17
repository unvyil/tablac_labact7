# Basic info about the user
name = (input("Enter your name: "))
section = (input("Enter your section: "))

# Transmuted grade for each term
prelim = round(float(input(f"Enter your prelim grade: ")), 2)
midterm = round(float(input(f"Enter your midterm grade: ")), 2)
final = round(float(input(f"Enter your final grade: ")), 2)

if (prelim >= 40 and prelim <= 100) and (midterm >= 40 and midterm <= 100) and (final >= 40 and final <= 100):    
    prelim = (33.33 * prelim) / 100
    midterm = (33.33 * midterm) / 100
    final = (33.33 * final) / 100
    
# GPA computation
    gpavg = round((prelim + midterm + final))
    print(f"Your FINAL GRADE is {gpavg}")

# GPA Percentage 
if (gpavg == 99 and gpavg == 100):
    percentage = 1.00
    print("Your GPA is 1.00")
    
elif gpavg >= 96:
    percentage = 1.25
    print("Your GPA is 1.25")
    
elif gpavg >= 93:
    percentage = 1.50
    print("Your GPA is 1.50")

elif gpavg >= 90:
    percentage = 1.75
    print("Your GPA is 1.75")
    
elif gpavg >= 87:
    percentage = 2.00
    print("Your GPA is 2.00")
    
elif gpavg >= 84:
    percentage = 2.25
    print("Your GPA is 2.25")

elif gpavg >= 81:
    percentage = 2.50
    print("Your GPA is 2.50")
    
elif gpavg >= 78:
    percentage = 2.75
    print("Your GPA is 2.75")
    
elif gpavg >= 75:
    percentage = 3.00
    print("Your GPA is 3.00")

elif gpavg >= 40:
    percentage = 5.00
    print("Your GPA is 5.00")
    
# Errors
else:
    print("Error: Invalid input.")
    if (prelim < 40 or prelim > 100):
        print("Invalid grade.")
    if (midterm < 40 or midterm > 100):
        print("Invalid grade.")
    if (final < 40 or final > 100):
        print("Invalid grade.")
