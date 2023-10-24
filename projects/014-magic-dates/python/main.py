def is_magic_date(day, month, year):
    year = year % 100
    return True if (day * month) == year else False 


def main():

    day = int(input("Please enter a day: "))
    month = int(input("Enter a month: "))
    while month < 1 or month > 12:
        print('Error. Month must be an integer between 1 and 12.')
        month = int(input("Enter a month: "))

        year = int(input("Enter a year from 20th century: "))
    while year < 1900 or year > 1999:
        print("Error. Please enter a year between 1900 and 1999.")
        year = int(input("Enter a year from 20th century: "))

    print(is_magic_date(day, month, year))


if __name__ == "__main__":
    main()