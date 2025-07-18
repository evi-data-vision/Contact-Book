from collections import defaultdict

class ContactBook :
    
    def __init__(self):
        self.contact = defaultdict(dict)
        self.id = 1

    def add_contact(self , name , phone , email = None) :
        if email is None : email = ''
        for key , value in self.contact.items() :
            if value['name'] == name and value['phone'] == phone :
                return ['exist' , (f'contact {name} already exists!')]
            
        id = self.id
        self.contact[id] = {'name' : name , 'phone' : phone , 'email' : email}
        self.id += 1
        return ['added' , (f'contact {name} added!')]

    def view_contacts(self) :
        return self.contact


    def get_contact(self , name) :
        keys = []
        finded_contact = defaultdict(dict)

        for key , value in self.contact.items() :
            if value['name'] == name :
                keys.append(key)
                finded_contact[key] = value
        
        return finded_contact


    def delete_contact(self , name , phone = None) :
        keys = self.get_contact(name)

        if len(keys) > 1 :
            for key in keys :
                if self.contact[key]['phone'] == phone :
                    del self.contact[key]
                    return (f'contact {name} deleted!')
                    
            else : return ('contact not found!')

        elif len(keys) == 1 :
            del self.contact[keys[0]]
            return (f'contact {name} deleted')

        else : return ('contact not found!')
    
    def update_contact(self , name , phone = None ,  new_name = None, new_phone = None , new_email = None) :
        keys = self.get_contact(name)

        if len(keys) > 1 :
            for key in keys :
                if self.contact[key]['phone'] == phone :
                    if new_name != '' : 
                        self.contact[key]['name'] = new_name
                    if new_phone != '' : 
                        self.contact[key]['phone'] = new_phone
                    if new_email != '' :
                        self.contact[key]['email'] = new_email
                    return (f'contact {name} updated!')
                    break
            else : 
                return ('contact not found!')

        elif len(keys) == 1 : 
            if new_name != '' : self.contact[key]['name'] = new_name
            if new_phone != '' : self.contact[key]['phone'] = new_phone
            if new_email != '' :self.contact[key]['email'] = new_email
            return (f'contact {name} updated!')
        else :    
            return ('contact not found!')

