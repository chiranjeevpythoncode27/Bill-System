from tkinter import *
from tkinter import messagebox
import random

































billnumber=random.randint(0,1000)
   
   
def bill_area ():
   if nameEntry.get()==''or phoneEntry.get()=="":
      messagebox.showerror("Details are Required")
   else:
      textarea.insert(END, "\t\t Welcome Customers|\n")    
      textarea.insert(END,f"\nBill Number:{billnumber}")
      textarea.insert(END,f"\nCustomer Name:{nameEntry.get()}")
      textarea.insert(END,f"\nCustomer Phone Number:{phoneEntry.get()}")
      textarea.insert(END,"\n=======================================================")
      textarea.insert(END,"Product\t\t\tQuantity\t\t\tPrice")
      textarea.insert(END,"\n=======================================================\n")
      if basmatiriceEntry.get()!="0":
         textarea.insert(END,f" Basmati Rice\t\t\t{basmatiriceEntry.get()}\t\t\t{bricevalue} Rs")
      if gopalbhogEntry.get()!="0":
         textarea.insert(END,f"   Gopal Bhog\t\t\t{gopalbhogEntry.get()}\t\t\t{gbhogvalue} Rs")

      if mixdaalEntry.get()!="0":
         textarea.insert(END,f"    Mix Daal\t\t\t{mixdaalEntry.get()}\t\t\t{mixdaalvalue} Rs")
      if malkadaalEntry.get()!="0":
         textarea.insert(END,f"   Malka Daal\t\t\t{malkadaalEntry.get()}\t\t\t{malkavalue} Rs")
      if chanadaalEntry.get()!="0":
         textarea.insert(END,f" Chana Daal \t\t\t{chanadaalEntry.get()}\t\t\t{chanavalue} Rs")
      if uraddaalEntry.get()!="0":
         textarea.insert(END,f" Urad Daal\t\t\t{uraddaalEntry.get()}\t\t\t{uradvalue} Rs")
      if milkEntry.get()!="0":
         textarea.insert(END,f" Milk\t\t\t{milkEntry.get()}\t\t\t{milkvalue} Rs")
      if curdEntry.get()!="0":
         textarea.insert(END,f"   Curd\t\t\t{curdEntry.get()}\t\t\t{curdvalue} Rs")
      if butterEntry.get()!="0":
         textarea.insert(END,f"   Butter\t\t\t{butterEntry.get()}\t\t\t{buttervalue} Rs")
      if creamEntry.get()!="0":
         textarea.insert(END,f" Cream\t\t\t{creamEntry.get()}\t\t\t{creamvalue} Rs")
      if waterEntry.get()!="0":
         textarea.insert(END,f" Water \t\t\t{waterEntry.get()}\t\t\t{watervalue} Rs")
      if drinksEntry.get()!="0":
         textarea.insert(END,f"  Cold Drink\t\t\t{drinksEntry.get()}\t\t\t{drinksvalue} Rs")
      if freshnersEntry.get()!="0":
         textarea.insert(END,f" Room Freshner\t\t\t{freshnersEntry.get()}\t\t\t{freshnersvalue} Rs")
      if spicesEntry.get()!="0":
         textarea.insert(END,f"   Spices\t\t\t{spicesEntry.get()}\t\t\t{spicesvalue} Rs")
      if nephkinesEntry.get()!="0":
         textarea.insert(END,f" Nephkines\t\t\t{nephkinesEntry.get()}\t\t\t{nephkinesvalue} Rs")
      if harpicEntry.get()!="0":
         textarea.insert(END,f"   Harpic\t\t\t{harpicEntry.get()}\t\t\t{harpicvalue} Rs")
      if papadEntry.get()!="0":
         textarea.insert(END,f"   Papad\t\t\t{papadEntry.get()}\t\t\t{papadvalue} Rs")
      if haldiEntry.get()!="0":
         textarea.insert(END,f"   Haldi\t\t\t{haldiEntry.get()}\t\t\t{haldivalue} Rs")
      textarea.insert(END, "\n-------------------------------------------------------")
      
      textarea.insert(END,f"\nTotal Cost\t\t\t\t\t\t{totalprice}Rs")
      textarea.insert(END,"\n------------------------------------------------------")
        
 
 

def total():
   global bricevalue, gbhogvalue,mixdaalvalue,mixdaalvalue,chanavalue,uradvalue,milkvalue,curdvalue,creamvalue,buttervalue,watervalue,drinksvalue,freshnersvalue,spicesvalue,nephkinesvalue,harpicvalue,haldivalue,papadvalue,malkavalue,totalprice,send_email 
   bricevalue=int(basmatiriceEntry.get())*100
   gbhogvalue=int(gopalbhogEntry.get())*80
   mixdaalvalue=int(mixdaalEntry.get())*130
   malkavalue=int(malkadaalEntry.get())*120
   chanavalue=int(chanadaalEntry.get())*150
   uradvalue=int(uraddaalEntry.get())*160
   milkvalue=int(milkEntry.get())*55
   curdvalue=int(curdEntry.get())*60
   buttervalue=int(butterEntry.get())*100
   creamvalue=int(creamEntry.get())*150
   watervalue=int(waterEntry.get())*20
   drinksvalue=int(drinksEntry.get())*40
   freshnersvalue=int(freshnersEntry.get())*200
   spicesvalue=int(spicesEntry.get())*50
   nephkinesvalue=int(nephkinesEntry.get())*30
   harpicvalue=int(harpicEntry.get())*90
   papadvalue=int(papadEntry.get())*40
   haldivalue=int(haldiEntry.get())*30

   totalprice=bricevalue+gbhogvalue+mixdaalvalue+chanavalue+uradvalue+milkvalue+buttervalue+curdvalue+creamvalue+watervalue+drinksvalue+freshnersvalue+spicesvalue+nephkinesvalue+harpicvalue+papadvalue+haldivalue
   totalButtonEntry.insert(0,totalprice)  






root=Tk()
root.title(" Billing System")
root.geometry("1270x685")

headingLabel=Label(root,text =" Suyal General Store Billing System",font=("times new roman", 30,"bold")
                   ,bg= "gray20", fg= "gold",bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame (root,text="Customer Details" ,font=("times new roman",15,"bold")
                                   ,fg="gold",bd=8,relief=GROOVE,bg="gray20")
customer_details_frame.pack(fill=X,pady=10)

nameLabel=Label(customer_details_frame, text= "Name",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame, text= "Phone Number",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8,pady=8)

billnumberLabel=Label(customer_details_frame, text= "Bill Number",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8,pady=8)

searchButton=Button(customer_details_frame,text="Search",font=("arial",12,"bold"),bd=7, width=10)
searchButton.grid(row=0, column=6, padx=20 ,pady=8)

ProductsFrame=Frame(root)
ProductsFrame.pack(pady=2)

riceFrame=LabelFrame(ProductsFrame,text="Rice, Wheat and Pulses",font=("times new roman",15,"bold"),bg="gray20",fg= "Gold",relief=GROOVE)
riceFrame.grid(row=0,column=0)

basmatiriceLabel=Label(riceFrame,text= "Basmati Rice",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
basmatiriceLabel.grid(row=0,column=0,pady=9)

basmatiriceEntry =Entry(riceFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
basmatiriceEntry.grid (row =0,column=1, pady=9)
basmatiriceEntry.insert(0,0)

gopalbhogLabel=Label(riceFrame,text= "Gopal Bhog",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
gopalbhogLabel.grid(row=1,column=0)
gopalbhogEntry =Entry(riceFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
gopalbhogEntry.grid (row =1,column=1, pady=9)
gopalbhogEntry.insert(0,0)

mixdaalLabel=Label(riceFrame,text= "Mix daal",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
mixdaalLabel.grid(row=2,column=0,)
mixdaalEntry =Entry(riceFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
mixdaalEntry.grid (row =2,column=1, pady=9)
mixdaalEntry.insert(0,0)


malkadaalLabel=Label(riceFrame,text= "Malka daal",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
malkadaalLabel.grid(row=3,column=0,)
malkadaalEntry =Entry(riceFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
malkadaalEntry.grid (row =3,column=1, pady=9)
malkadaalEntry.insert(0,0)


chanadaalLabel=Label(riceFrame,text= "Chana daal",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
chanadaalLabel.grid(row=4,column=0,)
chanadaalEntry =Entry(riceFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
chanadaalEntry.grid (row =4,column=1, pady=9)
chanadaalEntry.insert(0,0)


uraddaalLabel=Label(riceFrame,text= "Urad daal",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
uraddaalLabel.grid(row=5,column=0,)
uraddaalEntry =Entry(riceFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
uraddaalEntry.grid (row =5,column=1, pady=9 ,padx=10)
uraddaalEntry.insert(0,0)


dairyFrame=LabelFrame(ProductsFrame,text="Dairy Products and Cold Drinks ",font=("times new roman",15,"bold"),bg="gray20",fg= "Gold",relief=GROOVE)
dairyFrame.grid(row=0,column=1, padx=5)

milkLabel=Label(dairyFrame,text= "Milk",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
milkLabel.grid(row=0,column=0,)

milkEntry =Entry(dairyFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
milkEntry.grid (row =0,column=1, pady=9, padx=10)
milkEntry.insert(0,0)


curdLabel=Label(dairyFrame,text= "Curd",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
curdLabel.grid(row=1,column=0,)

curdEntry =Entry(dairyFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
curdEntry.grid (row= 1,column=1, pady=9, padx=10)
curdEntry.insert(0,0)


butterLabel=Label(dairyFrame,text= "Butter",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
butterLabel.grid(row=2,column=0,)

butterEntry =Entry(dairyFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
butterEntry.grid (row =2,column=1, pady=9, padx=10)
butterEntry.insert(0,0)




creamLabel=Label(dairyFrame,text= "Cream",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
creamLabel.grid(row=3,column=0,)

creamEntry =Entry(dairyFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
creamEntry.grid (row =3,column=1, pady=9, padx=10)
creamEntry.insert(0,0)

waterLabel=Label(dairyFrame,text= "Water",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
waterLabel.grid(row=4,column=0,)

waterEntry =Entry(dairyFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
waterEntry.grid (row =4,column=1, pady=9, padx=10)
waterEntry.insert(0,0)


drinksLabel=Label(dairyFrame,text= "Cold Drinks",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
drinksLabel.grid(row=5,column=0,)

drinksEntry =Entry(dairyFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
drinksEntry.grid (row =5,column=1, pady=9, padx=10)
drinksEntry.insert(0,0)


groceryFrame=LabelFrame(ProductsFrame,text="Grocery Products ",font=("times new roman",15,"bold"),bg="gray20",fg= "Gold",relief=GROOVE)
groceryFrame.grid(row=0,column=2, padx=5)

freshnersLabel=Label(groceryFrame,text= "Room Freshners",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
freshnersLabel.grid(row=0,column=0)

freshnersEntry =Entry(groceryFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
freshnersEntry.grid (row= 0,column=1, pady=9, padx=10)
freshnersEntry.insert(0,0)

spicesLabel=Label(groceryFrame,text= "Sabji Masala ",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
spicesLabel.grid(row=1,column=0)

spicesEntry =Entry(groceryFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
spicesEntry.grid (row= 1,column=1, pady=9, padx=10)
spicesEntry.insert(0,0)

nephkinesLabel=Label(groceryFrame,text= "Nephkines",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
nephkinesLabel.grid(row=2,column=0)

nephkinesEntry =Entry(groceryFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
nephkinesEntry.grid (row= 2,column=1, pady=9, padx=10)
nephkinesEntry.insert(0,0)

harpicLabel=Label(groceryFrame,text= "Harpic",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
harpicLabel.grid(row=3,column=0)

harpicEntry =Entry(groceryFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
harpicEntry.grid (row= 3,column=1, pady=9, padx=10)
harpicEntry.insert(0,0)

papadLabel=Label(groceryFrame,text= "Papad",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
papadLabel.grid(row=4,column=0)

papadEntry =Entry(groceryFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
papadEntry.grid (row= 4,column=1, pady=9, padx=10)
papadEntry.insert(0,0)

haldiLabel=Label(groceryFrame,text= "Haldi Masala",font=("times new roman",15,"bold"),bg="gray20",fg= "White")
haldiLabel.grid(row=5,column=0)

haldiEntry =Entry(groceryFrame, font=("times new roman",15,"bold"),width=10,bd=5,)
haldiEntry.grid (row= 5,column=1, pady=9, padx=10)
haldiEntry.insert(0,0)


billframe=Frame(ProductsFrame , bd=8,relief= GROOVE)
billframe.grid(row=0,column=3)

billareaLabel=Label(billframe,text="Label area ", font=("times new roman",15,"bold"))
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)



textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


buttonFrame=Frame(ProductsFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=6 ,column=3)

totalButton=Button(buttonFrame,text="Total",font=("arial",16,"bold"), bg="gray20", fg="white", bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0, pady=5,padx=5)


totalButtonEntry =Entry(ProductsFrame, font=("times new roman",20,"bold"),width=25,bd=12,)
totalButtonEntry.grid (row= 7,column=3, pady=15, padx=10)





clearButton=Button(buttonFrame,text="Clear",font=("arial",16,"bold"), bg="gray20", fg="white", bd=5,width=8,pady=10)
clearButton.grid(row=0,column=1,pady=5,padx=5)

billButton=Button(buttonFrame,text="Bill",font=("arial",16,"bold"), bg="gray20", fg="white", bd=5,width=8,pady=10, command= bill_area)
billButton.grid(row=0,column=2,pady=5,padx=5)

mailButton=Button(buttonFrame,text="Print",font=("arial",16,"bold"), bg="gray20", fg="white", bd=5,width=8,pady=10,)
mailButton.grid(row=0,column=3,pady=5,padx=5)


root.mainloop()
   