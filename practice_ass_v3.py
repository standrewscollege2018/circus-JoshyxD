from tkinter import *

# abstantiate the main window
root = Tk()

# create title
root.title("Circus")

#extra things
root.resizable(width=FALSE, height = FALSE)
root.geometry('500x250')

class Show:
    def __init__(self, name, available, capacity, price):
        self._name = name
        self._available = available
        self._capacity = capacity
        self._price = price
        show_list.append(self)
        show_name_list.append(self._name)

    def _change_available(self, ticket_number):
        self._available -= ticket_number.get()

    def _reset_shows(self):
        self._available = self._capacity
        update_label()

show_list = []
show_name_list = []

Show("10 AM SHOW", 150, 150, 5)
Show("3 PM SHOW", 150, 150, 5)
Show("8 PM SHOW", 250, 250, 12)
    

# heading labels
available = StringVar()

def update_label():
    available.set("")
    for s in show_list:
        available.set(available.get() + s._name + "- " + str(s._available) + " available/" + str(s._capacity) + " available ($" + str(s._price) + ")" + "\n")
        
    heading_lbl = Label(root, textvariable=available).grid(row = 0, column = 0)

update_label()

counter = IntVar()
counter.set(0)
counter_label_text = StringVar()
counter_label_text.set("")
counter_lbl = Label(root, textvariable = counter_label_text).grid(row =2, column = 2)



selected_show = StringVar()
selected_show.set(show_name_list[0])
sell_option = OptionMenu(root, selected_show, *show_name_list)
sell_option.grid(row=1)

ticket_number = IntVar()

sell_entry = Entry(root, textvariable = ticket_number).grid(row=1, column =2)
    
summary_counter = IntVar()
summary_counter.set(0)

summary_cost = IntVar()
summary_cost.set(0)

summary_label_text = StringVar()

#define function to sell tickets by reducing available of given show
price = IntVar()
def sell_tickets():
    try:
        if ticket_number.get() == 0:
           counter_label_text.set("You cannot order 0 tickets")

        else:
            for s in show_list:
                if selected_show.get() == s._name:
                    if (s._available - ticket_number.get()) >= 0:
                        s._change_available(ticket_number)  
                        price.set(s._price)
                        update_label()
                        update_counter(price)
                    else:
                        counter_label_text.set("You cannot order that amount of tickets")
    except:
        counter_label_text.set("Enter a number of tickets, goober")


def update_summary():
    summary_label_text.set("SUMMARY" + "\n" + str(summary_counter.get()) + " tickets sold today" + "\n" + "$" + str(summary_cost.get()) + " earned today")
summary_lbl = Label(root, textvariable = summary_label_text).grid(row=4, column = 0)



def update_counter(price):
    counter.set(ticket_number.get())
    counter_label_text.set(str(counter.get()) + " tickets sold")

    summary_counter.set(summary_counter.get() + counter.get())
    summary_cost.set(summary_cost.get() + ticket_number.get() * price.get())
    update_summary()

update_summary()

sell_button = Button(root, text = "Sell tickets", command = sell_tickets).grid(row=1, column=3)


def reset_shows():
    for s in show_list:
        s._reset_shows()
        ticket_number.set(0)
        summary_counter.set(0)
        summary_cost.set(0)
        counter.set(0)
        update_counter(price)
        update_summary()
        

reset_button = Button(root, text = "Reset shows", command = reset_shows).grid(row = 3, column = 2)

root.mainloop()
