from tkinter import Tk,Label,Text,DISABLED,Scrollbar,Entry,Button,messagebox,END,NORMAL,messagebox,ttk
from chat import get_response, bot_name
from time import time, sleep
import datetime
import pandas as pd
import playsound
import re

class ChatBot:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.default_message()

    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("ChatBot ITW Project")
        self.window.configure(width=470, height=550, bg="#ABB2B9")
        current_time = str(datetime.datetime.now())
        lenght = len(current_time)
        time = current_time[:lenght-10]
        head_label1 = Label(self.window, bg="#ABF470", fg="#000000", text="Welcome to IIIT Nagpur", font="Helvetica 14", pady=5)
        head_label1.place(relwidth=1)
        head_label2= Label(self.window, bg="#ABF470", fg="#000000", text="Current Time: "+time, font="Helvetica 14", pady=5)
        head_label2.place(relwidth=0.25)
        line = Label(self.window, width=450, bg="#ABB2B9")
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg="#DDE9E8", fg="#000000",
                                font="Helvetica 14", padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        bottom_label = Label(self.window, bg="#ABB2B9", height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg="#EAECEE", font="Helvetica 14")
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
      
        send_button = Button(bottom_label, text="Send", font="Helvetica 14", width=20, bg="#ABB2B9",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def warn():
        self._insert_message("r u there", "Sam")

    def _on_enter_pressed(self,event):
        msg = self.msg_entry.get()
        self.data(msg,"You")
        self._insert_message(msg, "You")

    def default_message(self):
        ct= str(datetime.datetime.now())
        info = {
                    'start_time':[ct],
                    'end_time':[""],
                }
        df=pd.DataFrame(info)
        df=df.dropna()
        df.to_csv('./time.csv',mode='a', index=False, header=False)
        size = len(ct)  
        time1 = int(ct[11:size-13])
        if time1>=0 and time1<12:
           message = "Admin: Hello there, Good Morning."
        elif time1>=12 and time1<18:
           message = "Admin: Hello there, Good Afternoon." 
        else:
           message = "Admin: Hello there, Good Evening." 
        message+="Currently I can assist you with admission related queries.\n\nEnter your phone no.\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, message)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

        
    
    def _insert_message(self, msg, sender):
        msg1 = f"{sender}: {msg}\n\n"
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        final_msg =get_response(msg)
        if final_msg == "Thank you for your time!":
            final_time= datetime.datetime.now()
            info = {
                    'start_time':[final_time],
                    'end_time':[""],
                }
            df=pd.DataFrame(info)
            df=df.dropna()
            df.to_csv('./time.csv',mode='a', index=False, header=False)
            
            
            
        if ((msg.isnumeric()==True and (type(int(msg)))!="<class 'str'>")) :
            phone=msg
            self.msg_entry.delete(0, END)
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(state=DISABLED)
            

            self.msg_entry.delete(0, END)
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, "Admin: Thank you! Please ask your questions!\n\n")
            self.text_widget.configure(state=DISABLED)
            playsound.playsound('./thankyou.wav', True)
        elif not msg :
            return
        else:
          self.msg_entry.delete(0, END)
          self.text_widget.configure(state=NORMAL)
          self.text_widget.insert(END, msg1)
          self.text_widget.configure(state=DISABLED)
        
          self.text_widget.configure(state=NORMAL)
          self.text_widget.insert(END, msg2)
          self.text_widget.configure(state=DISABLED)
          self.text_widget.see(END)
        
          if msg1.find('exit') != -1 or msg1.find('thank you') != -1 or msg1.find('stop') != -1:
            sleep(1.5)
            exit_button = Button(self.window, text="Exit",height= 3, width=10,command=self.window.destroy)
            exit_button.pack(pady=250) 
    
    def data(self,msg,sender):
        msg1 = f"{msg}\n\n"
        msg2 = f"{get_response(msg)}"
        nmsg1=msg1.replace("\n", "" )
        nmsg2=msg2.replace("\n", "" )

        if nmsg1.isnumeric()==False and msg2.find('clarifying')!=-1:
          msg1 = re.sub(' +', ' ', msg1)
          msg1=str(msg1)
          info = {
            'phone':[""],
            'question':[nmsg1]
          }
          df=pd.DataFrame(info)
          df.to_csv('./new_data.csv',mode='a', index=False, header=False)
        elif  msg2.find('clarifying')!=-1 and nmsg1.isnumeric()==True:
            current_time = str(datetime.datetime.now())
            lenght = len(current_time)
            time = current_time[:lenght-10]
            info = {
            'phone':[nmsg1],
            'question':[""]
            }
            df=pd.DataFrame(info)
            df.to_csv('./new_data.csv',mode='a', index=False, header=False)
            info = {
                    'phone':[nmsg1],
                    'question':[""],
                    'answer':[""],
                    'time':[time]
                }
            df=pd.DataFrame(info)
            df.to_csv('./info.csv',mode='a', index=False, header=False)
        else:
            if nmsg1.isnumeric()==True:
                msg2 = re.sub(' +', ' ', msg2)
                msg2=str(msg2)
                info = {
                    'phone':[nmsg1],
                    'question':[""],
                    'answer':[nmsg2]
                }
                df=pd.DataFrame(info)
                df.to_csv('./info.csv',mode='a', index=False, header=False)
            else:
                msg1 = re.sub(' +', ' ', msg1)
                msg1=str(msg1)
                msg2 = re.sub(' +', ' ', msg2)
                msg2=str(msg2)
                info = {
                    'phone':[""],
                    'question':[nmsg1],
                    'answer':[nmsg2]
                }
                df=pd.DataFrame(info)
                df.to_csv('./info.csv',mode='a', index=False, header=False)

if __name__ == "__main__":
    app = ChatBot()
    app.run()
