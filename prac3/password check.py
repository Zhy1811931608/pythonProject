def main():
    get_password=input("Enter your password: ")
    length=len(get_password)
    print_asterisks(length)
def print_asterisks(number):
    for i in range(number):
        print('*',end='')
main()
