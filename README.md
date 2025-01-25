# Analisis Attrition Karyawan

Proyek ini adalah proyek akhir dari **Course Data Scientist** yang diselenggarakan oleh Dicoding. Proyek ini bertujuan untuk menganalisis data attrition karyawan menggunakan eksplorasi data (EDA) dan membangun model klasifikasi untuk memprediksi apakah seorang karyawan berpotensi untuk resign atau tidak.

## Data yang Digunakan

Dataset yang digunakan dalam proyek ini disediakan oleh Dicoding sebagai bagian dari pelatihan. Data mencakup informasi mengenai karakteristik karyawan, seperti umur, departemen, tingkat pendidikan, gaji, dan lain-lain, yang dapat digunakan untuk menganalisis pola attrition.

## Struktur Repositori

Berikut adalah struktur dari repositori ini:

- **output/**
  - Berisikan output dari model klasifikasi attrition.
  - Terdapat juga screenshot dashboard hasil analisis attrition.

- **notebook.ipynb**
  - Berisi eksplorasi data (EDA) dan pembuatan model klasifikasi untuk analisis attrition.

- **requirements.txt**
  - Daftar package Python yang diperlukan untuk menjalankan analisis ini.

- **prediction.py**
  - Script untuk memprediksi status attrition karyawan berdasarkan data input tertentu.

## Tools dan Teknologi

- **Python**: Digunakan untuk EDA dan pembuatan model klasifikasi.
- **Jupyter Notebook**: Untuk penulisan dan dokumentasi analisis.
- **Tableau**: Untuk membuat dashboard visualisasi hasil analisis. Dashboard yang dibuat dapat diakses di [Tableau Public](https://public.tableau.com/views/Book1_17373773351950/Dashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

## Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/analisis-attrition-karyawan.git
   ```

2. Pindah ke direktori proyek:
   ```bash
   cd analisis-attrition-karyawan
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan

1. Buka file `notebook.ipynb` di Jupyter Notebook untuk melihat analisis dan model klasifikasi.
2. Lihat hasil model dan visualisasi pada folder `output/`.

**Menjalankan Script `prediction.py`**

- Ubah data input pada bagian `data` di dalam file `prediction.py` sesuai dengan informasi karyawan yang ingin diprediksi.

- Data input harus mencakup kolom berikut:
  - `Age`, `BusinessTravel`, `DailyRate`, `Department`, `DistanceFromHome`, `Education`, `EducationField`, `EnvironmentSatisfaction`, `Gender`, `HourlyRate`, `JobInvolvement`, `JobLevel`, `JobRole`, `JobSatisfaction`, `MaritalStatus`, `MonthlyIncome`, `MonthlyRate`, `NumCompaniesWorked`, `OverTime`, `PercentSalaryHike`, `PerformanceRating`, `RelationshipSatisfaction`, `StockOptionLevel`, `TotalWorkingYears`, `TrainingTimesLastYear`, `WorkLifeBalance`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsSinceLastPromotion`, `YearsWithCurrManager`, `overall_satisfaction`, `Age_Category`, `YearsWithManagerCategory`.

- Jalankan script prediksi dengan `prediction.py` yang berisi model klasifikasi.

```bash
python prediction.py
```

## Output

1. **Model Klasifikasi**: Hasil prediksi model untuk menentukan apakah karyawan akan resign atau tidak.
2. **Dashboard Analisis**: Visualisasi interaktif untuk membantu memahami faktor-faktor utama yang berkontribusi pada attrition. Dashboard dapat dilihat di [Tableau Public](https://public.tableau.com/views/Book1_17373773351950/Dashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

## Tentang Proyek

Proyek ini dibuat sebagai bagian dari pembelajaran dan evaluasi dalam **Course Data Scientist** dari Dicoding. Dengan proyek ini, diharapkan peserta mampu mengaplikasikan kemampuan analisis data dan machine learning untuk menyelesaikan permasalahan dunia nyata.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

Jika ada pertanyaan atau masukan, silakan hubungi melalui [email](mailto:alfito.pfp@gmail.com).