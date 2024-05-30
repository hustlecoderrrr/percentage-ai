from tkinter import *
root=Tk()
root.title("Percentage AI")
root.geometry("1000x700+300+100")
f=("MV Boli", 30 , "bold")

def compute():
	try:
		maths=float(ent_maths.get())
		chem=float(ent_chem.get())
		phy=float(ent_phy.get())
		percentage=(maths + chem + phy) * 100 / 300
		msg="percentage= " + str(round(percentage,2))
		lab_msg.configure(text=msg)
	except ValueError:
		lab_msg.configure(text="BHADVE MARKS NUMBERS ME HOTA HAI")

lab_maths = Label(root, text="enter maths marks", font=f)
ent_maths = Entry(root, font=f)
lab_chem = Label(root, text="enter chem marks", font=f)
ent_chem = Entry(root, font=f)
lab_phy = Label(root, text="enter phy marks", font=f)
ent_phy = Entry(root, font=f)
btn_find = Button(root, text="Find", font=f, command=compute)
lab_msg = Label(root,font=f)

lab_maths.pack(pady=10)
ent_maths.pack(pady=10)
lab_chem.pack(pady=10)
ent_chem.pack(pady=10)
lab_phy.pack(pady=10)
ent_phy.pack(pady=10)
btn_find.pack(pady=10)
lab_msg.pack(pady=10)

root.mainloop()
