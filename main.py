meme_dict = {
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").upper()
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kata itu tidak ada di dalam kamus")
