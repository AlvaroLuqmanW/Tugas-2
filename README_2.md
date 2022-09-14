# LINK
https://tugas-2-pbp-alvaroluqmanw.herokuapp.com
---
### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
>>> Virtual environment Python membantu memisahkan dan mengisolasi instalasi Python dan paket pip terkait. Hal ini memungkinkan pengguna akhir untuk menginstal dan mengelola paket mereka sendiri yang independen dari yang disediakan oleh sistem atau digunakan oleh proyek lain. Kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tertapi instalasi Python dan paket pip terkait tidak terisolasi dari sistem.
---
### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
>>> Untuk poin 1, yang saya lakukan adalah membuat fungsi yang memungkinan saya untuk render database yang sudah disediakan serta menghubungkannya juga dengan models.py. Selain itu, saya juga membuat code yang berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.
>>> Untuk poin 2, saya cukup memasukan code 'path('', show_katalog, name='show_katalog'),' ke dalam file urls.py dalam folder katalog dan kode 'path('', include('katalog.urls')), path('admin/', admin.site.urls), ' ke dalam file urls.py dalam folder project_django untuk memungkian routing.
>>> Untuk poin 3, Untuk melakukan mapping tersebut, saya menggunakan sintaks khusus template yang ada pada Django, yakni {{data}}. Saya memanggil nama variabel/atribut spesifik dari objek menggunakan for loop agar semua barang yang ada pada data base di-render pada halaman HTML.
>>> Untuk poin 4, saya cukup membuat aplikasi baru pada heroku, lalu saya hubungkan dengan repositori github saya, dan ahkirnya melakukan deployment melalui file yang telah saya push ke repositori github.
