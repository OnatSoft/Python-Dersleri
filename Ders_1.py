# x = 2
# print(x)
# print(type(x))
# a = 'Onat Somer'
# print(a)
# print(type(a))

# sayi_1 = int(input('Birinci sayıyı giriniz: '))
# sayi_2 = int(input('İkinci sayıyı giriniz: '))

# toplam = sayi_1 + sayi_2

# print(f'Toplam: {toplam}')
# print('Toplam: ', toplam)


# ==================== Dikdörtgenin Alan ve Çevresini Hesaplama ====================
# kisa_kenar = float(input('Kısa Kenar: '))
# uzun_kenar = float(input('Uzun kenar: '))

# --> Alternatif Yöntem
# alan = kisa_kenar * uzun_kenar
# cevre = 2 * (kisa_kenar + uzun_kenar)

# print(f'Alan Sonucu: {kisa_kenar * uzun_kenar}')
# print(f'Çevre Sonucu: {2 * (kisa_kenar + uzun_kenar)}')


# ==================== Karar Mekanizmaları ====================
# a = int(input('Birinci sayı: '))
# c = int(input('İkinci sayı: '))

# if a > c:
#     print(f'{a} sayısı büyüktür.')
# elif a < c:
#     print(f'{c} sayısı büyüktür.')
# elif a == c:
#     print(f'İki sayı birbirine eşit.')
# else:
#     print(f'Sayı bulunamadı lütfen bir sayı değerleri giriniz.')


# x = int(input('Tam sayı: '))

# if x % 2 == 0:
#     print(f'{x} çifttir.')
# else:
#     print(f'{x} tektir.')


# product = input('Aradığınız ürünü girin: ')

# if product == 'telefon' or product == 'tablet' or product == 'bilgisayar':
#     print('Teknoloji mağazasına git.')
# elif product == 'şampuan' or product == 'diş macunu' or product == 'katı sabun':
#     print('Kozmetik mağazasına git.')
# elif product == 'dergi' or product == 'kitap' or product == 'ansiklopedi':
#     print('Kitapçıya git.')
# else:
#     print('Aradığınız ürün bulunmamaktadır. Başka bir ürün giriniz.')


# username = input('User Name: ')
# password = input('Password: ')

# if username == 'onat' and password == '123':
#     print('Hoşgeldiniz! ' + username)
# else:
#     print('Kullanıcı adı veya parola hatalı girildi.')


# --> İç İçe if Kullanımı
# vehicle = input('Araç Türü Giriniz: ')
# speed = int(input('Hız: '))

# if speed > 0:
#     if vehicle == 'otomobil':
#         if speed >= 70:
#             print('Cezalısın!')
#         else:
#             print('Ceza yok!')
#     elif vehicle == 'kamyon':
#         if speed >= 50:
#             print('Cezalısın!')
#         else:
#             print('Ceza yok!')
#     elif vehicle == 'motosiklet':
#         if speed >= 70:
#             print('Cezalısın!')
#         else:
#             print('Ceza yok!')
#     else:
#         print('Lütfen uygun bir araç türü giriniz.')
# else:
#     print('Araç hızı sıfırdan küçük olamaz.')


# --> Aralık Kontrolü
# kitapSayisi = int(input('Kitap Sayısı: '))

# if kitapSayisi >= 1 and kitapSayisi <= 10:  # 1 <= kitapSayisi <= 10:
#     print(f'Ödenecek Toplam Tutar: {kitapSayisi * 5 * 0.90}')
# elif kitapSayisi >= 11 and kitapSayisi <= 15:
#     print(f'Ödenecek Toplam Tutar: {kitapSayisi * 5 * 0.85}')
# elif kitapSayisi >= 16 and kitapSayisi <= 20:
#     print(f'Ödenecek Toplam Tutar: {kitapSayisi * 5 * 0.80}')
# elif kitapSayisi >= 21 and kitapSayisi <= 25:
#     print(f'Ödenecek Toplam Tutar: {kitapSayisi * 5 * 0.75}')
# else:
#     print('Lütfen doğru kitap sayısı giriniz!')


# ============ Match-Case Kullanımı ==============
# Match-Case, metinsel ifadeleri performanslı ve daha hızlı şekilde 
# karşılaştırmak için kullanılıyor.

mevsim = input('Mevsim girin: ')

match mevsim:
    case 'kış':
        print('Aralık-Ocak-Şubat')
    case 'sonbahar':
        print('Eylül-Ekim-Kasım')
    case 'ilkbahar':
        print('Mart-Nisan-Mayıs')
    case 'yaz':
        print('Haziran-Temmuz-Ağustos')
    case _:
        print('Böyle bir mevsim yok.')


# ==================== Excaption Handling (TRY-CATCH) ====================

# try: 
#     bolen = int(input('Bölen: '))
#     bolunen = int(input('Bölünen: '))

#     sonuc = bolunen / bolen

#     print(f'Sonuc: {sonuc}')
# except ZeroDivisionError as err:
#     print('HATA: Sayı 0 ile bölünemez.', err)
# finally:
#     print(f'Hata olsa da olmasa da Finally komutu çalışıyor.')


# ==================== Döngüler ====================
# while - for - foreach















