from pprint import pprint
import csv
import re

PHONE_PAT = r'(\+7|8)?[\s(.]*(\d{3})[.)\s-]*(\d{3})[.-]*(\d{2})[.-]*(\d{2})[.\s(]*(доб.)*[.\s-]*(\d+)*[)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'
new_list = []
final_list = []
set_names = set()


def sort_contacts(csv_contacts):
    with open(csv_contacts, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    for contact in contacts_list:
        fio = ' '.join(contact[:3]).split(' ')
        filtered_contacts = [fio[0], fio[1], fio[2], contact[3], contact[4],
                             re.sub(PHONE_PAT, PHONE_SUB, contact[5]), contact[6]]
        new_list.append(filtered_contacts)

        for c in range(len(new_list)):
            if new_list[c][0] == fio[0] and new_list[c][1] == fio[1]:
                if new_list[c][2] == "":
                    new_list[c][2] = fio[2]
                if new_list[c][3] == "":
                    new_list[c][3] = contact[3]
                if new_list[c][4] == "":
                    new_list[c][4] = contact[4]
                if new_list[c][5] == "":
                    new_list[c][5] = contact[5]
                if new_list[c][6] == "":
                    new_list[c][6] = contact[6]

    for c in new_list:
        if (c[0] + c[1]) not in set_names:
            final_list.append(c)
            set_names.add(c[0] + c[1])

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_list)
    return final_list


if __name__ == '__main__':

    sorted_contact_list = sort_contacts('phonebook_raw.csv')
    pprint(sorted_contact_list)



