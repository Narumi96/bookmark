from tkinter import *
from tkinter import ttk
import chatgpt
import TriplusData as tp
import pandas as pd
import InsertDatabase
import json

class TriPlrsForm():
    def __init__(self):
        self.purpose_list = ['旅行に行きたい', '出張に行きたい', '帰省したい', '遊びに行きたい', 'その他']
        self.root = Tk()
        self.root.title('Triplrs')
        self.root.geometry("390x840")
        self.frame1 = ttk.Frame(self.root, padding=(32))
        
        self.nowLocation = '広島'
        self.purposeLocation ='東京'
        self.purpose = self.purpose_list[0]
        self.budget = '100000円'
        #イベントのフラグ
    
    def Home(self):#ウィンドウ表示継続
        self.frame1.grid()        
        # しおり
        self.button1 = ttk.Button(
            self.frame1, text='旅のしおり１', 
            command=self.set_Bookmark
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button1.grid(row=0, column=1)
        
        # Button
        self.button2 = ttk.Button(
            self.frame1, text='home', 
            command=self.set_Home
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button2.grid(row=6, column=0)
        # Button
        self.button3 = ttk.Button(
            self.frame1, text='Generate', 
            command=self.set_InputForm
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button3.grid(row=6, column=1)
        
        self.root.mainloop()   
    
    def Bookmark(self,bookmark_df):
        self.frame1.grid()  
        bookmark = ""
        for df in bookmark_df:
            bookmark+=df[1]
            bookmark+=" "
            bookmark+=df[0]
            bookmark+="\n"
        #しおりの内容表示
        print(bookmark)
        self.label1 = ttk.Label(self.frame1, text=bookmark, padding=(5, 2))
        self.label1.grid(row=0, column=0, sticky=E)
        
        # Button
        self.button2 = ttk.Button(
            self.frame1, text='home', 
            command=self.set_Home
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button2.grid(row=6, column=0)
        # Button
        self.button3 = ttk.Button(
            self.frame1, text='Generate', 
            command=self.set_InputForm
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button3.grid(row=6, column=1)
        
        self.root.mainloop()  
        
    def InputForm(self):
        #ウィンドウ表示継続
        self.frame1.grid()
        #現在地
        self.label1 = ttk.Label(self.frame1, text='現在地は？', padding=(5, 2))
        self.label1.grid(row=0, column=0, sticky=E)

        #目的地
        self.label2 = ttk.Label(self.frame1, text='目的地は？', padding=(5, 2))
        self.label2.grid(row=1, column=0, sticky=E)

        #日数
        self.label4 = ttk.Label(self.frame1, text='期間は？', padding=(5, 2))
        self.label4.grid(row=2, column=0, sticky=E)
        
        #日数
        self.label4 = ttk.Label(self.frame1, text='目的は？', padding=(5, 2))
        self.label4.grid(row=3, column=0, sticky=E)

        #予算
        self.label5 = ttk.Label(self.frame1, text='予算は？', padding=(5, 2))
        self.label5.grid(row=4, column=0, sticky=E)

        #現在地の入力
        self.nowLocation = StringVar()
        self.nowLocation_txt = ttk.Entry(
            self.frame1,
            textvariable=self.nowLocation,
            width=20)
        self.nowLocation_txt.grid(row=0, column=1)
        self.nowLocation_txt.insert(END,"広島")

        #目的地の入力
        self.purposeLocation = StringVar()
        self.purposeLocation_txt = ttk.Entry(
            self.frame1,
            textvariable=self.purposeLocation,
            width=20) 
        self.purposeLocation_txt.grid(row=1, column=1)
        self.purposeLocation_txt.insert(END,"東京")
        
        #日数の入力
        self.purposeDays = StringVar()
        self.purposeDays_txt = ttk.Entry(
            self.frame1,
            textvariable=self.purposeDays,
            width=20) 
        self.purposeDays_txt.grid(row=2, column=1)
        self.purposeDays_txt.insert(END,"8/8から8/11まで")

        #目的の入力
        self.purpose = StringVar()
        self.purpose_menu = ttk.Combobox(
            self.frame1, 
            textvariable=self.purpose, 
            values=self.purpose_list, 
            width=20)
        self.purpose_menu.set(self.purpose_list[0])
        self.purpose_menu.bind('<<ComboboxSelected>>')
        self.purpose_menu.grid(row=3, column=1)

        #予算の入力
        self.budget = StringVar()
        self.budget_text = ttk.Entry(
            self.frame1, 
            textvariable=self.budget,  
            width=20)
        self.budget_text.grid(row=4, column=1)
        self.budget_text.insert(END,"100000円")

        # Button
        self.button1 = ttk.Button(
            self.frame1, text='OK', 
            command=self.send
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button1.grid(row=5, column=1)
        # Button
        self.button2 = ttk.Button(
            self.frame1, text='home', 
            command=self.set_Home
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button2.grid(row=6, column=0)
        # Button
        self.button3 = ttk.Button(
            self.frame1, text='Generate', 
            command=self.set_InputForm
            )
        # lambda: print("%s, %s, %s, %s" % (self.nowLocation.get(), self.purposeLocation.get(), self.purpose.get(), self.budget.get()))
        self.button3.grid(row=6, column=1)
        
        self.root.mainloop()        
    
    def set_InputForm(self):
        self.frame1.destroy()
        self.frame1 = ttk.Frame(self.root, padding=(32))
        self.InputForm()
        return
    
    def set_Home(self):
        self.frame1.destroy()
        self.frame1 = ttk.Frame(self.root, padding=(32))
        self.Home()
        return
    
    def set_Bookmark(self):
        # with open('data.json', 'r', encoding='utf-8') as f:
        #     bookmark_df = pd.read_json(f)
        bookmark_df = InsertDatabase.InsertData()
        self.frame1.destroy()
        self.frame1 = ttk.Frame(self.root, padding=(32))
        self.Bookmark(bookmark_df)
        return
    
    def send(self):
        trip = tp.GenerateData()
        question =  {"現在地" :self.nowLocation.get(),
                     "行先"   :self.purposeLocation.get(),
                     "日数"   :self.purposeDays.get(),
                     "目的"   :self.purpose.get(),
                     "予算"   :self.budget.get()}
        
        for key,text in question.items():
            trip.setQuestion(key, text)
        trip.generateSendText()
        msg = trip.getSendText()
        print (msg)
        
        chatgpt.gpt(msg)
        #self.frame1.destroy()
