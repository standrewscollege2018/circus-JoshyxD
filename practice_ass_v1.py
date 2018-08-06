from tkinter import *

# abstantiate the main window
root = Tk()

# create title
root.title("Circus")

#extra things
root.resizable(width=FALSE, height = FALSE)
root.geometry('500x250')

class Show:
    def __init__(self, name, capacity, price):
        self._name = name
        self._capacity = capacity
        self._price = price
        show_list.append(self)
        show_name_list.append(self._name)

    def _change_capacity(self, ticket_number):
        self._capacity -= ticket_number.get()

show_list = []
show_name_list = []

Show("10 AM SHOW", 150, 5)
Show("3 PM SHOW", 150, 5)
Show("8 PM SHOW", 250, 12)
    

# heading labels
capacity = StringVar()
for s in show_list:
    capacity.set(capacity.get() + s._name + "- " + str(s._capacity) + " available/150 capacity ($" + str(s._price) + ")" + "\n")
    
heading_lbl = Label(root, textvariable=capacity).grid(row = 0, column = 0)

selected_show = StringVar()
selected_show.set(show_name_list[0])
sell_option = OptionMenu(root, selected_show, *show_name_list)
sell_option.grid(row=1)

ticket_number = IntVar()
sell_entry = Entry(root, textvariable = ticket_number).grid(row=1, column =2)

def update_lbl():
    capacity.set(capacity.get() + selected_show.get() + "- " + str(.get()) + "\n")

#define function to sell tickets by reducing capacity of given show
def sell_tickets():
    for s in show_list:
        if selected_show.get() == s._name:
            s._change_capacity(ticket_number)
            update_lbl()



sell_button = Button(root, text = "Sell tickets", command = sell_tickets).grid(row=1, column=3)


root.mainloop()
