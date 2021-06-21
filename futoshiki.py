import os
import time
import pickle
import tkinter as tk
from functools import partial

from tkinter import messagebox

class Futoshiki(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master =  master
        self.master.title('Futoshiki')
        self.master.geometry('600x600')

        #PARTIDAS DE JUEGO
        self.partidas= open('futoshiki2021partidas.dat','wb')
        pickle.dump([[(('5',0,1),('4',0,4),
        ('4',1,0),('>',1,2),('v',1,1),('v',1,2),
        ('>',2,3),
        ('<',3,2),('<',3,3),('3',3,4),('v',3,0),
        ('3',4,2)),
        (('>',0,3),('v',0,3),
        ('<',1,1),('5',1,4),('v',1,0),
        ('5',2,3),('ʌ',2,0),('v',2,4),
        ('3',3,1),('<',3,1),('5',3,2),('>',3,3),
        ('>',4,2),('4',4,3)),
        (('>',0,0),('2',0,4),('v',0,1),('v',0,3),
        ('4',1,2),('5',1,4),
        ('5',2,2),('>',2,2),('1',2,4),('ʌ',2,3),
        ('>',3,1),('>',3,3),
        ('>',4,3),('4',4,4))
        ]\
        ,[(('1',0,2),('3',0,4),('ʌ',0,0),('ʌ',0,4),
        ('3',1,0),('>',1,2),
        ('2',2,4),('v',2,3),
        ('4',3,2),('v',3,1),
        ('>',4,0),('1',4,1),('>',4,2)),
        (('5',0,0),('3',0,1),('4',0,3),('v',0,3),('ʌ',0,4),
        ('<',1,3),('ʌ',1,2),
        ('4',2,4),
        ('1',3,0),('v',3,3),('ʌ',3,4),
        ('<',4,0),('1',4,3)),
        (('1',0,4),('ʌ',0,2),('ʌ',0,4),
        ('5',1,3),('2',1,4),('ʌ',1,4),
        ('>',2,0),('3',2,1),('<',2,2),('v',2,1),('ʌ',2,2),('v',2,3),
        ('<',4,0),('>',4,1))
        ]\
        ,[(('1',0,3),('v',0,2),
        ('2',1,4),('ʌ',1,1),('v',1,3),('ʌ',1,4),
        ('<',2,0),('>',2,1),('ʌ',2,3),
        ('1',3,0),('3',3,4),('ʌ',3,1),
        ('<',4,0)),
        (('2',0,1),('1',0,2),('4',0,4),
        ('<',1,0),('>',1,2),('2',1,4),
        ('1',2,1),('2',2,3),('3',2,4),
        ('3',3,2),('v',3,3),
        ('2',4,2),('<',4,2)),
        (('3',0,3),('>',0,3),
        ('3',1,0),('5',1,4),('ʌ',1,1),('v',1,2),
        ('4',2,3),('ʌ',2,0),
        ('>',3,0),('1',3,1),('v',3,4),
        ('<',4,1),('5',4,2),('>',4,2))
        ]],self.partidas)
        self.partidas.close()

        self.inicializar_gui()

        #VARIABLES DE LA CONFIGURACION POR DEFAULT
        self.nivelJuego = tk.IntVar()
        self.nivelJuego.set('1')
        self.relojConfig = tk.IntVar()
        self.relojConfig.set('1')
        self.PosicionNumeros = tk.IntVar()
        self.PosicionNumeros.set('1')
        self.configuraciones = (self.nivelJuego.get(),self.relojConfig.get(),self.PosicionNumeros.get())

        #TEMPORIZADOR VARIABLES
        self.hour=tk.StringVar()
        self.minute=tk.StringVar()
        self.second=tk.StringVar()
        #Se configura las variables en el valor default
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        self.configuracion = open('futoshiki2021configuracion.dat','wb')
        pickle.dump([self.configuraciones],self.configuracion)
        self.configuracion.close()
        
    def inicializar_gui(self):
        self.lblTitulo = tk.Label(self.master,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X) 
        self.barMenu = tk.Menu(self.master)
        self.barMenu.add_command(label='Jugar',command=self.juego)
        self.barMenu.add_command(label='Configuracion',command=self.configurar)
        self.barMenu.add_command(label='Ayuda',command=self.ayuda)
        self.barMenu.add_command(label='Acerca De',command=self.acercaDe)
        self.barMenu.add_command(label='Salir',command=self.salir)
        self.master.config(menu=self.barMenu)

    def configurar(self):
        configurar = Configuracion(self.master)
        self.configuraciones = configurar.configuraciones()
    
    def juego(self):
        #CONFIGURACION DEL NIVEL DE JUEGO
        self.lblNivelJuego = tk.Label(self.master,text='NIVEL FÁCIL', font=('System',16))
        self.lblNivelJuego.place(x=250,y=40)
        if self.configuraciones[0] == 1:
            pass
        elif self.configuraciones[0] == 2:
            self.lblNivelJuego.configure(text="NIVEL INTERMEDIO")
        elif self.configuraciones[0] == 3:
            self.lblNivelJuego.configure(text="NIVEL DÍFICIL")
        
        self.lblNombre = tk.Label(self.master,text='Nombre del jugador',font=('System',12)).place(x=10,y=60)
        self.txtNombre = tk.Entry(self.master,width=50,font=('System',12)).place(x=150,y=60)
        self.btnIniciarJuego = tk.Button(self.master,text='INICIAR JUEGO',bg='red',font=('System',10),command=self.inicioJuego).place(x=5,y=450)
        self.btnBorrarJugada = tk.Button(self.master,text='BORRAR JUGADA',bg='blue',font=('System',10)).place(x=125,y=450)
        self.btnTerminarJuego = tk.Button(self.master,text='TERMINAR JUEGO',bg='green',font=('System',10)).place(x=265,y=450)
        self.btnBorraJuego = tk.Button(self.master,text='BORRAR JUEGO',bg='white',font=('System',10)).place(x=405,y=450)
        self.btnTopLevel = tk.Button(self.master,text='TOP 10',bg='yellow',font=('System',10)).place(x=535,y=450)

        #CONFIGURACION DEL RELOJ
        if self.configuraciones[1] == 1:
            self.hourLabel = tk.Label(self.master,text='Horas',width=8,font=('System',12))
            self.hourLabel.place(x=60,y=500)
            self.minuteLabel = tk.Label(self.master,text='Minutos',width=8,font=('System',12))
            self.minuteLabel.place(x=117,y=500)
            self.secondLabel = tk.Label(self.master,text='Segundos',width=8,font=('System',12))
            self.secondLabel.place(x=185,y=500)
            
            self.time = tk.Label(self.master, text= '0:0:0', font=('System',25,''))
            self.time.place(x=75,y=525)

        elif self.configuraciones[1] == 2:
            pass
        else:
            #TEMPORIZADOR 
            self.hourLabel = tk.Label(self.master,text='Horas',width=8,font=('System',12))
            self.hourLabel.place(x=60,y=500)
            self.minuteLabel = tk.Label(self.master,text='Minutos',width=8,font=('System',12))
            self.minuteLabel.place(x=117,y=500)
            self.secondLabel = tk.Label(self.master,text='Segundos',width=8,font=('System',12))
            self.secondLabel.place(x=185,y=500)
            
            # Use of Entry class to take input from the user
            self.hourEntry= tk.Entry(self.master, width=3, font=("System",18,""),
                            textvariable=self.hour)
            self.hourEntry.place(x=80,y=525)
            self.hour.set(self.configuraciones[3])
            
            self.minuteEntry= tk.Entry(self.master, width=3, font=("System",18,""),
                            textvariable=self.minute)
            self.minuteEntry.place(x=130,y=525)
            self.minute.set(self.configuraciones[4])
            
            self.secondEntry= tk.Entry(self.master, width=3, font=("System",18,""),
                            textvariable=self.second)
            self.secondEntry.place(x=180,y=525)
            self.second.set(self.configuraciones[5])
    
        #CONFIGURACION DE LA POSICION DE LOS BOTONES
                    #BOTONES DEL JUEGO
        self.btn1 = tk.Button(self.master,text='1',font=('System',12),activebackground='green',height=2,width=4)
        self.btn1.place(x=530,y=120)
        self.btn2= tk.Button(self.master,text='2',font=('System',12),activebackground='green',height=2,width=4)
        self.btn2.place(x=530,y=170)
        self.btn3 = tk.Button(self.master,text='3',font=('System',12),activebackground='green',height=2,width=4)
        self.btn3.place(x=530,y=220)
        self.btn4 = tk.Button(self.master,text='4',font=('System',12),activebackground='green',height=2,width=4)
        self.btn4.place(x=530,y=270)
        self.btn5 = tk.Button(self.master,text='5',font=('System',12),activebackground='green',height=2,width=4)
        self.btn5.place(x=530,y=320)
        
        if self.configuraciones[2] == 1:
            pass
        else:
            self.btn1.place_configure(x=50,y=120)
            self.btn2.place_configure(x=50,y=170)
            self.btn3.place_configure(x=50,y=220)
            self.btn4.place_configure(x=50,y=270)
            self.btn5.place_configure(x=50,y=320)

        self.btnGuardarJuego = tk.Button(self.master,text='GUARDAR JUEGO',font=('System',10)).place(x=305,y=525)
        self.btnCargarJuego = tk.Button(self.master,text='CARGAR JUEGO',font=('System',10)).place(x=445,y=525)
        
    #METODO PARA EL RELOJ E INICIA EL JUEGO
    def inicioJuego(self,h=0,m=0,s=0):
        global proceso
        if self.configuraciones[1] == 3:
            try:
                # la entrada proporcionada por el usuario es
                # almacenado aquí: temp
                self.temp = int(self.hour.get())*3600 + int(self.minute.get())*60 + int(self.second.get())
            except:
                print("Ingrese el valor correcto")
            while self.temp >-1:
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
                self.mins,self.secs = divmod(self.temp,60)
            
                # Conversión de la entrada ingresada en minutos o segundos a horas, minutos, segundos 
                # (input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
                self.hours=0
                if self.mins >60:
                        
                    # divmod(firstvalue = temp//60, secondvalue
                    # = temp%60)
                    self.hours, self.mins = divmod(self.mins, 60)
                    
                # usando el método format () para almacenar el valor hasta dos lugares decimales
                self.hour.set("{0:2d}".format(self.hours))
                self.minute.set("{0:2d}".format(self.mins))
                self.second.set("{0:2d}".format(self.secs))
            
                # actualizar la ventana de la GUI después de disminuir el 
                # valor del temp cada vez 
                self.master.update()
                time.sleep(1)
            
                # cuando valor de temp = 0; luego aparece un cuadro de mensaje
                # con el mensaje: "Tiempo Expirado" y consulta al usuario si desea continuar
                if (self.temp == 0):
                    respuesta= messagebox.askyesno("Tiempo Expirado", "¿Desea continuar el mismo juego?")
                    if respuesta==True:
                        # Si  responde  SI  entonces  el timer pasa a ser reloj inicializado con el tiempo que se había establecido en 
                        # el  timer.  Por  ejemplo  si  el  timer  estaba  para  1  hora  y  30  minutos,  ahora  el 
                        # reloj debe marcar que ya ha pasado 1 hora y 30 minutos y sigue contando el tiempo.
                        pass
                    else:
                        #Si responde NO el juego finaliza regresando a la opción de Jugar
                        pass
                    
                # after every one sec the value of temp will be decremented
                # by one
                self.temp -= 1
        elif self.configuraciones[1] == 1:
            if s >= 60:
                s = 0
                m = m + 1
                if m >= 60:
                    m = 0
                    h = h + 1
                    if h >= 24:
                        h = 0
        
            #etiqueta que muestra el cronometro en pantalla
            self.time['text'] = str(h)+":"+str(m)+":"+str(s)
        
            # iniciamos la cuenta progresiva de los segundos
            proceso=self.time.after(1000, self.inicioJuego, (h), (m), (s + 1))

    def radioTemporizador(self):
        pass
    
    def PosicionamientoNumeros(self):
        pass

    def ayuda(self):
        pass
        #path = ''
        #os.system(path)

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

    def salir(self):
        respuesta= messagebox.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta==True:
            self.master.destroy()

class Configuracion:
    def __init__(self,master):
        self.ventanaConfigurar = tk.Toplevel(master)
        self.ventanaConfigurar.geometry('500x300')
        self.ventanaConfigurar.title('Configuración')
        self.lblTitulo = tk.Label(self.ventanaConfigurar,text='FUTOSHIKI',fg='white',bg='red',font=('System',20)).pack(fill=tk.X)

        self.nivelJuego = tk.IntVar()
        self.nivelJuego.set('1')

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

        self.relojConfig = tk.IntVar()
        self.relojConfig.set('1')

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
        #TEMPORIZADOR VARIABLES
        self.hour=tk.StringVar()
        self.minute=tk.StringVar()
        self.second=tk.StringVar()
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

        self.PosicionNumeros = tk.IntVar()
        self.PosicionNumeros.set('1')

        self.lblPosicionDigitos = tk.Label(self.ventanaConfigurar,text='Posición en la ventana del panel de dígitos:',font=('System',12)).place(x=10,y=185)
        self.chkDerecha = tk.Radiobutton(self.ventanaConfigurar,text="Derecha", font=('System',12), value = 1, variable=self.PosicionNumeros \
                                                    ,command=self.configuraciones\
                                                    ).place(x=300,y=185)

        self.chkIzquierda = tk.Radiobutton(self.ventanaConfigurar,text="Izquierda", font=('System',12), value = 2, variable=self.PosicionNumeros \
                                                    ,command=self.configuraciones\
                                                    ).place(x=300,y=205)

        self.btnAceptar = tk.Button(self.ventanaConfigurar,text='Aceptar',command=self.confirmar).place(x=35,y=235)

    def configuraciones(self):
        self.ventanaConfigurar.wait_window()
        nivelJuego = self.nivelJuego.get()
        relojConfig = self.relojConfig.get()
        PosicionNumeros = self.PosicionNumeros.get()

        hora = self.hour.get()
        minuto = self.minute.get()
        segundo = self.second.get()

        self.configuracion = open('futoshiki2021configuracion.dat','wb')
        pickle.dump((nivelJuego,relojConfig,PosicionNumeros,hora,minuto,segundo),self.configuracion)
        self.configuracion.close()
        return (nivelJuego,relojConfig,PosicionNumeros,hora,minuto,segundo)

    def confirmar(self):
        self.ventanaConfigurar.destroy()

proceso=0

def main():
    app = tk.Tk()
    ventanaPrincipal = Futoshiki(app)
    app.mainloop()

if __name__ == "__main__":
    main()