from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import main_account_screen

class CashierView:
    def __init__(self):
        
        
        # main_account_screen()
        self.window = Toplevel(main_account_screen())
        # master self.window size
        self.window.geometry("700x600")
        self.window.title("10K")
        color = "#FAF733"
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.configure(bg=color)
        # main_account_screen()
        

        # top_frame = Frame(self.window, bg=color, width=700, height=20)
        # top_frame.pack(side=TOP)
        # california lebel in top frame
        title_label = Label(self.window, text="10K Akorno Limited (Cashier's View)",fg="blue", font=("Comic Sans MC", 17), bg=color,
                            pady=10)
        # left frame 
        # left_frame = Frame(self.window, bg=color, width=600, height=450)
        # left_frame.place(x=10, y=50)
        title_label.pack(side=TOP)

        # #bottom frame for buttons
        # bottom_frame = Frame(self.window, bg=color, height=130, width=705)
        # bottom_frame.place(x=10, y=660)



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

        
        total_btn = Button(self.window,text = "TOTAL",command=lambda:self.calc_total())
        total_btn.place(x=0, y=290)
        
        # optionmenu widget for dropdown of quantity place with food in self.window
        global list_menu
        list_menu = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.drop_op_1 = StringVar()
        self.drop_op_1.set(list_menu[0])
        drop1 = OptionMenu(self.window, self.drop_op_1, *list_menu)

        self.drop_op_2 = StringVar()
        self.drop_op_2.set(list_menu[0])
        drop2 = OptionMenu(self.window, self.drop_op_2, *list_menu)

        self.drop_op_3 = StringVar()
        self.drop_op_3.set(list_menu[0])
        drop3 = OptionMenu(self.window, self.drop_op_3, *list_menu)

        self.drop_op_4 = StringVar()
        self.drop_op_4.set(list_menu[0])
        drop4 = OptionMenu(self.window, self.drop_op_4, *list_menu)

        self.drop_op_5 = StringVar()
        self.drop_op_5.set(list_menu[0])
        drop5 = OptionMenu(self.window, self.drop_op_5, *list_menu)

 

        drop1.place(x=180, y=40)
        drop2.place(x=180, y=90)
        drop3.place(x=180, y=140)
        drop4.place(x=180, y=190)
        drop5.place(x=180, y=240)

        # sizes optionmenu in self.window
        self.s1 = StringVar()
        self.s1.set("size")
        list_menu2 = ["half-portion", "full-portion"]
        size_opt1 = OptionMenu(self.window, self.s1, *list_menu2)
        size_opt1.place(x=270, y=40)
        self.s2 = StringVar()
        self.s2.set("size")
        size_opt2 = OptionMenu(self.window, self.s2, *list_menu2)
        size_opt2.place(x=270, y=90)
        self.s3 = StringVar()
        self.s3.set("size")
        size_opt3 = OptionMenu(self.window, self.s3, *list_menu2)
        size_opt3.place(x=270, y=140)
        self.s4 = StringVar()
        self.s4.set("size")
        size_opt4 = OptionMenu(self.window, self.s4, *list_menu2)
        size_opt4.place(x=270, y=190)
        self.s5 = StringVar()
        self.s5.set("size")
        size_opt5 = OptionMenu(self.window, self.s5, *list_menu2)
        size_opt5.place(x=270, y=240)

  


    global item_quantity_price
    item_quantity_price = []

    def error_handling(self, msg):
        if msg == "error!":
            messagebox.showerror("Error", "No Digits to compute!")
        elif msg == "division by zero!":
            messagebox.showerror("Error", "You can not divide a digit by zero!")

    # back end and logic 
    def calc_total(self):

        # Set initial result to 0
        self.total_food= 0
        banku_result = 0
        fried_rice_result = 0
        indomie_result = 0
        beans_res = 0
        stir_fry_result = 0

        try:
            # for food 1
            if self.banku.get() == 1:
                if self.s1.get() == "full-portion":
                    banku_result = int(self.drop_op_1.get()) * 300   # option 1 in dropdown menu
                    p1_t = ("banku", str(self.drop_op_1.get()), "300")
                    item_quantity_price.append(p1_t)
                elif self.s1.get() == "half-portion":
                    banku_result = int(self.drop_op_1.get()) * 200
                    p1_t = ("banku", str(self.drop_op_1.get()), "200")
                    item_quantity_price.append(p1_t)
                else:
                    banku_result = int(self.drop_op_1.get()) * 150
                    p1_t = ("banku", str(self.drop_op_1.get()), "150")
                    item_quantity_price.append(p1_t)
                # item_quantity_price.append(p1_t)
            else:
                banku_result = 0

            # for food 2
            if self.fried_rice.get() == 1:
                if self.s2.get() == "full-portion":
                    fried_rice_result = int(self.drop_op_2.get()) * 300 #option 2 in dropdown menu
                    p2_t = ("Fried Rice and Chicken", str(self.drop_op_2.get()), "300")
                    item_quantity_price.append(p2_t)
                elif self.s2.get() == "half-portion":
                    fried_rice_result = int(self.drop_op_2.get()) * 200
                    p2_t = ("Fried Rice and Chicken", str(self.drop_op_2.get()), "200")
                    item_quantity_price.append(p2_t)
                else:
                    fried_rice_result = int(self.drop_op_2.get()) * 150
                    p2_t = ("Fried Rice and Chicken", str(self.drop_op_2.get()), "150")
                    item_quantity_price.append(p2_t)
                # item_quantity_price.append(p2_t)
            else:
                fried_rice_result = 0
            
            # for food 3
            if self.stir_fry.get() == 1:
                if self.s3.get() == "full-portion":
                    stir_fry_result = int(self.drop_op_3.get()) * 300  #option 3 in dropdown menu
                    p3_t = ("Stir Fry", str(self.drop_op_3.get()), "300")
                    item_quantity_price.append(p3_t)
                elif self.s3.get() == "half-portion":
                    stir_fry_result = int(self.drop_op_3.get()) * 200
                    p3_t = ("Stir Fry", str(self.drop_op_3.get()), "200")
                    item_quantity_price.append(p3_t)
                else:
                    stir_fry_result = int(self.drop_op_3.get()) * 150
                    p3_t = ("Stir Fry", str(self.drop_op_3.get()), "150")
                    item_quantity_price.append(p3_t)
                # item_quantity_price.append(p3_t)
            else:
                stir_fry_result = 0

            
            # for food 4
            if self.beans.get() == 1:
                if self.s4.get() == "full-portion":
                    beans_res = int(self.drop_op_4.get()) * 300   # option 4 in dropdown menu
                    p4_t = ("Beans and Plaintain", str(self.drop_op_1.get()), "300")
                    item_quantity_price.append(p4_t)
                elif self.s4.get() == "half-portion":
                    beans_res = int(self.drop_op_4.get()) * 200
                    p4_t = ("Beans and Plaintain", str(self.drop_op_4.get()), "200")
                    item_quantity_price.append(p4_t)
                else:
                    beans_res = int(self.drop_op_4.get()) * 150
                    p4_t = ("Beans and Plaintain", str(self.drop_op_4.get()), "150")
                    item_quantity_price.append(p4_t)
                # item_quantity_price.append(p4_t)
            else:
                beans_res = 0

     
            # for food 5
            if self.indomie.get() == 1:
                if self.s5.get() == "full-portion":
                    indomie_result = int(self.drop_op_5.get()) * 300  # option 5 in dropdown menu
                    p5_t = ("Indomie", str(self.drop_op_5.get()), "300")
                    item_quantity_price.append(p5_t)
                elif self.s5.get() == "half-portion":
                    indomie_result = int(self.drop_op_5.get()) * 200
                    p5_t = ("Indomie", str(self.drop_op_5.get()), "200")
                    item_quantity_price.append(p5_t)
                else:
                    indomie_result = int(self.drop_op_5.get()) * 150
                    p5_t = ("Indomie", str(self.drop_op_5.get()), "150")
                    item_quantity_price.append(p5_t)
                # item_quantity_price.append(p5_t)
            else:
                indomie_result = 0
          
        except:
            raise NameError

        self.total_food = (
                        banku_result + fried_rice_result + stir_fry_result + indomie_result +  beans_res)

        print(self.total_food)
        
        total = Label(self.window,text=self.total_food, bg="brown", font=("verdana", 20)).pack()
        total.place(x=0, y=300)
        
    def printvalue(self):
        self.calc_total
    
     
    def reset_sales(self):

        try:
            self.banku.set(0)
            self.fried_rice.set(0)
            self.stir_fry.set(0)
            self.beans.set(0)
            self.indomie.set(0)

            self.drop_op_1.set(list_menu[0])
            self.drop_op_2.set(list_menu[0])
            self.drop_op_3.set(list_menu[0])
            self.drop_op_4.set(list_menu[0])
            self.drop_op_5.set(list_menu[0])

            self.s1.set("size")
            self.s2.set("size")
            self.s3.set("size")
            self.s4.set("size")
            self.s5.set("size")
            
            # Reset checklist btns to 0
            self.d_ch_banku.set(0)
            self.d_ch_bt_2.set(0)
            self.d_ch_bt_3.set(0)
            self.d_ch_bt_4.set(0)
            self.d_ch_bt_5.set(0)

            self.drop_op_d_1.set(list_menu[0])
            self.drop_op_d_2.set(list_menu[0])
            self.drop_op_d_3.set(list_menu[0])
            self.drop_op_d_4.set(list_menu[0])
            self.drop_op_d_5.set(list_menu[0])

            self.s_ch_banku.set(0)
            self.s_ch_bt_2.set(0)
            self.s_ch_bt_3.set(0)
            self.s_ch_bt_4.set(0)
            self.s_ch_bt_5.set(0)

            global total_food
            self.total_food = 0
            global item_quantity_price
            item_quantity_price.clear()
            self.total_x_e.delete(0, END)

            self.receipt_made.delete("1.0", END)
            messagebox.showinfo("Next Customer!", "Serve the next customer please!")
        except NameError:
            messagebox.showerror("error nothing to clear")




if __name__=='__main__':
    self.window = Tk()

    root = CashierView(self.window)
    self.window.mainloop()