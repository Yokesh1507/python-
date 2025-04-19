import tkinter as tk

root = tk.Tk()
root.title("yokesh")

root.configure(bg="green")


tk.Label(root,text="name:",bg="green",fg="white").grid (row=0,column=0)
tk.Entry(root,bg='lightblue').grid(row=0,column=1)

tk.Label(root,text="mail:",bg="green",fg="white").grid(row=1,column=0)
tk.Entry(root,bg='lightblue').grid (row=1,column=1)

tk.Label(root,text="number:",bg="green",fg="white").grid(row=2,column=0)
tk.Entry(root,bg='lightblue').grid(row=2,column=1)

tk.Label(root, text="genter:",bg="green",fg="white").grid(row=4,column=0)
tk.Radiobutton(root,text="male",bg='green').grid(row=4,column=1)
tk.Radiobutton(root, text="female",bg="green").grid(row=5,column=1)

tk.Label(root, text="coures:",bg="green",fg="white").grid(row=7,column=0)
tk.Checkbutton(root,text="python",bg="green").grid(row=7,column=1)
tk.Checkbutton(root,text="linex",bg="green").grid(row=7,column=2)
tk.Checkbutton(root,text="sql",bg="green").grid(row=7,column=3)

tk.Label(root, text="Python Knowledge:",bg="green",fg="white").grid(row=8, column=0)
tk.Scale(root, from_=0, to=10, orient="horizontal",bg="green").grid(row=8, column=1)



tk.Label(root, text="addres:",bg="green",fg="white").grid(row=9, column=0)
text=tk.Text(root,bg='lightblue', height=5, width=35)
scroll = tk.Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.grid(row=9, column=1)
scroll.grid(row=9, column=2)


root.mainloop()