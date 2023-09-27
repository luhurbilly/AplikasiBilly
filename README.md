* Nama : Luhur Budi Arbilianto
* Kelas : PBP B
* NPM : 2206824262

Berikut adalah tautan aplikasi Adaptable yang sudah di-deploy : **[AplikasiBilly](https://aplikasibilly.adaptable.app/main/)**.

#### TUGAS 4

## Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

    Dalam ```views.py``` yang ada di ```main```, buat fungsi baru dengan nama ```register```, ```login_user```, dan ```logout_user```. jangan lupa import beberapa hal yang dibutuhkan seperti redirect dll. kemudian membuat file html baru dengan nama ```register.html``` dan ```login.html```, file ini berguna untuk landing page saat web meredirect. Lalu, tambahkan import  fungsi-fungsi yang sudah dibuat ke ```urls.py``` di main dan jangan lupa tambahkan path ke dalam variable urlspattern.

    tambahkan kode dibawah ini tepat diatas fungsi show_main yang ada di views.py. ini berguna untuk merestriksi webpagenya, supaya main page hanya bisa diakses oleh orang yang sudah login.

    ```@login_required(login_url='/login')```

- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    Setelah kode diatas dimplementasikan, langsung buat dua akun dan mengisi item 3 item di tiap-tiap akunnya.

- Menghubungkan model Item dengan User.

    Dalam ```views.py``` di main, kita tambahkan kode ini dibagian paling atas kelas Item

    ```user = models.ForeignKey(User, on_delete=models.CASCADE)```

    kode tersebut berfungsi mengasosiasikan item dengan user. sehinggs user hanya melihat item yang ditambahkan oleh dirinya sendiri. 

- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    untuk menampilkan data sesuai dengan user yang sedang login, kita bisa melakukan request setelah tadi user dan item sudah dihubungkan. untuk menampilkan nama, di context dalam fungsi show_main, kita bisa mengubah namenya menjadi seperti ini 

    ```
    context = {
        'name': request.user.username,
    ...
    ```

    dan untuk data las login, bisa menambahkan kode ini ke context di show_main ```'last_login': request.COOKIES['last_login'],```.

    dan jangan lupa membuat tampilan pesan untuk last login di file main.html 

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

UserCreationForm adalah suatu built-in form yang disediakan untuk memudahkan proses pembuatan user dalam pengembangan web yang menggunakan Django. Kelebihan dari UserCreationForm adalah kemudahan dalam penggunaan dan integrasinya, sehingga pengembang tidak perlu menulis form dari awal. Namun, kekurangannya adalah kurangnya fleksibilitas jika kita ingin menyesuaikannya dengan kebutuhan khusus aplikasi Anda. 


## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah proses verifikasi identitas pengguna, biasanya melalui username dan password. Otorisasi adalah proses yang mengatur izin akses pengguna ke suatu resource atau action di dalam aplikasi. Keduanya penting karena untuk memastikan bahwa pengguna yang dapat mengakses sistem adalah valid, dan tingkat akses yang didapat juga sesuai

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah sebua data kecil user yang disimpan oleh device saat user masuk ke suatu web. Cookies digunakan untuk menyimpan informasi tentang pengguna seperti preferensi pengguna, riwayat dll.

Penggunaan Cookies dalam Django adalah untuk mengelola data sesi pengguna. Ketika pengguna berhasil login, Django akan membuat cookie yang berisi informasi tentang sesi pengguna, seperti ID dll. 

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

keamanan penggunaan cookies dalam pengembangan web secara default adalah tidak aman, karena cookies dapat disalahgunakan oleh pihak yang tidak bertanggung jawab untuk mengakses personal information. risiko potensial yang harus diwaspadai adalah pelacakan aktivitas user, pencurian data dll.


#### TUGAS 3

## Membuat input form untuk menambahkan objek model pada app sebelumnya.

- Buat file baru di main dengan nama ```forms.py``` , kemudian buka ```views.py``` untuk mengimport form yang telah kita buat.

- Buat fungsi dengan nama ```create_item```, yang mana berfungsi untuk menerima data.

- Tambahkan ```items = Item.objects.all()``` di fungsi show_main pada views.py. ini berfungsi untuk mengambil seluruh objek Item yang ada pada database kita

- Kemudian import fungsi yang telah kita buat ke urls.py di main dan tambahlan path urlnya ke dalam urlpatterns

- Buat file baru ```create_item.html``` dengan kode sesuai tampilan yang diinginkan di templates yang ada di main, lalu tambahkan kode di main.html yang berfungsi untuk menampilkan data yang ada dan redirect webpage ke form pagenya.

## Memmbuat fungsi untuk menampilkan data dalam berbagai format

- Buat fungsi ```show_xml``` pada ```views.py``` yang berada di main dan tambahkan path urlnya ke urlpattern. Fungsi ini digunakan untuk menampilkan data dalam format xml.

- Buat fungsi ```show_json``` pada ```views.py``` yang berada di main dan tambahkan path urlnya ke urlpattern. Fungsi ini digunakan untuk menampilkan data dalam format json.

- Buat fungsi ```show_xml_by_id``` pada ```views.py``` yang berada di main dan tambahkan path urlnya ke urlpattern. Fungsi ini digunakan untuk menampilkan data dalam format xml berdasarkan id yang kita mau.

- Buat fungsi ```show_json_by_id``` pada ```views.py``` yang berada di main dan tambahkan path urlnya ke urlpattern. Fungsi ini digunakan untuk menampilkan data dalam format json berdasarkan id yang kita mau.

## Apa perbedaan antara form POST dan form GET dalam Django?

POST dan GET berguna untuk mengirim data dari sebuah form html ke server. Namun, kedua cara ini memiliki perbedaan karakteristik. Salah satu yang paling signifikan adalah, saat kita menggunakan POST, data yang kita kirimkan berjalan secara 'tersembunyi' sehingga tidak ditampilkan pada URL. Lalu, jika mita menggunakan GET, data yang kita kirimkan ditampilkan ke siapapun yang melihat url kita. Jadi, dengan perbedaan karakteristik yang cukup signifikan, tentunya kedua cara ini memiliki kelebihan dan kekurangannya sendiri dalam kondisi tertentu

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- **XML** , sering digunakan dalam pengiriman data yang mana data yang ada biasanya cukup kompleks. Format ini sangat fleksibel untuk menampilkan berbagai macam jenis data. Namun, dengan semua kelebihannya, xml memiliki sintaks yang bisa dibilang cukup rumit.

- **JSON** , sering digunakan karena formantnya yang sederhana dan mudah dimengerti. struktur yang digunakan juga memungkinkan JSON digunakan untuk berbagai tujuan, seperti RESTful API. JSON terkenal lebih efisien dan lebih nyaman digunakan dibandingkan XML

- **HTML** , bukan format yang secara eksplisit digunakan dalam pengiriman data, namun HTML dapat digunakan dalam pengaturan tampilan data di webpage. struktur yang digunakan juga jauh lebih sederhana dari XML dan JSON

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

- JSON memiliki sintaks yang sederhana dan mudah dimengerti 

- JSON sangat cocok untuk digunakan dalam pembuatan RESTful API karena strukturnya yang ringkas dan kemudahan dalam mewakili data. 

- Overhead yang rendah dalam hal ukuran data

- JSON lebih universal dalam banyak bahasa pemrograman

- JSON adalah format yang ringkas dan penggunaannya yang efisien

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

<img src='/images/postmanhtml.png'>
<img src='/images/postmanxml.png'>
<img src='/images/postmanjson.png'>
<img src='/images/postmanxmlid.png'>
<img src='/images/postmanjsonid.png'>


#### TUGAS 2
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


## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

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