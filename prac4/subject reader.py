"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject data.txt"


def main():
    data =get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    parts = []
    for line in input_file:
        part = line.split(',')
        part[2] = int(part[2])  # Make the number an integer (ignore PyCharm's warning)
        parts.append(part)
    input_file.close()
    return parts


main()
