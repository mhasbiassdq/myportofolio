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
- **Perbaikan & Eksekusi Manual:** Saya menuliskan dan menjalankan sendiri perintah `makemigrations`/`migrate`, mengisi data lewat *shell*, menguji halaman lewat `runserver`, serta menulis `unit test` dan menyesuaikannya sampai seluruh test lulus.

