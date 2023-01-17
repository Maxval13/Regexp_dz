import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def phones(i):
    pattern = r"(\+7|7|8)?\s?\(?(\d{3})\)?[\s-]?(\d{3})-?(\d{2})-?(\d{2})(\s?\(?(доб\.)\s?(\d{4})\)?)?"
    phone = r"+7(\2)\3-\4-\5 \7\8"
    result = re.sub(pattern, phone, str(contacts_list[i][5]))
    return result


def phonebooks():
    for i in range(len(contacts_list)):
        contacts_list[i][5] = phones(i)
        text = str(contacts_list[i][0]).split()
        if len(text) == 3:
            contacts_list[i][0] = text[0]
            contacts_list[i][1] = text[1]
            contacts_list[i][2] = text[2]
        elif len(text) == 1 and ' ' in contacts_list[i][1]:
            text = str(contacts_list[i][1]).split()
            contacts_list[i][1] = text[0]
            contacts_list[i][2] = text[1]
        elif len(text) == 2:
            contacts_list[i][0] = text[0]
            contacts_list[i][1] = text[1]

    return contacts_list


def finepeople():
    phonebooks()
    res_new = []
    res = {}
    for i in range(len(contacts_list)):
        text_list = str(contacts_list[i][0])
        if not text_list in res:
            res.setdefault(text_list, (contacts_list[i][1:]))
        else:
            value_1 = res[text_list]
            for j in range(6):
                if not value_1[j] and not contacts_list[i][j + 1]:
                    continue
                elif not value_1[j] and contacts_list[i][j + 1] != ' ':
                    value_1.pop(j)
                    value_1.insert(j, contacts_list[i][j + 1])
            res[text_list] = value_1

    new_v = []
    new_k = []
    for key, value_ in res.items():
        new_v.append(value_)
        new_k.append([key])
    for i in range(len(new_k)):
        res_new.insert(i, (new_k[i] + new_v[i]))

    return res_new