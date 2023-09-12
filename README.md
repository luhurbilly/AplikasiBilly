* Nama : Luhur Budi Arbilianto
* Kelas : PBP B
* NPM : 2206824262

Berikut adalah tautan aplikasi Adaptable yang sudah di-deploy : **[AplikasiBilly](https://aplikasibilly.adaptable.app/main/)**.

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

# Checklist Tugas
* Membuat sebuah proyek Django baru.
    Untuk membuat sebuah projek baru Django, kita perlu mengaktifkan Virtual Environment dalam direktori yang telah dibuat. Hal tersebut dapat dilakukan dengan menuliskan kode dibawah ini di dalam terminal (MacOS)
    ```
    python -m venv env
    ```

- Membuat aplikasi dengan nama main pada proyek tersebut.
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    name sebagai nama item dengan tipe CharField.
    amount sebagai jumlah item dengan tipe IntegerField.
    description sebagai deskripsi item dengan tipe TextField.
- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
-


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.