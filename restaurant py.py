from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("BILLING COUNTER")
#text_Input = StringVar()

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

##f2=Frame(root,width=300,height=700,relief=SUNKEN)
##f2.pack(side=RIGHT)Cost of Fries=140,Cost of Drinks=65,Cost of Noodles=90,Cost of Soup=140,Cost of Burger=260 

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="RESTAURANT",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)




lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#==========================================calculator========================================

##def btn(number):
##    global operator
##    operator = operator + str(numbers)
##    text_Input.set(operator)
##def btnClearDisplay():
##    global operator
##    operator=""
##    text_Input.set("")
##
##txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input, bd=30, insertwidth=4,
##                   bg="powder blue", justify='right')
##txtDisplay.grid(columnspan=4)
##
##btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2,column=0)
##
##btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2,column=1)
##
##btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2,column=2)
##Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2,column=3)
##btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3,column=0)
##btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3,column=1)
##btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3,column=2)
##Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3,column=3)
##btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4,column=0)
##btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4,column=1)
##btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4,column=2)
##Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="*", bg="powder blue", command=lambda: btnClick("*")).grid(row=4,column=3)
##btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5,column=4)
##btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="c", bg="powder blue",command=lambda:btnClearDisplay).grid(row=5,column=1)
##btnEqual=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="=", bg="powder blue").grid(row=5,column=2)
##Divison=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
##            text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5,column=3)
##
##root.mainloop()
##                                                                          
###=============
def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())


    
    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())



    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())



    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofFries =CoFries * 140
    CostofDrinks=CoD * 65
    CostofNoodles = CoNoodles* 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger* 260
    CostSandwich=CoSandwich * 300

    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich) * 0.2)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)
 
    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

lblInfo1=Label(f1,font=('helvetica',20,'bold'),text="Cost of Soup=140",fg="Black",bd=10,anchor='w')
lblInfo2=Label(f1,font=('helvetica',20,'bold'),text="Cost of Burger=260 ",fg="Black",bd=10,anchor='w')
lblInfo3=Label(f1,font=('helvetica',20,'bold'),text="Cost of Noodles=90 ",fg="Black",bd=10,anchor='w')
lblInfo4=Label(f1,font=('helvetica',20,'bold'),text="Cost of Drinks=65 ",fg="Black",bd=10,anchor='w')
lblInfo5=Label(f1,font=('helvetica',20,'bold'),text="Cost of Fries=140 ",fg="Black",bd=10,anchor='w')
lblInfo6=Label(f1,font=('helvetica',20,'bold'),text="Cost of Sandwich=300 ",fg="Black",bd=10,anchor='w')
def List():
    
    lblInfo1.grid(row=0,column=4)
   
    lblInfo2.grid(row=1,column=4)
  
    lblInfo3.grid(row=2,column=4)
    
    lblInfo4.grid(row=3,column=4)
    
    lblInfo5.grid(row=4,column=4)
 
    lblInfo6.grid(row=5,column=4)

def Dlt():
    #print("hide called")
    lblInfo1.grid_forget()
    lblInfo2.grid_forget()
    lblInfo3.grid_forget()
    lblInfo4.grid_forget()
    lblInfo5.grid_forget()
    lblInfo6.grid_forget()
   # print("Hide conmplete...:")
    
def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
    
rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f1, font=('arial', 16, 'bold'),text="Fries",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)


lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)


lblSoup= Label(f1, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="Sandwich",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=5,column=1)


lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=0)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=1)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=2)

btnList=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="PriceList",bg="powder blue",command=List).grid(row=7,column=3)

btnDlt=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Hide",bg="powder blue",command=Dlt).grid(row=7,column=4)

root.mainloop()


