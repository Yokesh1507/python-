import tkinter as tk

root = tk.Tk()   
root.title("yokesh bio data")

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)


tk.Label(root, text="Phone:").grid(row=2, column=0)
tk.Entry(root).grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
gender = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=3, column=1)
tk.Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=3, column=2)


tk.Label(root, text="Courses:").grid(row=4, column=0)
course1 = tk.BooleanVar()
course2 = tk.BooleanVar()
course3 = tk.BooleanVar()
tk.Checkbutton(root, text="Python", variable=course1).grid(row=4, column=1)
tk.Checkbutton(root, text="Linux", variable=course2).grid(row=5, column=1)
tk.Checkbutton(root, text="PowerBI", variable=course3).grid(row=6, column=1)


tk.Label(root, text="Python Knowledge:").grid(row=7, column=0)
tk.Scale(root, from_=0, to=10, orient="horizontal").grid(row=7, column=1)


tk.Label(root, text="addres:").grid(row=8, column=0)
text = tk.Text(root,bg='lightblue', height=5, width=35)
scroll = tk.Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.grid(row=8, column=1)
scroll.grid(row=8, column=2)

root.mainloop()


  
