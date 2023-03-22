#Library this use
from tkinter import *
import matplotlib.pyplot as plt
import csv
from tkinter import ttk , messagebox

#Function
def all_travels():     
    nations, values1, values2, values3 = [], [], [], []
    values_none = [0,0,0,0,0,0,0,0,0]
    filename = 'all_arrivers_travel2.csv'

    #Open File .CSV
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            counties = row[0]
            year_1 = int(row[1])
            year_2 = int(row[2])
            year_3 = int(row[3])
            nations.append(counties)
            values1.append(year_1)
            values2.append(year_2)
            values3.append(year_3)

    plt.clf()

    if selcet_graph.current() == 0:
        if checkvar1.get() == 0 and checkvar2.get() == 0 and checkvar3.get() == 0:
            # plt.plot(nations, values_none, label='None', c='black', alpha=1)
            messagebox.showerror('Error', 'Please select data')
        else:
            if checkvar1.get() == 1:
                plt.plot(nations, values1, label='2020', c='red', alpha=1)
            if checkvar2.get() == 1:
                plt.plot(nations, values2, label='2019', c='green', alpha=1)
            if checkvar3.get() == 1:
                plt.plot(nations, values3, label='2018', c='blue', alpha=1)

            plt.title("Number of Asians traveling in Thailand", fontsize=24)
            plt.xlabel('Nations', fontsize=16)
            plt.ylabel("Numbers", fontsize=16)
            plt.legend()
            plt.show()

    elif selcet_graph.current() == 1:
        if checkvar1.get() == 0 and checkvar2.get() == 0 and checkvar3.get() == 0:
            # plt.bar(nations, values_none, label='None', color='black', alpha=1)
            messagebox.showerror('Error', 'Please select data')
        else:
            if checkvar1.get() == 1:
                plt.bar(nations, values1, label='2020', color='red', alpha=1)
            if checkvar2.get() == 1:
                plt.bar(nations, values2, label='2019', color='green', alpha=1)
            if checkvar3.get() == 1:
                plt.bar(nations, values3, label='2018', color='blue', alpha=1)
            plt.title("Number of Asians traveling in Thailand", fontsize=24)
            plt.xlabel('Nations', fontsize=16)
            plt.ylabel("Numbers", fontsize=16)
            plt.legend()
            plt.show()

            
    elif selcet_graph.current() == 2:
        if checkvar1.get() == 0 and checkvar2.get() == 0 and checkvar3.get() == 0:
            # plt.scatter(nations, values_none, label='None', color='black', alpha=1)
            messagebox.showerror('Error', 'Please select data')
        else:
            if checkvar1.get() == 1:
                plt.scatter(nations, values1, label='2020', color='red', alpha=1)
            if checkvar2.get() == 1:
                plt.scatter(nations, values2, label='2019', color='green', alpha=1)
            if checkvar3.get() == 1:
                plt.scatter(nations, values3, label='2018', color='blue', alpha=1)
            plt.title("Number of Asians traveling in Thailand", fontsize=24)
            plt.xlabel('Nations', fontsize=16)
            plt.ylabel("Numbers", fontsize=16)
            plt.legend()
            plt.show()

    else:
        messagebox.showerror('Error', 'Please select a graph type')
    
    
#Header Tkinter Display
root = Tk()
root.option_add("*Font", "consolas 20")
root.title("Data Graph")
root.geometry("400x250")

#Variables
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()

#Use function's Tkinter
photo = PhotoImage(file="basic-bar-graph (2).png")
Checkbutton(root, text="2020 Year", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10).grid(row=0,column=0)
Checkbutton(root, text="2019 Year", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10).grid(row=1,column=0)
Checkbutton(root, text="2018 Year", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10).grid(row=2,column=0)
Button(root, image=photo, borderwidth=0).grid(row=1,column=1)
Button(root, text="Show Graph", command = all_travels).grid(row=2,column=1)
selcet_graph = ttk.Combobox(root, values=["Line Graph", "Bar Graph","Scatter"] , width=10)
selcet_graph.grid(row=0,column=1)
root.mainloop()
