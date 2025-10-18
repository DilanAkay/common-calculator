import tkinter as tk
from operations import hesapla, temizle

class HesapMakinesi:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("💖 Hesap Makinesi 💖")
        self.pencere.geometry("400x550")
        self.pencere.minsize(450, 550)
        self.pencere.config(bg="#f7e6f2")

        self.ekran_olustur()
        self.butolar_olustur()
        self.temizle_hesapla_butonlari()

    def ekran_olustur(self):
        self.ekran = tk.Entry(
            self.pencere,
            font=("Helvetica", 24),
            borderwidth=5,
            relief="flat",
            justify="right",
            bg="#fff0f5",
            fg="#000000"   # ekran yazısı siyah
        )
        self.ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

    def butolar_olustur(self):
        self.butonlar = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3)
        ]
        for (yazi, satir, sutun) in self.butonlar:
            self.olustur_buton(yazi, satir, sutun)

    def olustur_buton(self, yazi, satir, sutun, renk="#ffd1dc"):
        tk.Button(
            self.pencere,
            text=yazi,
            font=("Helvetica", 18),
            width=5, height=2,
            bg=renk,
            fg="#4a148c",  # sayı ve işlem butonları mor
            relief="ridge", bd=3,
            activebackground="#ffb6c1",
            command=lambda: self.ekran.insert("end", yazi)
        ).grid(row=satir, column=sutun, padx=8, pady=8)

    def temizle_hesapla_butonlari(self):
        # C butonu (yazı siyah)
        tk.Button(
            self.pencere, text="C", font=("Helvetica", 18), width=11, height=2,
            bg="#ffb6c1", fg="#000000",  # siyah yazı
            command=lambda: temizle(self.ekran),
            relief="ridge", bd=3,
            activebackground="#ff9bb0"
        ).grid(row=5, column=0, columnspan=2, padx=8, pady=8)

        # = butonu (yazı siyah)
        tk.Button(
            self.pencere, text="=", font=("Helvetica", 18), width=11, height=2,
            bg="#b19cd9", fg="#000000",  # siyah yazı
            command=lambda: hesapla(self.ekran),
            relief="ridge", bd=3,
            activebackground="#d8b3ff"
        ).grid(row=5, column=2, columnspan=2, padx=8, pady=8)

    def run(self):
        self.pencere.mainloop()

