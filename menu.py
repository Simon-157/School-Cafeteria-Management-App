from tkinter import *
  
  
class Days:
    def __init__(self, name_day):
        self.name_day = name_day
        self.foods_available = []
        
    def set_foods_available(self, food):
        self.foods_available.append((food.food_id,food.food_name, food.price, food.food_type))
        
        
class Foods:
    def __init__(self,food_id, food_name, price, food_type):
        self.food_id= food_id
        self.food_name = food_name
        self.price = price 
        self.food_type = food_type
        
    def change_price(self, new_price):
        self.price = new_price
        
        
    def __str__(self):
        pass
    
      
Day1 = Days('Monday')
food1 = Foods(1,'Jollof rice and Chicken', '15.00cedis', 'Local')
food2 = Foods(2,'Waakye and fish', '15cedis', 'local')
food3 = Foods(3,'Fried rice and chicken', '20cedis', 'continental')
Day1.set_foods_available(food1) 
Day1.set_foods_available(food2) 
Day1.set_foods_available(food2) 
      
      
      
      
      
class MenuView:
    def __init__(self, window):
        
        self.window = window
        
        
        # master self.window size
        self.window.geometry("700x600")
        self.window.title("10K")
        color = "#FAF733"
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.configure(bg=color)

        top_frame = Frame(self.window, bg=color, width=700, height=20)
        top_frame.pack(side=TOP)
        # california lebel in top frame
        title_label = Label(top_frame, text="10K Akorno Limited (Cashier's View)",fg="blue", font=("Comic Sans MC", 17), bg=color,
                            pady=10)
        # left frame 
        left_frame = Frame(self.window, bg=color, width=600, height=450)
        left_frame.place(x=10, y=50)
        title_label.pack(side=TOP)

        #bottom frame for buttons
        bottom_frame = Frame(self.window, bg=color, height=130, width=705)
        bottom_frame.place(x=10, y=660)



        label = Label(self.window, text="Today's Menu", font= ("Comic Sans MC","15"),  bg="black", fg="white")
        label.place(x=0, y=0)
  
    
        # checkbuttons for FOOD in self.window 
        self.banku = IntVar()
        banku = Checkbutton(self.window, text="Banku", variable=self.banku, font="Helvetica 12 bold italic", bg=color)

        banku.place(x=0, y=40)

        self.fried_rice = IntVar()
        fried_rice = Checkbutton(self.window, text="Fried Rice", variable=self.fried_rice, font="Helvetica 12 bold italic",
                           bg=color)

        fried_rice.place(x=0, y=90)
        self.stir_fry = IntVar()
        stir_fry = Checkbutton(self.window, text="Stir Fry", variable=self.stir_fry, font="Helvetica 12 bold italic",
                           bg=color)
        stir_fry.place(x=0, y=140)

        self.beans = IntVar()
        beans = Checkbutton(self.window, text="Beans and Plaintain", variable=self.beans, font="Helvetica 12 bold italic",
                           bg=color)

        beans.place(x=0, y=190)

        self.indomie = IntVar()
        indomie = Checkbutton(self.window, text="Indomie", variable=self.indomie, font="Helvetica 12 bold italic",
                           bg=color)

        indomie.place(x=0, y=240)
