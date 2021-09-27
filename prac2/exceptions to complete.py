"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number=int(input("Enter the number: "))
        finished=True
        result=number
        # TODO: this line
        # TODO: this line
    except ValueError:# TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
