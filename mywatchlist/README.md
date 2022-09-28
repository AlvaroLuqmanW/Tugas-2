# TUGAS 3

## Link Heroku
> https://tugas3-alvaroluqmanw-pbp.herokuapp.com/mywatchlist/

##  Jelaskan perbedaan antara JSON, XML, dan HTML!
> HyperText Markup Language, atau HTML. Ini adalah bahasa markup umum yang digunakan untuk membuat halaman web. 
Menggunakan komponen HTML, seperti tag dan atribut, memungkinkan pengembangan dan penataan bagian, paragraf, dan tautan.

> Extensible Markup Language (XML) adalah bahasa markup yang sebanding dengan HTML tetapi tidak memiliki tag bawaan. 
Sebagai gantinya, Anda membuat tag sendiri yang disesuaikan dengan kebutuhan Anda. 
Dalam format yang dapat disimpan, dicari, dan dibagikan, ini adalah cara ampuh untuk menyimpan data. 
Yang terpenting, karena struktur dasar XML terstandarisasi, penerima masih dapat mengurai data 
jika Anda mempublikasikan atau mengirimkan XML lintas sistem atau platform, baik secara lokal maupun melalui internet. Ini karena sintaks XML distandarisasi.

>Standar berbasis teks untuk pengkodean data terstruktur berdasarkan sintaks objek JavaScript disebut JavaScript Object Notation (JSON). 
Ini sering digunakan untuk transmisi data dalam aplikasi online 
(misalnya, mengirim beberapa data dari server ke klien, sehingga dapat ditampilkan di halaman web, atau sebaliknya). 
Oleh karena itu, kami menyediakan semua informasi yang Anda butuhkan dalam artikel ini untuk menangani JSON menggunakan JavaScript, 
termasuk mengurai JSON sehingga Anda dapat mengakses datanya dan menghasilkan JSON.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
> Tanpa delivery, maka semua data yang ingin kita tampilkan pada platform tersebut tidak akan muncul atau yang muncul pada platform
akan berbeda dari yang kita inginkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
> Agar saya bisa mengembalikan data mywatchlist dalam bentuk html, json, dan xml, yang pertama saya lakukan adalah membuat fungsi pada views.py
yang mengembalikan data dalam bentuk yang tertentu. Pada ahkirnya, terdapat 3 fungsi di file views.py, yang dimana masing-masing mengembalikan data dalam
bentuk html, xml, dan json. Untuk data xml, return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan 
parameter content_type="application/xml". Untuk data json, return function berupa HttpResponse yang berisi parameter data hasil query yang sudah 
diserialisasi menjadi JSON dan parameter content_type="application/json".
Setelah fungsi untuk pengembalian data telah dibuat, fungsi tersebut di import ke file urls.py agar bisa menambahkan path url untuk 
mengakses fungsi. 

## Screenshot Postman HTML
> ![HTML](/mywatchlist/Screenshot/PBP_Tugas3_html.png?raw=true "Optional Title")
## Screenshot Postman JSON
> ![JSON](/mywatchlist/Screenshot/PBP_Tugas3_json.png?raw=true "Optional Title")
## Screenshot Postman XML
> ![XML](/mywatchlist/Screenshot/PBP_Tugas3_xml.png?raw=true "Optional Title")
