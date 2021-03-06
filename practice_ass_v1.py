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

selected_show = StringVar()
selected_show.set(show_name_list[0])
sell_option = OptionMenu(root, selected_show, *show_name_list)
sell_option.grid(row=1)

ticket_number = IntVar()
sell_entry = Entry(root, textvariable = ticket_number).grid(row=1, column =2)

new_available = IntVar()

# def update_lbl(new_available):
    #global heading_lbl
    
   # heading_lbl.destroy()

    #for s in show_list:
        #if s._name == selected_show.get():
         #   available.set(available.get() + selected_show.get() + "- " + str(new_available.get()) + "\n")
        #else:
            #available.set(available.get() + s._name + "- " + str(s._available) + " available/150 available ($" + str(s._price) + ")" + "\n")  
        #
   # heading_lbl = Label(root, textvariable=available).grid(row = 0, column = 0)
  #  return heading_lbl

#define function to sell tickets by reducing available of given show
def sell_tickets():
    global new_available
    for s in show_list:
        if selected_show.get() == s._name:
            s._change_available(ticket_number)


        new_available.set(s._available)
        update_label()



sell_button = Button(root, text = "Sell tickets", command = sell_tickets).grid(row=1, column=3)


root.mainloop()
