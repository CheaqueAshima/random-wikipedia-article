import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import lxml
import urllib3 

http = urllib3.PoolManager()

class windowclass():
    def __init__(self, master):
        self.master = master
        
        helv36 = tkFont.Font(family="Helvetica",size=18,weight="bold")
        helv34 = tkFont.Font(family="Times",size=18,weight="bold")
        self.btn = tk.Button(master, text="Start", command=self.command,bg='#000000',
                fg='#b7f731',
                relief='flat',
                width=30,font = helv36)

        self.btn.pack(padx=50,pady=200)

    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("800x600")
        app = Demo2(toplevel)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,highlightbackground="green", highlightcolor="green", highlightthickness=2, width=700, height=600, bd= 0)
        self.tkvar = StringVar(root)
        # Dictionary with options
        choices = { 'Motivation','Psychology'}
        self.tkvar.set('Choose Category') # set the default option
        popupMenu = OptionMenu(self.frame, self.tkvar, *choices,command = self.change_dropdown)
        popupMenu.grid(row=0,column=0,padx=2,pady=20)
        popupMenu.configure(width=23)
        helv36 = tkFont.Font(family="Helvetica",size=18,weight="bold")
        helv34 = tkFont.Font(family="Malgun Gothic",size=15)
        self.randomButton = tk.Button(self.frame, text = 'Random', width = 15, command = self.randomButton)
        self.randomButton.grid(row=0,column=2,pady=20)

        # self.text2 = tk.Text(self.frame, height=20, width=50)
        # self.scroll = tk.Scrollbar(self.frame, command=self.text2.yview)
        # self.text2.grid(row=1,column=0,padx=10)


        self.titleLabel = tk.Label(self.frame,text="This will be my title",font=helv36,justify=LEFT,anchor='w',fg='MediumSeaGreen')
        self.titleLabel.grid(row=1,column=0,padx=10)


        self.contentLabel = tk.Label(self.frame,text="This will be my Content",font=helv34,justify=LEFT,anchor='w',bg="MINT CREAM",wraplength=800)
        self.contentLabel.grid(column=0,padx=10,rowspan=10)

        self.saveButton = tk.Button(self.frame, text = 'Save', width = 15, command = self.close_windows)
        self.saveButton.grid(row=2,column=2)

        self.cancelButton = tk.Button(self.frame, text = 'Cancel', width = 15, command = self.close_windows)
        self.cancelButton.grid(row=3,column=2,padx=10)

        self.frame.grid(padx=50,pady=30)

    def close_windows(self):
        self.master.destroy()
    def change_dropdown(self,*args):
      selected_category = self.tkvar.get()
      return selected_category
    def randomButton(self,*args):
      a = self.change_dropdown()
      if a == 'Motivation':
         response = http.request("GET", "https://en.wikipedia.org/wiki/Special:RandomInCategory/Motivation")
         #response = requests.get('https://en.wikipedia.org/wiki/Special:RandomInCategory/Motivation')
      elif a =='Psychology':
         response = http.request("GET", "https://en.wikipedia.org/wiki/Special:RandomInCategory/Psychology")
         #response = requests.get('https://en.wikipedia.org/wiki/Special:RandomInCategory/Psychology')
      else:
         response = http.request("GET", "https://en.wikipedia.org/wiki/Special:Random")
         #response = requests.get('https://en.wikipedia.org/wiki/Special:Random')


      print(response)
      soup  =BeautifulSoup(response.data,'lxml')
      title  = soup.find('h1',{'class':'firstHeading'}).text
      content =[]
      str1 = ""
      for i in soup.find_all('p'):
         content.append(i.text)
      content2 = str1.join(content)
      self.titleLabel.configure(text=title)
      self.contentLabel.configure(text=content2)

root = tk.Tk()
root.title("Random Wikipedia Article Generator")
root.geometry("800x600")

cls = windowclass(root)
root.mainloop()