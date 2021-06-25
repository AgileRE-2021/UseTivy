
# [UseTivy](https://github.com/AgileRE-2021/UseTivy) 
<br />
<p align="center">
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/core/static/assets/img/brand/logo_small.png" width="100" height="100">
</p>
<br />


[UseTivy](https://github.com/AgileRE-2021/UseTivy) adalah aplikasi berbasis web yang dapat melakukan generasi artefak **Activity Diagram** berdasarkan **Use Case Specification**. Use case specification bisa langsung diinputkan kedalam aplikasi, sehingga user tidak perlu melakukan *upload* file apapun. Activity diagram akan otomatis dibuat dan tersimpan pada folder tempat user melakukan *clone*
>- **Activity Diagram** pada dasarnya memiliki struktur yang mirip dengan *flowchart* atau diagram alir dalam perencanaan sistem secara terstruktur dan dibuat berdasarkan sebuah use case atau beberapa use case dalam use case diagram.
>- **Use Case Specification** merupakan salah satu artefak pengembangan software atau sistem informasi untuk menangkap fungsional dari sistem yang bersangkutan sekaligus menjelaskan interaksi yang terjadi antara Aktor dengan suatu sistem yang ada.

<br />
<br />

![UseTify Dashboard Page.](https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/contoh_1.png)

<br />

## Table of Contents

* [Application Requirement](#aplication-requirements)
* [Cara Instalasi](#cara-instalasi)
* [Cara Penggunaan Aplikasi](#cara-penggunaan-aplikasi)
* [UI Template](#ui-template)
* [Developer](#developer)

## Aplication Requirements
1. [Git](https://git-scm.com/downloads)
2. [Python 3.7 or higher](https://www.python.org/downloads/)
>make sure you put your python.exe into your computer PATH 
3. Browser support :

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

##  Cara Instalasi

Berikut adalah langkah-langkah instalasi aplikasi UseTivy:

1. Buat direktori untuk menyimpan aplikasi
   ```sh
   mkdir *nama direktori*  
   ```
2. Pastikan Anda sudah berada di dalam direktori tersebut
   ```
   cd *nama direktori*  
   ```
3. Setelah itu, buatlah _virtual environment_ pada Python 
   ```
   py -m venv env  
   ```
4. Lakukan _clone_ pada _repository_    
   ```
   git clone https://github.com/AgileRE-2021/UseTivy.git  
   ```
5. Masuk ke dalam _virtual environment_ tersebut 
   ```
   env\scripts\activate.bat  
   ```
6. Masuk ke folder aplikasi UseTivy 
   ```
   cd UseTivy  
   ```
7. Lakukan instalasi Django Framework 
   ```
   py -m pip install Django  
   ```
8. Lakukan instalasi modul - SQLite Storage 
    ```
    pip3 install -r requirements.txt  
    ```
9. Lakukan instalasi modul plantuml
    ```
    pip install plantuml  
    ```
10. Lakukan instalasi modul six
    ```
    pip install six  
    ```
11. Buat migrasi pada tabel yang ada
    ```
    python manage.py makemigrations  
    ```
    ```
    python manage.py migrate  
    ```
12. Jalankan aplikasi UseTivy (_development mode_)
    ```
    python manage.py runserver  
    ```
13. Jalankan aplikasi UseTivy (_custom port_)
    ```
    Akses aplikasi web di browser http://127.0.0.1:8000/
    ```
14. Klik Register, isikan _username_, _email_ dan _password_ kemudian klik Create Account
15.	Setelah proses pembuatan akun berhasil, klik Login. Anda akan diminta untuk mengisikan _username_ dan _password_ yang baru Anda buat, lalu klik Sign In

## Cara Penggunaan Aplikasi
1. Register : Buat akun jika belum ada
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/register.PNG">
2. Login : Login untuk Masuk ke dalam aplikasi
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/login.PNG">
3. Dashboard : Setelah login user akan diarahkan ke Halaman ini. Halaman ini berisikan informasi projek yang baru dibuat.
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/dashboard.PNG">
4. New Project : Untuk membuat projek pilih button 'New Project' yang ada di halaman dashboard. Setelah itu user dapat memasukan nama projecknya.
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/new_projek.PNG">
5. Usecase : Setelah membuat projek user akan diarahkan ke Halaman ini dengan cara memilih button 'Usecase' yang ada pada halaman dashboard. Halaman ini berisikan informasi usecase yang baru dibuat.
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/usecase.PNG">
6. Add New Usecase : Pertama, user dapat membuat usecase sesuai dengan keinginan.
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/add_usecase.PNG">
7. Edit Usecase : lalu user dapat melakukan pengisian form yang berisikan deskripsi usecase, Precondition, Postcondition, Basic step. 
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/edit_usecase.PNG">
8. Basic Step : user dapat mengisi basic step untuk menjelaskan langkah-langkah yang terjadi pada usecase.
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/basic_step.PNG">
9. Usecase View : halaman ini berisikan informasi yang telah di-inputkan pada halaman 'Edit Usecase' seperti deskripsi usecase, Precondition, Postcondition, Basic step.
<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/readme_asset/usecase_view.PNG">

## UI Template
UI template yang digunakan pada aplikasi UseTivy adalah [Argon admin template](https://github.com/creativetimofficial/argon-dashboard-django)
beberapa hal yang dapat dilihat lebih lanjut mengenai template : 
- Demo: <https://www.creative-tim.com/live/argon-dashboard-django>
- Download Page: <https://www.creative-tim.com/product/argon-dashboard-django>
- Documentation: <https://demos.creative-tim.com/argon-dashboard-django/docs/1.0/getting-started/getting-started-django.html>
- License Agreement: <https://www.creative-tim.com/license>
- Support: <https://www.creative-tim.com/contact-us>
- Issues: [Github Issues Page](https://github.com/creativetimofficial/argon-dashboard-django/issues)

## Developer
*UseTivy dibangun oleh mahasiswa S1 Sistem Informasi Universitas Airlangga*
- Bramantio Ghani S.	081811633005
- Aulia Marcha R. P	081811633016
- Hafidh Yanuar P.	081811633034
- Zhafira Hajar	081811633035
- Corine Stafanie	081811633040
- M. Najib Wafirur R.	081811633042
- Rizki Agung Mahendra	081811633045
- Ghalib Atthallah Alam	081811633056

---
<h2 align="center"> -------S1 Sistem Informasi - Universitas Airlangga - 2021------- </h2>
<br/>
