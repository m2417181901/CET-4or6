import tkinter as tk
from TEC import TEC
import tkinter.messagebox
from PIL import ImageTk,Image

class TK(object):
    def __init__(self):
        super(TK, self).__init__()
        self.top = tk.Tk()
        self.top.geometry("500x200")
        self.user_name = tk.StringVar()
        self.user_name.set('马泽伟')
        self.user_zh = tk.StringVar()
        self.user_yzm = tk.StringVar()
        self.user_zh.set('132480192108105')
        tk.Label(self.top,text="用户账号:").place(x=100,y=50)
        tk.Label(self.top,text="用户密码:").place(x=100,y=100)
        self.entry_user_name = tk.Entry(self.top,textvariable=self.user_name)
        self.entry_user_name.place(x=160,y=100)
        tk.Label(self.top, text="验证码:").place(x=100, y=150)
        self.entry_user_zh = tk.Entry(self.top,textvariable=self.user_zh)

        self.entry_user_yzm = tk.Entry(self.top, textvariable=self.user_yzm).place(x=160, y=150)
        self.entry_user_yzm = tk.Entry(self.top, textvariable=self.user_yzm).place(x=160, y=150)
        self.entry_user_zh.place(x=160,y=50)
        tk.Button(self.top, text="获取验证码", command=self.yzm).place(x=400, y=150)
        tk.Button(self.top, text="提交", height=5, width=15, activeforeground='red', background='#9ACD32',
                  command=self.result).place(x=350, y=30)
        self.top.mainloop()
    def yzm(self):
        self.a = TEC(self.user_zh.get(),self.user_name.get())
        global IMAGE
        IMAGE = self.a.yzm()
        tk.Label(self.top, image=IMAGE).place(x=10, y=10)
        print(self.yzm)
    def result(self):
        self.yzm = self.user_yzm.get()
        self.content = self.a.getresult(self.user_yzm.get())
        tk.messagebox.showinfo(title='成绩', message=self.content)
d = TK()
