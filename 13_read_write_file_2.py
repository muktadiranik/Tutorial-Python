from random import choice, shuffle

def generate_dna(length, required, percent):
    n = round(percent * length)
    fillin = list(set('GCTA') - set(required))
    dna = [choice(required) for _ in range(n)]
    dna += [choice(fillin) for _ in range(length - n)]
    shuffle(dna)
    return ''.join(dna)

generated = []
while len(generated) < 50000:
    generated.append(generate_dna(150, 'GC', 0.2))


f = open('DNA.txt', 'w')
for i in generated:
    f.write(">Numer|Human|Hearth" + "\n" + i + "\n")
f.close()

f = open('DNA.csv', 'w')
for i in generated:
    f.write(">Numer|Human|Hearth" + "," + i + "\n")
f.close()
