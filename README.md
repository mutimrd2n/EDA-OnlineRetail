## EDA ONLINE RETAIL

Proyek ini bertujuan melakukan Exploratory Data Analysis (EDA) terhadap dataset Online Retail yang diperoleh dari Kaggle. Dataset ini berisi transaksi penjualan antara Desember 2010 hingga Desember 2011 untuk sebuah perusahaan retail di Inggris.

Analisis ini mencakup:
- Pembersihan data (Data Cleaning)
- Eksplorasi distribusi variabel penting seperti Quantity dan UnitPrice
- Deteksi outlier
- Visualisasi hubungan antar fitur
- Analisis ringkasan berdasarkan negara asal transaksi

EDA dilakukan menggunakan Python dengan pustaka Pandas, Matplotlib, dan Seaborn.
Hasil eksplorasi divisualisasikan dalam bentuk histogram, boxplot, scatter plot, heatmap, dan tabel ringkasan.

## Tujuan Proyek
- Membersihkan dataset dari nilai-nilai yang tidak valid seperti missing values dan nilai ekstrim pada Quantity dan UnitPrice.
- Memahami karakteristik distribusi Quantity dan UnitPrice dalam transaksi retail.
- Mengidentifikasi outlier yang mungkin mempengaruhi analisis.
- Mengeksplorasi korelasi antara fitur numerik seperti Quantity, UnitPrice, dan TotalPrice.
- Menemukan pola pembelian berdasarkan negara untuk memahami pasar utama.
- Menyajikan hasil eksplorasi data dalam bentuk visualisasi dan insight yang mudah dipahami.

## Dataset

Dataset yang digunakan berasal dari Kaggle:  
[Online Retail - Kaggle](https://www.kaggle.com/datasets/vijayuv/onlineretail)

Pastikan file dataset disimpan di direktori project yang sama dengan `eda_onlineretail.py`.

## Instalasi

1. Clone repositori:
   ```bash
   git clone  https://github.com/mutimrd2n/EDA-OnlineRetail.git
   cd EDA-OlineRetail
   
2. Install dependencies :
   ```bash
   pip install -r requirements.txt

3. Menjalankan Program
   ```bash
   python eda_onlineretail.py
