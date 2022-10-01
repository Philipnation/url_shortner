import requests
from tkinter import *
from tkinter import messagebox
try:
    windows = Tk()
    windows.title('url shortener')
    windows.geometry("1200x600")
    windows.iconbitmap("sh.ico")


    def runner():
        try:
            page_url = "https://cutt.ly/scripts/shortenUrl.php"
            datas = {
                "url": linker.get(),
                "domain": 0
            }
            run = requests.post(url=page_url, data=datas)
            if linker.get() == '':
                messagebox.showinfo(title="Empty", message="Input is empty")
            elif 'The provided link is incorrect' in run.text:
                messagebox.showinfo(title="Invalid url", message="Invalid url")
            elif 'That is already a cutt.ly link' in run.text:
                messagebox.showinfo(title="Invalid url", message="Invalid url")
            else:
                messagebox.showinfo(title="new url", message=f"your new url is {run.text}")
                linker.delete(0, END)
                linker.insert(0, f"Your new link is---  {run.text}")
        except requests.exceptions.ConnectionError:
            messagebox.showinfo(title="No connection", message="No internet connection")
        return

    win = Frame(windows, width=1200, height=700, bg='black')
    win.pack()
    win.pack_propagate(False)

    page = Frame(win, width=500, height=500, bg='slateblue')
    page.place(x=350, y=30)
    page.pack_propagate(False)
    lab = Label(page, width=40, height=4, text='Enter the url you want to shorten', font=35)
    lab.place(x=70, y=10)
    linker = Entry(page, width=50)
    linker.place(x=100, y=150)
    btn = Button(page, text="Shorten now", width=20, command=runner)
    btn.place(x=170, y=200)
    windows.mainloop()
except requests.exceptions.ConnectionError:
    messagebox.showinfo(title="No connection", message="No internet connection")
