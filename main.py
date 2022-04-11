import tkinter as tk 

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry('600x600')
root.columnconfigure(1, weight = 1)
 
# 1st row
message_label = tk.Label(
    root,
    text = 'Enter message to encode:',
    font = ('Arial 16 bold'),
    bg = 'Black',
    fg='yellow'
)
message_label.grid(row = 0, column = 0, sticky= (tk.E, tk.W))
messagae_var = tk.StringVar(root)
message_input =tk.Entry(root, textvariable=messagae_var)
message_input.grid(row=0, column=1, sticky= (tk.N,tk.E,tk.S, tk.W), padx= 5)


# 2nd row
encoded_label = tk.Label(
    root,
    text = 'Your encoded message:',
    font = ('Arial 16 bold'),
    bg = 'Yellow',
    fg='black'
)
encoded_label.grid(row = 1, column = 0, sticky = (tk.E, tk.W))
encoded_var = tk.StringVar(root)
encoded_input =tk.Entry(root, textvariable=encoded_var)
encoded_input.grid(row=1, column=1, sticky= (tk.N,tk.E,tk.S, tk.W), padx= 5)

# 3rd row
submit_btn = tk.Button(root, text = 'Encode Text')
submit_btn.gride(row= 2, column = 1, sticky = (tk.E), padx = 10, pady = 10)


root.mainloop()
