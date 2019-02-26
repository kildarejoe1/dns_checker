from Tkinter import *
import socket

#Creates tkinter window app
window=Tk()
window.title="III DNS CHECKER"
domain=".iii.com"
tiers=["-db","-mt"]


def dnslookup():
    sitecode=e1_value.get()
    for tier in tiers:
        fqdn=sitecode+tier+domain
        external_record=externaldns(fqdn)
        internal_record=internaldns(fqdn)
        if external_record == internal_record:
            list1.insert(END,"The A Record External and Internal are set up correctly the FQDN of %s is %s" % (fqdn,external_record))
        else:
            return "Records dont Match - This needs to be fixed"


def externaldns(fqdn):
    ext_a_record=socket.gethostbyname(fqdn)
    return ext_a_record


def internaldns(fqdn):
    int_a_record=socket.gethostbyname(fqdn)
    return int_a_record


l1=Label(window,text="Enter Sitecode")
l1.grid(row=0,column=0)

b1=Button(window,text="Check now", command=dnslookup)
b1.grid(row=0,column=10)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

"""
r1=Radiobutton(window,text="Sierra App")
r1.grid(row=1,column=6)

r2=Radiobutton(window,text="Sierra DB")
r2.grid(row=2,column=6)
"""

list1=Listbox(window, height=6,width=35)
list1.grid(row=1,column=0,rowspan=10,columnspan=6)


l1=Label(window,text="Author=")
l1.grid(row=12,column=0)

l1=Label(window,text="henry.morrin@iii.com")
l1.grid(row=12,column=1)


sb1=Scrollbar(window)
sb1.grid(row=1,column=3)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="Close", command=dnslookup)
b1.grid(row=12,column=10)

#Creates Tkinter window
window.mainloop()
