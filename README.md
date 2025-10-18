# common-calculator
calculator project.
[hesap_makinesi_gui.py](https://github.com/user-attachments/files/22903258/hesap_makinesi_gui.py)
# Tkinter kütüphanesini içe aktarıyoruz. GUI (grafik kullanıcı arayüzü) için lazım.
import tkinter as tk

# ----------------------
# 1️⃣ PENCERE OLUŞTURMA
# ----------------------
# Tk() ile yeni bir pencere oluşturuyoruz
pencere = tk.Tk()
# Pencereye başlık veriyoruz.
pencere.title("💖 Hesap Makinesi 💖")
# Pencerenin boyutunu ayarlıyoruz (genişlik x yükseklik)
pencere.geometry("400x550")
# Pencerenin minimum boyutunu belirliyoruz
pencere.minsize(400, 550)
# Pencerenin arka plan rengini pastel pembe yapıyoruz
pencere.config(bg="#f7e6f2")

# ----------------------
# 2️⃣ EKRAN (ENTRY) OLUŞTURMA
# ----------------------
# Kullanıcının sayıları ve işlemleri göreceği ekranı oluşturuyoruz
ekran = tk.Entry(
    pencere,                # ekran hangi pencereye eklenecek
    font=("Helvetica", 24), # yazı tipi ve boyutu
    borderwidth=5,           # kenarlık kalınlığı
    relief="flat",           # kenarlık stili
    justify="right",         # yazıları sağa hizala
    bg="#fff0f5"             # ekranın arka plan rengi (açık pembe)
)
# Ekranı pencere içinde konumlandırıyoruz
ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# ----------------------
# 3️⃣ FONKSİYONLAR
# ----------------------
# Butona basıldığında ekranın sonuna yazıyı ekler
def tikla(sayi):
    ekran.insert(tk.END, sayi)  # ekranın sonuna sayıyı ekle

# C butonuna basınca ekranı temizler
def temizle():
    ekran.delete(0, tk.END)  # ekranın tüm içeriğini sil

# = butonuna basınca işlemi hesaplar ve sonucu ekrana yazdırır
def hesapla():
    try:
        # Ekrandaki yazıyı hesapla (örn: "7+2*3")
        sonuc = eval(ekran.get())
        # Önce ekranı temizle
        ekran.delete(0, tk.END)
        # Sonucu 10 basamak yuvarlayarak ekrana yaz
        ekran.insert(tk.END, str(round(sonuc, 10)))
    except:
        # Hata olursa ekranı temizle ve "Hata" yaz
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, "Hata")

# ----------------------
# 4️⃣ BUTON OLUŞTURMA FONKSİYONU
# ----------------------
# Butonların ortak özelliklerini buradan tanımlıyoruz
def olustur_buton(yazi, satir, sutun, renk="#ffd1dc"):
    tk.Button(
        pencere,                  # hangi pencereye eklenecek
        text=yazi,                # buton üzerindeki yazı
        font=("Helvetica", 18),   # yazı tipi ve boyutu
        width=5, height=2,        # buton boyutu
        bg=renk,                  # arka plan rengi
        fg="#4a148c",             # yazı rengi
        relief="ridge", bd=3,     # kenarlık stili ve kalınlığı
        activebackground="#ffb6c1", # tıklanınca renk değişimi
        command=lambda: tikla(yazi)  # tıklanınca hangi fonksiyon çalışacak
    ).grid(row=satir, column=sutun, padx=8, pady=8)  # butonun pencere içindeki konumu

# ----------------------
# 5️⃣ TUŞ DİZİLİMİ
# ----------------------
# Butonların yazısı ve hangi satır-sütunda olacağını tanımlıyoruz
butonlar = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3)
]

# Döngü ile tüm sayı ve işlem butonlarını oluşturuyoruz
for (yazi, satir, sutun) in butonlar:
    olustur_buton(yazi, satir, sutun)

# ----------------------
# 6️⃣ TEMİZLE VE HESAPLA BUTONLARI
# ----------------------
# C (temizle) butonu
tk.Button(
    pencere, text="C", font=("Helvetica", 18), width=11, height=2,
    bg="#ffb6c1", fg="#fff",
    command=temizle, relief="ridge", bd=3,
    activebackground="#ff9bb0"
).grid(row=5, column=0, columnspan=2, padx=8, pady=8)

# = (hesapla) butonu
tk.Button(
    pencere, text="=", font=("Helvetica", 18), width=11, height=2,
    bg="#b19cd9", fg="#fff",
    command=hesapla, relief="ridge", bd=3,
    activebackground="#d8b3ff"
).grid(row=5, column=2, columnspan=2, padx=8, pady=8)

# ----------------------
# 7️⃣ PENCEREYİ AÇIK TUTMAK
# ----------------------
# mainloop() ile pencereyi sürekli açık tutuyoruz
pencere.mainloop()
