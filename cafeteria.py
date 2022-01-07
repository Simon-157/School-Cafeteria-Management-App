from cashier import Cashiers


class Cafeterias:
    
    filename = "Cashiers.csv"
    
    def __init__(self, cafeteria_name, location, institution):
        self.cafeteria_name = cafeteria_name
        self.location = location 
        self.institution =  institution
        self.cashiers = []
        self.admins = {}
        
        
    def add_cashier(self, cashier):
        
        for cashier_ in self.cashiers:
            if cashier_.cashier_id == cashier.cashier_id:
                return False
        self.cashiers.append(cashier)
        return True
    
    
    def load_data_from_file(self):
        self.cashiers.clear()
        chashiersFile = open('Cashiers.csv', 'r')
        lines = chashiersFile.readlines()
        
        for line in lines[1:]:
            line=line.strip()
            line_list = line.split(',')
            cashier = Cashiers(line_list[0], line_list[1], line_list[2])
            self.add_cashier(cashier)
            
            
        
    
    def save_data_to_file(self):
        '''the first line in the file contains the column headings,
            the next line contains the details of each registered cashier
        '''
        
        file = open('Cashiers.csv', 'w')
        file.write('{},{},{}\n'.format('cashier_name', 'cashier_id', 'password')) 
        
        for cashier in self.cashiers:
            
            file.write('{},{},{}\n'.format(cashier.cashier_name, cashier.cashier_id, cashier.password))
        
        
        file.close()
        
if __name__ =='__main__':
        
    cafeteria1 = Cafeterias('Big Ben','Hive', 'Ashesi')
    cafeteria2 = Cafeterias('Akorno', 'Hive', 'Ashesi')
    cafeteria3 = Cafeterias('Munchies', 'Off campus', 'Ashesi')
    
    
