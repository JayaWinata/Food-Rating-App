def fuzzy_health_assessment(karbohidrat,protein,lemak):

    sehat = min(karbohidrat / 100.0, protein / 50.0, lemak / 70.0)
    cukup_sehat = max(min((karbohidrat - 50.0) / 30.0, (protein - 25.0) / 15.0), 0.0)
    perlu_diperhatikan = max(min((karbohidrat - 80.0) / 20.0, (lemak - 40.0) / 10.0), 0.0)

    nilai_kesehatan = (sehat * 0.7 + cukup_sehat * 0.4 + perlu_diperhatikan * 0.1) / (0.7+0.4+0.1)

    respon = ''
    if nilai_kesehatan >= 0.7:
        respon = "Kualitas makanan sangat baik."
    elif nilai_kesehatan >= 0.4:
        respon = "Kualitas makanan cukup Baik."
    else:
        respon = "Kualitas makanan buruk."

    saran = ''
    if karbohidrat > 60.0 and protein < 30.0:
        saran = "Perbanyak protein untuk keseimbangan nutrisi harian Anda!."
    elif lemak > 40.0:
        saran = "Kurangi kadar lemak pada makanan Anda!"
    else:
        saran = "Tetap pertahankan kualitas makanan Anda!"
    
    return (respon,saran)
