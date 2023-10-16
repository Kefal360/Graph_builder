import math
import matplotlib
matplotlib.use('TkAgg', force=True)
import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne 
from tkinter import * 
import openpyxl as op
from tkinter import ttk
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

"""
Нужно вынести логику графопостроитель в отдельный класс, который в конструктора принимает экземпляр Axes и реализует методы вроде plot, bar.
"""

class Graph:
    coords=[]
    #при создании должно быть задано уравнение, подключена таблица с данными для переменной(они идут в список)
    def __init__(self,chb,x, equal):
        self.x=x
        self.y=equal
        self.chb=chb
        
        self.y=[list(self.y[i]) for i in range(len(self.y))]
        
        #добавить создание plt объекта для набивки и создания нескольких графиков, сделать сеттер

        
          # from exel

    #задать доп настройки для графика
    
    def add_line(self,eq,lb):
        plt.axhline(eq,lb)
        
    #далее нужно вывести этот график
    def show(self,lab="f(x)",xl="x",yl="y",lt='k',lims=False ):
        #print(self.chb)
        root=Tk()

        fig =Figure(figsize=(5,4),dpi=100)#создали пустое поле для рисования
        #self.x self.y
        ax=fig.add_subplot()
        
        if self.chb==0:
            if len(self.x)>1:
               for i in range(len(self.x)):
                   n=int(f"{len(self.x)}1{i+1}")
                   
                   axes=fig.add_subplot(n)
                   axes.set_title(f"График №{i+1}")
                   c=axes.plot(self.x[i],self.y[i],label=lab,)
            else:
                line=ax.plot(self.x,self.y,label=lab,)

        else:
            if len(self.x)>1:
                #gr_lst=[]
                for i in range(len(self.x)):
                    ax.plot(self.x[i],self.y[i])
            
            else:

                line=ax.plot(self.x,self.y,label=lab,)

        ax.set_xlabel(xl)
        ax.set_ylabel(yl)
        
        # создаем холст канвас
        canvas=FigureCanvasTkAgg(fig,master=root)# переделать, сделать чтобы мастер со входа класса брался
        canvas.draw()
        toolbar=NavigationToolbar2Tk(canvas, root, pack_toolbar=False)# аналогично см window
        toolbar.update()
        canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
        canvas.mpl_connect("key_press_event", key_press_handler)

        button_quit = Button(master=root, text="Quit", command=root.destroy)
        button_quit.pack(side=BOTTOM)
        toolbar.pack(side=BOTTOM, fill=X)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        root.mainloop()






        

#####


#create one class instead 4 func?


window = Tk()
#create one button that will contain numbers of frames that we need to create



class DataFrame:
    def __init__(self, reps):
        
        window.title("Functional calculator")
        
        for i in range(reps):
            self.str_set=None
            self.data_set=None
            self.res=None
            self.show_g=None
            frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
            self.equal_entr = Entry(frame, width=30)
            #creating one more entry for f(x), if we need to draw y(x) with data that we have inside xlxs
            
            self.equal_entr.insert(END,"x")
            self.equal_entr.grid(column=1, row=1)

            self.lbl1 = Label(frame, text="Ввод выражения",font=("Arial Bold", 14))  
            self.lbl1.grid(column=0, row=1) 

            self.data_inp=Entry(frame, width=30)
            self.data_inp.insert(END,"/home/kefal/Desktop/VUZ/hw_and_labs/book.xlsx")
            self.data_inp.grid(column=1, row=3)

            self.column_label=Label(frame, text="Диапазон столбцов",font=("Arial Bold", 12))
            
            self.column_label.grid(column=2,row=2)

            self.column_inp=Entry(frame, width=10)#стлобцы
            self.column_inp.insert(END,"a,h")
            self.column_inp.grid(column=2, row=3)

            self.row_label=Label(frame,text="Диапазон строк",font=("Arial Bold", 12) )
            
            self.row_label.grid(column=3,row=2)

            self.row_inp=Entry(frame, width=10)#строки
            self.row_inp.insert(END,"1,3")
            self.row_inp.grid(column=3,row=3)


            self.lbl2 = Label(frame, text="Ввод данных",font=("Arial Bold", 12))  
            self.lbl2.grid(column=0, row=3) 

            self.fin_butt=Button(frame, text="Расчет", command=lambda: [ DataFrame.str_setup(self),DataFrame.data_setup(self), DataFrame.res_set(self),DataFrame.show_gr(self)] )  #show_gr
            self.fin_butt.grid(column=1, row=4)

            self.chvar=IntVar()
            self.chbutton=ttk.Checkbutton(text='несколько графиком в одном окне',variable=self.chvar)
            self.chbutton.pack()
            frame.pack()
        

    def str_setup(self):#setter
        self.str_set=self.equal_entr.get()
        return self.equal_entr.get()

    def chbutton_val(self):
        return self.chvar.get()

    def columnrow_set(self):
        adress=[list(map(int, self.row_inp.get().split(","))),list(map(str,self.column_inp.get().split(",")))]  # format: 1,4 A,B
        adress[1]=[x.lower() for x in adress[1]]
        adress[0]=[adress[0][0],adress[0][1]+1]
        for i in range(len(adress[1])):
            for j in self.let_num:
                if adress[1][i]==j:
                    adress[1][i]=self.let_num[j]
        return adress


    def data_setup(self):#setter

        self.let_num={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        self.num_let={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
        #path="/home/kefal/Desktop/VUZ/hw_and_labs/book.xlsx a-h 2-4" #пример пути на линухе
        if self.data_inp.get()[0]=="/" or self.data_inp.get()[0]=="C" or self.data_inp.get()[0]=="D":
            path=""
            for i in self.data_inp.get():
                if i==" ":
                    break
                else: path+=i
            

            book=op.open(path, read_only=True)
            sheet=book.active
            path=self.data_inp.get()


            # now data has format adress=[[1,2],[3,4]] all int
            
            adress=self.columnrow_set()
            data=[]
            for i in range(adress[0][0],adress[0][1]):
                temp=[]
                for j in range(adress[1][0],adress[1][1]):
                    temp.append(float(sheet[i][j].value))
                data.append(temp)
                
            self.data_set=data
            return data
        #если возвращается data , сделать возможность вывода нескольких функций на одном графике
        else:
            self.data_set=list(map(float, self.data_inp.get().split(",")))
            return list(map(float, self.data_inp.get().split(",")))
            

    def res_set(self):#setter
        x=self.data_set
        y=ne.evaluate(self.str_set)
        self.res=x,y
        return x,y
        
    def show_gr(self):#setter
        x,y=self.res
        #сделать учет того, что х может быть 2мерным массивом=>несколько прямых на одном графике
        #выбор вывода графиков : по отдельности или несколько на одном
      #this part is not working
        g=Graph(self.chbutton_val(),x, y) #тут 2 двумерных массива
        g.show(lab="f(x)",xl="x",yl="y",lt='k',lims=False )#we can create



frentry=Entry(window, width=30)
frentry.pack()
def count():
    DataFrame(int(frentry.get()))

frbutton=Button(window, text="Колво отдельных графиков", command=count  )
frbutton.pack()

window.mainloop()