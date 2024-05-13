from collections import UserDict

class Field:
    def __init__(self, value): 
        self.value = value

    def __str__(self): 
        return str(self.value)

class Name(Field):
    def __init__(self, name): 
        self.value = name

class Phone(Field):
    def __init__(self, number):
        self.value = number 

class Record:
    def __init__(self, name): 
        self.name = Name(name) 
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    # Method to add phone to record
    def add_phone(self, number: str): 
        self.phones.append(Phone(number))

    # Method to remove phone from record
    def remove_phone(self, number: str):
        self.phones = list(filter(lambda phone: phone == number, self.phones))

    # Method to edit phone in the record
    def edit_phone(self, old_number, new_number):
        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    # Method to find phone in record
    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone

class AddressBook(UserDict):
     # Method to add record to address book
    def add_record(self, record):
        self.data[record.name.value] = record

     # Method to edit record in address book
    def find(self, name):
        return self.data.get(name)

    # Method to delete record from address book
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        


