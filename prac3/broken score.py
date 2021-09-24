def main():
    score = float(input("Enter score: "))
    print(get_score(score))
def get_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:  # 相当于 if score<100 and score>=90
        return "Excellent"
    elif score >= 50:
        return "Possibal"
    else:
        return "Bad"
main()

