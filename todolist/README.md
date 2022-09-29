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
  

