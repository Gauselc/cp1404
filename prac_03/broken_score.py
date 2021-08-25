import random


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))
    score = random.randint(0, 101)
    print("Random score: {}".format(score))
    print(determine_score(score))


def determine_score(score):
    """Determine score grade"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"



main()
