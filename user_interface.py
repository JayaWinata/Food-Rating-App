import tkinter as tk

root = tk.Tk()
root.title('Penilaian Kualitas Makanan')
root.geometry('250x300')
root.resizable(False,False)
root.configure(padx=20,pady=20)

label_karbo = tk.Label(root,text='Karbohidrat')
label_karbo.grid(column=0,row=0,padx=10,pady=0,sticky=tk.W)
input_karbo = tk.Entry(root)
input_karbo.grid(column=0,row=1,padx=10,pady=5,sticky=tk.W)
tk.Label(root,text='gram').grid(column=1,row=1,padx=0,pady=5,sticky=tk.W)
blank = tk.Label(root,text='')
blank.grid(column=0,row=2)

label_pro = tk.Label(root,text='Protein')
label_pro.grid(column=0,row=3,sticky=tk.W,padx=10)
input_pro = tk.Entry(root)
input_pro.grid(row=4,column=0,padx=10,pady=5,sticky=tk.W)
tk.Label(root,text='gram').grid(column=1,row=4,padx=0,pady=5,sticky=tk.W)
tk.Label(root,text='').grid(column=0,row=5)

label_fat = tk.Label(root,text='Lemak')
label_fat.grid(column=0,row=6,sticky=tk.W,padx=10)
input_fat = tk.Entry(root)
input_fat.grid(row=7,column=0,padx=10,pady=5,sticky=tk.W)
tk.Label(root,text='gram').grid(column=1,row=7,padx=0,pady=5,sticky=tk.W)
tk.Label(root,text='').grid(column=0,row=8)

hitung_button = tk.Button(root,text='Hitung')
hitung_button.grid(row=9,column=0,pady=5,sticky=tk.W,padx=10)

root.mainloop()
