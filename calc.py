# -- encoding: utf-8 --
# encode as 'UTF8'
import sys , os
import time

#color
r="\033[31m"
g="\033[1;32m"
w="\033[1;37m"
c="\033[36m"
y="\033[33m"

menu = ("""
%s ╔═══════════════════════╗
 ║      %sMenu Tools  %s     ║             
 ╠═══╦═══════════════════╣
 ║%s 0 ║ Perpangkatan%s      ║
 ║%s 1 ║ Perkalian%s         ║ %sCoded By : %s~ Athien_7_Dev%s
 ║%s 2 ║ Pembagian%s         ║            
 ║%s 3 ║ Pengurangan%s       ║
 ║%s 4 ║ Pertambahan%s       ║
 ╚═══╩═══════════════════╝"""%(g,y,g,c,g,c,g,r,c,g,c,g,c,g,c,g))
print(menu)
#ini Fungsi untuk perpangkatan
def pangkat(a,b):
    return a ** b
#Ini fungsi untuk perkalian
def kali(a, b):
    return a * b
#ini fungsi untuk pembagian
def bagi(a, b):
    return a / b
#ini fungsi untuk pertambahan
def tambah(a, b):
    return a + b
#ini fungsi untuk pengurangan
def kurang(a, b):
    return a - b
#ini fungsi input soal dan hasil 
def soal():
    
    #ini untuk memilih menu
    pilih = raw_input("%s Pilih salah satu: %s"%(y,g))
    #angka 1 dan 2 untuk memasukan nilai yang ingin di hitung
    angka1 = int(input("%s masukan nilai 1 : %s"%(y,g)))
    angka2 = int(input("%s masukan nilai 2 : %s"%(y,g)))
    #fungsi ini untuk membaca pilihan dan soal yang akan di hitung
    if pilih == '0':
        a1 = pangkat(angka1,angka2)
        print(" %s pangkat(%s) = %s"%(angka1,angka2,a1))
    if pilih == '1':
        a1 = kali(angka1, angka2)
        print (" %s x %s = %s"%(angka1,angka2,a1))
    elif pilih == '2':
        a1 = bagi(angka1, angka2)
        print (" %s : %s = %s"%(angka1,angka2,a1))
    elif pilih == '3':
        a1 = kurang(angka1, angka2)
        print(" %s - %s = %s"%(angka1,angka2,a1))
    elif pilih =='4':
        a1 = tambah(angka1, angka2)
        print(" %s + %s = %s"%(angka1,angka2,a1))
    else :
        print('Pilihan yang anda maksud tidak ada di pilihan')
        soal()
    #fungsi ini untuk mengkonfirmasi apakah client ingin mencoba lagi soal yang lain
    while True:
        b = raw_input("Coba lagi ?(y/n) => ")
        if b == 'y':
            #ini untuk menghapus tampilan
            os.system("clear")
            #ini untuk menampilkan pilihan menu lagi
            print(menu)
            #ini fungsi untuk memanggil fungsi input soal dan hasil
            soal()
        elif b == 'n':
            print('Terimakasih sudah menggunakan tools kami')
            break #comand break disini untuk mengakhiri proses
        else:
            print("Masukan pilihan dengan Benar !")
soal()