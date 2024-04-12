meme_dict = { 
            "LOL" - "tanggapan terhadap sesuatu yang lucu",
            "CRINGE" - "sesuatu yang aneh atau memalukan",
            "ROFL" - "tanggapan terhadap lelucon",
            "SHEESH" - "sedikit ketidaksetujuan",
            "CREEPY" - "menakutkan, tidak menyenangkan",
            "AGGRO" - "untuk menjadi agresif/marah"
            }
word = input("Ketik kata yang tidak kamu mengerti (gunakan huruf kapital semua!):")

if word in meme_dict.keys():
    print('makna kata:', meme_dict.[word])
else:
    print('Kata tidak ditemukan')
