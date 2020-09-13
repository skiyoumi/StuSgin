import tkinter as tk
import time
import tkinter.messagebox
# 生成所有学生学号
schoolNumbers = []
succNumber = []
for i in range(35):
    num = "183020303"
    if i < 10:
        num = num+"0"+str(i+1)
    else:
        num = num+str(i+1)
    schoolNumbers.append(num)
# GUI界面
root=tk.Tk()
root.title("JAVA三班签到程序")
root.geometry('700x500')

# 创建签到区域
frame1 = tk.Frame(root, height=100, width=700)
frame1.pack()
lable1=tk.Label(frame1, text="请输入学生学号：")
entry = tk.Entry(frame1)
lable1.grid(row=0)
entry.grid(row=0,column=1)
def helloCallBack():
   tkinter.messagebox.askokcancel("Hello Python", "Hello Runoob")
cancelBt=tk.Button(root,text="取消",command = helloCallBack)
cancelBt.grid(row=1)

# # 创建已签到区域
frame3 = tk.Frame(root, height=400, width=350, bg='green')
frame3.pack(side="left")
#
# # 签到未签到区域
frame4 = tk.Frame(root, height=400, width=350, bg='red')
frame4.pack(side="right")

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello Runoob")
# 签到函数
def signIn(stuNum):
    times = time.strftime("%H:%M:%S")
    succStu = [stuNum, times]
    succNumber.append(succStu)
    if(schoolNumbers.index(stuNum)>0):
        del schoolNumbers[schoolNumbers.index(stuNum)]

root.mainloop()
