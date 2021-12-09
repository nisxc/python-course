import csv
from os import write


class Contact:
    def __init__(self, name, phone) -> None:
        self.__name = name
        self.__phone = phone


class Phone():
    def __init__(self) -> None:
        super().__init__()
        self.__contacts = []

    def load_contacts(self):
        with open('contacts.csv', newline='') as CSVFile:
            reader = csv.DictReader(CSVFile)
            for row in reader:
                self.__contacts.append(row)

    def export_contacts(self):
        with open('export_contacts.csv', 'w', newline='') as CSVFile:
            writer = csv.DictWriter(CSVFile, fieldnames=['Name', 'Phone'])
            writer.writeheader()
            for contact in self.__contacts:
                writer.writerow(contact)

    def get_contacts(self):
        return self.__contacts

    def search_contact(self, phrase):
        count = 0
        for contact in self.__contacts:
            if phrase.lower() in contact['Name'].lower() or phrase in contact['Phone']:
                count += 1
                print('{0} {1}'.format(contact['Name'], contact['Phone']))
        print('Search result count:', count)


phone = Phone()
phone.load_contacts()
print(phone.get_contacts())
phone.search_contact('mother')
phone.export_contacts()
