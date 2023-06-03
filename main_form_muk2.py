import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo


# Window
window = tkinter.Tk()
window.configure(background="#089ec7")
window.geometry("400x350")
window.resizable(False,False)
window.title("Pendaftaran Mukbang")


# Variabel and Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
MAKANAN_FAVORIT = tkinter.StringVar()
MINUMAN_FAVORIT = tkinter.StringVar()
OLAHRAGA_FAVORIT = tkinter.StringVar()

def tombol_click():
    if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not MAKANAN_FAVORIT.get() or not MINUMAN_FAVORIT.get() or not OLAHRAGA_FAVORIT.get():
        showinfo(title="Error", message="Mohon lengkapi semua form!")
    else:
        pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
        showinfo(title="Selamat!", message=pesan)

# frame input
style = ttk.Style()
style.configure(style="TEntry",fieldbackground="#69868a")
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen nama lengkap
nama_depan_label = ttk.Label(input_frame,text="Nama Lengkap :")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP)
nama_depan_entry.pack(padx=10,fill="x",expand=True)


# Komponen alamat
nama_alamat_label = ttk.Label(input_frame,text="Alamat :")
nama_alamat_label.pack(padx=10,fill="x",expand=True)
nama_alamat_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH)
nama_alamat_entry.pack(padx=10,fill="x",expand=True)
# Komponen makanan favorit
makanan_fav_label = ttk.Label(input_frame, text="Makanan Favorit :")
makanan_fav_label.pack(padx=10,fill="x",expand=True)
makanan_fav_entry = ttk.Entry(input_frame, textvariable=MAKANAN_FAVORIT)
makanan_fav_entry.pack(padx=10,fill="x", expand=True)
# Komponen minuman favorit
minuman_fav_label = ttk.Label(input_frame, text="Minuman Favorit :")
minuman_fav_label.pack(padx=10,fill="x",expand=True)
minuman_fav_entry = ttk.Entry(input_frame, textvariable=MINUMAN_FAVORIT)
minuman_fav_entry.pack(padx=10,fill="x", expand=True)
# Komponen olahraga favorit
olahraga_fav_label = ttk.Label(input_frame, text="Olahraga Favorit :")
olahraga_fav_label.pack(padx=10,fill="x",expand=True)
olahraga_fav_entry = ttk.Entry(input_frame, textvariable=OLAHRAGA_FAVORIT)
olahraga_fav_entry.pack(padx=10,fill="x", expand=True)


# Button
tombol_daftar = ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.pack(fill='x',expand=True,padx=10,pady=10)


# Method
window.mainloop()