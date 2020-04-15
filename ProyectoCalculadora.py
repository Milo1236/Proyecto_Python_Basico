import tkinter as tk
# Declarando los recursos que se van a utilizar en el programa

'''
numero1 = int(input(' Ingrese el 1er numero: '))
numero2 = int(input(' Ingrese el 2edo numero: '))
'''
root = tk.Tk()
root.geometry('800x500')
root.title('CALCULADORA BASICA')
root.configure(bg="#2E86C1")
tk.Label(root, text='CALCULADORA', bg="#009688", fg='white', font=('', 32)).place(x=240, y=30)


s1 = tk.StringVar()
s2 = tk.StringVar()
r1 = tk.StringVar()
r2 = tk.StringVar()
m1 = tk.StringVar()
m2 = tk.StringVar()
d1 = tk.StringVar()
d2 = tk.StringVar()

mensaje = tk.StringVar()
'''
mensaje2 = tk.StringVar()
mensaje3 = tk.StringVar()
mensaje4 = tk.StringVar()
'''
sw = True ##

# Lógica del programa

def sumar():
    x1 = int(s1.get())
    y1 = int(s2.get())
    s1.set('')
    s2.set('')
    mensaje.set(x1+y1)
    print(x1+y1)

def restar():
    x2 = int(r1.get())
    y2 = int(r2.get())
    r1.set('')
    r2.set('')
    mensaje.set(x2-y2)
    print(x2-y2)

def multiplicar():
    x3 = int(m1.get())
    y3 = int(m2.get())
    m1.set('')
    m2.set('')
    mensaje.set(x3 * y3)
    print(x3*y3)

def dividir():
    x4 = int(d1.get())
    y4 = int(d2.get())
    d1.set('')
    d2.set('')
    mensaje.set(x4 / y4)
    print(x4/y4)

def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


def opcion_no_disponible():
    print('Opcion no disponible')

# Metodos para la Consola
def sumar2():
    a = int(input('Ingrese el 1er numero: '))
    b = int(input('Ingrese el 2do numero: '))
    print('El Resultado es: ', a + b)

def restar2():
    a = int(input('Ingrese el 1er numero: '))
    b = int(input('Ingrese el 2do numero: '))
    print('El Resultado es: ', a - b)

def multiplicar2():
    a = int(input('Ingrese el 1er numero: '))
    b = int(input('Ingrese el 2do numero: '))
    print('El Resultado es: ', a * b)

def dividir2():
    a = int(input('Ingrese el 1er numero: '))
    b = int(input('Ingrese el 2do numero: '))
    print('El Resultado es: ', a / b)


#Sumar
tk.Label(root, text='Sumar', bg="#009688", fg='white', font=('', 24)).place(x=30, y=110)
tk.Entry(root, justify='center', textvariable=s1).place(x=200, y=120)
tk.Entry(root, justify='center', textvariable=s2).place(x=350, y=120)
tk.Button(root, text=' = ', bd=0, command=sumar).place(x=550, y=120)

#Restar
tk.Label(root, text='Restar', bg="#009688", fg='white', font=('', 24)).place(x=30, y=170)
tk.Entry(root, justify='center', textvariable=r1).place(x=200, y=180)
tk.Entry(root, justify='center', textvariable=r2).place(x=350, y=180)
tk.Button(root, text=' = ', bd=0, command=restar).place(x=550, y=180)

#Multiplicar
tk.Label(root, text='Multiplicar', bg="#009688", fg='white', font=('', 24)).place(x=30, y=230)
tk.Entry(root, justify='center', textvariable=m1).place(x=200, y=240)
tk.Entry(root, justify='center', textvariable=m2).place(x=350, y=240)
tk.Button(root, text=' = ', bd=0, command=multiplicar).place(x=550, y=240)

#Dividir
tk.Label(root, text='Dividir', bg="#009688", fg='white', font=('', 24)).place(x=30, y=290)
tk.Entry(root, justify='center', textvariable=d1).place(x=200, y=300)
tk.Entry(root, justify='center', textvariable=d2).place(x=350, y=300)
tk.Button(root, text=' = ', bd=0, command=dividir).place(x=550, y=300)

#mensaje o Igual
tk.Label(root, textvariable=mensaje, bg="#009688", fg='white', font=('', 24)).place(x=400, y=370)
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=400, y=450)


root.mainloop()




# La interfaz del usuario


menu = '''
======= Calculadora ======
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
'''

while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        sumar2()
    elif opcion == 2:
        restar2()
    elif opcion == 3:
        multiplicar2()
    elif opcion == 4:
        dividir2()
    elif opcion == 5:
        terminar_programa()
    else:
        opcion_no_disponible()


