## Crawling Komentar YouTube ke dalam database NoSQL ##

|NAMA                            | NIM       |
|:---:|:---:|
|ALVIN RENALDY NOVANZA           | 1202203346|
|MUHAMMAD RAYHAN KURNIAWAN       | 1202201259|
|ORVALAMARVA                     | 1202204249|

Alur pembuatan Tugas 1 Big Data - Crawling Komentar YouTube ke dalam database NoSQL:
1. Mengambil data menggunakan API dan membuat program crawling dengan bahasa pemograman python
2. Menambah command python agar dapat terhubung ke database MongoDB Atlas
3. Menghubungkan MongoDB Atlas ke container MongoDB pada Docker
4. Membuat image docker dari container atau hasil crawl data yang telah dibuat
5. Menampilkan hasil crawling data pada database NoSQL

Berikut merupakan langkah-langkah dari setiap alur diatas:

### 1. Membuat program crawling menggunakan Python ###
***File python tersedia di repository ini**
- Mengimport library pandas dan library googleapiclient untuk memanipulasi data dan build dari library googleapiclient.discovery untuk membuat objek YouTube API
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

uri ="mongodb+srv://orvalamarva:<password>@cluster0.smm9d1p.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
```

### 3. Connect MongoDB Atlas ke Mongo pada Docker ###
- Buka Command Prompt/Terminal
- Jalankan container Mongo pada Docker
```
docker start [nama-container]
```
- Masuk ke dalam container tersebut
```
docker exec -it [nama-container] bash
```
- Koneksikan server MongoDB Atlas pada terminal
```
mongosh "mongodb+srv://cluster0.smm9d1p.mongodb.net/" --apiVersion 1 --username orvalamarva
```

### 4. Membuat image dan container dari hasil crawl ###
- Membuat sebuah folder yang didalamnya terdapat file bernama "Dockerfile" dan file program python
- Pada file "Dockerfile", isi file tersebut dengan beberapa command yang dibutuhkan
```
FROM python
WORKDIR /app
# Install modul pandas
RUN pip install pandas

# Install modul googleapiclient
RUN pip install google-api-python-client

# Install modul pymongo
RUN pip install pymongo

COPY . /app
CMD ["python3", "tugasbigdata-update.py"]
```
- Jalankan terminal untuk membuat image
```
build -t [nama-image] .
```
- Membuat dan menjalankan container dengan image yang dibuat sebelumnya
```
docker run —-name [nama-container] [nama-image]
```

### 5. Menampilkan hasil crawl data menggunakan container yang telah dibuat ###
- pada terminal, jalankan container yang telah dibuat
```
docker start [nama-container]
```
- Lakukan perintah no. 3 diatas hingga dapat terkoneksi dengan MongoDB Atlas
- Cek database yang ada
```
show dbs
```
- Masuk kedalam sebuah database
```
use [nama-database]
```
- Cek collection yang terdapat pada sebuah database
```
show [nama-collections]
```
- Tampilkan isi dari collection tersebut
```
db.[nama-collection].find()
```
TARAA! Hasil crawl komentar youtube telah ditampilkan dengan menyertakan waktu publish, nama pengguna, isi komentar, dan jumlah like.

Semoga tutorial ini bermanfaat bagi teman-teman pembaca, terima kasih. ^_^
