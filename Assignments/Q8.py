# QUESTION 8
# A long-distance provider charges the following rates for telephone calls:


# Rate Category                    Rate per minute
# Daytime(6:00 AM through 5:59 PM)    $0.07
# Evening(6:00 PM through 11:59 PM)   0.12
# Off-Peak(Midnight through 5:59 AM)  0.05

# Write a GUI application that allows the user to select a rate category (from a set of radio buttons), and enter the number of minutes of the call into the Entry widget. An info dialog box should display the charge for the call.




import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
       
        self.label1 = tkinter.Label(self.top_frame, text = 'Please choose rate category:')
        self.label1.pack()
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                            text ='Daytime (6:00 AM through 5:59 PM), Rate: $0.07 per minute',
                            variable = self.radio_var, value = 1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                    text ='Evening (6:00 PM through 11:59 PM), Rate: $0.12 per minute',
                                    variable = self.radio_var, value = 2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                text ='Off-Peak (midnight through 5:59 AM), Rate: $0.05 per minute',
                                variable = self.radio_var, value = 3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text = 'Enter minutes:')
        self.min_entry = tkinter.Entry(self.top_frame, width = 10)
       
        self.prompt_label.pack(side ='left')
        self.min_entry.pack(side ='left')
       
        self.ok_button = tkinter.Button(self.bottom_frame,
                                          text = 'OK',
                                          command = self.call_charge)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
       
        self.ok_button.pack(side ='left')
        self.quit_button.pack(side='left')
       
        self.top_frame.pack()
        self.bottom_frame.pack()
       
        tkinter.mainloop()
       
    def call_charge(self):
       
        minutes = int(self.min_entry.get())
       
        if self.radio_var.get() == 1:
           charge =  minutes * 0.07
           tkinter.messagebox.showinfo('Call charge', 'Charge for ' +
                            str(self.min_entry.get()) + ' minute(s)' +
                            ' Daytime call is ' +
                            str('${:,.2f}'.format(charge)))
        elif self.radio_var.get() == 2:
           charge =  minutes * 0.12
           tkinter.messagebox.showinfo('Call charge', 'Charge for ' +
                            str(self.min_entry.get()) + ' minute(s)' +
                            ' Evening call is ' +
                            str('${:,.2f}'.format(charge)))
        elif self.radio_var.get() == 3:
           charge =  minutes * 0.05
           tkinter.messagebox.showinfo('Call charge', 'Charge for ' +
                            str(self.min_entry.get()) + ' minute(s)' +
                            ' Off-Peak call is ' +
                            str('${:,.2f}'.format(charge)))
        else:
            tkinter.messagebox.showinfo('Error', 'You must select a category!')
       
my_gui = MyGUI()
