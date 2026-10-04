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

### Tugas 4

## AI Disclosure

Dalam mengerjakan Tugas 4 ini, saya menggunakan bantuan **Google Gemini** sebagai teman diskusi untuk membantu memecahkan masalah (*troubleshooting*) dan memahami konsep.

**Bagian yang dibantu AI:**
* **Session & Cookies:** AI membantu menjelaskan alur kerja *cookie* untuk fitur `last_login` dan cara menghapusnya saat *logout*.
* **Zona Waktu:** Membantu memperbaiki masalah perbedaan jam antara *server* dan waktu lokal dengan mengarahkan saya mengubah konfigurasi `TIME_ZONE` di `settings.py`.
* **Hak Akses (Otorisasi):** Memberi petunjuk langkah demi langkah cara membatasi akses di `views.py` menggunakan `@login_required`, serta panduan mengatur grup *Editor* melalui antarmuka Django Admin.
* **Fitur Star:** Membantu merumuskan logika relasi *database* (`ManyToManyField`) dan cara kerja *toggle star* pada *backend*.

**Strategi Prompting & Penyesuaian Manual:**
Saya menggunakan AI secara bertahap (*step-by-step*). Setiap kali menemui *error* atau kebingungan, saya memberikan *screenshot* masalah atau potongan kode saya kepada AI, lalu meminta penjelasan letak kesalahannya.

Walaupun sangat membantu, kode dari AI jarang bisa langsung di-*copy-paste* 100%. Ada beberapa penyesuaian manual yang harus saya lakukan:
* AI sering tidak tahu struktur letak file HTML saya, jadi saya harus menyesuaikan sendiri lokasi penempatan *template tag* agar tampilan web tidak berantakan.
* Sesekali ada karakter yang berlebih dari jawaban AI (seperti kelebihan tanda kurung), sehingga saya tetap harus melakukan *debugging* dan membaca ulang logika kodenya untuk memperbaiki *syntax error*.

### Tugas 5

### Jawaban Pertanyaan Reflektif

**1. Jelaskan apa itu *debouncing* dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!**
*Debouncing* adalah pola pemrograman (*design pattern*) yang digunakan untuk membatasi laju eksekusi sebuah fungsi, dengan cara memberikan jeda waktu (misalnya 500ms) setelah *event* terakhir kali dipicu. Pada fitur pencarian AJAX, teknik ini sangat esensial karena tanpa *debouncing*, *event listener* akan menembakkan *request* HTTP ke server pada setiap ketikan *keystroke*. Jika pengguna mengetik kata "Universitas", browser akan mengirim 11 *request* secara beruntun dalam hitungan milidetik. Hal ini sangat memboroskan *bandwidth*, menurunkan performa UX (karena *UI freezing*), dan berisiko memicu *bottleneck* atau *overload* pada *server*. Dengan *debouncing*, fungsi `fetch()` hanya akan dieksekusi satu kali setelah pengguna benar-benar berhenti mengetik, memastikan penggunaan *resource* yang optimal.

**2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`. Apa yang akan terjadi jika kita tidak menggunakan `await`?**
Dalam eksekusi program *asynchronous*, `fetch()` mengembalikan sebuah *Promise* (janji bahwa data akan dikembalikan di masa depan, entah berhasil atau gagal), bukan data aktual secara instan. Kata kunci `await` berfungsi untuk memberi tahu *JavaScript engine* agar menjeda eksekusi kode pada baris tersebut dan menunggu hingga *Promise* dari `fetch()` berstatus *resolved* (selesai mengambil data dari jaringan). 
Jika kita mengabaikan `await`, JavaScript yang bersifat *non-blocking* akan langsung mengeksekusi baris kode berikutnya seketika. Akibatnya, saat program mencoba memanipulasi atau merender variabel hasil `fetch()` ke dalam DOM HTML, variabel tersebut masih berstatus *Pending Promise* atau *undefined*. Hal ini akan memicu *Runtime Error* dan membuat antarmuka gagal menampilkan data JSON yang diharapkan.

**3. Jelaskan apa itu serangan XSS (*Cross-Site Scripting*) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!**
XSS (*Cross-Site Scripting*) adalah kerentanan keamanan aplikasi web di mana peretas (hacker) berhasil mengeksekusi skrip berbahaya (biasanya JavaScript) di dalam *browser* pengguna lain dengan cara menyisipkannya ke dalam basis data atau URL. 
Data yang dirender menggunakan AJAX/JavaScript (seperti menetapkan *string* ke `innerHTML`) sangat rentan karena *browser* akan membaca dan mengeksekusi *string* tersebut sebagai elemen HTML atau skrip secara mentah. Jika data mengandung payload seperti `<img src="x" onerror="alert('Hacked')">`, skrip tersebut akan langsung berjalan. Sebaliknya, *template engine* Django (`{{ variable }}`) memiliki mekanisme *auto-escaping* bawaan secara *default*. Fitur ini secara otomatis mengubah karakter-karakter khusus HTML menjadi entitas aman (contoh: `<` diubah menjadi `&lt;` dan `>` menjadi `&gt;`) sebelum dirender ke klien, sehingga *browser* hanya akan membacanya sebagai teks biasa, bukan instruksi yang dapat dieksekusi.


### AI Disclosure & Analisis Kritis Pembelajaran

Dalam penyelesaian Tugas 5 ini, saya menggunakan AI (Google Gemini) sebagai *pair-programmer*. Melalui proses ini, saya mengalami transisi pembelajaran yang signifikan dari ketergantungan pasif menuju pemanfaatan AI yang analitis, sesuai dengan prinsip *Reinforcement Sehat*.

**1. Fase Awal: Terjebak dalam Pola "Reinforcement Pasif"**
Pada awal pengerjaan, saya memposisikan AI murni sebagai **"Answer Machine"**. Saya menghindari usaha kognitif dengan langsung meminta *full code* untuk fitur AJAX dan menempelkannya (*copy-paste*) ke dalam *codebase* saya tanpa evaluasi struktural yang mendalam. Akibatnya, saya kehilangan konteks dari sistem yang saya bangun sendiri.

**2. Titik Balik (TRY & THINK): Keterbatasan Konteks AI pada Error 500**
Pendekatan pasif tersebut terbukti gagal total ketika aplikasi saya mengalami *Internal Server Error (500)*. AI, yang hanya melihat potongan kode *views* dan *template* yang saya berikan, salah mendiagnosis masalah dan terus merekomendasikan perbaikan sintaksis pada `views.py`. Karena AI tidak memiliki akses absolut (*blind spot*) terhadap keseluruhan proyek, saya terpaksa harus menghentikan ketergantungan tersebut dan mulai membedah masalah secara mandiri (Fase *Try & Think*). Saya menjalankan server lokal, menelusuri *traceback* di terminal, dan menemukan bahwa akar masalahnya adalah *dangling import* (`ImportError` fungsi `cetak_admin_pws`) yang tertinggal di `urls.py` dari Tugas 4. 

**3. Transisi ke "Learning Coach" & Perbaikan Manual (REVISE & LEARN)**
Setelah menyadari batasan AI, saya mengubah pola *prompting* saya. Alih-alih meminta kode instan, saya meminta petunjuk (*hint*), evaluasi logika, dan penjelasan konsep (Fase *Revise & Learn*). Berikut adalah integrasi dan perbaikan manual tingkat lanjut yang saya lakukan setelah berdiskusi dengan AI:
*   **Restrukturisasi UI/UX (DOM Mapping):** Logika *render* HTML DOM yang dihasilkan AI awalnya menggunakan struktur div generik yang merusak desain. Saya secara manual membedah variabel JSON tersebut dan memetakannya kembali ke dalam arsitektur kelas CSS `retro-window`, `title-bar`, dan sistem *grid* tema Y2K portofolio saya untuk memastikan konsistensi antarmuka.
*   **Layer Keamanan XSS Ganda:** AI menyarankan fungsi manipulasi Regex `escapeHTML` di sisi *client/JavaScript*. Setelah mempelajari fungsinya, saya memutuskan untuk menerapkan pertahanan ganda, yaitu membersihkan *input* di sisi *backend* menggunakan `strip_tags` pada *ModelForm* Django, sekaligus melakukan *escaping* di sisi *frontend* saat *rendering* AJAX.
*   **Integrasi Toast Dinamis:** Saya menolak menggunakan *default* `alert()` browser dari *output* mentah AI, dan memodifikasi *Promise resolver* pada `fetch()` untuk memicu komponen `showToast()` dari tutorial sebelumnya agar interaksi pengguna jauh lebih profesional.

**Kesimpulan:**
Tugas ini menyadarkan saya bahwa jika AI hanya digunakan untuk memberi jawaban tercepat, saya tidak benar-benar belajar, melainkan hanya mahir dalam merangkai pertanyaan (prompt). Memposisikan AI sebagai *Learning Coach* untuk berdiskusi, memberikan *hint*, dan memberikan umpan balik atas *trial-and-error* mandiri adalah metode paling efektif untuk membangun pemahaman yang solid.