
def hesapla(ekran):
    
    try:
        sonuc = eval(ekran.get())
        ekran.delete(0, "end")
        ekran.insert("end", str(round(sonuc, 10)))
    except:
        ekran.delete(0, "end")
        ekran.insert("end", "Hata")

def temizle(ekran):
    ekran.delete(0, "end")

