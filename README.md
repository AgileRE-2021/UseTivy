
# [UseTivy](https://github.com/AgileRE-2021/UseTivy) 

<img src="https://github.com/AgileRE-2021/UseTivy/blob/master/core/static/assets/img/brand/logo_small.png" width="100" height="100">

[UseTivy](https://github.com/AgileRE-2021/UseTivy) adalah aplikasi berbasis web yang dapat melakukan generasi artefak **Activity Diagram** berdasarkan **Use Case Specification**. Use case specification bisa langsung diinputkan kedalam aplikasi, sehingga user tidak perlu melakukan *upload* file apapun. Activity diagram akan otomatis dibuat dan tersimpan pada folder tempat user melakukan *clone*
>- **Activity Diagram** pada dasarnya memiliki struktur yang mirip dengan *flowchart* atau diagram alir dalam perencanaan sistem secara terstruktur dan dibuat berdasarkan sebuah use case atau beberapa use case dalam use case diagram.
>- **Use Case Specification** merupakan salah satu artefak pengembangan software atau sistem informasi untuk menangkap fungsional dari sistem yang bersangkutan sekaligus menjelaskan interaksi yang terjadi antara Aktor dengan suatu sistem yang ada.
>
<br />

![UseTify Dashboard Page.](https://github.com/AgileRE-2021/UseTivy/blob/master/contoh_1.png)

<br />

## Table of Contents

* [Application Requirement](#aplication-requirements)
* [Cara Instalasi](#cara-instalasi)
* [Cara Penggunaan Aplikasi](#cara-penggunaan-aplikasi)
* [UI Template](#ui-template)
* [Licensing](#licensing)

## Aplication Requirements
1. [Git](https://git-scm.com/downloads)
2. [Python 3.7 or higher](https://www.python.org/downloads/)
>make sure you put your python.exe into your computer PATH 
3. Browser yang mensupport :

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

##  Cara Instalasi

> To authenticate use the default credentials ***test / ApS12_ZZs8*** or create a new user on the **registration page**.

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

Berikut adalah langkah-langkah instalasi aplikasi UseTivy:

3. Buat direktori untuk menyimpan aplikasi
   ```sh
   mkdir *nama direktori*  
   ```
4. Pastikan Anda sudah berada di dalam direktori tersebut
   ```
   cd *nama direktori*  
   ```
5. Setelah itu, buatlah _virtual environment_ pada Python 
   ```
   py -m venv env  
   ```
6. Lakukan _clone_ pada _repository_    
   ```
   git clone https://github.com/AgileRE-2021/UseTivy.git  
   ```
7. Masuk ke dalam _virtual environment_ tersebut 
   ```
   env\scripts\activate.bat  
   ```
8. Masuk ke folder aplikasi UseTivy 
   ```
   cd UseTivy  
   ```
9. Lakukan instalasi Django Framework 
   ```
   py -m pip install Django  
   ```
10. Lakukan instalasi modul - SQLite Storage 
    ```
    pip3 install -r requirements.txt  
    ```
11. Lakukan instalasi modul plantuml
    ```
    pip install plantuml  
    ```
12. Lakukan instalasi modul six
    ```
    pip install six  
    ```
13. Buat migrasi pada tabel yang ada
    ```
    python manage.py makemigrations  
    ```
    ```
    python manage.py migrate  
    ```
14. Jalankan aplikasi UseTivy (_development mode_)
    ```
    python manage.py runserver  
    ```
15. Jalankan aplikasi UseTivy (_custom port_)
    ```
    Akses aplikasi web di browser http://127.0.0.1:8000/
    ```
16. Klik Register, isikan _username_, _email_ dan _password_ kemudian klik Create Account
17.	Setelah proses pembuatan akun berhasil, klik Login. Anda akan diminta untuk mengisikan _username_ dan _password_ yang baru Anda buat, lalu klik Sign In

## Cara Penggunaan Aplikasi


## UI Template
UI template yang digunakan pada aplikasi UseTivy adalah [Argon admin template](https://github.com/creativetimofficial/argon-dashboard-django)
beberapa hal yang dapat dilihat lebih lanjut mengenai template : 
- Demo: <https://www.creative-tim.com/live/argon-dashboard-django>
- Download Page: <https://www.creative-tim.com/product/argon-dashboard-django>
- Documentation: <https://demos.creative-tim.com/argon-dashboard-django/docs/1.0/getting-started/getting-started-django.html>
- License Agreement: <https://www.creative-tim.com/license>
- Support: <https://www.creative-tim.com/contact-us>
- Issues: [Github Issues Page](https://github.com/creativetimofficial/argon-dashboard-django/issues)
## Licensing

- Copyright 2019 - present [Creative Tim](https://www.creative-tim.com/)
- Licensed under [Creative Tim EULA](https://www.creative-tim.com/license)

---
