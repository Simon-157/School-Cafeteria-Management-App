from cafeteria import *

class App:
    app_register = 'app_register.txt'
    
    def __init__(self):
        self.list_registered_cafeterias = []
        self.list_registered_cafeterias_obj = []
        
    def register_cafeteria(self, cafeteria):
        if not isinstance(cafeteria, Cafeterias):
            raise TypeError
        else:
            for item in self.list_registered_cafeterias:
                    if cafeteria.cafeteria_name in item:
                        return False
            self.list_registered_cafeterias.append((cafeteria.cafeteria_name, cafeteria.institution, cafeteria.location))
        self.list_registered_cafeterias_obj.append(cafeteria)
            
            
    def loading_registeredCafeteriaData_from_file(self):
        self.list_registered_cafeterias.clear()
        file = open(App.app_register)
        cafeterias_details = file.readline()
        cafeteria_details_list = cafeterias_details.split('\t')
        for cafeteria_details in cafeteria_details_list:
            account = cafeteria_details.split(' ')
            self.list_registered_cafeterias.append(account)

            
    def add_registered_cafeteria_to_file(self):
        file = open(App.app_register, 'w')
        for account in self.list_registered_cafeterias:
            file.write('{}\t'.format(' '.join(account)))
    
        file.close()

##instance of the app; if any other we want to register any other institution we will create an instance of the app here manually 
AshesiCafeteriasApp = App()

cafeteria1 = Cafeterias('Big Ben','Hive', 'Ashesi')
cafeteria2 = Cafeterias('Akorno', 'Hive', 'Ashesi')
cafeteria3 = Cafeterias('Munchies', 'Off campus', 'Ashesi')
cafeterias = (cafeteria1, cafeteria2, cafeteria3)
for cafeteria in cafeterias:
    AshesiCafeteriasApp.register_cafeteria(cafeteria)
AshesiCafeteriasApp.add_registered_cafeteria_to_file()