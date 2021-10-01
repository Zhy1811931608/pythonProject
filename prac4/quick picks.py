import random
quick_picks = int(input('How many quick picks? '))
for i in range(quick_picks):
   CONSTANTA = []
   for j in range(6):
      numbers = random.randint(1, 45)
      CONSTANTA.append(numbers)
   CONSTANTA.sort()
   for k in range(6):
      print(CONSTANTA[k], ' ', end='')
   print()
