from gensim.models import KeyedVectors

kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)

def benzerKelimeler():

    anahtarKelime = []
    anahtarKelime.append(input("1. Anahtar Kelime: ").lower())
    anahtarKelime.append(input("2. Anahtar Kelime: ").lower())
    anahtarKelime.append(input("3. Anahtar Kelime: ").lower())
    print("Anahtar Kelime : "+ str(anahtarKelime))
    oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
    print(oneriler)

benzerKelimeler()

