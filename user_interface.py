import tkinter as tk
import fuzzy

def exit_():
    new_window.destroy()
    root.destroy()

def back():
    new_window.destroy()
    input_fat.delete(0,tk.END)
    input_karbo.delete(0,tk.END)
    input_pro.delete(0,tk.END)

def button_clicked():
    global new_window
    karbohidrat = int(input_karbo.get())
    protein = int(input_pro.get())
    lemak = int(input_fat.get())
    respon, saran = fuzzy.fuzzy_health_assessment(karbohidrat,protein,lemak)

    new_window = tk.Toplevel(root)
    new_window.title("Kualitas Makanan")
    new_window.resizable(False,False)
    new_window.configure(pady=30,padx=10)

    label_respon = tk.Label(new_window,text=respon,font=('Helvetica',12),justify='center')
    label_respon.grid(column=0,row=0,columnspan=2)
    label_saran = tk.Label(new_window,text=saran,font=('Helvetica',12),justify='center')
    label_saran.grid(column=0,row=1,pady=10,columnspan=2)
    
    label_saran.update_idletasks()
    label_width = label_saran.winfo_reqwidth()
    window_width = label_width + 20
    button_back = tk.Button(new_window,text='Kembali ke Menu Awal',command=back)
    button_back.grid(column=0,row=2,pady=20)
    button_back = tk.Button(new_window,text='Keluar',command=exit_)
    button_back.grid(column=1,row=2,pady=20,padx=10)
    new_window.geometry(f"{window_width}x200")


def main():
    global root, input_karbo, input_pro, input_fat

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

    hitung_button = tk.Button(root,text='Hitung',command=button_clicked)
    hitung_button.grid(row=9,column=0,pady=5,sticky=tk.W,padx=10)

    root.mainloop()

if __name__ == '__main__':
    main()
