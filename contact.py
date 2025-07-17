from collections import defaultdict

class ContactBook :
    
    def __init__(self):
        self.contact = defaultdict(dict)
        self.id = 1

    def add_contact(self , name , phone , email = None) :
        id = self.id
        self.contact[id] = {'name' : name , 'phone' : phone , 'email' : email}
        print(f'contact {name} added!')
        self.id += 1


    def view_contacts(self) :
        for key , value in self.contact.items() :
            print(f'\nname : {self.contact[key]["name"]}')
            print(f'phone : {self.contact[key]["phone"]}')
            print(f'email : {self.contact[key]["email"]}')
            print('_' * 50)


    def get_contact(self , name) :
        keys = []

        for key , value in self.contact.items() :
            if value['name'] == name :
                keys.append(key)

        for key in keys :
            print(f'\nname : {self.contact[key]["name"]}')
            print(f'phone : {self.contact[key]["phone"]}')
            print(f'email : {self.contact[key]["email"]}')
            print('_' * 50)
        
        if keys == [] : print('contact not found!')


    def delete_contact(self , name) :
        keys = []

        for key ,value in self.contact.items() :
            if value['name'] == name :
                keys.append(key)

        if len(keys) > 1 :
            self.get_contact(name)
            print('\nplease enter the phone of contact that you want to delete')
            phone = input('phone : ')
            for key in keys :
                if self.contact[key]['phone'] == phone :
                    del self.contact[key]
                    print(f'contact {name} deleted!')
                    break
            else : print('contact not found!')
        
        elif len(keys) == 1 :
            del self.contact[keys[0]]
            print(f'contact {name} deleted')

        else : print('contact not found!')

    
    def update_contact(self , name , new_phone , new_email = None , new_name = None) :
        keys = []

        for key , value in self.contact.items() :
            if value['name'] == name :
                keys.append(key)
        if len(keys) > 1 :
            self.get_contact(name)
            print('\nplease enter the phone of contact that you want to update')
            phone = input('phone : ')
            for key in keys :
                if self.contact[key]['phone'] == phone :
                    if new_name != '' : 
                        self.contact[key]['name'] = new_name
                    if new_phone != '' : 
                        self.contact[key]['phone'] = new_phone
                    if new_email != '' :
                        self.contact[key]['email'] = new_email
                    print(f'contact {name} updated!')
                    break
            else : 
                print('contact not found!')

        elif len(keys) == 1 : 
            if new_name != '' : self.contact[key]['name'] = new_name
            if new_phone != '' : self.contact[key]['phone'] = new_phone
            if new_email != '' :self.contact[key]['email'] = new_email
            print(f'contact {name} updated!')
        else :    
            print('contact not found!')

