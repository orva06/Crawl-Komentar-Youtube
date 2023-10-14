## Crawl Komentar Youtube ##

|NAMA                            | NIM       |
|:---:|:---:|
|ALVIN RENALDI NOVANZA           | 1202203346|
|MUHAMMAD RAYHAN KURNIAWAN       | 1202201259|
|ORVALAMARVA                     | 1202204249|

Alur penggunaan container NoSQL untuk crawl data / Alur pembuatan tugas 1 Big Data (??)
1. Mengambil data menggunakan API dan membuat program crawling dengan bahasa pemograman python
2. Menghubungkan python ke MongoDB Atlas
3. Menghubungkan MongoDB Atlas ke container MongoDB pada Docker
4. Membuat image dari container atau hasil crawl data yang telah dibuat
---
Berikut merupakan langkah-langkah untuk crawl data komentar suatu video youtube:

### 1. Membuat program crawling menggunakan Python ###
- Mengimport library pandas dan  library pandas untuk memanipulasi data dan build dari library googleapiclient.discovery untuk membuat objek YouTube API
- Membuat fungsi untuk mendapatkan komentar dan memproses setiap komentar. Informasi yang diambil termasuk tanggal publikasi, nama pengguna, isi komentar, dan jumlah like
- Menjalankan crawl data dengan memanggil fungsi yang telah dibuat
- Mengubah menjadi data frame menggunakan pandas agar terlihat lebih rapih
 
|Parameter       | Description
|:---:|:---:|
|API             | YouTube API untuk mengambil data
|Id Youtube      | Id video yang akan di crawl komentarnya
 

### 2. Connect python ke MongoDB Atlas ###
Menghubungkan menggunakan URI yang telah disediakan di MongoDB Atlas dan membuat objek koneksi MongoDB.
```
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri ="mongodb+srv://orvalamarva:[password]@cluster0.smm9d1p.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
```

### 3. Connect MongoDB Atlas ke Mongo pada Docker ###
- Buka CMD
- Jalankan container Mongo pada Docker
- .....
```
mongosh "mongodb+srv://cluster0.smm9d1p.mongodb.net/" --apiVersion 1 --username orvalamarva
```

### 4. Membuat image dan container dari hasil crawl ###
- Membuat file bernama "Dockerfile"
- Isi file tersebut dengan command untuk menginstall library yang dibutuhkan
- Membuat image 
```
build -t [nama image] .
```
- Membuat dan menjalankan container dengan image yang dibuat sebelumnya
```
docker run —name [nama] [nama image]
```
---
### Menampilkan hasil crawl data menggunakan container yang telah dibuat ###
Jalankan container yang telah dibuat
```
docker start [nama container]
```
Cek database
```
show [nama collections]
```
Tampilkan isi
```
db.[nama collections].find()
```

