import csv
from Regexp import finepeople


if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        new_list = finepeople()
        datawriter.writerows(new_list)