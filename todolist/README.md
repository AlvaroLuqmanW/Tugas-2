# TUGAS 4

## LINK HEROKU
> https://tugas-alvaroluqmanw-pbp.herokuapp.com/todolist/login/
## Akun Pengguna Tersedia:
> Username: Kurus, Password: Labby123
> 
> Username: Luqman, Password: 123Labby

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
> Django menampilkan token csrf yang digunakan untuk mencegah serangan qwebsite. Saat membuat halaman di server, 
itu menghasilkan token dan memastikan bahwa setiap request yang masuk kembali diperiksa silang terhadap token ini. 
Token tidak termasuk dalam request yang masuk; dengan demikian mereka tidak dieksekusi. Halaman tersebut akan mengalami error jika metod form yang digunakan
adalah POST dan tidak mencantum {% csrf_token %} pada file html.
  
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
> Kita dapat membuat elemen <form> secara manual. Hal ini biasa dilakukan untuk membuat form sebagaimanapun kita mau dengan beberapa efek CSS.
  Hal ini bisa kita lakukan dengan membuat file baru dalam folder app kita bernama forms.py. Dalam file tersebut, kita mampu membuat form custom kita sendiri.
  
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
> Setelah data diinput dalam form dan si submisi, maka akan dicheck terlebih dahulu jika method request adalah POST atau GET. Dalam kasus ini karena method yang digunakan
  adalah POST, maka akan dicheck lagi jika data yang dimasukan ke dalam field sesuai. Jika sesuai, maka data tersebut akan diambil dan disimpan ke dalam variabel,
  dan dengan variabel tersebut kita gunakan untuk create object baru pada model Task dan kemudian di save. Setelah di save, maka akan kembali ke halaman utama dan
  data tersebut akan ditampilkan.
  
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
> Untuk halaman create-text, saya menggunakan method POST sehingga pada file html tersebut harus tercantum {% csrf_token %} agar tidak menyebabkan error. Kemudian,
  saya menggunakan form manual untuk menerima data 'title' dan 'description' untuk membuat object Task baru dengan atribut tersebut. Setelah di buat, maka saya save form
  agar data tersebut tersimpan dalam database, dan bisa ditampilkan di halaman web todolist utama.
  
# TUGAS 5
  
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
> CSS internal mengharuskan kita untuk menambahkan tag <style> di bagian <head> dokumen HTML.
Gaya CSS ini adalah metode yang efektif untuk menata satu halaman. Namun, menggunakan gaya ini untuk beberapa halaman memakan waktu karena Anda perlu menempatkan aturan CSS di setiap halaman situs web. Kelebihan dari internal CSS adalah kita dapat menggunakan class dan ID selector dalam file html yang sama, sehingga kita tidak perlu mengunggah banyak file. Kekurangan dari internal CSS adalah menambahkan kode ke file HTML dapat meningkatkan ukuran halaman dan waktu pemuatan.

> Dengan CSS external, kita mampu menautkan halaman web kita ke file .css external, yang dapat dibuat oleh editor teks apa pun di perangkat kita, seperti Notepad++.
Jenis CSS ini adalah metode yang lebih efisien, terutama untuk menata situs web besar. Dengan mengedit satu file .css, kita dapat mengubah seluruh situs sekaligus. Kelebihan dari CSS external adalah karena kode CSS berada dalam file terpisah, file HTML akan memiliki struktur yang lebih bersih dan ukurannya lebih kecil, sehingga kita dapat menggunakan file .css yang sama untuk beberapa halaman. Kekurangannya adalah halaman web mungkin tidak dirender dengan benar hingga CSS eksternal dimuat.
Mengunggah atau menautkan ke beberapa file CSS dapat meningkatkan waktu pengunduhan situs Anda.
  
> Inline CSS digunakan untuk menata elemen HTML tertentu. Untuk gaya CSS ini, kita hanya perlu menambahkan atribut gaya ke setiap tag HTML, tanpa menggunakan penyeleksi. Jenis CSS ini sangat tidak disarankan, karena setiap tag HTML perlu ditata secara individual. Mengelola situs web Anda mungkin menjadi terlalu sulit jika kita hanya menggunakan CSS sebaris. Namun, CSS sebaris dalam HTML dapat berguna dalam beberapa situasi. Misalnya, dalam kasus di mana kita tidak memiliki akses ke file CSS atau perlu menerapkan gaya untuk satu elemen saja. Kelebihan dari CSS Inline adalah kita dapat dengan mudah dan cepat memasukkan aturan CSS ke halaman HTML. Itulah mengapa metode ini berguna untuk menguji atau melihat pratinjau perubahan, dan melakukan perbaikan cepat pada situs web. Kita tidak perlu membuat dan mengunggah dokumen terpisah seperti pada gaya eksternal. Kekurangannya adalah menambahkan aturan CSS ke setiap elemen HTML memakan waktu dan membuat struktur HTML Anda berantakan. Menata beberapa elemen dapat memengaruhi ukuran halaman dan waktu pengunduhan.
  
## Jelaskan tag HTML5 yang kamu ketahui.
> <p>  </p> adalah paragraf tag html. Tag ini memformat teks apa pun antara tag <p> pembuka dan tag </p> penutup sebagai paragraf standar atau teks isi utama.
> <h2>  </h2> adalah heading tag html. Menggunakan tag ini akan memformat teks apa pun antara tag pembuka <h2> dan tag penutup </h2> sebagai heading 2.
> <b>  </b> adalah bold tag html. Tag ini akan memformat teks apa pun antara tag pembuka <b> dan tag penutup </b> sebagai huruf tebal.
  
## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
>CSS element selector: Element selector memilih elemen HTML berdasarkan nama elemen.
> CSS ID Selector: ID selector menggunakan atribut ID dari elemen HTML untuk memilih elemen tertentu. ID dari sebuah elemen unik dalam sebuah halaman, jadi pemilih id digunakan untuk memilih satu elemen unik. Untuk memilih elemen dengan id tertentu, tulis karakter hash (#), diikuti dengan id elemen.
> CSS class Selector: Class selector memilih elemen HTML dengan atribut kelas tertentu. Untuk memilih elemen dengan kelas tertentu, tulis karakter titik (.), diikuti dengan nama kelas.
> CSS Universal Selector: Universal selector (*) memilih semua elemen HTML pada halaman.
  
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
> Untuk men-design halaman todolist saya, saya menggunakan internal dan inline CSS sebagai pilihan style saya karena lebih mudah. Saya menggunakan beberapa tipe-tipe CSS selector juga seperti element, grouping dan class selector untuk semua elemen html saya.
