import time
from tkinter import *
from tkinter import messagebox
 
 

class Temporizador:
    def __init__(self,root) -> None:
        self.root = root
        # setting geometry of tk window
        self.root.geometry("300x250")
        # Using title() to display a message in
        # the dialogue box of the message in the
        # title bar.
        self.root.title("Time Counter")
        
        # Declaration of variables
        self.hour=StringVar()
        self.minute=StringVar()
        self.second=StringVar()
        
        # setting the default value as 0
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")
        
        # Use of Entry class to take input from the user
        self.hourEntry= Entry(self.root, width=3, font=("Arial",18,""),
                        textvariable=self.hour)
        self.hourEntry.place(x=80,y=20)
        
        self.minuteEntry= Entry(self.root, width=3, font=("Arial",18,""),
                        textvariable=self.minute)
        self.minuteEntry.place(x=130,y=20)
        
        self.secondEntry= Entry(self.root, width=3, font=("Arial",18,""),
                        textvariable=self.second)
        self.secondEntry.place(x=180,y=20)
    
        # button widget
        self.btn = Button(self.root, text='Set Time Countdown', bd='5',
                    command= self.submit)
        self.btn.place(x = 70,y = 120)
        
        
    def submit(self):
        try:
            # the input provided by the user is
            # stored in here :temp
            self.temp = int(self.hour.get())*3600 + int(self.minute.get())*60 + int(self.second.get())
        except:
            print("Please input the right value")
        while self.temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            self.mins,self.secs = divmod(self.temp,60)
        
            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            self.hours=0
            if self.mins >60:
                    
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                self.hours, self.mins = divmod(self.mins, 60)
                
            # using format () method to store the value up to
            # two decimal places
            self.hour.set("{0:2d}".format(self.hours))
            self.minute.set("{0:2d}".format(self.mins))
            self.second.set("{0:2d}".format(self.secs))
        
            # updating the GUI window after decrementing the
            # temp value every time
            self.root.update()
            time.sleep(1)
        
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (self.temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
                
            # after every one sec the value of temp will be decremented
            # by one
            self.temp -= 1
    
def main():
    # creating Tk window
    root = Tk()
    ventanaPrincipal = Temporizador(root)
    # infinite loop which is required to
    # run tkinter program infinitely
    # until an interrupt occurs
    root.mainloop()

if __name__ == "__main__":
    main()