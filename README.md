# Aplikasi Pilihan Ganda Berbasis Streamlit

Aplikasi ini adalah platform berbasis web untuk memfasilitasi kuis pilihan ganda. Pengguna dapat mengunggah file soal dalam format DOCX, PDF, atau TXT. Setelah file diunggah, aplikasi secara otomatis memproses soal dan menyajikannya dalam bentuk pertanyaan pilihan ganda dengan opsi A, B, C, atau D.
Setelah menjawab seluruh pertanyaan, pengguna dapat mengklik tombol <b>Submit</b> untuk melihat skor mereka dan pembenaran jawaban. Skor menunjukkan jumlah jawaban benar, sedangkan pembenaran membantu pengguna memahami jawaban yang benar untuk setiap soal.

## Features
`1.` <b>Upload File Soal:</b> Mendukung format DOCX, PDF, dan TXT.\
`2.` <b>Interaktif:</b> Menyediakan UI yang mudah digunakan untuk menjawab soal pilihan ganda.\
`3.` <b>Penilaian Otomatis:</b> Skor dihitung secara otomatis setelah pengguna mengklik tombol **Submit**..\
`4.` <b>Pembenaran Jawaban:</b> Menampilkan jawaban benar dan analisis hasil.

## Project Structure
```bash
aplikasi-pilihan-ganda/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_handler.py
│   │   └── question_parser.py
│   ├── static/
│   │   └── style.css
├── requirements.txt
└── README.md
```

## Requirements
```bash
streamlit
python-docx
```

## Question File Format
```bash
Apa alasan utama para selir dan putra-putri Prabu Siliwangi ingin menyingkirkan Putri Kandita dari istana?
A. Karena Putri Kandita sering membuat masalah di istana.
B. Karena Putri Kandita memiliki sifat jahat yang merugikan istana.
C. Karena mereka tidak suka Putri Kandita akan dijadikan penerus tahta.
D. Karena Putri Kandita mengidap penyakit yang sulit disembuhkan.
Jawaban: C
```

## How to Run
```bash
# Step 1 -> Clone repository
git clone https://github.com/username/aplikasi-pilihan-ganda.git

# Step 2 -> Navigate to project directory
cd aplikasi-pilihan-ganda

# Step 3 -> Install dependencies
pip install -r requirements.txt

# Last step -> Run the application
streamlit run app/main.py
```

## Online Access
<b>Link:</b> https://prediction-orange-quality.streamlit.app/

## MIT License
Copyright (c) 2024 Imroatu Solicah
