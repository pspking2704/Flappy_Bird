import pygame
import random
from pygame import mixer

class Bird:
    def __init__(self):
        pygame.init()
        self.xScreen = 500
        self.yScreen = 600
        linkBackground = "./work/background.jpg"
        self.linkImgBird = "./work/bird.png"
        self.screen = pygame.display.set_mode((self.xScreen, self.yScreen))
        pygame.display.set_caption("Flappy from Nam")
        self.background = pygame.image.load(linkBackground)
        self.gamerunning = True
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)
        # Khoi tao Bird
        self.xSizeBird = 80
        self.ySizeBird = 60
        self.xBird = self.xScreen/3
        self.yBird = self.yScreen/2
        self.VBirdUp = 70
        self.VBirdDown = 7
        # Khoi tao cot
        self.xColunm = self.yScreen + 250
        self.yColunm = 0
        self.xSizeColunm = 100
        self.ySizeColunm = self.yScreen
        self.VColunm = 6
        self.ColunmChange = 0

        # Khoi tao diem
        self.score = 0 
        self.checkLost = False

    
    # Ham chay am thanh
    def music(self,url):
        Sound = mixer.Sound(url)
        Sound.play()
    # Ham xuat hinh anh
    def img_draw(self, url, xLocal, yLocal,xImg,yImg):
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(PlanesImg,(xImg,yImg))
        self.screen.blit(PlanesImg, (xLocal,yLocal))
    
    # Ham xuat diem
    def show_score(self,x,y,score,size):
        font = pygame.font.SysFont("coman.......", size)
        score = font.render(str(score),True,(255,255,255))
        self.screen.blit(score,(x,y))
    
    # Ham colunm
    def colunm(self):
        marginColunm = 80
        yColunmCahngeTop =  -self.ySizeColunm/2 - marginColunm + self.ColunmChange   
        yColunmCahngeBotom  = self.ySizeColunm/2 + marginColunm +self.ColunmChange
         

    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            self.image_draw(self.linkImgBird, self.xBird,self.yBird, self.xSizeBird, self.ySizeBird)
                                                                                                            

if __name__ == '__main__':
    bird = Bird()
    bird.run()
    