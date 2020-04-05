import pygame
import time

white=(255,255,255)
black=(100,100,100)
color1=(200,250,200)
red=(255,0,0)

img=pygame.image.load("reset.jpg")
img=pygame.transform.scale(img,(200,200))

def text_objects(text,font,color):
     textSurface=font.render(text,True,color)
     return textSurface,textSurface.get_rect()

def message_display(text="",pos=(0,0),size=60,space='',color=color1):#pos=(x,y) top left pointer, size=font size
     Ltext=pygame.font.Font('freesansbold.ttf',size)
     text=space+text
     textSurf,textRect=text_objects(text,Ltext,color)
     textRect=pos
     gameDisplay.blit(textSurf,textRect)
     pygame.display.update()

def tipe(t=10):
     name=''
     start=int(time.time())
     while True:
            x=int(time.time()-start)
            if x >= t:
                 return name
            pygame.draw.rect(gameDisplay,black,(0,200,1200,100))
            for evt in pygame.event.get():
                if evt.type == pygame.KEYDOWN:
                    if evt.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == pygame.K_RETURN:
                        name = ""
                    elif evt.key == pygame.K_SPACE:
                         name=name+" "
                    elif evt.unicode : #.isalpha():
                        name += evt.unicode
                elif evt.type == pygame.QUIT:
                    return
            message_display(name,(0,200),30)
            message_display("time : "+str(x),(0,250),20)
     
pygame.init()
display_width=1200
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Typing krke chand pr jaega kya")

def game():     
     while True:
          intro=True
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
          message_display("TYPING MASTER PRO",(200,50),60)
          task="Face the dark or stay forever in it."
          message_display(task,(150,150),30,color=white)
          name=tipe()# what the banda typed
          if len(name)<len(task):
               name=name+"*"*(len(task)-len(name))
          count=0
          for i in range(len(task)):
               if task[i]==name[i]:
                    count+=1

          acc=(count/len(task))*100
          acc="%.2f"%acc
          #print("accuracy  : %s"%acc)
          pygame.draw.rect(gameDisplay,black,(0,250,1200,40))
          message_display("TIME's UP",(0,250),40,color=red)
          message_display("accuracy : "+str(acc)+"%",(250,250),40,color=red)
          gameDisplay.blit(img,((display_width/2)-100,350))
          
          pygame.display.update()

          while intro:
               for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                         pygame.quit()
                         quit()
               
               mouse=pygame.mouse.get_pos()
               click=pygame.mouse.get_pressed()
               x,y=mouse[0],mouse[1]
               #print(mouse)               
               if display_width/2<x<display_width/2+200 and 350<y<350+200 and click==(1,0,0):
                    print('************')
                    intro=False     

game()
# add a reset button. lvl is back to 0 if reset is pressed. 
# add levels. banda moves to next lvl for each success.
