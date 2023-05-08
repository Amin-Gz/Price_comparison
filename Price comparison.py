from tkinter import *
from tkinter import ttk
price01 = None
price02 = None
price03 = None
price04 = None
# window
win=Tk()
win.title('Price Comparison  for Digital')
win.geometry('600x500')
# frame
frame = Frame(win,)
frame.pack(side="top", expand=False, fill="both")
# label
h=Label(frame,text='Price Comparison for Digital:', font=("Tohoma",13)).pack(pady=20)
# main page
def main():
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame,text='WELCOME',font=('Tahoma',20),fg='dark green').pack(pady=20)
    btn1=Button(frame,text='Photography', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=photography).pack(pady=10)
    btn2=Button(frame,text='Phone', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=phone).pack(pady=10)
    btn3=Button(frame,text='Laptop', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=laptop).pack(pady=10)
    btn4=Button(frame,text='Speaker', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=speaker).pack(pady=10)
    btn5=Button(frame,text='Headset', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=headset).pack(pady=10)

# second page (what do you want?)

def photography():
    for widgets in frame.winfo_children():
        widgets.destroy()
    btn01=Button(frame,text='DSLR', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_DSLR).pack(pady=10)
    btn02=Button(frame,text='Compact', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_compact).pack(pady=10)
    btn03=Button(frame,text='Fujifilm', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_fujifilm).pack(pady=10)
    btn04=Button(frame,text='Record', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_record).pack(pady=10)
    btn05=Button(frame,text='back', font=("Tohoma",15),bg = 'light gray',fg='red',command=main).pack(pady=20)

def phone():
    for widgets in frame.winfo_children():
        widgets.destroy()
    btn01=Button(frame,text='Apple', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_apple).pack(pady=10)
    btn02=Button(frame,text='Samsung', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_samsung).pack(pady=10)
    btn03=Button(frame,text='Nokia', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_nokia).pack(pady=10)
    btn04=Button(frame,text='Vertu', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_vertu).pack(pady=10)
    btn05=Button(frame,text='back', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def laptop():
    for widgets in frame.winfo_children():
        widgets.destroy()
    btn01=Button(frame,text='Apple', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_laptop_apple).pack(pady=10)
    btn02=Button(frame,text='Lenovo', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_lenovo).pack(pady=10)
    btn03=Button(frame,text='Asus', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_asus).pack(pady=10)
    btn04=Button(frame,text='back', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)


def speaker():
    for widgets in frame.winfo_children():
        widgets.destroy()
    btn01=Button(frame,text='JBL', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_JBL).pack(pady=10)
    btn02=Button(frame,text='Harman', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_harman).pack(pady=10)
    btn03=Button(frame,text='Sony', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_speaker_sony).pack(pady=10)
    btn04=Button(frame,text='Maxeeder', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_maxeeder).pack(pady=10)
    btn05=Button(frame,text='back', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def headset():
    for widgets in frame.winfo_children():
        widgets.destroy()
    btn01=Button(frame,text='Apple', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_headset_apple).pack(pady=10)
    btn02=Button(frame,text='Anker', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_anker).pack(pady=10)
    btn03=Button(frame,text='Samsung', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_headset_samsung).pack(pady=10)
    btn04=Button(frame,text='Beats', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=input_beats).pack(pady=10)
    btn05=Button(frame,text='back', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

# third page(list & search)

def input_apple():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " iPhone 13 pro max")
    z.insert(2, " iPhone 13 pro")
    z.insert(3, " iPhone 12 pro max")
    z.insert(4, " iPhone 11")
    z.insert(5, " iPhone xs")
    z.insert(6, " iPhone se")
    z.pack()
    def appleprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'iPhone 13 pro max':
            price01 = 41000000
            price02 = 39300000
            price03 = 'ناموجود'
            price04 = 40950000
        elif x == 'iPhone 13 pro':
            price01 = 36890000
            price02 = 35950000
            price03 = 'ناموجود'
            price04 = 39100000
        elif x == 'iPhone 12 pro max':
            price01 = 34500000
            price02 = 36000000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'iPhone 11':
            price01 = 19746000
            price02 = 17600000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'iPhone xs':
            price01 = 'ناموجود'
            price02 = 12500000
            price03 = 'ناموجود'
            price04 = 'توقف توليد'
        elif x == 'iPhone se':
            price01 = 12889000
            price02 = 10260000
            price03 = 'ناموجود'
            price04 = 14100000
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[appleprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstp=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_samsung():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Galaxy A52s")
    z.insert(2, " Galaxy S20")
    z.insert(3, " Galaxy S21")
    z.insert(4, " Galaxy Note 20")
    z.insert(5, " Galaxy Z Flip3")
    z.pack()
    def samsungprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Galaxy A52s':
            price01 = 9849000
            price02 = 8596000
            price03 = 'ناموجود'
            price04 = 10380000
        elif x == 'Galaxy S20':
            price01 = 12699000
            price02 = 12189000
            price03 = 'ناموجود'
            price04 = 13700000
        elif x == 'Galaxy S21':
            price01 = 15800000
            price02 = 16155000
            price03 = 'ناموجود'
            price04 = 17600000
        elif x == 'Galaxy Note 20':
            price01 = 25200000
            price02 = 24399000
            price03 = 'ناموجود'
            price04 = 26800000
        elif x == 'Galaxy Z Flip3':
            price01 = 19990000
            price02 = 20554300
            price03 = 'موجود نيست'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[samsungprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_nokia():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Nokia G20")
    z.insert(2, " Nokia G10")
    z.insert(3, " Nokia C20")
    z.insert(4, " Nokia C10")
    z.insert(5, " Nokia 1.4")
    z.pack()
    def nokiaprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Nokia G20':
            price01 = 4599000
            price02 = 4398000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Nokia G10':
            price01 = 3360000
            price02 = 3089000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Nokia C20':
            price01 = 2390000
            price02 = 2125000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Nokia C10':
            price01 = 1699000
            price02 = 1656000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Nokia 1.4':
            price01 = 2900000
            price02 = 2629000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[nokiaprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_vertu():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Vertu V10")
    z.insert(2, " Vertu V8")
    z.pack()
    def vertuprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Vertu V10':
            price01 = 'ناموجود'
            price02 = 1190000000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Vertu V8':
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[vertuprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_DSLR():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Nikon D5600")
    z.insert(2, " Sony Alfa 850")
    z.insert(3, " Canon X")
    z.pack()
    def DSLRprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Nikon D5600':
            price01 = 20600000
            price02 = 21200000
            price03 = 20617000
            price04 = 'ناموجود'
        elif x == 'Sony Alfa 850':
            price01 = '20000000'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Canon X':
            price01 = 'ناموجود'
            price02 = 31100000
            price03 = 23765000
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[DSLRprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_compact():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Canon IXUS")
    z.insert(2, " Canon IS")
    z.insert(3, " Canon Powershot")
    z.pack()
    def compactprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Canon IXUS':
            price01 = 4000000
            price02 = 3980000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Canon IS':
            price01 = 'ناموجود'
            price02 = 1280000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Canon Powershot':
            price01 = 1685000
            price02 = 1480000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[compactprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_fujifilm():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " instax mini 9")
    z.insert(2, " instax SQ6")
    z.insert(3, " instax mini Liplay")
    z.insert(4, " instax mini 90")
    z.pack()
    def FFprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'instax mini 9':
            price01 = 1750000
            price02 = 1640000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'instax SQ6':
            price01 = 3100000
            price02 = 3100000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'instax mini Liplay':
            price01 = 4830000
            price02 = 4700000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'instax mini 90':
            price01 = 4600000
            price02 = 4580000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[FFprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_record():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " panasonic HC-X1")
    z.insert(2, " GO 360")
    z.insert(3, " sony HDR")
    z.insert(4, " sony fdr-ax700")
    z.pack()
    def recordprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'panasonic HC-X1':
            price01 = 82800000
            price02 = 82920000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'GO 360':
            price01 = 6600000
            price02 = 9580000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'sony HDR':
            price01 = 13500000
            price02 = 6658510
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'sony fdr-ax700':
            price01 = 58000000
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[recordprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_laptop_apple():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " MacBook Air MGN63")
    z.insert(2, " MacBook Air MGN73")
    z.insert(3, " MacBook Air MGNE3")
    z.insert(4, " MacBook Air MYDC2")
    z.pack()
    def laptopappleprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'MacBook Air MGN63':
            price01 = 29869000
            price02 = 27450000
            price03 = 'ناموجود'
            price04 = 28300000
        elif x == 'MacBook Air MGN73':
            price01 = 34790000
            price02 = 35358000
            price03 = 'ناموجود'
            price04 = 33200000
        elif x == 'MacBook Air MGNE3':
            price01 = 34899000
            price02 = 32749000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'MacBook Air MYDC2':
            price01 = 35899000
            price02 = 38777000
            price03 = 'ناموجود'
            price04 = 37900000
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[laptopappleprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_lenovo():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Ideapad")
    z.insert(2, " V15 i3")
    z.insert(3, " ThinkBook")
    z.insert(4, " Legion-5 JD")
    z.pack()
    def lenovoprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Ideapad':
            price01 = 10600000
            price02 = 11899000
            price03 = 'ناموجود'
            price04 = 14200000
        elif x == 'V15 i3':
            price01 = 14800000
            price02 = 12650000
            price03 = 'ناموجود'
            price04 = 12400000
        elif x == 'ThinkBook':
            price01 = 23000000
            price02 = 21900000
            price03 = 'ناموجود'
            price04 = 20700000
        elif x == 'Legion-5 JD':
            price01 = 35900000
            price02 = 34500000
            price03 = 'ناموجود'
            price04 = 34500000
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[lenovoprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_asus():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " VivoBook")
    z.insert(2, " ZenBook")
    z.insert(3, " X543MA")
    z.insert(4, " R556EP")
    z.pack()
    def asusprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'VivoBook':
            price01 = 14820000
            price02 = 12400000
            price03 = 'ناموجود'
            price04 = 19200000
        elif x == 'ZenBook':
            price01 = 26670000
            price02 = 36844000
            price03 = 'ناموجود'
            price04 = 46100000
        elif x == 'X543MA':
            price01 = 8490000
            price02 = 7920000
            price03 = 'ناموجود'
            price04 = 8400000
        elif x == 'R556EP':
            price01 = 22450000
            price02 = 20800000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[asusprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_JBL():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " PARTYBOX")
    z.insert(2, " Go 3")
    z.insert(3, " Flip 5")
    z.insert(4, " Pulse 4")
    z.insert(5, " Clip 3")
    z.pack()
    def JBLprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'PARTYBOX':
            price01 = 16400000
            price02 = 19840000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Go 3':
            price01 = 949000
            price02 = 820000
            price03 = 'ناموجود'
            price04 = 915000
        elif x == 'Flip 5':
            price01 = 2450000
            price02 = 2270000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Pulse 4':
            price01 = 5460000
            price02 = 4900000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Clip 3':
            price01 = 1300000
            price02 = 1200000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[JBLprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_harman():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Go play")
    z.insert(2, " Onyx Studio 6")
    z.insert(3, " Aura Studio 7")
    z.insert(4, " soundsticks 4")
    z.pack()
    def harmanprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Go play':
            price01 = 6980000
            price02 = 6399000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Onyx Studio 6':
            price01 = 5500000
            price02 = 5200000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Aura Studio 7':
            price01 = 6980000
            price02 = 6300000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'soundsticks 4':
            price01 = 9200000
            price02 = 8650000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[harmanprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_speaker_sony():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " SRS-XB33")
    z.insert(2, " SRS-XB41")
    z.insert(3, " SRS-XB13")
    z.insert(4, " SRS-XP500")
    z.pack()
    def speaker_sonyprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'SRS-XB33':
            price01 = 3000000
            price02 = 2860000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'SRS-XB41':
            price01 = 'ناموجود'
            price02 = 1905000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'SRS-XB13':
            price01 = 1380000
            price02 = 1230000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'SRS-XP500':
            price01 = 8960000
            price02 = 7840000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[speaker_sonyprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_maxeeder():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " MX-TS102")
    z.insert(2, " NN-103")
    z.insert(3, " IRT223")
    z.insert(4, " FY305")
    z.pack()
    def maxeederprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'MX-TS102':
            price01 = 8350000
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'NN-103':
            price01 = 99000
            price02 = 135000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'IRT223':
            price01 = 11500000
            price02 = 9200000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'FY305':
            price01 = 2000000
            price02 = 1790000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[maxeederprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_headset_apple():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " hoco M1")
    z.insert(2, " wb earphone")
    z.insert(3, " airpod")
    z.pack()
    def headsetappleprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'hoco M1':
            price01 = 40000
            price02 = 100000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'wb earphone':
            price01 = 313200
            price02 = 150000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'airpod':
            price01 = 398760
            price02 = 530000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[headsetappleprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_anker():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " A3902J21")
    z.insert(2, " A3212")
    z.insert(3, " A3919")
    z.insert(4, " A3908")
    z.pack()
    def ankerprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'A3902J21':
            price01 = 2640000
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'A3212':
            price01 = 1000000
            price02 = 900000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'A3919':
            price01 = 2330000
            price02 = 1691000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'A3908':
            price01 = 1449000
            price02 = 1279000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[ankerprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_headset_samsung():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " Galaxy Buds 2")
    z.insert(2, " Galaxy Buds pro 2")
    z.insert(3, " Level U2")
    z.insert(4, " IG935")
    z.pack()
    def headsetsamsungprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'Galaxy Buds 2':
            price01 = 2000000
            price02 = 1130000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Galaxy Buds pro 2':
            price01 = 2776000
            price02 = 1130000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Level U2':
            price01 = 708000
            price02 = 600000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'IG935':
            price01 = 310000
            price02 = 215000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[headsetsamsungprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

def input_beats():
    b = StringVar()
    for widgets in frame.winfo_children():
        widgets.destroy()
    Label(frame, text='Enter the exact Model from the list, Press submit & then search: ').pack()
    a = Entry(frame,textvariable=b).pack()
    z=Listbox(frame)
    z.insert(1, " MARY BEATS 3")
    z.insert(2, " beats studio 3")
    z.insert(3, " power beats pro")
    z.insert(4, " Flex")
    z.insert(5, " urbeats")
    z.pack()
    def beatsprices():
        global price01
        global price02
        global price03
        global price04
        x = b.get()
        if x == 'MARY BEATS 3':
            price01 = 355000
            price02 = 215000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'beats studio 3':
            price01 = 5000000
            price02 = 4500000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'power beats pro':
            price01 = 5000000
            price02 = 4889000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'Flex':
            price01 = 1345000
            price02 = 1148000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        elif x == 'urbeats':
            price01 = 1400000
            price02 = 2821000
            price03 = 'ناموجود'
            price04 = 'ناموجود'
        else:
            price01 = 'ناموجود'
            price02 = 'ناموجود'
            price03 = 'ناموجود'
            price04 = 'ناموجود'

    btntaid=Button(frame, text='submit', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=lambda:[beatsprices(),submitt()]).pack(pady=10)
    def submitt():
        Label(frame, text='submitted',font=("Tohoma",15),fg = 'green',pady=20).pack()
    btnjstju=Button(frame,text='search', font=("Tohoma",15),bg = 'light gray',fg='dark blue', command=transport).pack(pady=20)
    btnback=Button(frame,text='back to main', font=("Tohoma",15),bg = 'light gray',fg='red', command=main).pack(pady=20)

# ye def e haminjoori bara in ke buttonemoon alaki vase khodesh command nashe

def transport():
    table(price01,price02,price03,price04)

# last page (result)

def table(price01,price02,price03,price04):
    window=Tk()
    window.geometry('550x400')
    table_f=Frame(window)
    table_f.pack()
    kala_t=ttk.Treeview(table_f)
    kala_t['columns']=('Id','Site','Rank','Price','Address')

    kala_t.column("#0", width=0,  stretch=NO)
    kala_t.column("Id",anchor=CENTER,width=50)
    kala_t.column("Site",anchor=CENTER,width=100)
    kala_t.column("Rank",anchor=CENTER,width=100)
    kala_t.column("Price",anchor=CENTER,width=100)
    kala_t.column("Address",anchor=CENTER,width=120)

    kala_t.heading("#0",text="",anchor=CENTER)
    kala_t.heading("Id",text="Id",anchor=CENTER)
    kala_t.heading("Site",text="Site",anchor=CENTER)
    kala_t.heading("Rank",text="Rank",anchor=CENTER)
    kala_t.heading("Price",text="Price",anchor=CENTER)
    kala_t.heading("Address",text="Address",anchor=CENTER)


    kala_t.insert(parent='',index='end',values=('1','digikala','4.7',price01,'digikala.com'))
    kala_t.insert(parent='',index='end',values=('2','torob','4.5',price02,'torob.ir'))
    kala_t.insert(parent='',index='end',values=('3','zanbil','3.6',price03,'zanbil.ir'))
    kala_t.insert(parent='',index='end',values=('4','berozkala','2.0',price04,'berozkala.com'))
    kala_t.pack()

main()

win.mainloop()
