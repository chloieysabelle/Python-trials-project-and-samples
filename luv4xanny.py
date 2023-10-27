import tkinter as tk
import webbrowser

def button_click(loved):
    if loved:
        url = "https://i.pinimg.com/564x/3e/b1/33/3eb133b14841714d422e4f775730831a.jpg"
    else:
        url = "https://i.pinimg.com/564x/06/08/32/0608326a9b15a7e77164b5a7cd393fc6.jpg"
    webbrowser.open(url)

def submit_msg():
    entered_text = entry_variable.get()
    print(entered_text)
    entry_variable.set("")

root = tk.Tk()


root.geometry("500x250")
root.title("for my loverboyxanny<33")

label = tk.Label(root,
                text="Hi baby xanny! i love you",
                font=("Times", "24"),
                fg="black",
                 )
label.pack(padx=50, pady=10)

button1=tk.Button(root,
              text="click here if you love me too",
              font=("Times", "14"),
              fg="blue",
              bg="white",
              command=lambda: button_click(True))
button1.pack(padx=10, pady=5)

button2=tk.Button(root,
              text="click here if you dont -.-",
              font=("Times", "14"),
              fg="blue",
              bg="white",
              command=lambda: button_click(False))
button2.pack(padx=10, pady=5)

label = tk.Label(root,
                text="type ur message below lol (4 my eyes only):",
                font=("Times", "12"),
                fg="black",
                 )
label.pack(padx=50, pady=10)

entry_variable = tk.StringVar()
entry = tk.Entry(root,
                 textvariable=entry_variable
                 )
entry.pack()

entry.bind("<Return>", submit_msg)

show_msg_button = tk.Button(root,
                             text="send",
                             font=("Arial", "6"),
                             width=10,
                             height=1,
                             command=submit_msg)
show_msg_button.pack()

saved_text = tk.StringVar()

root.mainloop(

)
