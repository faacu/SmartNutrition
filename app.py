from tkinter import *

#configuracion de la raiz
root= Tk()
root.title("SmartNutrition")
root.config(bg="lightpink")

#configuracion del frame
frame= Frame(root)
frame.config(bg="lightpink")
frame.config(width=1000,height=1000)
frame.pack(fill="both",expand=1)

#primera formula
n1= StringVar()
n2= StringVar()
r= StringVar()

label= Label(frame,text="Peso Actual",bg="lightpink",font="Arial")
label.grid(row=0,column=0, sticky="w",padx=5)
entry= Entry(frame)
entry.grid(row=0,column=1,padx=5)
label2= Label(frame,text="Talla",bg="lightpink",font="Arial")
label2.grid(row=1,column=0, sticky="w",padx=5)
entry2= Entry(frame)
entry2.grid(row=1,column=1,padx=5)
entry.config(justify="center",textvariable=n1)
entry2.config(justify="center",textvariable=n2)
label3= Label(frame,text="Indice de Masa Corporal",bg="lightpink",font="Arial")
label3.grid(row=2,column=0, sticky="w",padx=5)
entry3= Entry(frame)
entry3.grid(row=2,column=1,padx=5)
entry3.config(state="disable",textvariable=r)
Label(frame,bg="lightpink").grid(row=3,column=1)

#funcion porcentaje indice masa corporal
def calcular():
    r.set( float(n1.get())/ float(n2.get())**2)
    borrar()
def borrar():
    n1.set("")
    n2.set("")

buton=Button(frame,text="Calcular",command=calcular)
buton.grid(row=4,column=1,pady=3)
buton.config(bg="violet",fg="white",font="Constantia")

#segunda formula
n3= StringVar()
n4= StringVar()
r1= StringVar()

label1= Label(frame,text="Peso Actual",bg="lightpink",font="Arial")
label1.grid(row=5,column=0, sticky="w",padx=5)
entry1= Entry(frame)
entry1.grid(row=5,column=1,padx=5)
label4= Label(frame,text="Peso Usual",bg="lightpink",font="Arial")
label4.grid(row=6,column=0, sticky="w",padx=5)
entry4= Entry(frame)
entry4.grid(row=6,column=1,padx=5)
entry1.config(justify="center",textvariable=n3)
entry4.config(justify="center",textvariable=n4)
label5= Label(frame,text="Porcentaje Peso Usual(%)",bg="lightpink",font="Arial")
label5.grid(row=7,column=0, sticky="w",padx=5)
entry5= Entry(frame)
entry5.grid(row=7,column=1,padx=5)
entry5.config(state="disable",textvariable=r1)
Label(frame,bg="lightpink").grid(row=8,column=1)

#formula porcentaje de peso usual
def calculo():
    r1.set(float(n3.get())/float(n4.get())*100)
    borrar1()
def borrar1():
    n3.set("")
    n4.set("")
buton1=Button(frame,text="Calcular",command=calculo)
buton1.grid(row=9,column=1,pady=3)
buton1.config(bg="violet",fg="white",font="Constantia")

#tercera formula
n5= StringVar()
n6= StringVar()
r2= StringVar()

label6= Label(frame,text="Urea Urinaria",bg="lightpink",font="Arial")
label6.grid(row=10,column=0, sticky="w",padx=5)
entry6= Entry(frame)
entry6.grid(row=10,column=1,padx=5)
label7= Label(frame,text="Diuresis",bg="lightpink",font="Arial")
label7.grid(row=11,column=0, sticky="w",padx=5)
entry7= Entry(frame)
entry7.grid(row=11,column=1,padx=5)
entry6.config(justify="center",textvariable=n5)
entry7.config(justify="center",textvariable=n6)
label8= Label(frame,text="Nitrogeno Ureico Urinario",bg="lightpink",font="Arial")
label8.grid(row=12,column=0, sticky="w",padx=5)
entry8= Entry(frame)
entry8.grid(row=12,column=1,padx=5)
entry8.config(state="disable",textvariable=r2)
Label(frame,bg="lightpink").grid(row=13,column=1)

#funcion nitrogeno ureico urinario
def calculo1():
    r2.set(float(n5.get())*float(n6.get())*0.467)
    borrar2()
def borrar2():
    n5.set("")
    n6.set("")
buton2=Button(frame,text="Calcular",command=calculo1)
buton2.grid(row=14,column=1,pady=3)
buton2.config(bg="violet",fg="white",font="Constantia")

#Cuarta formula
n7= StringVar()
n8= StringVar()
r3= StringVar()

label9= Label(frame,text="Nitrogeno Ureico Urinario",bg="lightpink",font="Arial")
label9.grid(row=15,column=0, sticky="w",padx=5)
entry9= Entry(frame)
entry9.grid(row=15,column=1,padx=5)
label10= Label(frame,text="Nitrogeno Ingerido",bg="lightpink",font="Arial")
label10.grid(row=16,column=0, sticky="w",padx=5)
entry10= Entry(frame)
entry10.grid(row=16,column=1,padx=5)
entry9.config(justify="center",textvariable=n7)
entry10.config(justify="center",textvariable=n8)
label11= Label(frame,text="Indice Catabolico",bg="lightpink",font="Arial")
label11.grid(row=17,column=0, sticky="w",padx=5)
entry11= Entry(frame)
entry11.grid(row=17,column=1,padx=5)
entry11.config(state="disable",textvariable=r3)
Label(frame,bg="lightpink").grid(row=18,column=1)

#funcion indice catabolica de bistrian
def calculo2():
    r3.set(float(n7.get())-(0.5*(float(n8.get())/6.25)+3))
    borrar3()
def borrar3():
    n7.set("")
    n8.set("")
buton3=Button(frame,text="Calcular",command=calculo2)
buton3.grid(row=19,column=1,pady=3)
buton3.config(bg="violet",fg="white",font="Constantia")

#formula cinco
n9= StringVar()
n10= StringVar()
r4= StringVar()

label12= Label(frame,text="Perimetro Branquial",bg="lightpink",font="Arial")
label12.grid(row=15,column=3, sticky="w",padx=5)
entry12= Entry(frame)
entry12.grid(row=15,column=4,padx=5)
label13= Label(frame,text="Pliegue Tricipital",bg="lightpink",font="Arial")
label13.grid(row=16,column=3, sticky="w",padx=5)
entry13= Entry(frame)
entry13.grid(row=16,column=4,padx=5)
entry12.config(justify="center",textvariable=n9)
entry13.config(justify="center",textvariable=n10)
label14= Label(frame,text="Circunferencia Muscular del Brazo(cm)",bg="lightpink",font="Arial")
label14.grid(row=17,column=3, sticky="w",padx=5)
entry14= Entry(frame)
entry14.grid(row=17,column=4,padx=5)
entry14.config(state="disable",textvariable=r4)
Label(frame,bg="lightpink").grid(row=18,column=4)

#funcion circunferencia muscular del brazo
def calculo3():
    r4.set(float(n9.get())-0.314*float(n10.get()))
    borrar4()
def borrar4():
    n9.set("")
    n10.set("")
buton4=Button(frame,text="Calcular",command=calculo3)
buton4.grid(row=19,column=4,pady=3)
buton4.config(bg="violet",fg="white",font="Constantia")

#formula seis
n11= StringVar()
n12= StringVar()
r5= StringVar()

label15= Label(frame,text="Creatinina Urinaria Real",bg="lightpink",font="Arial")
label15.grid(row=0,column=3, sticky="w",padx=5)
entry15= Entry(frame)
entry15.grid(row=0,column=4,padx=5)
label16= Label(frame,text="Creatinina Urinaria Ideal para Talla",bg="lightpink",font="Arial")
label16.grid(row=1,column=3, sticky="w",padx=5)
entry16= Entry(frame)
entry16.grid(row=1,column=4,padx=5)
entry15.config(justify="center",textvariable=n11)
entry16.config(justify="center",textvariable=n12)
label17= Label(frame,text="Indice Creatinina/Talla",bg="lightpink",font="Arial")
label17.grid(row=2,column=3, sticky="w",padx=5)
entry17= Entry(frame)
entry17.grid(row=2,column=4,padx=5)
entry17.config(state="disable",textvariable=r5)
Label(frame,bg="lightpink").grid(row=3,column=4)

#funcion indice creatinina/talla
def calculo4():
    r5.set((float(n11.get())/float(n12.get()))*100)
    borrar5()
def borrar5():
    n11.set("")
    n12.set("")
buton5=Button(frame,text="Calcular",command=calculo4)
buton5.grid(row=4,column=4,pady=3)
buton5.config(bg="violet",fg="white",font="Constantia")

#formula siete
n13= StringVar()
n14= StringVar()
r6= StringVar()

label18= Label(frame,text="Peso Actual",bg="lightpink",font="Arial")
label18.grid(row=5,column=3, sticky="w",padx=5)
entry18= Entry(frame)
entry18.grid(row=5,column=4,padx=5)
label19= Label(frame,text="Peso Habitual",bg="lightpink",font="Arial")
label19.grid(row=6,column=3, sticky="w",padx=5)
entry19= Entry(frame)
entry19.grid(row=6,column=4,padx=5)
entry18.config(justify="center",textvariable=n13)
entry19.config(justify="center",textvariable=n14)
label20= Label(frame,text="Porcentaje Perdida de Peso(%)",bg="lightpink",font="Arial")
label20.grid(row=7,column=3, sticky="w",padx=5)
entry20= Entry(frame)
entry20.grid(row=7,column=4,padx=5)
entry20.config(state="disable",textvariable=r6)
Label(frame,bg="lightpink").grid(row=8,column=4)
#funcion % perdida de peso
def calcular2():
    r6.set(((float(n14.get())-float(n13.get()))/float(n14.get()))*100)
    borrar6()
def borrar6():
     n13.set("")
     n14.set("")

buton6=Button(frame,text="Calcular",command=calcular2)
buton6.grid(row=9,column=4,pady=3)
buton6.config(bg="violet",fg="white",font="Constantia")

#formula nueve
n19= StringVar()
n20= StringVar()
r8= StringVar()

label24= Label(frame,text="Peso Actual",bg="lightpink",font="Arial")
label24.grid(row=10,column=3, sticky="w",padx=5)
entry24= Entry(frame)
entry24.grid(row=10,column=4,padx=5)
label25= Label(frame,text="Peso Ideal",bg="lightpink",font="Arial")
label25.grid(row=11,column=3, sticky="w",padx=5)
entry25= Entry(frame)
entry25.grid(row=11,column=4,padx=5)
entry24.config(justify="center",textvariable=n19)
entry25.config(justify="center",textvariable=n20)
label26= Label(frame,text="Porcentaje Peso Ideal(%)",bg="lightpink",font="Arial")
label26.grid(row=12,column=3, sticky="w",padx=5)
entry26= Entry(frame)
entry26.grid(row=12,column=4,padx=5)
entry26.config(state="disable",textvariable=r8)
Label(frame,bg="lightpink").grid(row=13,column=4)

#formula porcentaje peso ideal
def calcular4():
    r8.set(float(n19.get())/float(n20.get())*100)
    borrar7()
def borrar7():
    n19.set("")
    n20.set("")
buton7=Button(frame,text="Calcular",command=calcular4)
buton7.grid(row=14,column=4,pady=3)
buton7.config(bg="violet",fg="white",font="Constantia")

#funcion ocho
n15= StringVar()
n16= StringVar()
n17= StringVar()
n18= StringVar()
r7= StringVar()

label21= Label(frame,text="Pliegue Tricipital",bg="lightpink",font="Arial")
label21.grid(row=20,column=0, sticky="w",padx=5)
entry21= Entry(frame)
entry21.grid(row=20,column=1,padx=5)
label22= Label(frame,text="Pliegue Bicipital",bg="lightpink",font="Arial")
label22.grid(row=21,column=0, sticky="w",padx=5)
entry22= Entry(frame)
entry22.grid(row=21,column=1,padx=5)
entry21.config(justify="center",textvariable=n15)
entry22.config(justify="center",textvariable=n16)
label24= Label(frame,text="Pliegue Subescapular",bg="lightpink",font="Arial")
label24.grid(row=22,column=0,sticky="w",padx=5)
entry24= Entry(frame)
entry24.grid(row=22,column=1,padx=5)
entry24.config(justify="center",textvariable=n17)
label25= Label(frame,text="Pliegue Supraillaco",bg="lightpink",font="Arial")
label25.grid(row=23,column=0, sticky="w",padx=5)
entry25= Entry(frame)
entry25.grid(row=23,column=1,padx=5)
entry25.config(justify="center",textvariable=n18)
label23= Label(frame,text="Grasa por 4 Pliegues(mm)",bg="lightpink",font="Arial")
label23.grid(row=24,column=0,sticky="w",padx=5)
entry23= Entry(frame)
entry23.grid(row=24,column=1,padx=5)
entry23.config(state="disable",textvariable=r7)
Label(frame,bg="lightpink").grid(row=25,column=1)

#formula % de grasa por 4 pliegues
def calcular3():
    r7.set(float(n15.get())+float(n16.get())+float(n17.get())+float(n18.get()))
    borrar8()
def borrar8():
    n15.set("")
    n16.set("")
    n17.set("")
    n18.set("")
buton8=Button(frame,text="Calcular",command=calcular3)
buton8.grid(row=26,column=1,pady=5)
buton8.config(bg="violet",fg="white",font="Constantia")

label24=Label(frame,text="Todos los derechos reservados 2020 ©", bg="lightpink",font=("Arial",8),fg="white")
label24.grid(row=26,column=15)


#nucleo de apertura
root.mainloop()