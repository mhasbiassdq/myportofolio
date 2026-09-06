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