#currency converter using python
#firstly install the library "pip install CurrencyConverter" and "pip install tkinter"
from currency_converter import CurrencyConverter
import tkinter as tk
c=CurrencyConverter()
#print(c.convert(12,"USD","INR"))


#name of the application
window=tk.Tk()
window.geometry("500x360")   #size of the application
window.title("CurrencyConverter")     #name of application


#convert the currency
def clicked():
    amount=int(entry1.get())
    cur1=entry2.get()
    cur1=entry3.get()

#heading of application
label=tk.Label(window,text="Currency Converter",font="Time 20 bold").place(x=120,y=40)


#amount entering column
label1=tk.Label(window,text="Enter amount here: ",font="Time 16 bold").place(x=100,y=100)
entry2=tk.Entry(window).place(x=300,y=105)


#currency entering column
label2=tk.Label(window,text="Enter your currency here: ",font="Time 16 bold").place(x=40,y=150)
entry2=tk.Entry(window).place(x=300,y=155)


#desired currency entering column
label3=tk.Label(window,text="Enter your desired currency: ",font="Time 16 bold").place(x=10,y=200)
entry3=tk.Entry(window).place(x=300,y=205)

#convertion button
button=tk.Button(window,text="click",font="Time 16 bold").place(x=200,y=250)
window.mainloop()
