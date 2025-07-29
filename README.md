# tokopedia-ai-assistant

# Tokopedia AI Assistant

AI Assistant sederhana untuk membantu seller Tokopedia menganalisis data penjualan dan performa toko secara otomatis. Assistant ini juga bisa menjawab pertanyaan seputar penjualan toko lewat dashboard web interaktif.

## Fitur

- Analisis penjualan, order, dan rating toko otomatis.
- Memberikan insight dan saran singkat dari AI.
- Bisa tanya-jawab langsung dengan AI soal performa toko.
- Dashboard web sederhana dan mudah digunakan.

## Cara Menjalankan

1. **Pastikan sudah install Python dan pip di komputer.**
2. **Clone atau download semua file project ini ke komputer.**
3. **Buat virtual environment baru:**
python -m venv venv

markdown
Salin
Edit
Aktifkan virtual environment:
- **Windows:**  
  ```
  venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```
  source venv/bin/activate
  ```
4. **Install semua dependency Python yang dibutuhkan:**
pip install -r requirements.txt

markdown
Salin
Edit
5. **Masukkan API Key Hugging Face ke dalam file `config.py`.**
6. **Jalankan aplikasi:**
python run.py

markdown
Salin
Edit
7. **Buka browser ke alamat:**  
[http://localhost:8501](http://localhost:8501)

## Catatan

- Project ini hanya contoh dan menggunakan data simulasi.
- Bisa dikembangkan atau dihubungkan ke data asli Tokopedia.
- Silakan modifikasi sesuai kebutuhan.
