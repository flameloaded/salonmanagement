from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win = Tk()
win.state('zoomed')
win.config(bg='black')
#---------------------BUTTON FUNCTION-----------
def save():
    try:
        if e1.get() == "" or e2.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            con = mysql.connector.connect(host="localhost",
                                          username="root",
                                          password="1234",
                                          database="salon")
            my_cursor = con.cursor()
            my_cursor.execute("INSERT INTO transaction VALUES (%s, %s, %s, %s, %s, %s)", (
                transaction_id.get(),
                numberofcustomer.get(),
                nameofcustomer.get(),
                service.get(),
                amount.get(),
                date.get(),
                
                
                
            ))
            con.commit()
            fetch_data()
            con.close()
            messagebox.showinfo("Success", "Record has been added to database")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")

def fetch_data():
    con = mysql.connector.connect(host="localhost",
                                     username="root",
                                      password="1234",database="salon")
    my_cursor = con.cursor()
    my_cursor.execute("select * from transaction")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('', END,values=items)
        con.commit()
    con.close()

def get_data(event=''):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data['values']
    transaction_id.set(row[0])
    numberofcustomer.set(row[1])
    nameofcustomer.set(row[2])
    service.set(row[3])
    amount.set(row[4])
    date.set(row[5])

#-------------------------------show details button---------------
def showdetails():
    txt_frme.insert(END,'Transaction Number:\t\t\t'+ transaction_id.get()+'\n')
    txt_frme.insert(END,'Phone Number:\t\t\t'+ numberofcustomer.get()+'\n')
    txt_frme.insert(END,'Customer Name:\t\t\t'+ nameofcustomer.get()+'\n')
    txt_frme.insert(END,'Service:\t\t\t'+ service.get()+'\n')
    txt_frme.insert(END,'Amount:\t\t\t'+ amount.get()+'\n')
    txt_frme.insert(END,'Date:\t\t\t'+ date.get()+'\n')
    
#---------------------------Delete Button-----------------------
def delete():
    con = mysql.connector.connect(host="localhost",
                                      username="root",
                                      password="1234",database="salon")
    my_cursor = con.cursor()
    querry = ('delete from transaction where transactionid=%s')
    value = (transaction_id.get(),)
    print(value)
    my_cursor.execute(querry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Deleted','Customer details has been successfully deleted')
#==================clear button===============================
def clear():
    numberofcustomer.set('')
    nameofcustomer.set('')
    service.set('')
    amount.set('')
    date.set('')
    transaction_id.set('')
    txt_frme.delete(1.0,END)

def exit():
    confirm = messagebox.askyesno('confirmation', 'Are you sure you want to exit')
    if confirm>0:
        win.destroy()
        return
    

# Button for searching customer

#Heading
Label(win,text='OBS Salon Management system', font='impack 31 bold', bg='green',fg='white').pack(fill=X)
#Frame1
frame1 = Frame(win, bd=15, relief=RIDGE)
frame1.place(x=0, y=54, width=1350, height=310)
#Label Frame For Customer Info.
lf1 = LabelFrame(frame1, text='Transaction Information', font= 'ariel 10 bold', bd=10,bg='pink')
lf1.place(x=10,y=0,width=750,height=280)

#Labels for customer information
Label(lf1,text='Transaction Number', bg='pink').place(x=5,y=10)
Label(lf1,text='Phone Number', bg='pink').place(x=5,y=40)
Label(lf1,text='Customer Name', bg='pink').place(x=5,y=70)
Label(lf1,text='Service', bg='pink').place(x=5,y=100)
Label(lf1,text='Amount', bg='pink').place(x=5,y=130)
Label(lf1,text='Date', bg='pink').place(x=5,y=160)

#TextVariable for Every Entry field
transaction_id = StringVar()
numberofcustomer = StringVar()
nameofcustomer = StringVar()
service = StringVar()
amount = StringVar()
date = StringVar()
#Entry Field
e1 = Entry(lf1,bd=4,textvariable=transaction_id)
e1.place(x=130,y=10,width=200)
e2 = Entry(lf1,bd=4,textvariable=numberofcustomer)
e2.place(x=130,y=40,width=200)
e3 = Entry(lf1,bd=4,textvariable=nameofcustomer)
e3.place(x=130,y=70,width=200)
e4 = Entry(lf1,bd=4,textvariable=service)
e4.place(x=130,y=100,width=200)
e5 = Entry(lf1,bd=4,textvariable=amount)
e5.place(x=130,y=130,width=200)
e6 = Entry(lf1,bd=4,textvariable=date)
e6.place(x=130,y=160,width=200)


#Label Frame For Customer Info.
lf2 = LabelFrame(frame1, text='Display Transactions', font= 'ariel 12 bold', bd=10)
lf2.place(x=770,y=0,width=550,height=280)
#Textbox for Customer Info.
txt_frme = Text(lf2, font='impack 10 bold', width=40,height=30,bg='pink')
txt_frme.pack(fill=BOTH)
#Frame2
frame2 = Frame(win,bd=15, relief=RIDGE)
frame2.place(x=0, y=360, width=1350,height=250)
#Button
#Delete Button
d_btn = Button(win, text='Delete', font='ariel 15 bold',bg='brown',fg='white',bd=6, cursor='hand2', command=delete)
d_btn.place(x=0,y=600,width=270)





#Save customer name
s_btn = Button(win, text='Save', font='ariel 15 bold',bg='purple',fg='white',bd=6, cursor='hand2',command=save)
s_btn.place(x=270,y=600,width=270)
#show customer info
sh_btn = Button(win, text='Show Details', font='ariel 15 bold',bg='green',fg='white',bd=6, cursor='hand2', command=showdetails)
sh_btn.place(x=540,y=600,width=270)
#clear button
c_btn = Button(win, text='Clear', font='ariel 15 bold',bg='orange',fg='white',bd=6, cursor='hand2',command=clear)
c_btn.place(x=810,y=600,width=270)
#Exit button
e_btn = Button(win, text='Exit', font='ariel 15 bold',bg='red',fg='white',bd=6, cursor='hand2',command=exit)
e_btn.place(x=1080,y=600,width=270)
#Scroll Bar for Customer transaction details 
scroll_x = ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom', fill='x')
scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right', fill='y')

table = ttk.Treeview(frame2,columns=('tran_no','cnumb', 'cname', 'serv', 'amt','date'))
scroll_x = ttk.Scrollbar(command=table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)

#Heading for customer transactions
table.heading('date', text='Date')
table.heading('cnumb', text='Customer Number')
table.heading('cname', text='Customer Name')
table.heading('serv', text='Service')
table.heading('amt', text='Amount')
table.heading('tran_no', text='Transaction Number')

table['show'] = 'headings'
table.pack(fill=BOTH,expand=1)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()