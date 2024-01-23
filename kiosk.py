import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

root = tk.Tk()

root.title('Kiosk')
root.geometry('700x900')
root.config(bg='#fab6fa')
root.resizable(width=False, height=False)

# image = tk.PhotoImage(file='C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\3.png')

pillow_image = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\one.png')
pillow_image = pillow_image.resize((700,200))
image = ImageTk.PhotoImage(pillow_image)

label = tk.Label(root, image = image)
label.pack()

button = tk.Button(root, text='Back', font=('inter', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=2)
button.pack(side=tk.TOP,anchor=tk.NE, padx=10, pady=10)




a1 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\two.png')
a1 = a1.resize((140,80))
image1 = ImageTk.PhotoImage(a1)

label1 = tk.Label(root, image = image1, borderwidth=1, relief='solid')
label1.place(x=225,y=260)

a2 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\three.png')
a2 = a2.resize((140,80))
image2 = ImageTk.PhotoImage(a2)

label2 = tk.Label(root, image = image2, borderwidth=1, relief='solid')
label2.place(x=390,y=260)

a3 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\four.png')
a3 = a3.resize((140,80))
image3 = ImageTk.PhotoImage(a3)

label3 = tk.Label(root, image = image3, borderwidth=1, relief='solid')
label3.place(x=550,y=260)




a4 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\5.png')
a4 = a4.resize((140,80))
image4 = ImageTk.PhotoImage(a4)

label4 = tk.Label(root, image = image4, borderwidth=1, relief='solid')
label4.place(x=225,y=360)

a5 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\six.png')
a5 = a5.resize((140,80))
image5 = ImageTk.PhotoImage(a5)

label5 = tk.Label(root, image = image5, borderwidth=1, relief='solid')
label5.place(x=390,y=360)

a6 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\seven.png')
a6 = a6.resize((140,80))
image6 = ImageTk.PhotoImage(a6)

label6 = tk.Label(root, image = image6, borderwidth=1, relief='solid')
label6.place(x=550,y=360)




a7 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\eight.png')
a7 = a7.resize((140,80))
image7 = ImageTk.PhotoImage(a7)

label7 = tk.Label(root, image = image7, borderwidth=1, relief='solid')
label7.place(x=225,y=460)

a8 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\nine.png')
a8 = a8.resize((140,80))
image8 = ImageTk.PhotoImage(a8)

label8 = tk.Label(root, image = image8, borderwidth=1, relief='solid')
label8.place(x=390,y=460)

a9 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\ten.png')
a9 = a9.resize((140,80))
image9 = ImageTk.PhotoImage(a9)

label9 = tk.Label(root, image = image9, borderwidth=1, relief='solid')
label9.place(x=550,y=460)






a10 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\eleven.png')
a10 = a10.resize((140,90))
image10 = ImageTk.PhotoImage(a10)

label10 = tk.Label(root, image = image10, borderwidth=1, relief='solid')
label10.place(x=225,y=560)

a11 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\twelve.png')
a11 = a11.resize((140,90))
image11 = ImageTk.PhotoImage(a11)

label11 = tk.Label(root, image = image11, borderwidth=1, relief='solid')
label11.place(x=390,y=560)

a12 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\thirteen.png')
a12 = a12.resize((140,90))
image12 = ImageTk.PhotoImage(a12)

label12 = tk.Label(root, image = image12, borderwidth=1, relief='solid')
label12.place(x=550,y=560)




a13 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\fourtheen.png')
a13 = a13.resize((140,90))
image13 = ImageTk.PhotoImage(a13)

label13 = tk.Label(root, image = image13, borderwidth=1, relief='solid')
label13.place(x=225,y=670)

a14 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\fiftheen.png')
a14 = a14.resize((140,90))
image14 = ImageTk.PhotoImage(a14)

label14 = tk.Label(root, image = image14, borderwidth=1, relief='solid')
label14.place(x=390,y=670)


a15 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\sixtheen.png')
a15 = a15.resize((140,90))
image15 = ImageTk.PhotoImage(a15)

label15 = tk.Label(root, image = image15, borderwidth=1, relief='solid')
label15.place(x=550,y=670)




meals = tk.Label(root, text='MEALS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
meals.place(x=40,y=275)
appe = tk.Label(root, text='APPETIZERS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
appe.place(x=10,y=375)
drinks = tk.Label(root, text='DRINKS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
drinks.place(x=40,y=475)
desserts = tk.Label(root, text='DESSERTS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
desserts.place(x=25,y=580)
snacks = tk.Label(root, text='SNACKS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
snacks.place(x=40,y=690)

placeorder = tk.Label(root, text='PLACE ORDER - DINE IN', background='#13ab40',font=('Inter', 10, 'bold'), width=700,padx=12,pady=4, anchor='w')
placeorder.place(x=0,y=780)

quantity = tk.Label(root, text='QUANTITY', background='#fab6fa',font=('Inter', 10, 'bold'),)
quantity.place(x=100,y=820)


a17 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\plus.png')
a17 = a17.resize((28,28))
image17 = ImageTk.PhotoImage(a17)

label17 = tk.Label(root, image = image17, borderwidth=0, relief='solid')
label17.place(x=120,y=850)

a18 = Image.open('C:\\Users\\Ryan Alcaraz\\Downloads\\tk_project\\Pillow\\minus.png')
a18 = a18.resize((28,28))
image18 = ImageTk.PhotoImage(a18)

label18 = tk.Label(root, image = image18, borderwidth=0, relief='solid')
label18.place(x=160,y=850)

quantity1 = tk.Label(root, text='01', background='WHITE',font=('Inter', 10, 'bold'), borderwidth=1, relief='solid',padx=12, pady=8)
quantity1.place(x=220,y=845)

button1 = tk.Button(root, text='Cancel order', font=('inter', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=26, pady=8)
button1.place(x=320,y=830)
button2 = tk.Button(root, text='Place order', font=('inter', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=26, pady=8)
button2.place(x=520,y=830)


meal1 = tk.Label(root, text='A-1 Burger with Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
meal1.place(x=225,y=342)
meal2 = tk.Label(root, text='A-2 Spaghetti with Chicken', background='#fab6fa',font=('Inter', 7, 'bold'),)
meal2.place(x=390,y=342)
meal3 = tk.Label(root, text='A3-2 piece Chicken with Mashed potato', background='#fab6fa',font=('Inter', 7, 'bold'),)
meal3.place(x=548,y=342)

appe1 = tk.Label(root, text='B1-Salad', background='#fab6fa',font=('Inter', 7, 'bold'),)
appe1.place(x=225,y=442)
appe2 = tk.Label(root, text='B2-Chicken with Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
appe2.place(x=390,y=442)
appe3 = tk.Label(root, text='B3-Bucket of Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
appe3.place(x=548,y=442)

drink1 = tk.Label(root, text='C1-Coke,Fanta,Sprite,Pepsi', background='#fab6fa',font=('Inter', 7, 'bold'),)
drink1.place(x=225,y=542)
drink2 = tk.Label(root, text='C2-Coke Float', background='#fab6fa',font=('Inter', 7, 'bold'),)
drink2.place(x=390,y=542)
drink3 = tk.Label(root, text='C3-Iced Coffee', background='#fab6fa',font=('Inter', 7, 'bold'),)
drink3.place(x=548,y=542)

dessert1 = tk.Label(root, text='D1-Apple pie', background='#fab6fa',font=('Inter', 7, 'bold'),)
dessert1.place(x=225,y=652)
dessert2 = tk.Label(root, text='D2-Cupcakes', background='#fab6fa',font=('Inter', 7, 'bold'),)
dessert2.place(x=390,y=652)
dessert3 = tk.Label(root, text='D3-Ice Cream', background='#fab6fa',font=('Inter', 7, 'bold'),)
dessert3.place(x=548,y=652)

snack1 = tk.Label(root, text='E1-Hotdot Sandwich', background='#fab6fa',font=('Inter', 7, 'bold'),)
snack1.place(x=225,y=762)
snack2 = tk.Label(root, text='E2-Fries and Nuggets', background='#fab6fa',font=('Inter', 7, 'bold'),)
snack2.place(x=390,y=762)
snack3 = tk.Label(root, text='E3-6 pieces Nuggets with Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
snack3.place(x=548,y=762)


price1 = tk.Label(root, text='₱129', background='WHITE',font=('Inter', 7, 'bold'),)
price1.place(x=335,y=265)
price2 = tk.Label(root, text='₱159', background='WHITE',font=('Inter', 7, 'bold'),)
price2.place(x=500,y=265)
price3 = tk.Label(root, text='₱201', background='WHITE',font=('Inter', 7, 'bold'),)
price3.place(x=660,y=265)

price4 = tk.Label(root, text='₱150', background='WHITE',font=('Inter', 7, 'bold'),)
price4.place(x=335,y=365)
price5 = tk.Label(root, text='₱130', background='WHITE',font=('Inter', 7, 'bold'),)
price5.place(x=500,y=365)
price6 = tk.Label(root, text='₱105', background='WHITE',font=('Inter', 7, 'bold'),)
price6.place(x=660,y=365)

price7 = tk.Label(root, text='₱90', background='WHITE',font=('Inter', 7, 'bold'),)
price7.place(x=335,y=465)
price8 = tk.Label(root, text='₱109', background='WHITE',font=('Inter', 7, 'bold'),)
price8.place(x=500,y=465)
price8 = tk.Label(root, text='₱115', background='WHITE',font=('Inter', 7, 'bold'),)
price8.place(x=660,y=465)

price9 = tk.Label(root, text='₱130', background='WHITE',font=('Inter', 7, 'bold'),)
price9.place(x=335,y=565)
price10 = tk.Label(root, text='₱100', background='WHITE',font=('Inter', 7, 'bold'),)
price10.place(x=500,y=565)
price11 = tk.Label(root, text='₱50', background='WHITE',font=('Inter', 7, 'bold'),)
price11.place(x=660,y=565)

price12 = tk.Label(root, text='₱112', background='WHITE',font=('Inter', 7, 'bold'),)
price12.place(x=335,y=675)
price13 = tk.Label(root, text='₱145', background='WHITE',font=('Inter', 7, 'bold'),)
price13.place(x=500,y=675)
price14 = tk.Label(root, text='₱120', background='WHITE',font=('Inter', 7, 'bold'),)
price14.place(x=660,y=675)


root.mainloop()



















# appetizer = tk.Label(root, text='APPETIZERS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 18, 'bold'), background='WHITE', fg='black')
# appetizer.place(x=20,y=440)