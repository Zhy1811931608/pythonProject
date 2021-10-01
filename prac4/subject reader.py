"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject data.txt"


def main():
    data =get_data()
    print(data)
    print_detail()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    parts = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        part = line.split(',')  # Separate the data into its parts
        part[2] = int(part[2])  # Make the number an integer (ignore PyCharm's warning)
        print(part)  # See if that worked
        print("----------")
        parts.append(part)
    input_file.close()
    return parts

def print_detail():
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        part = line.split(',')
        print('{} is taught by {} and has {} students'.format(part[0], part[1], part[2]))
    input_file.close()

main()
