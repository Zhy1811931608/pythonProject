out_file = open("results.txt", 'w')
def main():
    import random
    for i in range(4):
        number=random.randint(0, 100)
        print('{:.0f} is {}'.format(number,results(number)))
        print('{:.0f} is {}'.format(number, results(number)), file=out_file)
def results(number):
    if number < 0 or number > 100:
        return "Invalid score"
    elif number >= 90:  # 相当于 if score<100 and score>=90
        return "Excellent"
    elif number >= 50:
        return "Possibal"
    else:
        return "Bad"
main()