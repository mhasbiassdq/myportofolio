# Muhammad Hasbi Assiddiq - Portfolio (PBP Tugas 1)

- **NPM:** 2506624360
- **Prodi:** S1 Sistem Informasi, Universitas Indonesia
- **PWS Deployment:** http://muhammad.hasbi52.pws.cs.ui.ac.id/

## Setup

1. Clone repositori ke perangkat lokal.
2. Buat dan aktifkan *virtual environment* (`python -m venv env`).
3. Install dependensi (`pip install -r requirements.txt`).
4. Jalankan server lokal (`python manage.py runserver`).

### Tugas 1

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>` ? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat *static web*? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
   - Ya, saya menggunakan elemen semantik seperti `<section>` untuk memisahkan bagian utama halaman dan `<article>` untuk membungkus kartu konten. Elemen ini membantu menyusun struktur *static web* yang bersih, mudah dibaca, dan memudahkan pengaturan CSS secara modular.

2. Ketika Anda mengatur CSS Anda agar tetap *responsive*, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
   - Tantangan utamanya adalah menjaga agar kartu konten tidak menumpuk atau terpotong di layar HP. Masalah ini diatasi dengan *responsive grid* (`grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`) supaya tata letaknya otomatis menyesuaikan dan turun ke bawah secara vertikal pada layar kecil.

3. Website yang Anda buat saat ini adalah *static web* murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
   - Batasan utamanya adalah seluruh konten masih tertulis manual di file HTML, sehingga pembaruan data memerlukan penyuntingan kode. Pada iterasi berikutnya, saya ingin menambahkan integrasi database menggunakan Django ORM dan *admin dashboard* agar konten portofolio bisa dikelola secara dinamis.

## AI Disclosure
- **Peran AI:** AI dimanfaatkan sebagai *learning partner* atau tutor untuk berdiskusi mengenai konsep HTML/CSS, referensi perintah Git, dan struktur penulisan portofolio.
- **Keterbatasan AI:** Draf awal yang diberikan AI terkadang masih bersifat generik dan belum sepenuhnya selaras dengan struktur direktori lokal Django atau standar spesifik tata letak yang diinginkan.
- **Perbaikan & Eksekusi Manual:** Seluruh kode ditinjau ulang, diuji langsung secara mandiri lewat server lokal (`runserver`), serta disesuaikan secara manual agar akurat dengan data profil asli dan memenuhi standar rubrik penilaian.

### Tugas 2

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada *browser*. Dalam jawabanmu, jelaskan peran `urls.py` proyek, `urls.py` aplikasi, *view*, model, dan *template*.
   - Permintaan pertama diterima oleh `urls.py` level proyek, yang meneruskannya ke `urls.py` aplikasi `main` lewat `include()`. Di `main/urls.py`, path `"projects/"` dicocokkan ke *view* `show_projects`. *View* ini mengambil data lewat `Project.objects.all()`, memasukkannya ke `context`, lalu me-`render` `template` `projects.html`. Di *template*, data ditampilkan dengan perulangan `{% for %}`, dan hasil HTML-nya dikirim balik sebagai *response* ke *browser*.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam *template*? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
   - Karena kalau data ditulis langsung di *template* (*hardcoded*), setiap kali ada perubahan data saya harus edit file HTML dan deploy ulang. Kalau disimpan di model, data bisa diubah kapan saja lewat Django *admin* atau *shell* tanpa menyentuh kode *template* sama sekali, sehingga lebih mudah dipelihara dan tetap konsisten di semua halaman yang memakai data yang sama.

3. Apa perbedaan fungsi `makemigrations` dan `migrate` pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
   - `makemigrations` membuat berkas migrasi berdasarkan perubahan yang terdeteksi di model, tanpa langsung mengubah database. `migrate` menerapkan berkas migrasi itu ke database sehingga skemanya benar-benar berubah. Contohnya saat saya menambahkan model `Project` baru — setelah nulis `class Project` di `models.py`, saya jalankan `makemigrations` untuk bikin file migrasinya, lalu `migrate` supaya tabelnya benar-benar terbentuk di database dan bisa mulai diisi data.

## AI Disclosure
- **Peran AI:** AI digunakan sebagai *learning partner* untuk berdiskusi menyusun struktur model `Project`, alur *view*-*template* mengikuti pola `Experience` yang sudah ada, serta membantu menelusuri penyebab error saat pengisian data lewat *shell* (`ImportError`) dan konfigurasi `urls.py`.
- **Keterbatasan AI:** Saran awal AI perlu disesuaikan lagi dengan konvensi penamaan dan struktur proyek yang sudah saya buat sebelumnya, termasuk detail *field* model dan isi data aktual.
- **Perbaikan & Eksekusi Manual:** Menuliskan dan menjalankan mandiri perintah `makemigrations`/`migrate`, mengisi data lewat *shell*, menguji halaman lewat `runserver`, serta menulis `unit test` dan menyesuaikannya sampai seluruh test lulus.

### Tugas 3

1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!   
   - Menggunakan ModelForm jauh lebih efisien karena Django secara otomatis membuatkan elemen input HTML (beserta validasinya) berdasarkan struktur model yang sudah ada (seperti Project atau Experience). Ini menghemat waktu, mencegah penulisan kode yang berulang, dan memudahkan penyimpanan data langsung ke database. Sementara itu, {% csrf_token %} sangat diwajibkan untuk keamanan dari serangan Cross-Site Request Forgery. Token unik ini berfungsi sebagai verifikasi keamanan untuk memastikan bahwa data (POST request) yang dikirim benar-benar berasal dari pengguna di situs web kita sendiri, bukan dari script jahat di situs web lain.

2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
   - JSON (JavaScript Object Notation) lebih disukai karena sintaksnya jauh lebih ringan, ringkas, dan lebih mudah dibaca dibandingkan XML. XML cenderung boros karakter karena mengharuskan penulisan tag pembuka dan penutup di setiap data. Selain itu, JSON berakar dari JavaScript, sehingga data yang dikirim dalam format JSON bisa langsung diolah (parsing) secara native dan sangat cepat oleh sistem frontend web modern tanpa memerlukan alat konversi tambahan.

3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?
   - Alurnya dimulai ketika klien (browser/Postman) melakukan request ke endpoint URL yang telah ditentukan (contoh: /api/experience/). URL tersebut mengarahkan request ke fungsi view (seperti get_experience_json). Di dalam view, aplikasi akan melakukan query ke database (misal: Experience.objects.all()). Data yang didapat ini masih berupa QuerySet (objek kompleks bawaan Python/Django). Di sinilah proses serialization diperlukan: kita harus mengubah objek kompleks tersebut menjadi format teks (seperti string JSON) agar datanya bisa dikirim melalui jaringan internet (protokol HTTP). Setelah diubah menjadi JSON, string tersebut dibungkus menggunakan HttpResponse dengan tipe konten application/json dan dikirimkan kembali sebagai response ke klien.

## AI Disclosure
- **Peran AI:** AI digunakan sebagai pair programmer untuk berdiskusi memahami sintaks ModelForm, logika pengambilan data berdasarkan ID untuk fitur Update (penggunaan instance), serta membantu merancang struktur Pop-up Modal HTML untuk konfirmasi penghapusan data.
- **Keterbatasan AI:** Kode snippet awal yang diberikan AI seringkali menggunakan gaya styling atau kelas CSS bawaan (default) yang tidak cocok dengan desain antarmuka portofolio yang sudah saya buat di Tugas 1. AI juga kadang memberikan saran impor (import statements) yang kurang lengkap atau tidak terpakai.
- **Perbaikan & Eksekusi Manual:** Secara manual mengintegrasikan logika views.py dan forms.py agar sinkron dengan model Experience saya. Juga menulis ulang penamaan kelas CSS pada form dan modal agar menyatu mulus dengan style.css bawaan proyek saya, serta melakukan uji coba fitur Create, Update, Delete, dan pencarian (Search) langsung di server lokal dengan meminta bantuan teman.