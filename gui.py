from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import scrolledtext, messagebox
import csv 
from pandas import *
from time import sleep 

df = read_csv('/home/valtzz/Documents/data.csv',sep=',')
df['Name'] = df['Name'].str.strip()
adversaries = df['Name'].tolist() 
#print(adversaries)

class Page(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
	def show(self):
		self.lift()

class InitialAccess(Page):
	def clicked(self,txt):
		txt.insert(INSERT,'Escaneando nodos activos ...\n')
		sleep(5)
		txt.insert(INSERT,'[+] 0 nodos encontrados\n')
		txt.insert(INSERT,'Escaneando versiones de navegador ...\n')
		sleep(8)
		txt.insert(INSERT,'[+] 0 nodos con navegadores vulnerables\n')
		txt.insert(INSERT,'[+] Iniciando ejecución de código en los navegadores...\n')
		sleep(6)
		txt.insert(INSERT,'[+] Éxito!\n')

	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Initial Access')
		txt = scrolledtext.ScrolledText(self,width=40,height=20)
		txt.grid(column=0,row=3)
		btn = Button(self, text="Drive-by-Compromise", command=lambda : self.clicked(txt))
		btn.grid(column=1, row=3)
		


class Execution(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Execution')

class Persistence(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Persistence')

class PrivilegeEscalation(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Privilege Escalation')

class DefenceEvasion(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Defense Evasion')

class CredentialAccess(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Credential Access')

class Discovery(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Discovery')

class LateralMovement(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Lateral Movement')

class Collection(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Collection')

class CommandControl(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Command and Control')
		txt = scrolledtext.ScrolledText(self,width=40,height=20)
		txt.grid(column=0,row=3)
		btn = Button(self, text="QUICKRIDE over HTTP", command=lambda : self.clicked(txt))
		btn2 = Button(self, text="QUICKRIDE over HTTPS", command=lambda : self.clicked(txt))
		btn.grid(column=1, row=3)
		btn2.grid(column=1, row=4)



class Exfiltration(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Exfiltration')

class Impact(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		print('Impact')


class Page1(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		#label = tk.Label(self, text="This is page 1")
		#label.pack(side="top", fill="both", expand=True)
		lbl1 = Label(self, text="Posibles adversarios")
		lbl2 = Label(self, text="Se han relacionado los siguientes adversarios potenciales al perfil de su empresa:")
		lbl1.grid(column=0, row=0)
		lbl2.grid(column=0, row=1)

		txt = scrolledtext.ScrolledText(self,width=40,height=20)
		txt.grid(column=0,row=3)
		i = 3
		for x in adversaries:
		#print(x)
		#adv = Label(window,text = x)
			txt.insert(INSERT,x+'\n')
			#adv.grid(column=1, row=i)
			i = i +1
		Label(self, text="Estos adversarios son motivados por fines económicos y políticos.").grid(column=0, row=5)


class Page2(Page):

	def clicked(self,select):
		#lbl.configure(text="Button was clicked !!")
		if messagebox.askyesno('Elegir camino','¿Desea hacer pruebas personalizadas con ATT&CK?'):
			print(select)
			cframe = tk.Tk()
			custom = CustomEmulation(cframe)
			custom.group = select
			custom.pack(side="top", fill="both", expand=True)
			cframe.title(select)
			cframe.wm_geometry("400x400")
			cframe.mainloop()
			txt = scrolledtext.ScrolledText(self,width=40,height=20)
			txt.grid(column=0,row=3)
			#cframe = tk.Tk()
			#cframe.title = 'Pruebas personalizadas.'
			#custom = CustomEmulation(cframe)

	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		label = tk.Label(self, text="Elija un adversario para emulación.")
		label.grid(column=0, row=1)
		combo = Combobox(self)
		combo['values']= tuple(adversaries)
		combo.current(1)
		combo.grid(column=0, row=3)
		btn = Button(self, text="Comenzar Emulación", command=lambda : self.clicked(combo.get()))
		btn.grid(column=1, row=3)
		#label.pack(side="top", fill="both", expand=True)


class Page3(Page):
   def __init__(self, *args, **kwargs):
	   Page.__init__(self, *args, **kwargs)
	   label = tk.Label(self, text="This is page 3")
	   label.pack(side="top", fill="both", expand=True)

class Tactics(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.group = 'APT38'
		print(self.group)
		tk.Frame.__init__(self, *args, **kwargs)
		p1 = InitialAccess(self)
		p2 = Execution(self)
		p3 = Persistence(self)
		p4 = PrivilegeEscalation(self)
		p5 = DefenceEvasion(self)
		p6 = CredentialAccess(self)
		p7 = Discovery(self)
		p8 = LateralMovement(self)
		p9 = Collection(self)
		p10 = CommandControl(self)
		p11 = Exfiltration(self)
		p12= Impact(self)

		p1.group = self.group
		p2.group = self.group

		buttonframe = tk.Frame(self)
		container = tk.Frame(self)
		buttonframe.pack(side="top", fill="x", expand=False)
		container.pack(side="top", fill="both", expand=True)

		p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p9.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p10.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p11.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p12.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		b1 = tk.Button(buttonframe, text="InitialAccess", command=p1.lift)
		b2 = tk.Button(buttonframe, text="Execution", command=p2.lift)
		b3 = tk.Button(buttonframe, text="Persistence", command=p3.lift)
		b4 = tk.Button(buttonframe, text="Privilege Escalation", command=p4.lift)
		b5 = tk.Button(buttonframe, text="Defense Evasion", command=p5.lift)
		b6 = tk.Button(buttonframe, text="Credential Access", command=p6.lift)
		b7 = tk.Button(buttonframe, text="Discovery", command=p7.lift)
		b8 = tk.Button(buttonframe, text="Lateral Movement", command=p8.lift)
		b9 = tk.Button(buttonframe, text="Collection", command=p9.lift)
		b10 = tk.Button(buttonframe, text="Command and Control", command=p10.lift)
		b11 = tk.Button(buttonframe, text="Exfiltration", command=p11.lift)
		b12 = tk.Button(buttonframe, text="Impact", command=p12.lift)

		b1.pack(side="left")
		b2.pack(side="left")
		b3.pack(side="left")
		b4.pack(side="left")
		b5.pack(side="left")
		b6.pack(side="left")
		b7.pack(side="left")
		b8.pack(side="left")
		b9.pack(side="left")
		b10.pack(side="left")
		b11.pack(side="left")
		b12.pack(side="left")

		p1.show()

class Description(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.group = ''
		txt = scrolledtext.ScrolledText(self,width=40,height=20)
		txt.grid(column=0,row=3)
		txt.insert(INSERT,'APT38 is a financially-motivated threat group that is backed by the North Korean regime. The group mainly targets banks and financial institutions.\n')

class MainView(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
		p1 = Page1(self)
		p2 = Page2(self)
		p3 = Page3(self)

		buttonframe = tk.Frame(self)
		container = tk.Frame(self)
		buttonframe.pack(side="top", fill="x", expand=False)
		container.pack(side="top", fill="both", expand=True)

		p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		b1 = tk.Button(buttonframe, text="Adversarios", command=p1.lift)
		b2 = tk.Button(buttonframe, text="Emulación", command=p2.lift)
		b3 = tk.Button(buttonframe, text="Reporte", command=p3.lift)

		b1.pack(side="left")
		b2.pack(side="left")
		b3.pack(side="left")

		p1.show()

class CustomEmulation(tk.Frame):
	def __init__(self, *args, **kwargs):
		self.group = 'APT38'
		print(self.group)
		tk.Frame.__init__(self, *args, **kwargs)
		p1 = Tactics(self)
		p2 = Description(self)
		p3 = Page3(self)

		p1.group = self.group
		p2.group = self.group

		buttonframe = tk.Frame(self)
		container = tk.Frame(self)
		buttonframe.pack(side="top", fill="x", expand=False)
		container.pack(side="top", fill="both", expand=True)

		p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
		p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		b1 = tk.Button(buttonframe, text="Tacticas", command=p1.lift)
		b2 = tk.Button(buttonframe, text="Descripción", command=p2.lift)
		b3 = tk.Button(buttonframe, text="", command=p3.lift)

		b1.pack(side="left")
		b2.pack(side="left")
		b3.pack(side="left")

		p1.show()



if __name__ == "__main__":
	root = tk.Tk()
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.title('Emulación de Adversarios')
	root.wm_geometry("400x400")
	root.mainloop()
