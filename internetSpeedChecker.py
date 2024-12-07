from tkinter import *
import speedtest
def speedCheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str ( round(sp.download()/(10**6),3))+" Mbps"
    up=str(round(sp.upload()/(10**6),3))+" Mbps"
    labDown.config(text=down)
    labUp.config(text=up)

sp =Tk()
sp.title("Internet Speed Test")
sp.geometry("500x520")
sp.config(bg="#ADD8E6")
lab=Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="#ADD8E6",fg="#2F4F4F")
lab.place(x=50,y=10,height="50",width="400")

lab=Label(sp,text="Download Speed",font=("Time New Roman",25,"bold"),bg="#ADD8E6",fg="#2F4F4F")
lab.place(x=50,y=110,height="50",width="400")

labDown=Label(sp,text="00",font=("Time New Roman",25,"bold"),fg="#2F4F4F")
labDown.place(x=50,y=170,height="50",width="400")


lab=Label(sp,text="Upload Speed",font=("Time New Roman",25,"bold"),bg="#ADD8E6",fg="#2F4F4F")
lab.place(x=50,y=250,height="50",width="400")

labUp=Label(sp,text="00",font=("Time New Roman",25,"bold"),fg="#2F4F4F")
labUp.place(x=50,y=310,height="50",width="400")

Button=Button(sp,text="Check Speed",font=("Time New Roman",25,"bold"),fg="#D3D3D3",relief=RAISED,bg="#800020",command=speedCheck)
Button.place(x=50,y=390,height="50",width="400")

sp.mainloop()