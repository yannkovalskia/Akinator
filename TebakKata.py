import random
kata_kunci=["python", "java", "javascript", "c++", "ruby", "html", "css", "php", "swift", "kotlin"] #keywords
def tebak_kata():
    jawaban=random.choice(kata_kunci) #answer
    kesempatan=6 #chance
    for i in range(kesempatan):
        tebakan=input(f"Tebak hayo (Kamu punya: {kesempatan-i} kesempatan loh): ")
        if tebakan.lower()==jawaban:
           print("Selamat, tebakanmu benar")
           return
        else:
           print("SALAH WLEE!")
    print("jawabannya", jawaban)
while True:
    tebak_kata()
    lagi=input("Mau lagi? (y/n): ")
    if lagi.lower()!='y':
        print("Sampai jumpa lagi!")
        break
    print("Oke, kita mulai lagi!")
