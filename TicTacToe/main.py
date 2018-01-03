from tkinter import *
import tkinter.messagebox

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.startframe = Frame()
        self.startframe.grid()

        #Label
        label1 = Label(self.startframe, text="Tic Tac Toe\n Created by Sebastian Wittrock\n\n\n")
        label1.grid(row=0, column=0)
        label1.config(font=(10),)


        Button(self.startframe, text="START!", command=self.start, width=8).grid(row=4, column=0)

    def start(self):
        #destroy old frame
        self.startframe.destroy()

        #create new frame
        self.gameframe = Frame()
        self.gameframe.grid()

        self.turn = True
        self.button1 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height = 4, width = 8,
        command=lambda:self.checker(self.button1))

        self.button1.grid(row = 0, column= 0, sticky = S + N + E + W)

        self.button2 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button2))

        self.button2.grid(row=0, column=1, sticky=S + N + E + W)

        self.button3 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button3))

        self.button3.grid(row=0, column=2, sticky=S + N + E + W)

        self.button4 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button4))

        self.button4.grid(row=1, column=0, sticky=S + N + E + W)

        self.button5 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button5))

        self.button5.grid(row=1, column=1, sticky=S + N + E + W)

        self.button6 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button6))

        self.button6.grid(row=1, column=2, sticky=S + N + E + W)

        self.button7 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button7))

        self.button7.grid(row=2, column=0, sticky=S + N + E + W)

        self.button8 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button8))

        self.button8.grid(row=2, column=1, sticky=S + N + E + W)

        self.button9 = Button(self.gameframe, text=" ", font=("Times 26 bold"), height=4, width=8,
        command=lambda: self.checker(self.button9))

        self.button9.grid(row=2, column=2, sticky=S + N + E + W)


    def checker(self, bttn):

        if bttn["text"] == " " and self.turn == True:
            bttn["text"] = "X"
            self.turn = False
        elif bttn["text"] == " " and self.turn == False:
            bttn["text"] = "O"
            self.turn = True
        elif bttn["text"] == "X" or bttn["text"] == "O":
            tkinter.messagebox.showinfo("Invalid", "Cannot place here, try again!")
        if(self.button1["text"] == "X" and self.button2["text"] == "X" and self.button3["text"] == "X" or
             self.button4["text"] == "X" and self.button5["text"] == "X" and self.button6["text"] == "X" or
             self.button7["text"] == "X" and self.button8["text"] == "X" and self.button9["text"] == "X" or
             self.button3["text"] == "X" and self.button5["text"] == "X" and self.button7["text"] == "X" or
             self.button1["text"] == "X" and self.button5["text"] == "X" and self.button9["text"] == "X" or
             self.button1["text"] == "X" and self.button4["text"] == "X" and self.button7["text"] == "X" or
             self.button2["text"] == "X" and self.button5["text"] == "X" and self.button8["text"] == "X" or
             self.button3["text"] == "X" and self.button6["text"] == "X" and self.button9["text"] == "X"):
                tkinter.messagebox.showinfo("Winner", "Player One wins!")
                sys.exit()

        if (self.button1["text"] == "O" and self.button2["text"] == "O" and self.button3["text"] == "O" or
              self.button4["text"] == "O" and self.button5["text"] == "O" and self.button6["text"] == "O" or
              self.button7["text"] == "O" and self.button8["text"] == "O" and self.button9["text"] == "O" or
              self.button3["text"] == "O" and self.button5["text"] == "O" and self.button7["text"] == "O" or
              self.button1["text"] == "O" and self.button5["text"] == "O" and self.button9["text"] == "O" or
              self.button1["text"] == "O" and self.button4["text"] == "O" and self.button7["text"] == "O" or
              self.button2["text"] == "O" and self.button5["text"] == "O" and self.button8["text"] == "O" or
              self.button3["text"] == "O" and self.button6["text"] == "O" and self.button9["text"] == "O"):
                tkinter.messagebox.showinfo("Winner", "Player Two wins!")
                sys.exit()

        elif(self.button1["text"] != " " and self.button2["text"] != " " and self.button3["text"] != " " and self.button4["text"] != " " and
             self.button5["text"] != " " and self.button6["text"] != " " and self.button7["text"] != " " and self.button8["text"] != " " and
             self.button9["text"] != " "):
                tkinter.messagebox.showinfo("Tie", "Better luck next Time!")
                sys.exit()



def main():
    root = Tk()
    root.title('Tic Tac Toe')
    turn = True

    app = Application(root)

    root.mainloop()

main()