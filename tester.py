import pygame
import os
import random

pygame.init()
#untuk layar
tinggi_layar, lebar_layar = 600, 1100
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
kecepatan = 20
berlari = [pygame.image.load(os.path.join("Python/Tubes/Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Python/Tubes/Assets/Dino", "DinoRun2.png"))]
melompat = pygame.image.load(os.path.join("Python/Tubes/Assets/Dino", "DinoJump.png"))
menunduk = [pygame.image.load(os.path.join("Python/Tubes/Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Python/Tubes/Assets/Dino", "DinoDuck2.png"))]
berawan = pygame.image.load(os.path.join("Python/Tubes/Assets/Other", "Cloud.png"))
gurun = pygame.image.load(os.path.join("Python/Tubes/Assets/Other", "Track.png"))

kaktus_kecil = [pygame.image.load(os.path.join("Python/Tubes/Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Python/Tubes/Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Python/Tubes/Assets/Cactus", "SmallCactus3.png"))]
kaktus_besar = [pygame.image.load(os.path.join("Python/Tubes/Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Python/Tubes/Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Python/Tubes/Assets/Cactus", "LargeCactus3.png"))]
burung_jahat = [pygame.image.load(os.path.join("Python/Tubes/Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Python/Tubes/Assets/Bird", "Bird2.png"))]

class Dinosaurus:
    posisi_x = 80
    posisi_y = 310
    posisi_nuduk = 340
    mengapung = 8.5

    def __init__(self):
        self.gambar_lari = berlari
        self.gambar_lompat = melompat
        self.gambar_nunduk = menunduk

        self.dino_lari = True
        self.dino_lompat = False
        self.dino_nunduk = False

        self.indeks_langkah = 0
        self.gambar = self.gambar_lari[0]
        self.dino_hit = self.gambar.get_rect()
        self.dino_hit.x = self.posisi_x
        self.dino_hit.y = self.posisi_y
        self.diatas = self.mengapung

    def update(self, masukan):
        if self.dino_lari:
            self.lari()
        if self.dino_lompat:
            self.lompat()
        if self.dino_nunduk:
            self.nunduk()

        if self.indeks_langkah >= 10:
            self.indeks_langkah = 0

        if masukan[pygame.K_UP] and not self.dino_lompat:
            self.dino_lari = False
            self.dino_lompat = True
            self.dino_nunduk = False
        elif masukan[pygame.K_DOWN] and not self.dino_lompat:
            self.dino_lari = False
            self.dino_lompat = False
            self.dino_nunduk = True
        elif not (self.dino_lompat or masukan[pygame.K_DOWN]):
            self.dino_lari = True
            self.dino_lompat = False
            self.dino_nunduk = False

    def lari(self):
        self.gambar = self.gambar_lari[self.indeks_langkah // 5]
        self.dino_hit = self.gambar.get_rect()
        self.dino_hit.x = self.posisi_x
        self.dino_hit.y = self.posisi_y
        self.indeks_langkah += 1

    def lompat(self):
        self.gambar = self.gambar_lompat
        if self.dino_lompat :
            self.dino_hit.y -= self.diatas* 4
            self.diatas -= 0.8
        if self.diatas < - self.mengapung:
            self.dino_lompat = False
            self.diatas = self.mengapung

    def nunduk(self):
        self.gambar = self.gambar_nunduk[self.indeks_langkah // 5]
        self.dino_hit = self.gambar.get_rect()
        self.dino_hit.x = self.posisi_x
        self.dino_hit.y = self.posisi_nuduk
        self.indeks_langkah += 1

    def tampil(self, layar):
        layar.blit(self.gambar, (self.dino_hit.x, self.dino_hit.y))



class Awan:
    def __init__(self):
        self.posisi_x_awan = lebar_layar + random.randint(800, 1000)
        self.posisi_y_awan = random.randint(50, 100)
        self.gambar = berawan
        self.lebar = self.gambar.get_width()

    def update(self):
        self.posisi_x_awan -= kecepatan
        if self.posisi_x_awan < - self.lebar:
            self.posisi_x_awan = lebar_layar + random.randint(2500, 3000)
            self.posisi_y_awan = random.randint(50, 100)

    def tampil(self, layar):
        layar.blit(self.gambar, (self.posisi_x_awan, self.posisi_y_awan))


def main():
    global latar_x,latar_y,rintangan
    run = True
    user = Dinosaurus()
    waktu = pygame.time.Clock()
    cepat = kecepatan
    latar_x, latar_y = 0, 380
    awan = Awan()
    rintangan = []

    def latar():
        global latar_x,latar_y
        lebar_gambar = gurun.get_width()
        layar.blit(gurun, (latar_x, latar_y))
        layar.blit(gurun, (lebar_gambar + latar_x, latar_y))
        if latar_x <= -lebar_gambar:
            layar.blit(gurun, (lebar_gambar + latar_x, latar_y))
            latar_x = 0
        latar_x -= kecepatan 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        layar.fill((255, 255, 255))
        masukan = pygame.key.get_pressed()
        
        user.tampil(layar)
        user.update(masukan)

        latar()
        awan.tampil(layar)
        awan.update()
        
        waktu.tick(45)
        pygame.display.update()

        if len(rintangan) == 0:
            if random.randint(0, 2) == 0:
                rintangan.append(KaktusKecil(kaktus_kecil))
            elif random.randint(0, 2) == 1:
                rintangan.append(KaktusBesar(kaktus_besar))
            elif random.randint(0, 2) == 2:
                rintangan.append(Burung(burung_jahat))

        for halangan in rintangan:
            halangan.tampil(layar)
            halangan.update()
            if user.dino_hit.colliderect(halangan.hit):
                pygame.draw.rect(layar, (255, 0 , 0), user.dino_hit, 2)

main()
