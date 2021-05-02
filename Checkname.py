from tkinter import *
import csv


GUI = Tk ()
GUI.title('ໂປຣເເກຣມບັນທຶກຊື່')
GUI.geometry('600x900+490+30') #ເເກນx  x ເເກນy
FONT1 = ('Phetsarath OT',20)
FONT2 = ('Phetsarath OT',20)
FONT3 = ('Phetsarath OT',20)

photo = PhotoImage(file='unclemedia.png').subsample(2) # file = png
p = Label(GUI,image=photo)
p.pack(pady=20)

L1 = Label(GUI,text='ຊື່',font=FONT1).pack()
v_keep1 = StringVar()
E1 = Entry(textvariable=v_keep1,font=FONT2)
E1.pack()

L2 = Label(GUI,text='ນາມສະກຸນ',font=FONT2).pack()
v_keep2 = StringVar()
E2 = Entry(textvariable=v_keep2,font=FONT2).pack()

L3 = Label(GUI,text='ຊັ້ນຮຽນ',font=FONT3).pack()
v_keep3 = StringVar()
E3 = Entry(textvariable=v_keep3,font=FONT3).pack()

def Save(envent=None):
	keep1 = v_keep1.get()
	keep2 = v_keep2.get()
	keep3 = v_keep3.get()
	print('ຊື່:{}ນາມສະກຸນ:{}ຊັ້ນຮຽນ:{}'.format(keep1,keep2,keep3))
	v_keep1.set('')
	v_keep2.set('')
	v_keep3.set('')

	# read CSV
	with open('UncleMedia01.csv','a',encoding='utf-8',newline='') as f:
		fw = csv.writer(f)
		data = [keep1,keep2,keep3]
		fw.writerow(data)
	E1.focus()



GUI.bind('<Return>',Save)
B = Button(GUI,text='ຢືນຢັນການລົງຊື່',font=FONT1,command=Save).pack(ipadx=5,ipady=10,padx=20,pady=20)

GUI.mainloop()
