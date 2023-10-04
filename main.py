from cgitb import text
from gc import disable
from operator import truediv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import Tree
root = Tk(screenName="Tic Tac Toe")
frm = ttk.Frame(root, padding=10)
#Whose Turns
clicked = True
count = 0



#Disable all buttons
def disable__all__buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
#Checks if someone wins
def check_winner():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b3["text"] == 'X' and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b3["text"] == 'X' and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b4["text"] == 'X' and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b6.config(bg="red")
        b5.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b7["text"] == 'X' and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b1["text"] == 'X' and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    elif b2["text"] == 'X' and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","X Wins !!!")
        disable__all__buttons()
    


    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b3["text"] == 'O' and b6["text"] == "O" and b9["text"] == "XO":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b2["text"] == 'O' and b5["text"] == "O" and b7["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b3["text"] == 'O' and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b4["text"] == 'O' and b5["text"] == "O" and b6["text"] == "OX":
        b4.config(bg="red")
        b6.config(bg="red")
        b5.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b7["text"] == 'O' and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b1["text"] == 'O' and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b2["text"] == 'O' and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif b4["text"] == 'O' and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner= True
        messagebox.showinfo("Tic Tac Toe","O Wins !!!")
        disable__all__buttons()
    elif count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe","It's a Tie !")
        reset()
    
#Our Click Function
def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Tic Tac Toe", "This Box Has Been Already Taken\n Goo Find Another Box")
#Start the game over !
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked,count
    clicked = True
    count = 0
    b1 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b1))
    b2 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b2))
    b3 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b3))

    b4 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b4))
    b5 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b5))
    b6 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b6))

    b7 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b7))
    b8 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b8))
    b9 = Button(root,height=4,width=5,text=' ',font=("Helvetica", 20),bg="Silver",command = lambda: b_click(b9))

    #Grid Our Buttons to the screen
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

myMenu = Menu(root)
root.config(menu=myMenu)

options_menu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Options Menu",menu=options_menu)
options_menu.add_command(label="Reset game", command=reset)
reset()
root.mainloop()