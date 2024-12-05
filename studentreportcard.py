
name = input("Enter the student's name: ")
score1 = float(input("Enter score for subject 1: "))
score2 = float(input("Enter score for subject 2: "))
score3 = float(input("Enter score for subject 3: "))

if score1 < 35 or score2 < 35 or score3 < 35:
 result = "Fail"
else:

    total = score1 + score2 + score3
    average = total / 3

if average >= 60:
 result = "1st Class"
elif average >= 50:
 result = "2nd Class"
elif average >= 35:
 result = "Pass Class"
else:
 result = "Fail"

print("\nStudent Report Card")
print("Name:", name)
if result == "Fail":
 print("Result:", result)
else:
 print("Total:", total)
 print("Average:", average)
 print("Result:", result)