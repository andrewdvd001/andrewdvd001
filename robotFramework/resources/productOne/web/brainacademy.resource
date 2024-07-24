*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Access brainacademy
    Go To    https://app.brainacademy.id
    Page Should Contain    Brain Academy Online

Open login page
    Click Link    Masuk/Daftar
    Page Should Contain    Yuk, daftar atau masuk sekarang.

Fill correct email
    Input Text    name=emailOrPhone    andrew.david@ruangguru.com
    Click Button    Lanjutkan
    Page Should Contain    Halo! Selamat datang kembali!
    
Fill correct password
    Input Text    name=password    adasubally
    Click Button    Masuk
    Page Should Contain    Andrew D

Fill incorrect password
    Input Text    name=password    adasubally1
    Click Button    Masuk
    Page Should Contain    Email atau password yang dimasukkan salah.
