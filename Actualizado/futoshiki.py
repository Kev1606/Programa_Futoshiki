# Tecnológico de Costa Rica 
# Escuela de Computación
# Carrera: Ingeniería en Computación

# Curso: Taller de Programación     
# Grupo: 05
# Profesor: William Mata Rodríguez
# Semestre: I 2021

# Autor: Kevin Vinicio Núñez Cruz
# Fecha de Inicio: 12 de Junio del 2021
# Fecha de Entrega: 29 de Junio del 2021
######################################################## MÓDULOS ##################################################################################
import os
import time
import pickle
import random
import tkinter as tk
from tkinter import messagebox
######################################################## CLASES ###################################################################################
class Configuracion:
# Esta opción es para indicar las condiciones con que se va a jugar.  
# Contiene los siguientes datos que se van a guardar en el archivo “futoshiki2021configuración.dat”: 
# (los valores por omisión –o default- están señalados con el círculo en rojo) 
    def __init__(self,master):  #Método Constructor
        self.ventanaConfigurar = tk.Toplevel(master)    #Se crea la ventana de configuración 
        self.ventanaConfigurar.geometry('500x300')      
        self.ventanaConfigurar.title('Configuración')
        self.lblTitulo = tk.Label(self.ventanaConfigurar,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X)

        self.nivelJuego = tk.IntVar()   #variable int del nivel de juego
        configure = open('futoshiki2021configuracion.dat','rb')    #se abre el archivo que guarda la configuración
        configuracion = pickle.load(configure)                     #se cargan en la variable "configuracion"

        self.nivelJuego.set(str(configuracion[0]))  #se asignan los valores que se guardan directamente y se conserva de esa manera al desplegar nuevamente la ventana
        configure.close()      #se cierra el archivo|

        self.lblJuego = tk.Label(self.ventanaConfigurar,text='Nivel:',font=('System',12)).place(x=10,y=45)
        self.check1 = tk.Radiobutton(self.ventanaConfigurar,text="Fácil", font=('System',12),value = 1, variable=self.nivelJuego \
                                                            , command=self.configuraciones \
                                                            ).place(x=55,y=45)

        self.check2 = tk.Radiobutton(self.ventanaConfigurar,text="Intermedio", font=('System',12),value = 2, variable=self.nivelJuego \
                                                            ,command=self.configuraciones \
                                                            ).place(x=55,y=65)

        self.check3 = tk.Radiobutton(self.ventanaConfigurar,text="Díficil",font=('System',12), value = 3, variable=self.nivelJuego \
                                                            ,command=self.configuraciones \
                                                            ).place(x=55,y=85)

        self.relojConfig = tk.IntVar()      #variable int de la configuración del reloj
        configure = open('futoshiki2021configuracion.dat','rb')
        configuracion = pickle.load(configure)
        self.relojConfig.set(str(configuracion[1]))
        configure.close()

        self.lblReloj = tk.Label(self.ventanaConfigurar,text='Reloj:',font=('System',12)).place(x=10,y=115)
        self.chkConTiempo = tk.Radiobutton(self.ventanaConfigurar,text="Si", font=('System',12), value = 1, variable=self.relojConfig \
                                                    ,command=self.configuraciones\
                                                    ).place(x=55,y=115)

        self.chkSinTiempo = tk.Radiobutton(self.ventanaConfigurar,text="No", font=('System',12), value = 2, variable=self.relojConfig \
                                                    ,command=self.configuraciones\
                                                    ).place(x=55,y=135)

        self.chkTimer = tk.Radiobutton(self.ventanaConfigurar,text="Timer", font=('System',12), value = 3, variable=self.relojConfig \
                                                    ,command=self.configuraciones\
                                                    ).place(x=55,y=155)
        # TEMPORIZADOR VARIABLES
        self.hour= tk.StringVar()
        self.minute= tk.StringVar()
        self.second= tk.StringVar()

        #Se configura las variables en el valor default
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")
        self.hourLabel = tk.Label(self.ventanaConfigurar,text='Horas',width=8,font=('System',12)).place(x=285,y=110)
        self.minuteLabel = tk.Label(self.ventanaConfigurar,text='Minutos',width=8,font=('System',12)).place(x=337,y=110)
        self.secondLabel = tk.Label(self.ventanaConfigurar,text='Segundos',width=8,font=('System',12)).place(x=399,y=110)
        self.hourEntry= tk.Entry(self.ventanaConfigurar, width=3, font=("System",18,""),
                            textvariable=self.hour)
        self.hourEntry.place(x=300,y=135)
            
        self.minuteEntry= tk.Entry(self.ventanaConfigurar, width=3, font=("System",18,""),
                            textvariable=self.minute)
        self.minuteEntry.place(x=350,y=135)
            
        self.secondEntry= tk.Entry(self.ventanaConfigurar, width=3, font=("System",18,""),
                            textvariable=self.second)
        self.secondEntry.place(x=400,y=135)

        self.PosicionNumeros = tk.IntVar()                      #variable int de la posición de los botones de juego
        configure = open('futoshiki2021configuracion.dat','rb')
        configuracion = pickle.load(configure)
        self.PosicionNumeros.set(str(configuracion[2]))

        self.lblPosicionDigitos = tk.Label(self.ventanaConfigurar,text='Posición en la ventana del panel de dígitos:',font=('System',12)).place(x=10,y=185)
        self.chkDerecha = tk.Radiobutton(self.ventanaConfigurar,text="Derecha", font=('System',12), value = 1, variable=self.PosicionNumeros \
                                                    ,command=self.configuraciones\
                                                    ).place(x=300,y=185)

        self.chkIzquierda = tk.Radiobutton(self.ventanaConfigurar,text="Izquierda", font=('System',12), value = 2, variable=self.PosicionNumeros \
                                                    ,command=self.configuraciones\
                                                    ).place(x=300,y=205)

        self.btnAceptar = tk.Button(self.ventanaConfigurar,text='Aceptar',command=self.confirmar).place(x=35,y=235)
####################################################################################################################################################
    def configuraciones(self):
        self.ventanaConfigurar.wait_window()    #espera la ventana a que se cierre

        # Se asignan variables tomando los datos de los radioButton
        nivelJuego = self.nivelJuego.get()      
        relojConfig = self.relojConfig.get()
        PosicionNumeros = self.PosicionNumeros.get()

        hora = self.hour.get()
        minuto = self.minute.get()
        segundo = self.second.get()

        secondAux = segundo
        minuteAux = minuto
        hourAux = hora

        self.configuracion = open('futoshiki2021configuracion.dat','wb')    #se abre el archivo para guardar la configuración
        pickle.dump((nivelJuego,relojConfig,PosicionNumeros,hora,minuto,segundo),self.configuracion)#se graban las variables cada vez que se ingrese a la ventana Configuración
        self.configuracion.close()
        return (nivelJuego,relojConfig,PosicionNumeros,hora,minuto,segundo,hourAux,minuteAux,secondAux)     #retorna las variables
####################################################################################################################################################
    def confirmar(self):
        if int(self.relojConfig.get()) == 3:
            try:
                    s = int(self.secondEntry.get())
                    m = int(self.minuteEntry.get())
                    h = int(self.hourEntry.get())

                    if s <= 59 and m <= 59 and h <= 2:

                        if s > 0 or m > 0 or h > 0:
                            self.ventanaConfigurar.destroy()
                        else:
                            messagebox.showinfo("Tiempo Incorrecto","Por favor ingresar un intervalo de tiempo correcto")
                    else:
                        messagebox.showinfo("Tiempo Incorrecto","Por favor ingresar un intervalo de tiempo correcto")
                        return
            except:
                messagebox.showinfo("Tiempo Incorrecto","Por favor ingresar un intervalo de tiempo correcto")
                return
        else:
            self.ventanaConfigurar.destroy()

######################################################## CLASE PRINCIPAL ##########################################################################
class Futoshiki(tk.Frame):                  #se crea la clase padre
    # Método Constructor
    def __init__(self,master=None):
        super().__init__(master)
        self.master =  master   #esta variable almacena la ventana principal
        self.master.title('Futoshiki')
        self.master.geometry('600x600')

        # PARTIDAS DE JUEGO #
        partidas= open('futoshiki2021partidas.dat','wb')
        #graba las partidas de juego
        pickle.dump([
                [(("4",0,1),("1",0,3),
                ("2",2,1),("5",2,3),("3",2,4),
                ("1",3,1),("2",3,3),("5",4,4)),
                (("2",0,3),
                ("2",1,0),("1",1,2),("3",1,3),
                ("3",2,2),("1",2,3),
                ("1",4,0),("5",4,4)),
                (("5",0,2),
                ("1",1,0),("3",1,1),("2",1,4),
                ("3",3,0),("1",3,4),
                ("1",4,3),("5",4,4))
                ],\
                [
                (("5",0,0),("3",0,4),(">",0,2),
                ("2",1,1),("v",2,0),
                (">",3,0),("ʌ",3,2),
                (">",4,1)),
                (("3",0,0),("v",0,0),("4",0,1),("˅",1,3),("˄",1,4),
                (">",2,3),("2",2,4),(">",4,3)),
                (("5",0,0),("<",0,1),
                ("ʌ",1,0),("3",1,3),
                ("ʌ",3,1),("ʌ",3,3),
                ("3",4,1),(">",4,2))
                ],\
                [
                (("2",0,0),("v",0,4),
                ("v",1,0),("<",1,1),
                ("5",2,1),("<",2,3),
                (">",3,0),("˅",3,3),
                ("1",4,2)),
                ((">",0,1),("4",0,3),("ʌ",0,3),
                (">",1,0),("4",1,4),
                ("<",2,0),("ʌ",2,1),("ʌ",2,0),
                ("1",3,3)),
                (("ʌ",0,0),("<",0,3),
                ("5",1,0),(">",0,1),("ʌ",1,3),
                ("4",2,1),("v",2,4),
                (">",3,0),("ʌ",3,0))
                ]],partidas)
        partidas.close()

        #llama al método que mantiene toda la interfaz principal del juego
        self.inicializar_gui()

        # VARIABLES DE LA CONFIGURACION POR DEFAULT #
        self.nivelJuego = tk.IntVar()
        self.nivelJuego.set('1')
        self.relojConfig = tk.IntVar()
        self.relojConfig.set('1')
        self.PosicionNumeros = tk.IntVar()
        self.PosicionNumeros.set('1')
        self.configuraciones = (self.nivelJuego.get(),self.relojConfig.get(),self.PosicionNumeros.get())    #se crea una lista que guarde la configuración por default 

        self.valor00 = 0
        self.valor01 = 0
        self.valor02 = 0
        self.valor03 = 0
        self.valor04 = 0

        self.valor10 = 0
        self.valor11 = 0
        self.valor12 = 0
        self.valor13 = 0
        self.valor14 = 0

        self.valor20 = 0
        self.valor21 = 0
        self.valor22 = 0
        self.valor23 = 0
        self.valor24 = 0

        self.valor30 = 0
        self.valor31 = 0
        self.valor32 = 0
        self.valor33 = 0
        self.valor34 = 0

        self.valor40 = 0
        self.valor41 = 0
        self.valor42 = 0
        self.valor43 = 0
        self.valor44 = 0

        self.valoresH = [[self.valor00,self.valor01,self.valor02,self.valor03,self.valor04],\
                      [self.valor10,self.valor11,self.valor12,self.valor13,self.valor14],\
                      [self.valor20,self.valor21,self.valor22,self.valor23,self.valor24],\
                      [self.valor30,self.valor31,self.valor32,self.valor33,self.valor34],\
                      [self.valor40,self.valor41,self.valor42,self.valor43,self.valor44]]

        self.valoresV = [[self.valor00,self.valor10,self.valor20,self.valor30,self.valor40],\
                      [self.valor01,self.valor11,self.valor21,self.valor31,self.valor41],\
                      [self.valor02,self.valor12,self.valor22,self.valor32,self.valor42],\
                      [self.valor03,self.valor13,self.valor23,self.valor33,self.valor43],\
                      [self.valor04,self.valor14,self.valor24,self.valor34,self.valor44]]

        self.signoRestriccionesH = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
        self.signoRestriccionesV = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    
        self.matrizResultados = []

        #TEMPORIZADOR VARIABLES
        self.flag = False

        self.hour=tk.StringVar()
        self.minute=tk.StringVar()
        self.second=tk.StringVar()
        #Se configura las variables en el valor default del reloj
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        self.Top10Facil = []
        self.Top10Intermedio = []
        self.Top10Dificil = []


        self.configuracion = open('futoshiki2021configuracion.dat','wb')
        pickle.dump(self.configuraciones,self.configuracion)    #grabo la configuración en el archivo .dat
        self.configuracion.close()
###################################################################################################################################################      
    def inicializar_gui(self):
        self.lblTitulo = tk.Label(self.master,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X)
        # Se crea el menú de juego llamando cada uno al método correspondiente #
        self.barMenu = tk.Menu(self.master)
        self.barMenu.add_command(label='Jugar',command=self.juego)
        self.barMenu.add_command(label='Configuracion',command=self.configurar)
        self.barMenu.add_command(label='Ayuda',command=self.ayuda)
        self.barMenu.add_command(label='Acerca De',command=self.acercaDe)
        self.barMenu.add_command(label='Salir',command=self.salir)
        self.master.configure(menu=self.barMenu)
###################################################################################################################################################
    def configurar(self):
        configurar = Configuracion(self.master)                 #en configuración se llama a la clase hija "Configuracion" enviando la ventana principal como parámetro
        self.configuraciones = configurar.configuraciones()     #en esta variable se guarda lo que se retorna de la clase 
###################################################################################################################################################  
    def juego(self):
        # CONFIGURACION DEL NIVEL DE JUEGO #
        self.lblNivelJuego = tk.Label(self.master,text='NIVEL FÁCIL', font=('System',16),width=50)
        self.lblNivelJuego.place(x=100,y=40)

        self.lblNombre = tk.Label(self.master,text='Nombre del jugador',font=('System',12))
        self.lblNombre.place(x=10,y=60)
        self.txtNombre = tk.Entry(self.master,width=50,font=('System',12))
        self.txtNombre.place(x=150,y=60)
        # BOTONES DE LA INTERACCIÓN CON EL JUEGO #
        self.btnIniciarJuego = tk.Button(self.master,text='INICIAR JUEGO',bg='red',font=('System',10),command=self.inicioJuego)
        self.btnIniciarJuego.place(x=5,y=450)

        # Estos botones se mantienen inhabilitados hasta que se inicie una partida
        self.btnBorrarJugada = tk.Button(self.master,text='BORRAR JUGADA',bg='blue',font=('System',10),state=tk.DISABLED,command=self.borrarJugada)
        self.btnBorrarJugada.place(x=125,y=450)
        self.btnTerminarJuego = tk.Button(self.master,text='TERMINAR JUEGO',bg='green',font=('System',10),state=tk.DISABLED,command=self.terminarJuego)
        self.btnTerminarJuego.place(x=265,y=450)
        self.btnBorraJuego = tk.Button(self.master,text='BORRAR JUEGO',bg='white',font=('System',10),state=tk.DISABLED,command=self.borrarJuego)
        self.btnBorraJuego.place(x=405,y=450)
        self.btnTopLevel = tk.Button(self.master,text='TOP 10',bg='yellow',font=('System',10),command=self.Top)
        self.btnTopLevel.place(x=535,y=450)

################################################ CUADRICULA ######################################################################################
        self.btnPos00 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_0x0)
        self.btnPos00.place(x=130,y=100)
        self.btnPos01 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_0x1)
        self.btnPos01.place(x=200,y=100)
        self.btnPos02 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_0x2)
        self.btnPos02.place(x=270,y=100)
        self.btnPos03 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_0x3)
        self.btnPos03.place(x=340,y=100)
        self.btnPos04 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_0x4)
        self.btnPos04.place(x=410,y=100)

        self.btnPos10 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_1x0)
        self.btnPos10.place(x=130,y=170)
        self.btnPos11 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_1x1)
        self.btnPos11.place(x=200,y=170)
        self.btnPos12 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_1x2)
        self.btnPos12.place(x=270,y=170)
        self.btnPos13 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_1x3)
        self.btnPos13.place(x=340,y=170)
        self.btnPos14 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_1x4)
        self.btnPos14.place(x=410,y=170)

        self.btnPos20 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_2x0)
        self.btnPos20.place(x=130,y=240)
        self.btnPos21 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_2x1)
        self.btnPos21.place(x=200,y=240)
        self.btnPos22 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_2x2)
        self.btnPos22.place(x=270,y=240)
        self.btnPos23 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_2x3)
        self.btnPos23.place(x=340,y=240)
        self.btnPos24 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_2x4)
        self.btnPos24.place(x=410,y=240)

        self.btnPos30 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_3x0)
        self.btnPos30.place(x=130,y=310)
        self.btnPos31 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_3x1)
        self.btnPos31.place(x=200,y=310)
        self.btnPos32 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_3x2)
        self.btnPos32.place(x=270,y=310)
        self.btnPos33 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_3x3)
        self.btnPos33.place(x=340,y=310)
        self.btnPos34 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_3x4)
        self.btnPos34.place(x=410,y=310)

        self.btnPos40 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_4x0)
        self.btnPos40.place(x=130,y=380)
        self.btnPos41 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_4x1)
        self.btnPos41.place(x=200,y=380)
        self.btnPos42 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_4x2)
        self.btnPos42.place(x=270,y=380)
        self.btnPos43 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_4x3)
        self.btnPos43.place(x=340,y=380)
        self.btnPos44 = tk.Button(self.master,bg='white',font=('System'),width=5,height=2,command=self.cambio_cuadricula_4x4)
        self.btnPos44.place(x=410,y=380)
###################################################################################################################################################

        # RESTRICCIONES HORIZONTALES #
        self.lblPos00 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos00.place(x=185,y=115)
        self.lblPos01 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos01.place(x=255,y=115)
        self.lblPos02 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos02.place(x=325,y=115)
        self.lblPos03 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos03.place(x=395,y=115)

        self.lblPos10 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos10.place(x=185,y=185)
        self.lblPos11 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos11.place(x=255,y=185)
        self.lblPos12 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos12.place(x=325,y=185)
        self.lblPos13 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos13.place(x=395,y=185)

        self.lblPos20 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos20.place(x=185,y=255)
        self.lblPos21 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos21.place(x=255,y=255)
        self.lblPos22 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos22.place(x=325,y=255)
        self.lblPos23 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos23.place(x=395,y=255)

        self.lblPos30 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos30.place(x=185,y=325)
        self.lblPos31 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos31.place(x=255,y=325)
        self.lblPos32 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos32.place(x=325,y=325)
        self.lblPos33 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos33.place(x=395,y=325)

        self.lblPos40 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos40.place(x=185,y=395)
        self.lblPos41 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos41.place(x=255,y=395)
        self.lblPos42 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos42.place(x=325,y=395)
        self.lblPos43 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPos43.place(x=395,y=395)

        # RESTRICCIONES VERTICALES #
        self.lblPosV00 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV00.place(x=145,y=144)
        self.lblPosV01 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV01.place(x=215,y=144)
        self.lblPosV02 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV02.place(x=285,y=144)
        self.lblPosV03 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV03.place(x=355,y=144)
        self.lblPosV04 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV04.place(x=425,y=144)

        self.lblPosV10 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV10.place(x=145,y=214)
        self.lblPosV11 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV11.place(x=215,y=214)
        self.lblPosV12 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV12.place(x=285,y=214)
        self.lblPosV13 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV13.place(x=355,y=214)
        self.lblPosV14 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV14.place(x=425,y=214)

        self.lblPosV20 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV20.place(x=145,y=284)
        self.lblPosV21 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV21.place(x=215,y=284)
        self.lblPosV22 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV22.place(x=285,y=284)
        self.lblPosV23 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV23.place(x=355,y=284)
        self.lblPosV24 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV24.place(x=425,y=284)

        self.lblPosV30 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV30.place(x=145,y=354)
        self.lblPosV31 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV31.place(x=215,y=354)
        self.lblPosV32 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV32.place(x=285,y=354)
        self.lblPosV33 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV33.place(x=355,y=354)
        self.lblPosV34 = tk.Label(self.master,text='',font=('System'),width=1,height=1)
        self.lblPosV34.place(x=425,y=354)

        # LISTA QUE CONTIENE LOS BOTONES DE LA CUADRICULA #
        self.casillas = [[self.btnPos00,self.btnPos01,self.btnPos02,self.btnPos03,self.btnPos04],[self.btnPos10,self.btnPos11,self.btnPos12,self.btnPos13,self.btnPos14]\
            ,[self.btnPos20,self.btnPos21,self.btnPos22,self.btnPos23,self.btnPos24],[self.btnPos30,self.btnPos31,self.btnPos32,self.btnPos33,self.btnPos34]\
            ,[self.btnPos40,self.btnPos41,self.btnPos42,self.btnPos43,self.btnPos44]]

        # LISTA QUE CONTIENE LAS RESTRICCIONES EN HORIZONTAL
        self.restriccionesH = [[self.lblPos00,self.lblPos01,self.lblPos02,self.lblPos03],[self.lblPos10,self.lblPos11,self.lblPos12,self.lblPos13]\
            ,[self.lblPos20,self.lblPos21,self.lblPos22,self.lblPos23],[self.lblPos30,self.lblPos31,self.lblPos32,self.lblPos33]\
            ,[self.lblPos40,self.lblPos41,self.lblPos42,self.lblPos43]]

        # LISTA QUE CONTIENE LAS RESTRICCIONES EN VERTICAL 
        self.restriccionesV = [[self.lblPosV00,self.lblPosV01,self.lblPosV02,self.lblPosV03,self.lblPosV04],[self.lblPosV10,self.lblPosV11\
            ,self.lblPosV12,self.lblPosV13,self.lblPosV14],[self.lblPosV20,self.lblPosV21,self.lblPos22,self.lblPosV23,self.lblPosV24]\
            ,[self.lblPosV30,self.lblPosV31,self.lblPosV32,self.lblPosV33,self.lblPosV34]]

        
        # EVALUA EL NIVEL DE JUEGO PARA CREAR LAS PARTIDAS DE JUEGO #
        # Partidas en nivel Fácil #
        if self.configuraciones[0] == 1:
            self.lblNivelJuego.configure(text="NIVEL FÁCIL")
            partidas = open('futoshiki2021partidas.dat','rb')
            x = pickle.load(partidas)
            # CARGA DE ARCHIVOS .DAT #
            self.azar = random.randint(0,2)     #se crean las partidas de forma aleatoria
            for i,filas in enumerate(self.casillas):
                    for op,botones in enumerate(filas):
                            for ind,numeros in enumerate(x[0][self.azar]):
                                if i == numeros[1]:
                                        if op == numeros[2]:
                                            # Si el dígito que se encuentra en ese momento se puede transforma en entero se almacena en la lista de botones de la cuadricula
                                            try:
                                                int(numeros[0])
                                                self.casillas[i][op].configure(text=numeros[0])
                                                self.casillas[i][op].configure(state=tk.DISABLED)
                                                self.valoresH[i][op] = int(numeros[0])
                                                self.valoresV[op][i] = int(numeros[0])
                                            except:
                                                # Si no se puede pues se evalua si es horizontal o vertical la restricción
                                                if numeros[0] == 'v' or numeros[0] == 'ʌ':
                                                    self.restriccionesV[i][op].configure(text=numeros[0])
                                                    self.signoRestriccionesV[i][op] = numeros[0]
                                                else:
                                                    self.restriccionesH[i][op].configure(text=numeros[0])
                                                    self.signoRestriccionesH[i][op] = numeros[0]
            partidas.close()
        # Partidas en nivel Intermedio #
        elif self.configuraciones[0] == 2:
            self.lblNivelJuego.configure(text="NIVEL INTERMEDIO")
            partidas = open('futoshiki2021partidas.dat','rb')
            x = pickle.load(partidas)
            # CARGA DE ARCHIVOS .DAT #
            self.azar = random.randint(0,2)     #se crean las partidas de forma aleatoria
            for i,filas in enumerate(self.casillas):
                    for op,botones in enumerate(filas):
                            for ind,numeros in enumerate(x[1][self.azar]):
                                if i == numeros[1]:
                                        if op == numeros[2]:
                                            try:
                                            # Si el dígito que se encuentra en ese momento se puede transforma en entero se almacena en la lista de botones de la cuadricula                                               
                                                int(numeros[0])
                                                self.casillas[i][op].configure(text=numeros[0])
                                                self.casillas[i][op].configure(state=tk.DISABLED)
                                                self.valoresH[i][op] = int(numeros[0])
                                                self.valoresV[op][i] = int(numeros[0])
                                            except:
                                                # Si no se puede pues se evalua si es horizontal o vertical la restricción
                                                if numeros[0] == 'v' or numeros[0] == 'ʌ':
                                                    self.restriccionesV[i][op].configure(text=numeros[0])
                                                    self.signoRestriccionesV[i][op] = numeros[0]
                                                else:
                                                    self.restriccionesH[i][op].configure(text=numeros[0])
                                                    self.signoRestriccionesH[i][op] = numeros[0]
            partidas.close()
        # Partidas en nivel Díficil #
        elif self.configuraciones[0] == 3:
            self.lblNivelJuego.configure(text="NIVEL DÍFICIL")
            partidas = open('futoshiki2021partidas.dat','rb')
            x = pickle.load(partidas)
            # CARGA DE ARCHIVOS .DAT #
            self.azar = random.randint(0,2)     #se crean las partidas de forma aleatoria
            for i,filas in enumerate(self.casillas):
                    for op,botones in enumerate(filas):
                            for ind,numeros in enumerate(x[2][self.azar]):
                                if i == numeros[1]:
                                        if op == numeros[2]:
                                            # Si el dígito que se encuentra en ese momento se puede transforma en entero se almacena en la lista de botones de la cuadricula
                                            try:
                                                int(numeros[0])
                                                self.casillas[i][op].configure(text=numeros[0])
                                                self.casillas[i][op].configure(state=tk.DISABLED)
                                                self.valoresH[i][op] = int(numeros[0])
                                                self.valoresV[op][i] = int(numeros[0])
                                            except:
                                                # Si no se puede pues se evalua si es horizontal o vertical la restricción
                                                if numeros[0] == 'v' or numeros[0] == 'ʌ':
                                                    self.restriccionesV[i][op].configure(text=numeros[0])
                                                    self.signoRestriccionesV[i][op] = numeros[0]
                                                else:
                                                    self.restriccionesH[i][op].configure(text=numeros[0])
                                                    self.signoRestriccionesH[i][op] = numeros[0]
            partidas.close()

        # CONFIGURACION DEL RELOJ #
        # EVALUA LA CONFIGURACIÓN DEL RELOJ PARA AJUSTAR EN VENTANA PRINCIPAL EL RELOJ (TIMER, CRONÓMETRO O SIN RELOJ) #
        if self.configuraciones[1] == 1:
            # CRONÓMETRO #
            self.time = tk.Label(self.master, text= 'Reloj',font=('System',20))
            self.time.place(x=107,y=485)
            self.hourLabel = tk.Label(self.master,text='00',font=('System',20))
            self.hourLabel.place(x=60,y=525)
            self.minuteLabel = tk.Label(self.master,text='00',font=('System',20))
            self.minuteLabel.place(x=117,y=525)
            self.secondLabel = tk.Label(self.master,text='00',font=('System',20))
            self.secondLabel.place(x=185,y=525)
        
        elif self.configuraciones[1] == 2:
            # SIN RELOJ #
            self.lblOcultar = tk.Label(self.master,text='',width=40,height=10)
            self.lblOcultar.place(x=60,y=500)
        else:
            # TEMPORIZADOR # 
            self.time = tk.Label(self.master, text= 'Timer', font=('System',20))
            self.time.place(x=107,y=485)
            self.hourLabel = tk.Label(self.master,text=self.configuraciones[3],font=('System',20))
            self.hourLabel.place(x=60,y=525)
            self.minuteLabel = tk.Label(self.master,text=self.configuraciones[4],font=('System',20))
            self.minuteLabel.place(x=117,y=525)
            self.secondLabel = tk.Label(self.master,text=self.configuraciones[5],font=('System',20))
            self.secondLabel.place(x=185,y=525)
    
        # CONFIGURACION DE LA POSICION DE LOS BOTONES #
####################################################### BOTONES DE JUEGO ###########################################################################################
        self.btn1 = tk.Button(self.master,text='1',font=('System',12),activebackground='green',height=2,width=4,command=lambda:self.botones(1),state=tk.DISABLED)
        self.btn1.place(x=530,y=120)
        self.btn2= tk.Button(self.master,text='2',font=('System',12),activebackground='green',height=2,width=4,command=lambda:self.botones(2),state=tk.DISABLED)
        self.btn2.place(x=530,y=170)
        self.btn3 = tk.Button(self.master,text='3',font=('System',12),activebackground='green',height=2,width=4,command=lambda:self.botones(3),state=tk.DISABLED)
        self.btn3.place(x=530,y=220)
        self.btn4 = tk.Button(self.master,text='4',font=('System',12),activebackground='green',height=2,width=4,command=lambda:self.botones(4),state=tk.DISABLED)
        self.btn4.place(x=530,y=270)
        self.btn5 = tk.Button(self.master,text='5',font=('System',12),activebackground='green',height=2,width=4,command=lambda:self.botones(5),state=tk.DISABLED)
        self.btn5.place(x=530,y=320)

        # LISTA CON LOS BOTONES DEL JUEGO #
        self.botonesJuego = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5]

        self.lblOcultar1 = tk.Label(self.master,text='',width=6,height=20)
        self.lblOcultar1.place(x=50,y=120)
        
        # Si el usuario configuro que con reloj pasa
        if self.configuraciones[2] == 1:
            pass
        else:
            # sino pues se cambia de lugar los botones
            self.btn1.place_configure(x=50,y=120)
            self.btn2.place_configure(x=50,y=170)
            self.btn3.place_configure(x=50,y=220)
            self.btn4.place_configure(x=50,y=270)
            self.btn5.place_configure(x=50,y=320)
            self.lblOcultar1.place_forget()
            self.lblOcultar = tk.Label(self.master,text='',width=6,height=20)
            self.lblOcultar.place(x=530,y=120)
        
        # INTERACCIÓN CON LAS PARTIDAS DE JUEGO #
        # Estos botones se mantienen inhabilitados hasta que se inicie una partida
        self.btnGuardarJuego = tk.Button(self.master,text='GUARDAR JUEGO',font=('System',10),state=tk.DISABLED)
        self.btnGuardarJuego.place(x=305,y=525)
        self.btnCargarJuego = tk.Button(self.master,text='CARGAR JUEGO',font=('System',10),state=tk.DISABLED)
        self.btnCargarJuego.place(x=445,y=525)

###################################################################################################################################################
    def botones(self,num):          #Método que almacena el botón de juego que se presiona
        self.numero = str(num)      #y guarda el parámetro recibido en la variable "self.numero"

###################################################################################################################################################

    def temporizador(self):
        
        hora = int(self.configuraciones[3])
        minuto = int(self.configuraciones[4])
        segundo = int(self.configuraciones[5])

        segundo -= 1

        if segundo <= 0:
            if minuto !=0:
                segundo = 59
                minuto -= 1
            else:
                minuto = 0
                segundo = 0
                if minuto <= 0:
                    if hora !=0:
                        minuto = 59
                        hora -= 1
                    else:
                        minuto = 0
                        hora = 0
                        if segundo <= 0 and minuto <= 0 and hora <= 0:
                            respuesta = messagebox.askyesno("TIEMPO EXPIRADO", "¿DESEA CONTINUAR EL MISMO JUEGO")

                            if respuesta == True:

                                segundo = -1
                                hora = -1
                                minuto = -1

                                self.segundoReloj = self.configuraciones[8]
                                self.minutoReloj = self.configuraciones[7]
                                self.horaReloj = self.configuraciones[6]

                                self.flag = True
                                self.relojCronometro()
                            else:

                                segundo = self.configuraciones[8]
                                hora = self.configuraciones[7]
                                minuto = self.configuraciones[6]
                                
                                self.juego()
    
        if self.flag == False:
            if segundo >= 0:
                self.secondLabel.configure(text=str(segundo))
            if hora >= 0:
                self.hourLabel.configure(text=str(hora))
            if minuto >= 0:
                self.minuteLabel.configure(text=str(minuto))
        self.time.after(1000,self.temporizador)

    def relojCronometro(self):
        global h,m,s

        s += 1
        if s >= 60:
            s = 0
            m = m + 1
            if m >= 60:
                m = 0
                h = h + 1
                if h >= 24:
                    h = 0
        
        #etiqueta que muestra el cronometro en pantalla
        self.hourLabel.configure(text=str(h))
        self.minuteLabel.configure(text=str(m))
        self.secondLabel.configure(text=str(s))
        
        # iniciamos la cuenta progresiva de los segundos
        self.time.after(1000, self.relojCronometro)


    # MÉTODO DE INICIO DEL JUEGO #
    def inicioJuego(self):

        # VALIDACIONES DE BOTONES HABILITADOS y DESABILITADOS #
        self.btnIniciarJuego.configure(state=tk.DISABLED)
        self.btnGuardarJuego.configure(state=tk.NORMAL)
        self.btnCargarJuego.configure(state=tk.NORMAL)
        self.btnBorraJuego.configure(state=tk.NORMAL)
        self.btnTerminarJuego.configure(state=tk.NORMAL)
        self.btnBorrarJugada.configure(state=tk.NORMAL)

        # SE HABILITAN LOS BOTONES DE JUEGO 
        for i in self.botonesJuego:
            i.configure(state=tk.NORMAL)

        # Se evalua si el usuario escribio su nombre, de lo contrario el juego no puede iniciar 
        nombreJugador = str(self.txtNombre.get())
        if not(nombreJugador != "" and len(nombreJugador)<20):
            messagebox.showerror('Nombre del Jugador','Debe de ingresar el nombre del jugador')
        else:
            # Evalua la configuración del reloj
            if self.configuraciones[1] == 1:
                self.time.after(1000,self.relojCronometro)

            elif self.configuraciones[1] == 3:
                # TEMPORIZADOR
                self.inicio = time.time()
                self.time.after(1000,self.temporizador)

            elif self.configuraciones[1] == 2:
                pass

###################################################################################################################################################
    def borrarJugada(self):
#       Elimina la última jugada dejando la casilla vacía. Puede borrar todas las jugadas que ha hecho.  
#       Use un TDA pila para registrar la información de las jugadas que van sucediento de tal manera que pueda implementar esta funcionalidad. 
#       Cada vez que se hace una jugada se agrega a la pila (fila y columna de  la  jugada), y si seleccionan este botón, se toma la última jugada agregada en la pila 
#       (el manejo de la pila es tipo LIFO: Last In First Out, último en entrar primero en salir) y se borra la casilla respectiva de la cuadrícula. 
#       La jugada se quita de la  pila. En el diseño de la solución describa la estructura del TDA usado y el algoritmo de manipulación.
        pass
###################################################################################################################################################
    def terminarJuego(self):
#       Si responde SI termina de inmediato el juego y se vuelve a mostrar otro juego como si estuviera entrando a la opción de Jugar.  
#       Si responde NO sigue jugando con el mismo juego.
        respuesta = messagebox.askyesno('TERMINAR JUEGO','¿ESTÁ SEGURO DE TERMINAR EL JUEGO?')
        if respuesta == True:
            return
        else:
            pass
###################################################################################################################################################
    def borrarJuego(self):
#       Si responde SI vuelve a la opción de Jugar usando la misma partida, pero eliminando todas las jugadas que hizo. 
#       Si responde NO sigue jugando con el mismo juego. 
        respuesta = messagebox.askyesno('BORRAR JUEGO','¿ESTÁ SEGURO DE BORRAR EL JUEGO?')
        if respuesta == True:
            return
        else:
            pass

    def cambio_cuadricula_0x0(self):
        print('signoRh',self.signoRestriccionesH)
        print('signoRv',self.signoRestriccionesV)
        print('valoresH',self.valoresH)
        print('valoresV',self.valoresV)
        try:
            if int(self.numero) in self.valoresV[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[0] and int(self.numero) not in self.valoresV[0]:
                self.valoresH[0][0] = int(self.numero)
                self.valoresV[0][0] = int(self.numero)
                self.btnPos00.configure(text=int(self.numero))
                self.matrizResultados.append((0,0,int(self.numero)))

            if self.valoresH[1][0] != 0 and int(self.numero) > self.valoresH[1][0] and self.signoRestriccionesV[0][0] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos00.configure(text="")
                if self.matrizResultados[-1] == (0,0,int(self.numero)):
                    self.valoresH[0][0] = 0
                    self.valoresV[0][0] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][0] != 0 and int(self.numero) < self.valoresH[1][0] and self.signoRestriccionesV[0][0] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos00.configure(text="")
                if self.matrizResultados[-1] == (0,0,int(self.numero)):
                    self.valoresH[0][0] = 0
                    self.valoresV[0][0] = 0
                    self.matrizResultados.pop()

        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_0x1(self):
        try:
            if int(self.numero) in self.valoresV[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[0] and int(self.numero) not in self.valoresV[1]:
                self.valoresH[0][1] = int(self.numero)
                self.valoresV[1][0] = int(self.numero)
                self.btnPos01.configure(text=int(self.numero))
                self.matrizResultados.append((0,1,int(self.numero)))

            if self.valoresH[0][2] != 0 and int(self.numero) < self.valoresH[0][2] and self.signoRestriccionesH[0][1] == ">": 
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos01.configure(text="")
                if self.matrizResultados[-1] == (0,1,int(self.numero)):
                    self.valoresH[0][1] = 0
                    self.valoresV[1][0] = 0
                    self.matrizResultados.pop()

            if self.valoresH[0][2] != 0 and int(self.numero) > self.valoresH[0][2] and self.signoRestriccionesH[0][1] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos01.configure(text="")
                if self.matrizResultados[-1] == (0,1,int(self.numero)):
                    self.valoresH[0][1] = 0
                    self.valoresV[1][0] = 0
                    self.matrizResultados.pop()   

        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")


    def cambio_cuadricula_0x2(self):
        try:
            
            if int(self.numero) in self.valoresV[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[0]and int(self.numero) not in self.valoresV[2]:
                self.valoresH[0][2] = int(self.numero)
                self.valoresV[2][0] = int(self.numero)
                self.btnPos02.configure(text=int(self.numero))
                self.matrizResultados.append((0,2,int(self.numero)))

            if self.valoresH[0][3] != 0 and int(self.numero) < self.valoresH[0][3] and self.signoRestriccionesH[0][2] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos02.configure(text="")
                if self.matrizResultados[-1] == (0,2,int(self.numero)):
                    self.valoresH[0][2] = 0
                    self.valoresV[2][0] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[0][1] != 0 and int(self.numero) > self.valoresH[0][1] and self.signoRestriccionesH[0][1] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos02.configure(text="")
                if self.matrizResultados[-1] == (0,2,int(self.numero)):
                    self.valoresH[0][2] = 0
                    self.valoresV[2][0] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[0][1] != 0 and int(self.numero) < self.valoresH[0][1] and self.signoRestriccionesH[0][1] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos02.configure(text="")
                if self.matrizResultados[-1] == (0,2,int(self.numero)):
                    self.valoresH[0][2] = 0
                    self.valoresV[2][0] = 0
                    self.matrizResultados.pop()      
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_0x3(self):
        try:
            if int(self.numero) in self.valoresV[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[0]and int(self.numero) not in self.valoresV[3]:
                self.valoresH[0][3] = int(self.numero)
                self.valoresV[3][0] = int(self.numero)
                self.btnPos03.configure(text=int(self.numero))
                self.matrizResultados.append((0,3,int(self.numero)))
            
            if self.valoresH[0][2] != 0 and int(self.numero) > self.valoresH[0][2] and self.signoRestriccionesH[0][2] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos03.configure(text="")
                if self.matrizResultados[-1] == (0,3,int(self.numero)):
                    self.valoresH[0][3] = 0
                    self.valoresV[3][0] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[0][4] != 0 and int(self.numero) > self.valoresH[0][4] and self.signoRestriccionesH[0][3] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos03.configure(text="")
                if self.matrizResultados[-1] == (0,3,int(self.numero)):
                    self.valoresH[0][3] = 0
                    self.valoresV[3][0] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][3] != 0 and int(self.numero) > self.valoresH[1][3] and self.signoRestriccionesV[0][3] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos03.configure(text="")
                if self.matrizResultados[-1] == (0,3,int(self.numero)):
                    self.valoresH[0][3] = 0
                    self.valoresV[3][0] = 0
                    self.matrizResultados.pop()
                
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_0x4(self):
        try:
            if int(self.numero) in self.valoresV[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[0]and int(self.numero) not in self.valoresV[4]:
                self.valoresH[0][4] = int(self.numero)
                self.valoresV[4][0] = int(self.numero)
                self.btnPos04.configure(text=int(self.numero))
                self.matrizResultados.append((0,4,int(self.numero)))
            
            if self.valoresH[0][3] != 0 and int(self.numero) < self.valoresH[0][3] and self.signoRestriccionesH[0][3] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos04.configure(text="")
                if self.matrizResultados[-1] == (0,4,int(self.numero)):
                    self.valoresH[0][4] = 0
                    self.valoresV[4][0] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][4] != 0 and int(self.numero) < self.valoresH[1][4] and self.signoRestriccionesV[0][4] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos04.configure(text="")
                if self.matrizResultados[-1] == (0,4,int(self.numero)):
                    self.valoresH[0][4] = 0
                    self.valoresV[4][0] = 0
                    self.matrizResultados.pop()    
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    #Fila 1

    def cambio_cuadricula_1x0(self):

        try:
            if int(self.numero) in self.valoresV[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[1]and int(self.numero) not in self.valoresV[0]:
                self.valoresH[1][0] = int(self.numero)
                self.valoresV[0][1] = int(self.numero)
                self.btnPos10.configure(text=int(self.numero))
                self.matrizResultados.append((1,0,int(self.numero)))
            
            if self.valoresH[1][1] != 0 and int(self.numero) < self.valoresH[1][1] and self.signoRestriccionesH[1][0] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos10.configure(text="")
                if self.matrizResultados[-1] == (1,0,int(self.numero)):
                    self.valoresH[1][0] = 0
                    self.valoresV[0][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[0][0] != 0 and int(self.numero) < self.valoresH[0][0] and self.signoRestriccionesV[0][0] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos10.configure(text="")
                if self.matrizResultados[-1] == (1,0,int(self.numero)):
                    self.valoresH[1][0] = 0
                    self.valoresV[0][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[2][0] != 0 and int(self.numero) > self.valoresH[2][0] and self.signoRestriccionesV[1][0] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos10.configure(text="")
                if self.matrizResultados[-1] == (1,0,int(self.numero)):
                    self.valoresH[1][0] = 0
                    self.valoresV[0][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[0][0] != 0 and int(self.numero) > self.valoresH[0][0] and self.signoRestriccionesV[0][0] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos10.configure(text="")
                if self.matrizResultados[-1] == (1,0,int(self.numero)):
                    self.valoresH[1][0] = 0
                    self.valoresV[0][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[2][0] != 0 and int(self.numero) < self.valoresH[2][0] and self.signoRestriccionesV[1][0] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos10.configure(text="")
                if self.matrizResultados[-1] == (1,0,int(self.numero)):
                    self.valoresH[1][0] = 0
                    self.valoresV[0][1] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_1x1(self):
        try:
            if int(self.numero) in self.valoresV[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[1]and int(self.numero) not in self.valoresV[1]:
                self.valoresH[1][1] = int(self.numero)
                self.valoresV[1][1] = int(self.numero)
                self.btnPos11.configure(text=int(self.numero))
                self.matrizResultados.append((1,1,int(self.numero)))
            
            if self.valoresH[1][0] != 0 and int(self.numero) > self.valoresH[1][0] and self.signoRestriccionesH[1][0] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos11.configure(text="")
                if self.matrizResultados[-1] == (1,1,int(self.numero)):
                    self.valoresH[1][1] = 0
                    self.valoresV[1][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][2] != 0 and int(self.numero) > self.valoresH[1][2] and self.signoRestriccionesH[1][1] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos11.configure(text="")
                if self.matrizResultados[-1] == (1,1,int(self.numero)):
                    self.valoresH[1][1] = 0
                    self.valoresV[1][1] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_1x2(self):
        try:
            if int(self.numero) in self.valoresV[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[1]and int(self.numero) not in self.valoresV[2]:
                self.valoresH[1][2] = int(self.numero)
                self.valoresV[2][1] = int(self.numero)
                self.btnPos12.configure(text=int(self.numero))
                self.matrizResultados.append((1,2,int(self.numero)))
            
            if self.valoresH[1][1] != 0 and int(self.numero) < self.valoresH[1][1] and self.signoRestriccionesH[1][1] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos12.configure(text="")
                if self.matrizResultados[-1] == (1,2,int(self.numero)):
                    self.valoresH[1][2] = 0
                    self.valoresV[2][1] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_1x3(self):
        try:
            if int(self.numero) in self.valoresV[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[1]and int(self.numero) not in self.valoresV[3]:
                self.valoresH[1][3] = int(self.numero)
                self.valoresV[3][1] = int(self.numero)
                self.btnPos13.configure(text=int(self.numero))
                self.matrizResultados.append((1,3,int(self.numero)))
            
            if self.valoresH[2][3] != 0 and int(self.numero) > self.valoresH[2][3] and self.signoRestriccionesV[1][3] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos13.configure(text="")
                if self.matrizResultados[-1] == (1,3,int(self.numero)):
                    self.valoresH[1][3] = 0
                    self.valoresV[3][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[0][3] != 0 and int(self.numero) < self.valoresH[0][3] and self.signoRestriccionesV[0][3] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos13.configure(text="")
                if self.matrizResultados[-1] == (1,3,int(self.numero)):
                    self.valoresH[1][3] = 0
                    self.valoresV[3][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[2][3] != 0 and int(self.numero) < self.valoresH[2][3] and self.signoRestriccionesV[1][3] == 'v':  
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos13.configure(text="")
                if self.matrizResultados[-1] == (1,3,int(self.numero)):
                    self.valoresH[1][3] = 0
                    self.valoresV[3][1] = 0
                    self.matrizResultados.pop()   
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_1x4(self):
        try:
            if int(self.numero) in self.valoresV[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[1]and int(self.numero) not in self.valoresV[4]:
                self.valoresH[1][4] = int(self.numero)
                self.valoresV[4][1] = int(self.numero)
                self.btnPos14.configure(text=int(self.numero))
                self.matrizResultados.append((1,4,int(self.numero)))
            
            if self.valoresH[2][4] != 0 and int(self.numero) > self.valoresH[2][4] and self.signoRestriccionesV[1][4] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos14.configure(text="")
                if self.matrizResultados[-1] == (1,4,int(self.numero)):
                    self.valoresH[1][4] = 0
                    self.valoresV[4][1] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[0][4] != 0 and int(self.numero) > self.valoresH[0][4] and self.signoRestriccionesV[0][4] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos14.configure(text="")
                if self.matrizResultados[-1] == (1,4,int(self.numero)):
                    self.valoresH[1][4] = 0
                    self.valoresV[4][1] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    # Fila 2

    def cambio_cuadricula_2x0(self):
        try:
            if int(self.numero) in self.valoresV[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[2]and int(self.numero) not in self.valoresV[0]:
                self.valoresH[2][0] = int(self.numero)
                self.valoresV[0][2] = int(self.numero)
                self.btnPos20.configure(text=int(self.numero))
                self.matrizResultados.append((2,0,int(self.numero)))
            
            if self.valoresH[2][1] != 0 and int(self.numero) > self.valoresH[2][1] and self.signoRestriccionesH[2][0] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos20.configure(text="")
                if self.matrizResultados[-1] == (2,0,int(self.numero)):
                    self.valoresH[2][0] = 0
                    self.valoresV[0][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][0] != 0 and int(self.numero) < self.valoresH[1][0] and self.signoRestriccionesV[1][0] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos20.configure(text="")
                if self.matrizResultados[-1] == (2,0,int(self.numero)):
                    self.valoresH[2][0] = 0
                    self.valoresV[0][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[3][0] != 0 and int(self.numero) > self.valoresH[3][0] and self.signoRestriccionesV[2][0] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos20.configure(text="")
                if self.matrizResultados[-1] == (2,0,int(self.numero)):
                    self.valoresH[2][0] = 0
                    self.valoresV[0][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[3][0] != 0 and int(self.numero) < self.valoresH[3][0] and self.signoRestriccionesV[2][0] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos20.configure(text="")
                if self.matrizResultados[-1] == (2,0,int(self.numero)):
                    self.valoresH[2][0] = 0
                    self.valoresV[0][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][0] != 0 and int(self.numero) > self.valoresH[1][0] and self.signoRestriccionesV[1][0] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos20.configure(text="")
                if self.matrizResultados[-1] == (2,0,int(self.numero)):
                    self.valoresH[2][0] = 0
                    self.valoresV[0][2] = 0
                    self.matrizResultados.pop()
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_2x1(self):
        try:
            if int(self.numero) in self.valoresV[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[2]and int(self.numero) not in self.valoresV[1]:
                self.valoresH[2][1] = int(self.numero)
                self.valoresV[1][2] = int(self.numero)
                self.btnPos21.configure(text=int(self.numero))
                self.matrizResultados.append((2,1,int(self.numero)))
            
            if self.valoresH[2][0] != 0 and int(self.numero) < self.valoresH[2][0] and self.signoRestriccionesH[2][0] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos21.configure(text="")
                if self.matrizResultados[-1] == (2,1,int(self.numero)):
                    self.valoresH[2][1] = 0
                    self.valoresV[1][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[3][1] != 0 and int(self.numero) > self.valoresH[3][1] and self.signoRestriccionesV[2][1] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos21.configure(text="")
                if self.matrizResultados[-1] == (2,1,int(self.numero)):
                    self.valoresH[2][1] = 0
                    self.valoresV[1][2] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_2x2(self):
        try:
            if int(self.numero) in self.valoresV[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[2]and int(self.numero) not in self.valoresV[2]:
                self.valoresH[2][2] = int(self.numero)
                self.valoresV[2][2] = int(self.numero)
                self.btnPos22.configure(text=int(self.numero))
                self.matrizResultados.append((2,2,int(self.numero)))

        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_2x3(self):
        try:
            if int(self.numero) in self.valoresV[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[2]and int(self.numero) not in self.valoresV[3]:
                self.valoresH[2][3] = int(self.numero)
                self.valoresV[3][2] = int(self.numero)
                self.btnPos23.configure(text=int(self.numero))
                self.matrizResultados.append((2,3,int(self.numero)))
            
            if self.valoresH[2][4] != 0 and int(self.numero) < self.valoresH[2][4] and self.signoRestriccionesH[2][3] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos23.configure(text="")
                if self.matrizResultados[-1] == (2,3,int(self.numero)):
                    self.valoresH[2][3] = 0
                    self.valoresV[3][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[2][4] != 0 and int(self.numero) > self.valoresH[2][4] and self.signoRestriccionesH[2][3] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos23.configure(text="")
                if self.matrizResultados[-1] == (2,3,int(self.numero)):
                    self.valoresH[2][3] = 0
                    self.valoresV[3][2] = 0
                    self.matrizResultados.pop()

            if self.valoresH[1][3] != 0 and int(self.numero) < self.valoresH[1][3] and self.signoRestriccionesV[1][3] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos23.configure(text="")
                if self.matrizResultados[-1] == (2,3,int(self.numero)):
                    self.valoresH[2][3] = 0
                    self.valoresV[3][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][3] != 0 and int(self.numero) > self.valoresH[1][3] and self.signoRestriccionesV[1][3] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos23.configure(text="")
                if self.matrizResultados[-1] == (2,3,int(self.numero)):
                    self.valoresH[2][3] = 0
                    self.valoresV[3][2] = 0
                    self.matrizResultados.pop()  
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_2x4(self):
        try:
            if int(self.numero) in self.valoresV[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[2]and int(self.numero) not in self.valoresV[4]:
                self.valoresH[2][4] = int(self.numero)
                self.valoresV[4][2] = int(self.numero)
                self.btnPos24.configure(text=int(self.numero))
                self.matrizResultados.append((2,4,int(self.numero)))
            
            if self.valoresH[2][3] != 0 and int(self.numero) > self.valoresH[2][3] and self.signoRestriccionesH[2][3] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos24.configure(text="")
                if self.matrizResultados[-1] == (2,4,int(self.numero)):
                    self.valoresH[2][4] = 0
                    self.valoresV[4][2] = 0
                    self.matrizResultados.pop()

            if self.valoresH[2][3] != 0 and int(self.numero) < self.valoresH[2][3] and self.signoRestriccionesH[2][3] == "<":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos24.configure(text="")
                if self.matrizResultados[-1] == (2,4,int(self.numero)):
                    self.valoresH[2][4] = 0
                    self.valoresV[4][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[1][4] != 0 and int(self.numero) < self.valoresH[1][4] and self.signoRestriccionesV[1][4] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos24.configure(text="")
                if self.matrizResultados[-1] == (2,4,int(self.numero)):
                    self.valoresH[2][4] = 0
                    self.valoresV[4][2] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[3][4] != 0 and int(self.numero) < self.valoresH[3][4] and self.signoRestriccionesV[2][4] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos24.configure(text="")
                if self.matrizResultados[-1] == (2,4,int(self.numero)):
                    self.valoresH[2][4] = 0
                    self.valoresV[4][2] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    #Fila 3

    def cambio_cuadricula_3x0(self):
        try:
            if int(self.numero) in self.valoresV[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[3]and int(self.numero) not in self.valoresV[0]:
                self.valoresH[3][0] = int(self.numero)
                self.valoresV[0][3] = int(self.numero)
                self.btnPos30.configure(text=int(self.numero))
                self.matrizResultados.append((3,0,int(self.numero)))
            
            if self.valoresH[3][1] != 0 and int(self.numero) < self.valoresH[3][1] and self.signoRestriccionesH[3][0] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos30.configure(text="")
                if self.matrizResultados[-1] == (3,0,int(self.numero)):
                    self.valoresH[3][0] = 0
                    self.valoresV[0][3] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[4][0] != 0 and int(self.numero) > self.valoresH[4][0] and self.signoRestriccionesV[3][0] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos30.configure(text="")
                if self.matrizResultados[-1] == (3,0,int(self.numero)):
                    self.valoresH[3][0] = 0
                    self.valoresV[0][3] = 0
                    self.matrizResultados.pop()

            if self.valoresH[2][0] != 0 and int(self.numero) < self.valoresH[2][0] and self.signoRestriccionesV[2][0] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos30.configure(text="")
                if self.matrizResultados[-1] == (3,0,int(self.numero)):
                    self.valoresH[3][0] = 0
                    self.valoresV[0][3] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[2][0] != 0 and int(self.numero) > self.valoresH[2][0] and self.signoRestriccionesV[2][0] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos30.configure(text="")
                if self.matrizResultados[-1] == (3,0,int(self.numero)):
                    self.valoresH[3][0] = 0
                    self.valoresV[0][3] = 0
                    self.matrizResultados.pop()
                
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_3x1(self):
        try:
            if int(self.numero) in self.valoresV[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[3] and int(self.numero) not in self.valoresV[1]:
                self.valoresH[3][1] = int(self.numero)
                self.valoresV[1][3] = int(self.numero)
                self.btnPos31.configure(text=int(self.numero))
                self.matrizResultados.append((3,1,int(self.numero)))
            
            if self.valoresH[3][0] != 0 and int(self.numero) > self.valoresH[3][0] and self.signoRestriccionesH[3][0] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos31.configure(text="")
                if self.matrizResultados[-1] == (3,1,int(self.numero)):
                    self.valoresH[3][1] = 0
                    self.valoresV[1][3] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[2][1] != 0 and int(self.numero) < self.valoresH[2][1] and self.signoRestriccionesV[2][1] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos31.configure(text="")
                if self.matrizResultados[-1] == (3,1,int(self.numero)):
                    self.valoresH[3][1] = 0
                    self.valoresV[1][3] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[4][1] != 0 and int(self.numero) > self.valoresH[4][1] and self.signoRestriccionesV[3][1] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos31.configure(text="")
                if self.matrizResultados[-1] == (3,1,int(self.numero)):
                    self.valoresH[3][1] = 0
                    self.valoresV[1][3] = 0
                    self.matrizResultados.pop()
                
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_3x2(self):
        try:
            if int(self.numero) in self.valoresV[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[3]and int(self.numero) not in self.valoresV[2]:
                self.valoresH[3][2] = int(self.numero)
                self.valoresV[2][3] = int(self.numero)
                self.btnPos32.configure(text=int(self.numero))
                self.matrizResultados.append((3,2,int(self.numero)))
            
            if self.valoresH[4][2] != 0 and int(self.numero) > self.valoresH[4][2] and self.signoRestriccionesV[3][2] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos32.configure(text="")
                if self.matrizResultados[-1] == (3,2,int(self.numero)):
                    self.valoresH[3][2] = 0
                    self.valoresV[2][3] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_3x3(self):
        try:
            if int(self.numero) in self.valoresV[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[3]and int(self.numero) not in self.valoresV[3]:
                self.valoresH[3][3] = int(self.numero)
                self.valoresV[3][3] = int(self.numero)
                self.btnPos33.configure(text=int(self.numero))
                self.matrizResultados.append((3,3,int(self.numero)))
            
            if self.valoresH[4][3] != 0 and int(self.numero) > self.valoresH[4][3] and self.signoRestriccionesV[3][3] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos33.configure(text="")
                if self.matrizResultados[-1] == (3,3,int(self.numero)):
                    self.valoresH[3][3] = 0
                    self.valoresV[3][3] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[4][3] != 0 and int(self.numero) < self.valoresH[4][3] and self.signoRestriccionesV[3][3] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos33.configure(text="")
                if self.matrizResultados[-1] == (3,3,int(self.numero)):
                    self.valoresH[3][3] = 0
                    self.valoresV[3][3] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_3x4(self):
        try:
            if int(self.numero) in self.valoresV[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[3]and int(self.numero) not in self.valoresV[4]:
                self.valoresH[3][4] = int(self.numero)
                self.valoresV[4][3] = int(self.numero)
                self.btnPos34.configure(text=int(self.numero))
                self.matrizResultados.append((3,4,int(self.numero)))
            
            if self.valoresH[2][4] != 0 and int(self.numero) > self.valoresH[2][4] and self.signoRestriccionesV[2][4] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos34.configure(text="")
                if self.matrizResultados[-1] == (3,4,int(self.numero)):
                    self.valoresH[3][4] = 0
                    self.valoresV[4][3] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    #Fila 4

    def cambio_cuadricula_4x0(self):
        try:
            if int(self.numero) in self.valoresV[0]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[4]and int(self.numero) not in self.valoresV[0]:
                self.valoresH[4][0] = int(self.numero)
                self.valoresV[0][4] = int(self.numero)
                self.btnPos40.configure(text=int(self.numero))
                self.matrizResultados.append((4,0,int(self.numero)))
            
            if self.valoresH[3][0] != 0 and int(self.numero) < self.valoresH[3][0] and self.signoRestriccionesV[3][0] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos40.configure(text="")
                if self.matrizResultados[-1] == (4,0,int(self.numero)):
                    self.valoresH[4][0] = 0
                    self.valoresV[0][4] = 0
                    self.matrizResultados.pop()
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_4x1(self):
        try:
            if int(self.numero) in self.valoresV[1]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[4]and int(self.numero) not in self.valoresV[1]:
                self.valoresH[4][1] = int(self.numero)
                self.valoresV[1][4] = int(self.numero)
                self.btnPos41.configure(text=int(self.numero))
                self.matrizResultados.append((4,1,int(self.numero)))

            if self.valoresH[4][2] != 0 and int(self.numero) < self.valoresH[4][2] and self.signoRestriccionesH[4][1] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos41.configure(text="")
                if self.matrizResultados[-1] == (4,1,int(self.numero)):
                    self.valoresH[4][1] = 0
                    self.valoresV[1][4] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[3][1] != 0 and int(self.numero) < self.valoresH[3][1] and self.signoRestriccionesV[3][1] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos41.configure(text="")
                if self.matrizResultados[-1] == (4,1,int(self.numero)):
                    self.valoresH[4][1] = 0
                    self.valoresV[1][4] = 0
                    self.matrizResultados.pop()       
            
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_4x2(self):
        try:
            if int(self.numero) in self.valoresV[2]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[4]and int(self.numero) not in self.valoresV[2]:
                self.valoresH[4][2] = int(self.numero)
                self.valoresV[2][4] = int(self.numero)
                self.btnPos42.configure(text=int(self.numero))
                self.matrizResultados.append((4,2,int(self.numero)))

            if self.valoresH[4][1] != 0 and int(self.numero) > self.valoresH[4][1] and self.signoRestriccionesH[4][1] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos42.configure(text="")
                if self.matrizResultados[-1] == (4,2,int(self.numero)):
                    self.valoresH[4][2] = 0
                    self.valoresV[2][4] = 0
                    self.matrizResultados.pop()

            if self.valoresH[4][3] != 0 and int(self.numero) < self.valoresH[4][3] and self.signoRestriccionesH[4][2] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos42.configure(text="")
                if self.matrizResultados[-1] == (4,2,int(self.numero)):
                    self.valoresH[4][2] = 0
                    self.valoresV[2][4] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[3][2] != 0 and int(self.numero) < self.valoresH[3][2] and self.signoRestriccionesV[3][2] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR!")
                self.btnPos42.configure(text="")
                if self.matrizResultados[-1] == (4,2,int(self.numero)):
                    self.valoresH[4][2] = 0
                    self.valoresV[2][4] = 0
                    self.matrizResultados.pop()
                
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_4x3(self):
        try:
            if int(self.numero) in self.valoresV[3]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[4]and int(self.numero) not in self.valoresV[3]:
                self.valoresH[4][3] = int(self.numero)
                self.valoresV[3][4] = int(self.numero)
                self.btnPos43.configure(text=int(self.numero))
                self.matrizResultados.append((4,3,int(self.numero)))
            
            if self.valoresH[4][4] != 0 and int(self.numero) < self.valoresH[4][4] and self.signoRestriccionesH[4][3] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos43.configure(text="")
                if self.matrizResultados[-1] == (4,3,int(self.numero)):
                    self.valoresH[4][3] = 0
                    self.valoresV[3][4] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[4][2] != 0 and int(self.numero) > self.valoresH[4][2] and self.signoRestriccionesH[4][2] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos43.configure(text="")
                if self.matrizResultados[-1] == (4,3,int(self.numero)):
                    self.valoresH[4][3] = 0
                    self.valoresV[3][4] = 0
                    self.matrizResultados.pop()
            
            if self.valoresH[3][3] != 0 and int(self.numero) < self.valoresH[3][3] and self.signoRestriccionesV[3][3] == 'ʌ':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                self.btnPos43.configure(text="")
                if self.matrizResultados[-1] == (4,3,int(self.numero)):
                    self.valoresH[4][3] = 0
                    self.valoresV[3][4] = 0
                    self.matrizResultados.pop()
            

            if self.valoresH[3][3] != 0 and int(self.numero) > self.valoresH[3][3] and self.signoRestriccionesV[3][3] == 'v':
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos43.configure(text="")
                if self.matrizResultados[-1] == (4,3,int(self.numero)):
                    self.valoresH[4][3] = 0
                    self.valoresV[3][4] = 0
                    self.matrizResultados.pop()  
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

    def cambio_cuadricula_4x4(self):
        try:
            if int(self.numero) in self.valoresV[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

            if int(self.numero) in self.valoresH[4]:
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

            if int(self.numero) not in self.valoresH[4]and int(self.numero) not in self.valoresV[4]:
                self.valoresH[4][4] = int(self.numero)
                self.valoresV[4][4] = int(self.numero)
                self.btnPos44.configure(text=int(self.numero))
                self.matrizResultados.append((4,4,int(self.numero)))
            
            if self.valoresH[4][3] != 0 and int(self.numero) > self.valoresH[4][3] and self.signoRestriccionesH[4][3] == ">":
                messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                self.btnPos44.configure(text="")
                if self.matrizResultados[-1] == (4,4,int(self.numero)):
                    self.valoresH[4][4] = 0
                    self.valoresV[4][4] = 0
                    self.matrizResultados.pop()
        except:
            messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

###################################################################################################################################################
    def Top(self):
        # Detiene el reloj si lo está usando. 
        # Despliega una sola pantalla con los registros de los mejores 10 primeros jugadores por cada nivel: aquellos que hicieron menos tiempo para completar el juego.  
        # En caso de no tener los 10 jugadores en algún nivel se despliegan los que se tengan.  
        # El Top 10 se guarda en el archivo “futoshiki2021top10.dat”.
        global proceso
        global running
        # verifica si el tiempo ha iniciado
        if running:
            self.time.after_cancel(proceso)     #el tiempo se detiene
            running = False                     #la indicadora pasa a False
        # Ventana que se desplega para ver el TOP 10
        self.top = tk.Toplevel()
        self.top.geometry('500x800')
        self.top.title('TOP 10')
        self.lblTitulo = tk.Label(self.top,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X)

        top10= open('futoshiki2021top10.dat','rb')
        tops = pickle.load(top10)
        jugadores = str(self.txtNombre.get())
        if self.configuraciones[0] == 1:
            tops[0].append(jugadores)
        elif self.configuraciones[0] == 2:
            tops[1].append(jugadores)
        elif self.configuraciones[0] == 3:
            tops[2].append(jugadores)
        top10.close()

        self.lblDificil = tk.Label(self.top,text='NIVEL DÍFICIL:',font=('System'))
        self.lblDificil.place(x=20,y=50)
        self.nombre = tk.Label(self.top,text='JUGADOR',font=('System'))
        self.nombre.place(x=200,y=50)
        self.tiempo = tk.Label(self.top,text='TIEMPO',font=('System'))
        self.tiempo.place(x=360,y=50)

        self.lblIntermedio = tk.Label(self.top,text='NIVEL INTERMEDIO:',font=('System'))
        self.lblIntermedio.place(x=20,y=290)
        self.nombre = tk.Label(self.top,text='JUGADOR',font=('System'))
        self.nombre.place(x=200,y=290)
        self.tiempo = tk.Label(self.top,text='TIEMPO',font=('System'))
        self.tiempo.place(x=360,y=290)

        self.lblFacil = tk.Label(self.top,text='NIVEL FÁCIL:',font=('System'))
        self.lblFacil.place(x=20,y=530)
        self.nombre = tk.Label(self.top,text='JUGADOR',font=('System'))
        self.nombre.place(x=200,y=530)
        self.tiempo = tk.Label(self.top,text='TIEMPO',font=('System'))
        self.tiempo.place(x=360,y=530)

######################################################## JUGADORES EN MODO DÍFICIL ################################################################
        self.nombreD1 = tk.Label(self.top,text='',font=('System'))
        self.nombreD1.place(x=195,y=70)
        self.nombreD2 = tk.Label(self.top,text='',font=('System'))
        self.nombreD2.place(x=195,y=90)
        self.nombreD3 = tk.Label(self.top,text='',font=('System'))
        self.nombreD3.place(x=195,y=110)
        self.nombreD4 = tk.Label(self.top,text='',font=('System'))
        self.nombreD4.place(x=195,y=130)
        self.nombreD5 = tk.Label(self.top,text='',font=('System'))
        self.nombreD5.place(x=195,y=150)
        self.nombreD6 = tk.Label(self.top,text='',font=('System'))
        self.nombreD6.place(x=195,y=170)
        self.nombreD7 = tk.Label(self.top,text='',font=('System'))
        self.nombreD7.place(x=195,y=190)
        self.nombreD8 = tk.Label(self.top,text='',font=('System'))
        self.nombreD8.place(x=195,y=210)
        self.nombreD9 = tk.Label(self.top,text='',font=('System'))
        self.nombreD9.place(x=195,y=230)
        self.nombreD10 = tk.Label(self.top,text='',font=('System'))
        self.nombreD10.place(x=195,y=250)

        nombreD1 = tk.Label(self.top,text='1-',font=('System'))
        nombreD1.place(x=180,y=70)
        nombreD2 = tk.Label(self.top,text='2-',font=('System'))
        nombreD2.place(x=180,y=90)
        nombreD3 = tk.Label(self.top,text='3-',font=('System'))
        nombreD3.place(x=180,y=110)
        nombreD4 = tk.Label(self.top,text='4-',font=('System'))
        nombreD4.place(x=180,y=130)
        nombreD5 = tk.Label(self.top,text='5-',font=('System'))
        nombreD5.place(x=180,y=150)
        nombreD6 = tk.Label(self.top,text='6-',font=('System'))
        nombreD6.place(x=180,y=170)
        nombreD7 = tk.Label(self.top,text='7-',font=('System'))
        nombreD7.place(x=180,y=190)
        nombreD8 = tk.Label(self.top,text='8-',font=('System'))
        nombreD8.place(x=180,y=210)
        nombreD9 = tk.Label(self.top,text='9-',font=('System'))
        nombreD9.place(x=180,y=230)
        nombreD10 = tk.Label(self.top,text='10-',font=('System'))
        nombreD10.place(x=177,y=250)

######################################################## JUGADORES EN MODO INTERMEDIO #############################################################
        self.nombreI1 = tk.Label(self.top,text='',font=('System'))
        self.nombreI1.place(x=195,y=310)
        self.nombreI2 = tk.Label(self.top,text='',font=('System'))
        self.nombreI2.place(x=195,y=330)
        self.nombreI3 = tk.Label(self.top,text='',font=('System'))
        self.nombreI3.place(x=195,y=350)
        self.nombreI4 = tk.Label(self.top,text='',font=('System'))
        self.nombreI4.place(x=195,y=370)
        self.nombreI5 = tk.Label(self.top,text='',font=('System'))
        self.nombreI5.place(x=195,y=390)
        self.nombreI6 = tk.Label(self.top,text='',font=('System'))
        self.nombreI6.place(x=195,y=410)
        self.nombreI7 = tk.Label(self.top,text='',font=('System'))
        self.nombreI7.place(x=195,y=430)
        self.nombreI8 = tk.Label(self.top,text='',font=('System'))
        self.nombreI8.place(x=195,y=450)
        self.nombreI9 = tk.Label(self.top,text='',font=('System'))
        self.nombreI9.place(x=195,y=470)
        self.nombreI10 = tk.Label(self.top,text='',font=('System'))
        self.nombreI10.place(x=195,y=490)

        nombreI1 = tk.Label(self.top,text='1-',font=('System'))
        nombreI1.place(x=180,y=310)
        nombreI2 = tk.Label(self.top,text='2-',font=('System'))
        nombreI2.place(x=180,y=330)
        nombreI3 = tk.Label(self.top,text='3-',font=('System'))
        nombreI3.place(x=180,y=350)
        nombreI4 = tk.Label(self.top,text='4-',font=('System'))
        nombreI4.place(x=180,y=370)
        nombreI5 = tk.Label(self.top,text='5-',font=('System'))
        nombreI5.place(x=180,y=390)
        nombreI6 = tk.Label(self.top,text='6-',font=('System'))
        nombreI6.place(x=180,y=410)
        nombreI7 = tk.Label(self.top,text='7-',font=('System'))
        nombreI7.place(x=180,y=430)
        nombreI8 = tk.Label(self.top,text='8-',font=('System'))
        nombreI8.place(x=180,y=450)
        nombreI9 = tk.Label(self.top,text='9-',font=('System'))
        nombreI9.place(x=180,y=470)
        nombreI10 = tk.Label(self.top,text='10-',font=('System'))
        nombreI10.place(x=177,y=490)

######################################################## JUGADORES EN MODO FÁCIL ##################################################################
        self.nombreF1 = tk.Label(self.top,text='',font=('System'))
        self.nombreF1.place(x=195,y=550)
        self.nombreF2 = tk.Label(self.top,text='',font=('System'))
        self.nombreF2.place(x=195,y=570)
        self.nombreF3 = tk.Label(self.top,text='',font=('System'))
        self.nombreF3.place(x=195,y=590)
        self.nombreF4 = tk.Label(self.top,text='',font=('System'))
        self.nombreF4.place(x=195,y=610)
        self.nombreF5 = tk.Label(self.top,text='',font=('System'))
        self.nombreF5.place(x=195,y=630)
        self.nombreF6 = tk.Label(self.top,text='',font=('System'))
        self.nombreF6.place(x=195,y=650)
        self.nombreF7 = tk.Label(self.top,text='',font=('System'))
        self.nombreF7.place(x=195,y=670)
        self.nombreF8 = tk.Label(self.top,text='',font=('System'))
        self.nombreF8.place(x=195,y=690)
        self.nombreF9 = tk.Label(self.top,text='',font=('System'))
        self.nombreF9.place(x=195,y=710)
        self.nombreF10 = tk.Label(self.top,text='',font=('System'))
        self.nombreF10.place(x=195,y=730)

        nombreF1 = tk.Label(self.top,text='1-',font=('System'))
        nombreF1.place(x=180,y=550)
        nombreF2 = tk.Label(self.top,text='2-',font=('System'))
        nombreF2.place(x=180,y=570)
        nombreF3 = tk.Label(self.top,text='3-',font=('System'))
        nombreF3.place(x=180,y=590)
        nombreF4 = tk.Label(self.top,text='4-',font=('System'))
        nombreF4.place(x=180,y=610)
        nombreF5 = tk.Label(self.top,text='5-',font=('System'))
        nombreF5.place(x=180,y=630)
        nombreF6 = tk.Label(self.top,text='6-',font=('System'))
        nombreF6.place(x=180,y=650)
        nombreF7 = tk.Label(self.top,text='7-',font=('System'))
        nombreF7.place(x=180,y=670)
        nombreF8 = tk.Label(self.top,text='8-',font=('System'))
        nombreF8.place(x=180,y=690)
        nombreF9 = tk.Label(self.top,text='9-',font=('System'))
        nombreF9.place(x=180,y=710)
        nombreF10 = tk.Label(self.top,text='10-',font=('System'))
        nombreF10.place(x=177,y=730)

        # LISTA QUE ALMACENA CADA UNO DE LOS NOMBRES DE LOS JUGADORES 
        self.TOP10 = [[self.nombreD1,self.nombreD2,self.nombreD3,self.nombreD4,self.nombreD5,self.nombreD6,self.nombreD7,self.nombreD8,self.nombreD9,self.nombreD10],\
                      [self.nombreI1,self.nombreI2,self.nombreI3,self.nombreI4,self.nombreI5,self.nombreI6,self.nombreI7,self.nombreI8,self.nombreI9,self.nombreI10],\
                      [self.nombreF1,self.nombreF2,self.nombreF3,self.nombreF4,self.nombreF5,self.nombreF6,self.nombreF7,self.nombreF8,self.nombreF9,self.nombreF10]]

        for i,nombre in enumerate(tops[2]):
            self.TOP10[0][i].configure(text=tops[2][i])
        for i,nombre in enumerate(tops[1]):
            self.TOP10[1][i].configure(text=tops[1][i])
        for i,nombre in enumerate(tops[0]):
            self.TOP10[2][i].configure(text=tops[0][i])
        top10.close()

        self.btnSalir = tk.Button(self.top,text='Salir',font=('System'),command=self.salirVentana)
        self.btnSalir.place(x=20,y=710)

###################################################################################################################################################
    def salirVentana(self):
        global h,m,s
        global running
        global proceso
        self.time.after(1000,self.inicioJuego)  #el tiempo se reanuda
        self.top.destroy()
###################################################################################################################################################
    def guardarJuego(self):
#Este botón se puede usar en cualquier momento que el juego haya iniciado, antes de ello permanece inhabilitado. 
# Guarda en el archivo “futoshiki2021juegoactual.dat” todo el estado del  juego  actual: configuración, cuadrícula, nombre del jugador, etc.  
# El objetivo es que el jugador pueda en cualquier momento guardar el juego y posteriormente continuarlo en el punto donde hizo el guardado del juego. 
# Este archivo solo va a contener una partida. En caso de que haya una partida en el archivo, se borra y se guarda la del momento.
        pass
###################################################################################################################################################
    def cargarJuego(self):
#Este botón se puede usar solamente cuando un juego no se haya iniciado, luego de ello permanece inhabilitado. 
# Trae del archivo “futoshiki2021juegoactual.dat” el juego que fue guardado y lo pone en la pantalla como el juego actual con exactamente el 
# mismo estado que tenía cuando fue guardado. El juego continúa cuando el jugador usa el botón de INICIAR JUEGO.
        pass
##################################################################################################################################################
    def ayuda(self):
        # Esta opción la usaremos para que el usuario pueda ver el Manual de Usuario directamente en la computadora (despliega el pdf  respectivo). 
        path = 'manual_de_usuario_futoshiki.pdf'
        os.system(path)
###################################################################################################################################################
    def acercaDe(self):
        self.ventanaInfo = tk.Tk()
        self.ventanaInfo.geometry('800x300')
        self.ventanaInfo.title('Información del Programa')
        self.lblTitulo = tk.Label(self.ventanaInfo,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X) 
        Autor = tk.Label(self.ventanaInfo,text='Autor del Programa:',font=('Courier New',16,'bold')).place(x=0,y=60)
        nombreAutor = tk.Label(self.ventanaInfo,text='Kevin Vinicio Núñez Cruz',font=('Courier New',16)).place(x=300,y=60)
        programa = tk.Label(self.ventanaInfo,text='Nombre del Programa:',font=('Courier New',16,'bold')).place(x=0,y=90)
        nombrePrograma = tk.Label(self.ventanaInfo,text='Juego Futoshiki',font=('Courier New',16)).place(x=300,y=90)
        version = tk.Label(self.ventanaInfo,text='Versión:',font=("Courier New",16,'bold')).place(x=0,y=120)
        nombreVersion = tk.Label(self.ventanaInfo,text='Python 3.8.3',font=('Courier New',16)).place(x=300,y=120)
        creacion = tk.Label(self.ventanaInfo,text='Fecha de Creacion:',font=('Courier New',16,'bold')).place(x=0,y=150)
        fechaCreacion = tk.Label(self.ventanaInfo,text='12 de Junio del 2021',font=('Courier New',16)).place(x=300,y=150)
###################################################################################################################################################
    def salir(self):
        respuesta= messagebox.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta==True:
            self.master.destroy()
###################################################################################################################################################

######################################################## PROGRAMA PRINCIPAL #######################################################################
proceso=0  
h=0         
m=0
s=0
running = False
###################################################################################################################################################
def main():
    app = tk.Tk()
    ventanaPrincipal = Futoshiki(app)
    app.mainloop()

if __name__ == "__main__":
    main()
###################################################################################################################################################