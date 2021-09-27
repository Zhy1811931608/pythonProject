
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:                #相当于 if score<100 and score>=90
    print("Excellent")
elif score >= 50:
    print("Possibal")
else:
     print("Bad")


