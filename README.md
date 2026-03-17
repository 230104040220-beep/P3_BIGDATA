# 📊 Big Data Dashboard - Batch Analytics & Visualization

## 📌 Deskripsi Project

Project ini merupakan implementasi **Big Data Pipeline** menggunakan PySpark untuk melakukan proses **Batch Analytics** dan menghasilkan **dashboard visualisasi** menggunakan Power BI.

Pipeline yang dibuat mencakup:

* Data Processing (PySpark)
* Analytics Layer (KPI)
* Visualization Layer (Matplotlib & Power BI)

---

## 🏗️ Arsitektur Pipeline

```
Raw Data (CSV)
      ↓
Spark Processing
      ↓
Clean Data (Parquet)
      ↓
Analytics Layer (KPI)
      ↓
Serving Layer (CSV)
      ↓
Visualization (Power BI)
```

---

## 🛠️ Tools & Teknologi

* Python
* PySpark
* Pandas
* Matplotlib
* Power BI
* VS Code
* WSL / Linux

---

## 📂 Struktur Project

```
project/
├── data/
│   ├── clean/parquet/
│   └── serving/
├── scripts/
│   ├── generate_data.py
│   ├── analytics_layer.py
│   └── visualization_layer.py
├── reports/
│   └── category_revenue.png
├── bigdata_dashboard.pbix
└── README.md
```

---

## 🚀 Cara Menjalankan Project

### 1. Generate Data

```
python scripts/generate_data.py
```

### 2. Jalankan Analytics Layer

```
python scripts/analytics_layer.py
```

### 3. Jalankan Visualization

```
python scripts/visualization_layer.py
```

---

## 📊 Output Analytics (KPI)

* Total Revenue
* Top Products
* Revenue per Category
* Average Transaction per Customer

---

## 📈 Dashboard Power BI

Dashboard menampilkan:

* KPI Total Revenue
* Grafik Top Products
* Grafik Revenue per Category

---

## 🖼️ Screenshot Dashboard

Tambahkan screenshot di sini:

```
![Dashboard](reports/dashboard.png)
```

---

## 📌 Insight

* Power BI digunakan hanya untuk visualisasi, bukan pemrosesan data
* Proses utama terjadi di Spark (Analytics Layer)
* Dashboard membantu pengambilan keputusan berbasis data

---

## ✅ Status Project

✔ Data Pipeline berhasil
✔ Analytics Layer berjalan
✔ Visualization berhasil
✔ Dashboard selesai

---

## 👨‍💻 Author

Nama: mahmudah
Mata Kuliah: Big Data

---

