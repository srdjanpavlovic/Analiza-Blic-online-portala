import time
import requests
from bs4 import BeautifulSoup

mesec = 4  # ovde se definise za koji mesec skidamo podatke!!!

dana_u_mesecu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # ne dirati ovu listu naravno :)

# moglo je i sa .tolower elegantnije, al ajde nema veze,
# definisemo istu rec all-caps i sa pocetnim velikim za pretragu posle:

trazena_rec1 = 'Đilas'
trazena_rec2 = 'ĐILAS'

reci_na_dan = 0
info_dan = []

for dan in range(1, int(dana_u_mesecu[mesec-1]) + 1):
    for stranica in range(1, 11):
        link = (f'https://www.vesti.rs/arhiva/2021/{mesec}/{dan}/blic/{stranica}/')
        sadrzaj = BeautifulSoup(requests.get(link).content, "html.parser")
        if str(sadrzaj).count(trazena_rec1) > 0 or str(sadrzaj).count(trazena_rec2) > 0:
            print('Tražena reč detektovana!')
        reci_na_dan += str(sadrzaj).count(trazena_rec1) + str(sadrzaj).count(trazena_rec2)
        print(f'{link} : do sada pronađeno {reci_na_dan} reči u danu {dan}.')
        time.sleep(3)
    info_dan.append(str(reci_na_dan))
    print(info_dan)
    reci_na_dan = 0

with open(f'podaci-blic-mesec-{mesec}.txt', 'w', encoding='utf-8') as f:
    f.write(str(info_dan))
