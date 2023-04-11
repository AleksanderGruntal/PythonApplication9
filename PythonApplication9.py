import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((440,480))
ekraani_pind.fill((0,220,0))
pygame.display.set_caption("Ülesanne 2,Aleksander")


pilt=pygame.image.load("haha.png")
ekraani_pind.blit(pilt,(0,0))


kaka=pygame.Rect(200,100,200,100)
pygame.draw.ellipse(ekraani_pind,(0,0,0),kaka)
lill=pygame.Rect(250,210,50,50)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill)
lill4=pygame.Rect(250,140,80,80)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill4)
lill1=pygame.Rect(250,250,20,20)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill1)
lill2=pygame.Rect(250,265,10,10)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill2)

font=pygame.font.SysFont("Broadway",20)
sõnad="Aleksander!"
värv=[250,250,250]
teksti_lisamine=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisamine,(235,130))


pilt=pygame.image.load("snail.png")
ekraani_pind.blit(pilt,(80,250))

kaka=pygame.Rect(210,285,10,10)
pygame.draw.ellipse(ekraani_pind,(250,100,33),kaka)



pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: #функцмя для кнопки "выход" (крест)
        break
pygame.quit()
