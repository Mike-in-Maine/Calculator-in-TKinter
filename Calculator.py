from tkinter import *
from tkinter import Tk
from tkinter import ttk
import webbrowser
import requests
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import xml.etree.ElementTree as ET
import xmltodict, json
import untangle


engine = sqlalchemy.create_engine('mysql+pymysql://miky1973:itff2020@mysql.irish-booksellers.com:3306/irishbooksellers')
emails = []
cities = []
codes = []
countrys = []
names = []
phones = []
regions = []
streets = []
street2s = []
processed = []



#runs a browser URL
def link():
    webbrowser.open_new(r'www.itff.it/'+ 'yello')

# gets all the orders stored in sql
def get_abe_orders():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    df_orders = pd.read_sql(sql='orders', con=engine)
    print(df_orders.head(10))

# gets only new and unprocessed orders
def get_abe_API_neworders():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    df = pd.DataFrame()
    data = """
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <orderUpdateRequest version="1.1">
        <action name="getAllNewOrders">
            <username>irishbooksellers</username>
            <password>ef624a8bd5a843cda651</password>
        </action>
    </orderUpdateRequest>
    """
    headers = {'username': 'irishbooksellers', 'password': 'ef624a8bd5a843cda651'}
    response = requests.get('https://orderupdate.abebooks.com:10003', data=data, headers=headers)
    #print(response.text)
    root = ET.fromstring(response.text)
    dump = xmltodict.parse(response.text)

    obj = untangle.parse(response.text)
    emails = []
    cities = []
    codes = []
    countrys = []
    names = []
    phones = []
    regions = []
    streets = []
    street2s = []
    processed = []

    for po in root.findall('purchaseOrderList'):
        for po2 in po.findall('purchaseOrder'):
            for po3 in po2.findall('buyer'):
                for po5 in po3.findall('email'):
                    emails.append(po5.text)
                for po4 in po3.findall('mailingAddress'):
                    city = po4.find('city').text
                    code = po4.find('code').text
                    country = po4.find('country').text
                    name = po4.find('name').text
                    phone = po4.find('phone').text
                    region = po4.find('region').text
                    street = po4.find('street').text
                    street2 = po4.find('street2').text
                    cities.append(city)
                    codes.append(code)
                    countrys.append(country)
                    names.append(name)
                    phones.append(phone)
                    regions.append(region)
                    streets.append(street)
                    street2s.append(street2)
    print(cities)
    print(codes)
    print(countrys)
    print(phones)
    print(names)
    print(regions)
    print(streets)
    print(street2s)
    print(emails)

    print(len(cities))
    print(len(codes))
    print(len(countrys))
    print(len(names))
    print(len(phones))
    print(len(regions))
    print(len(streets))
    print(len(street2s))

    for zip in codes:
        labelNumberOfOrders = Label(text=zip, font=('bold', 2))
        labelNumberOfOrders
    for phone in phones:
        labelphone = Label(text=phone, font=('bold', 2), fg='red')#.grid(column=1, row=0, padx=5, pady=5)
        labelphone.pack()
    for street in streets:
        labelstreet = Label(text=street, font=('bold', 2))#.grid(column=2, row=0, padx=5, pady=5)
        labelstreet.pack()



root = Tk()
root.title('Discovery - 0.5')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
math = "none"
#e.insert(0, "Enter your name")

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)
    
def button_add():
    first_number = e.get()
    global add_num
    global math
    math = "addition"
    add_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global sub_num
    global math
    math = "subtraction"
    sub_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    #e.insert(0, sub_num - int(second_number))

    if math == "addition":
        e.insert(0, add_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, sub_num - int(second_number))
    elif math == "none":
        e.insert(0, "You have to insert something")


button_1 = Button(root, text=1, padx=40, pady=20, command=lambda:button_click(1))
button_2 = Button(root, text=2, padx=40, pady=20, command=lambda:button_click(2))
button_3 = Button(root, text=3, padx=40, pady=20, command=lambda:button_click(3))
button_4 = Button(root, text=4, padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text=5, padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text=6, padx=40, pady=20, command=lambda:button_click(6))
button_7 = Button(root, text=7, padx=40, pady=20, command=lambda:button_click(7))
button_8 = Button(root, text=8, padx=40, pady=20, command=lambda:button_click(8))
button_9 = Button(root, text=9, padx=40, pady=20, command=lambda:button_click(9))
button_0 = Button(root, text=0, padx=40, pady=20, command=lambda:button_click(0))
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=84, pady=20, command=button_subtract)
button_equal = Button(root, text="=", padx=84, pady=20, command=button_equal)
button_clear = Button(root, text="CLR", padx=80, pady=20, command=button_clear)

#put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=6, column=1, columnspan=3)

LabelMonth_Ago2 = Label(root, text=names, font=('bold', 14))
#LabelMonth_Ago2.pack(pady = 10)
LabelMonth_Ago = Label(root, text="Welcome", font=('bold', 14))
#LabelMonth_Ago.pack(pady = 10)

get_order_buttn = Button(root,text='Get Orders', command=get_abe_API_neworders)
#while True:
#    for zip in codes:
#        labelNumberOfOrders = Label(text=zip, font=('bold', 5))
#        labelNumberOfOrders.pack()
#        print(codes)
#get_order_buttn.pack()


root.mainloop()
