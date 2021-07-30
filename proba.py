import nums_from_string
from matplotlib import pyplot as plt

podaci_lista = []

for i in range (1, 7):
    with open(f'podaci-blic-mesec-{i}.txt', 'r', encoding='utf-8') as f:
        podaci = f.read()
        print(f'U mesecu {i}. 2021. godine reč Đilas se pojavljivala {sum(nums_from_string.get_nums(podaci))} puta.')
        podaci_lista = podaci_lista + (nums_from_string.get_nums(podaci))

print(f'Od 1. januara do danas, reč Đilas ukupno je upotrebljena {sum(podaci_lista)} puta u online izdanju Blica.')

xosa = []
yosa = podaci_lista

for x in range(1, len(podaci_lista) + 1):
    xosa.append(x)

plt.plot(xosa, yosa)
plt.grid(True)
plt.tight_layout()
plt.show()