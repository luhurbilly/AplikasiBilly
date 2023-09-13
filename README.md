* Nama : Luhur Budi Arbilianto
* Kelas : PBP B
* NPM : 2206824262

Berikut adalah tautan aplikasi Adaptable yang sudah di-deploy : **[AplikasiBilly](https://aplikasibilly.adaptable.app/main/)**.

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di bawah ini secara step-by-step (bukan hanya sekadar mengikuti tutorial).

# Checklist Tugas
* Membuat sebuah proyek Django baru.

    Untuk membuat sebuah projek baru Django, kita perlu membuat Virtual Environment dalam direktori yang telah dibuat. Hal tersebut dapat dilakukan dengan menuliskan kode dibawah ini di dalam terminal (MacOS)

    ```
    python3 -m venv env
    ```

    Kemudian virtual environment diaktifkan. Hal ini bertujuan untuk *dependencies* sebuah projek supaya tidak terjadi pertukaran versi projek satu dengan projek lainnya. Virtual Environment dapat diaktifkan dengan menjalankan perintah dibawah ini.

    ```
    source env/bin/activate
    ```

    Lalu, untuk membuat sebuah projek Django diperlukan beberapa keperluan yang harus diinstall, hal tersebut bisa dilakukan dengan membuat file .txt dengan nama ```requirements.txt``` . Kemudian requirement tersebut diinstall dengan menggunakan perintah ```pip install -r requirements.txt```

    Setelah semua berhasil diselesaikan, kita baru bisa membuat projek Django kita dengan menggunakan perintah ```django-admin startproject <nama_projek> .```

    Setelah dibuat, Django dengan otomatis membuatkan file - file yang diperlukan untuk kebutuhan deployment. Namun, kita juga perlu membuat file ```.gitignore``` untuk kebutuhan pemilihan file dalam proses push git.

* Membuat aplikasi dengan nama main pada proyek tersebut.

    Setelah projek Django berhasil dibuat, kita perlu membuat aplikasi baru dalam projek tersebut, aplikasi baru tersebut bernama ```main``` . Aplikasi main bisa dibuat dengan menjalankan ```python manage.py startapp main``` pada terminal. Prosesnya tidak hanya berhenti disana, kita juga perlu mendaftarkan aplikasi main ke dalam projek dengan menambahkan ``` 'main' ``` dalam variabel ```INSTALLED_APPS``` dalam file ```settings.py``` yang ada di projek kita.

    Nah, begitulah cara mendaftarkan apliksi dengan nama main di dalam projek Django kita.

* Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

    Untuk melakukan routing, kita harus membuka file ```urls.py``` di dalam direktori projek kita , *bukan```main```* kita. Kemudian tambahkan 

    ```
     path('main/', include('main.urls')),
    ```

    ke dalam variabel ```urlpatterns``` , dengan begitu kita berhasil mengimport url aplikasi main kita, supaya aplikasi main dapat dijalankan.

* Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.

    Dalam file ```models.py``` di direktori ```main``` kita perlu membuat kelas Item, dengan ```models.Model``` sebagai class dasar. kemudian menambahkan atribut dibawah ini di dalam kelasnya

    ```name``` sebagai nama item dengan tipe ```CharField```.
    ```amount``` sebagai jumlah item dengan tipe ```IntegerField```.
    ```description``` sebagai deskripsi item dengan tipe ```TextField```.

* Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

    Dalam aplikasi ```main``` kita perlu membuka file ```views.py``` , kemudian kita membuat fungsi dengan nama ```show_main``` untuk mengatur request dan mereturn ke html kita. fungsi itu berisikan variabel yang kita perlukan , seperti nama dan kelas.

* Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

    Dalam file ```urls.py``` di ```main```,kita bisa menambahkan barisan kode ini ```path('', show_main, name='show_main'),``` ke dalam variabel ```urlpatterns``` dengan tujuan untuk menghubungkan fungsi yang terlah kita buat di ```views.py```

* Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

    Proses Deployment bisa dilakukan dengan membuat aplikasi baru pada dashboard, kemudian mengubungkan adaptable dengan repo github projek kita. Lalu, sinkronisasi pemilihan frameworks dan database.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img src='/images/nomor 2.png'>

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

- Virtual Environment sangan berguna untuk kepentingan dependensi dan untuk mengisolate projek kita supaya tidak terjadi konflik atau kebingungan pemilihan paket dalam projek. Dengan begitu, kita telah memastikan bahwa semua dependensi source kita berada dalam satu lingkup yang sama. sehingga hal ini memudahkan kita untuk melakukan proses pengembangan dan pengelolaan projek.

- Jadi, Virtual environment itu merupakan komponen penting dalam pengembangan suatu projek. Namun, kita tetap bisa membuat sebuah projek Django tanpa menggunakan virtual environment. Tetapi, hal tersebut bukan sebuah *best practice* karena dapat menimbulkan masalah - masalah yang seharusnya bisa ditangani oleh virtual environment.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    - MVC (Model-View-Controller) : 
        - Model = Mewakili data dan logika aplikasi
        - View = Mengatur tampilan aplikasi
        - Controller = Perantara Model dan View, mengatur alur aplikasi

    - MVT (Model-View-Template) :
        - Model = Mewakili data dan logika aplikasi
        - View = Mengatur tampilan aplikasi
        - Template = Mengontrol bagaimana data dari model ditampilkan di view
    
    - MVVM (Model-View-ViewModel) :
        - Model = Mewakili data dan logika aplikasi
        - View = Mengatur tampilan aplikasi
        - ViewModel = Mengelola tampilan dan sebagai perantara model dan view. 

    Perbedaan utama antara ketiga pola desain ini adalah terletak pada organisasi komponen Model, View, dan perantara antara keduanya (Controller, Template, atau ViewModel). Selain itu, pola desain ini memiliki kelebihannya sendiri di masing-masing platform. MVC sering digunakan dalam pengembangan web, MVT adalah adaptasi dari MVC yang diterapkan dalam Django, sedangkan MVVM biasanya digunakan dalam pembuatan aplikasi desktop atau mobile.