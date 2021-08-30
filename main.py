import keyboard
from pygame import *
import time
from button import *
class App():
    def __init__(self):

        self.l = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#
        self.sc = display.set_mode((700,700))

        self.y = 50
        self.x = 0
        self.colliders = []
        self.size = (100,100)

        self.main_lavels = Button(self.sc,size=(100,50), path="1.png",text="Играть", pos=(300, 325))
        self.to_left = Button(self.sc, size=(50, 70), path="1.png", text="<", pos=(550, 400))
        self.to_right = Button(self.sc, size=(50, 70), path="1.png", text=">", pos=(550, 550))
        self.to_up = Button(self.sc, size=(50, 70), path="1.png", text="|", pos=(100, 400))
        self.to_down = Button(self.sc, size=(50, 70), path="1.png", text="|", pos=(100, 550))
        self.step = 1
        self.left = 0
        self.vector = 0
        self.main_font = font.Font(None, 36)

        while True:
            for e in event.get():  # Обрабатываем события
                if e.type == QUIT:
                    quit()
                self.main_lavels.update(e)

                self.main_lavels.update_show()


            if self.main_lavels.get_value():
                break
            display.update()

        while True:



            #print(event.get())



            self.update()
            display.update()

    def to_main_lavels(self):
        print(123)
    def update(self):
        #time.sleep(1/100)
        self.sc.fill((0,0,0))

        for i in range(30):
                for j in range(30):
                    if self.l[i][j] == 1:
                        draw.rect(self.sc, (255, 255, 255),
                                  (j * self.size[0] - self.x, i * self.size[1] - self.y, self.size[0], self.size[1]))
            #display.update()
        
        for e in event.get():  # Обрабатываем события
            #print(e)
            if e.type == QUIT:
                quit()


            #elif e.type == KEYDOWN:

            elif self.to_right.get_value():
                #print(self.to_right.get_value())
                self.vector = 1#
            elif self.to_down.get_value():


                self.vector = 2
            elif self.to_left.get_value():

                self.vector = 3
            elif self.to_up.get_value():

                self.vector = 4
            self.to_right.update(e)
            self.to_left.update(e)

            self.to_down.update(e)
            self.to_up.update(e)
            #self.test.update_show()


        self.to_right.update_show()
        self.to_left.update_show()
        self.to_down.update_show()
        self.to_up.update_show()
    #print(int(self.x/50)+6*50)



        try:
            draw.rect(self.sc, (0, 255, 0), (350 ,350, self.size[0], self.size[1]))
            #if keyboard.is_pressed("s") and self.l[int((self.y + 350 + self.size[1]) / self.size[1])][
            #    int((self.x + 350) / self.size[0])] != 1 and self.l[int((self.y + 350 + self.size[1]) / self.size[1])][
            #    int((self.x + 349 + self.size[0]) / self.size[0])] != 1:
            #    self.hor = 1
            #if keyboard.is_pressed("w") and self.l[int((self.y + 349) / self.size[1])][
                #int((self.x + 350) / self.size[0])] != 1 and self.l[int((self.y + 349) / self.size[1])][
                #int((self.x + 349 + self.size[1]) / self.size[0])] != 1:
                #self.y -= 1
            #if keyboard.is_pressed("d") and self.l[int((self.y + 350) / self.size[1])][
                #int((self.x + 350 + self.size[0]) / self.size[0])] != 1 and \
                #    self.l[int((self.y + 349 + self.size[1]) / self.size[1])][
                #        int((self.x + 350 + self.size[0]) / self.size[0])] != 1:
                ##self.x += 1



        except:
            pass



        if self.vector == 1 and self.l[int((self.y + 350) / self.size[1])][
                int((self.x + 350 + self.size[0]) / self.size[0])] != 1 and self.l[int((self.y + 349 + self.size[1]) / self.size[1])][
                int((self.x + 350 + self.size[0]) / self.size[0])] != 1:
            self.x +=1
        if self.vector == 2 and self.l[int((self.y + 350 + self.size[1]) / self.size[1])][
                int((self.x + 350) / self.size[0])] != 1 and self.l[int((self.y + 350 + self.size[1]) / self.size[1])][
                int((self.x + 349 + self.size[0]) / self.size[0])] != 1:
            self.y += 1
        if self.vector == 3 and self.l[int((self.y + 350) / self.size[1])][
                int((self.x + 349) / self.size[1])] != 1 and self.l[int((self.y + 349 + self.size[1]) / self.size[1])][
                int((self.x + 349) / self.size[0])] != 1:
            self.x-=1
        if self.vector == 4 and self.l[int((self.y + 349) / self.size[1])][
                int((self.x + 350) / self.size[0])] != 1 and self.l[int((self.y + 349) / self.size[1])][
                int((self.x + 349 + self.size[1]) / self.size[0])] != 1:

            self.y -=1

        #print(self.vector)

App()