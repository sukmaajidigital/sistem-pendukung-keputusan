import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist

# Definisi Kriteria dan Alternatif
kriteria = ['Biaya', 'Efektivitas', 'Dampak Jangka Panjang']
alternatif = ['Promosi Digital', 'Diskon Besar']

# Matriks Perbandingan Kriteria
matriks_kriteria = np.array([
    [1, 3, 5],
    [1/3, 21, 3],
    [1/5, 1/3, 1]
])

# Matriks Perbandingan Alternatif terhadap Kriteria
matriks_alternatif = {
    'Biaya': np.array([[1, 1/5], [5, 1]]),
    'Efektivitas': np.array([[1, 3], [1/3, 1]]),
    'Dampak Jangka Panjang': np.array([[1, 7], [1/7, 1]])
}

# Fungsi Normalisasi dan Perhitungan Bobot
def normalisasi_matriks(matriks):
    return matriks / matriks.sum(axis=0)

def hitung_bobot(matriks):
    return np.mean(normalisasi_matriks(matriks), axis=1)

# Bobot Kriteria
bobot_kriteria = hitung_bobot(matriks_kriteria)
print('bobot kriteria',bobot_kriteria)
# Bobot Alternatif untuk Masing-Masing Kriteria
bobot_alternatif = {k: hitung_bobot(m) for k, m in matriks_alternatif.items()}

# Menghitung Skor Akhir Berdasarkan Bobot Kriteria
skor_akhir = np.zeros(len(alternatif))
for i, k in enumerate(kriteria):
    skor_akhir += bobot_kriteria[i] * bobot_alternatif[k]
# Menampilkan Hasil
hasil = pd.DataFrame({'Alternatif': alternatif, 'Skor': skor_akhir})
hasil.sort_values(by='Skor', ascending=False, inplace=True)
print(hasil)
