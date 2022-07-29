import math
import os
import pygame as pg
import codecs
width = 1280
height = 720
tile_width = tile_height = width/10

pg.init()
screen = pg.display.set_mode((width, height));
block_group = pg.sprite.Group()
all_sprites = pg.sprite.Group()
player_group = pg.sprite.Group()
grass_group = pg.sprite.Group()
hud_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
border_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()


def ScriptQuest00000():
    script = "Quest/00000/Script.txt"

    fileStats = open(script, "r")
    line = fileStats.readline().strip()
    for enemy in npc_group:
        if enemy.id == "00000":
            enemy.kill()
            break
    if line == 'NPC':
        ID = fileStats.readline().strip()
        Position = fileStats.readline().strip()
        Position = Position.split('_')

        tmp = ScriptEnemy("00000", "Nappa", Point(enemy.rect.x/tile_width, enemy.rect.y/tile_height), (tile_width, tile_height), Animation(r"NPC\Nappa"), Stats(10, 50000, 0, 10000, 50000, 500, 10, 100, 10, 10, 100))
    fileStats.close()

def ScriptQuest00001():
    script = "Quest/00001/Script.txt"

    fileStats = open(script, "r")
    line = fileStats.readline().strip()
    for enemy in npc_group:
        if enemy.id == "00001":
            enemy.kill()
            break
    if line == 'NPC':
        ID = fileStats.readline().strip()
        Position = fileStats.readline().strip()
        Position = Position.split('_')

        tmp = ScriptEnemy(ID, "Goku", Point(enemy.rect.x/tile_width, enemy.rect.y/tile_height), (tile_width, tile_height), Animation("Goku"), Stats(10, 80000, 0, 10000, 80000, 2000, 50, 100, 10, 10, 100))

    fileStats.close()

def ScriptEnemy00001(enemy):
    file2 = codecs.open("Save/CompleteQuest.txt", "a")
    file2.write(enemy.ID + '\n')
    file2.close()
    file2 = codecs.open("Save/CurrentQuest.txt", "r")
    lines = file2.readlines()
    file2.close()
    file2 = codecs.open("Save/CurrentQuest.txt", "w")
    for line in lines:
        if line != enemy.ID + "\n":
            file2.write(line)
    file2.close()
    vegeta.exp += 1000

def ScriptEnemy00000(enemy):
    script = "Quest/00000/Status.txt"
    fileStats = open(script, "w")
    tmp = NPC("00000", "Nappa", Point(enemy.rect.x/tile_width, enemy.rect.y/tile_height), (tile_width, tile_height),
                      Animation("NPC/Nappa"), Stats(10, 100000, 0, 10000, 100000, 5000, 5, 10, 10, 10, 100))
    fileStats.write(enemy.ID)
    fileStats.close()
def CheckQuestComplited(name):
    objective = "Quest/"+name+"/Objective.txt"
    status= "Quest/"+name+"/Status.txt"
    fileObj = open(objective, "r")
    fileStat = open(status,"r")
    objList = []
    statList = []
    while True:
        line = fileObj.readline()

        if not(line):
            break;
        objList.append(line)
    while True:
        line = fileStat.readline()

        if not(line):
            break;
        statList.append(line)
    fileObj.close()
    fileStat.close()
    print(len(statList), len(objList))
    print(objList[0])

    if len(statList) == len(objList):
        return True
    else:
        return False

def CheckCurrentQuest(questId):
    file2 = codecs.open("Save/CurrentQuest.txt", "r")
    while True:
        line = file2.readline().strip()
        if not(line):
            break
        if line == questId:
            file2.close()
            return False
    file2.close()
    return True

def CheckQuestComplite(questId):
    file2 = codecs.open("Save/CompleteQuest.txt", "r")
    while True:
        line = file2.readline().strip()
        if not(line):
            break
        if line == questId:
            file2.close()
            return False
    file2.close()
    return True
def Draw_Base_Dialoge_Text(enemy):
    MainD = "Dialogue/" + enemy.Name + "/Main.txt"

    if CheckQuestComplited(enemy.id) and CheckQuestComplite(enemy.id):
        Question = "Dialogue/" + enemy.Name + "/Question2.txt"

    else:
        Question = "Dialogue/" + enemy.Name + "/Question.txt"
    fileMain = open(MainD, "r")
    welcome = fileMain.readline().strip()

    file = codecs.open(Question, "r", "utf-8")
    quest = []
    while True:
        line = file.readline().strip()
        if not line:
            break
        line = line.split('_')
        quest.append(line)
    file.close()

    npc_text = pg.font.Font(None, 20);
    text = npc_text.render(enemy.Name+':'+' '+welcome, 1, (255, 255, 255));
    screen.blit(text, (width/20, height/1.5));

    question_positon = height/1.25
    iterator = 1
    for x in quest:
        ques = pg.font.Font(None, 20);
        if x[0] == 'Quest':
            text = ques.render(str(iterator)+'.'+' '+x[1], 1, (255, 200, 10));
        else:
            text = ques.render(str(iterator)+'.'+' '+x[1], 1, (255, 255, 255));
        screen.blit(text, (width/20, question_positon));
        question_positon += height/50
        iterator += 1
    pg.display.flip()
    return quest

    fileMain.close
def Draw_Base_Dialoge_Border(enemy, Dark, Line):
    screen.fill(pg.Color('black'));
    grass_group.update()
    grass_group.draw(screen)
    grass_group.update()
    camera_group.custom_draw()
    pg.display.flip()
    if Dark == 'NPC':
        vegeta.dialog = pg.transform.scale(vegeta.dialog, (width/3, height))
        screen.blit(vegeta.dialog, (0, 0))
        s = pg.Surface((width, height))
        s.set_alpha(128)
        s.fill((30, 30, 30))
        screen.blit(s, (0, 0))
        enemy.dialog = pg.transform.scale(enemy.dialog, (width/3, height))
        screen.blit(enemy.dialog, (width/1.5, 0))
    else:
        enemy.dialog = pg.transform.scale(enemy.dialog, (width/3, height))
        screen.blit(enemy.dialog, (width/1.5, 0))
        s = pg.Surface((width, height))
        s.set_alpha(128)
        s.fill((30, 30, 30))
        screen.blit(s, (0, 0))
        vegeta.dialog = pg.transform.scale(vegeta.dialog, (width/3, height))
        screen.blit(vegeta.dialog, (0, 0))
    pg.draw.rect(screen, (0, 0, 0), (0, height/1.7, width, height/2))
    pg.draw.rect(screen, (0, 0, 0), (0, height/1.9, width/3, height/12))
    pg.draw.rect(screen, (0, 0, 0), (width- width/3.1, height/1.9, width/3, height/12))
    pg.display.flip()
    if Line:
        pg.draw.line(screen, (255, 255, 255), (0, height/1.35), (width, height/1.35), 2)

    if Dark == 'NPC':
        name_pl = pg.font.Font(None, 20);
        name_npc = pg.font.Font(None, 20);
        text = name_pl.render(str(vegeta.Name), 1, (200, 200, 200));
        screen.blit(text, (width/6, height/1.8));
        text = name_npc.render(str(enemy.Name), 1, (255, 255, 255));
        screen.blit(text, (width/1.2, height/1.8));
    else:
        name_pl = pg.font.Font(None, 20);
        name_npc = pg.font.Font(None, 20);
        text = name_pl.render(str(vegeta.Name), 1, (255, 255, 255));
        screen.blit(text, (width/6, height/1.8));
        text = name_npc.render(str(enemy.Name), 1, (200, 200, 200));
        screen.blit(text, (width/1.2, height/1.8));


def Dialogue(enemy):
    Draw_Base_Dialoge_Border(enemy, 'Player', True)
    tmp = Draw_Base_Dialoge_Text(enemy)
    chek = 1
    while chek:

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    file = codecs.open("Dialogue/"+enemy.Name+'/'+tmp[0][0]+'/1.txt', "r", "utf-8")
                    #iter = 0

                    questId = file.readline().strip()
                    status =[]
                    while True:
                        line = file.readline().strip()
                        if not(line):
                            break
                        status.append(line)
                    file.close()
                    if CheckQuestComplited(questId) and CheckQuestComplite(questId):
                        vegeta.exp += 500
                        file = codecs.open("Dialogue/"+enemy.Name+'/'+tmp[0][0]+'/'+status[2]+'.txt', "r", "utf-8")
                        file2 = codecs.open("Save/CompleteQuest.txt", "a")
                        file2.write(questId+'\n')
                        file2.close()
                        file2 = codecs.open("Save/CurrentQuest.txt", "r")
                        lines =file2.readlines()
                        file2.close()
                        file2 = codecs.open("Save/CurrentQuest.txt", "w")
                        for line in lines:
                            if line != questId + "\n":
                                file2.write(line)
                        file2.close()
                    elif not(CheckQuestComplite(questId)):
                        file = codecs.open("Dialogue/" + enemy.Name + '/' + tmp[0][0] + '/' + status[1] + '.txt', "r", "utf-8")
                    elif CheckCurrentQuest(questId):
                        file = codecs.open("Dialogue/" + enemy.Name + '/' + tmp[0][0] + '/' + status[0] + '.txt', "r", "utf-8")
                        file2 = codecs.open("Save/CurrentQuest.txt", "a")
                        file2.write(questId+'\n')
                        file2.close()
                        eval("ScriptQuest"+questId)()
                    else:
                        file = codecs.open("Dialogue/" + enemy.Name + '/' + tmp[0][0] + '/' + status[0] + '.txt', "r", "utf-8")

                    line = file.readline().strip()
                    if not line:
                        break
                    line = line.split('_')
                    Draw_Base_Dialoge_Border(enemy, line[0], False)
                    now_text = pg.font.Font(None, 20);
                    if line[0] == 'NPC':
                        text = now_text.render(enemy.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                    else:
                        text = now_text.render(vegeta.Name + ':' + ' ' + line[1], 1, (255, 255, 255));

                    screen.blit(text, (width / 20, height / 1.5));

                    pg.display.flip()
                    while True:
                        for event in pg.event.get():

                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_SPACE:
                                    line = file.readline().strip()
                                    if not line:
                                        break
                                    line = line.split('_')
                                    print(line[1])
                                    Draw_Base_Dialoge_Border(enemy, line[0], False)
                                    now_text = pg.font.Font(None, 20);
                                    if line[0] == 'NPC':
                                        text = now_text.render(enemy.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                                    else:
                                        text = now_text.render(vegeta.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                                    screen.blit(text, (width / 20, height / 1.5));

                                    pg.display.flip()
                        if not line:
                            break
                        #iter +=1
                    file.close()
                    screen.fill(pg.Color('black'));
                    grass_group.update()
                    grass_group.draw(screen)
                    grass_group.update()
                    camera_group.custom_draw()
                    pg.display.flip()
                    Draw_Base_Dialoge_Border(enemy, 'Player', True)
                    Draw_Base_Dialoge_Text(enemy)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_2:
                    file = codecs.open("Dialogue/"+enemy.Name+'/'+tmp[1][0]+'/2.txt', "r", "utf-8")
                    #iter = 0
                    line = file.readline().strip()
                    line = file.readline().strip()
                    if not line:
                        break
                    line = line.split('_')
                    print(line[1])
                    Draw_Base_Dialoge_Border(enemy, line[0], False)
                    now_text = pg.font.Font(None, 20);
                    text = now_text.render(vegeta.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                    screen.blit(text, (width / 20, height / 1.5));
                    pg.display.flip()
                    while True:
                        for event in pg.event.get():

                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_SPACE:
                                    line = file.readline().strip()
                                    if not line:
                                        break
                                    line = line.split('_')
                                    print(line[1])
                                    Draw_Base_Dialoge_Border(enemy, line[0], False)
                                    now_text = pg.font.Font(None, 20);
                                    if line[0] == 'NPC':
                                        text = now_text.render(enemy.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                                    else:
                                        text = now_text.render(vegeta.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                                    screen.blit(text, (width / 20, height / 1.5));
                                    pg.display.flip()
                        if not line:
                            break
                        #iter +=1
                    file.close()
                    screen.fill(pg.Color('black'));
                    grass_group.update()
                    grass_group.draw(screen)
                    grass_group.update()
                    camera_group.custom_draw()
                    pg.display.flip()
                    Draw_Base_Dialoge_Border(enemy, 'Player', True)
                    Draw_Base_Dialoge_Text(enemy)
                    #Draw_Base_Dialoge(enemy)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_3:
                    file = codecs.open("Dialogue/"+enemy.Name+'/'+tmp[2][0]+'/3.txt', "r", "utf-8")
                    line = file.readline().strip()
                    line = file.readline().strip()
                    if not line:
                        break
                    line = line.split('_')
                    print(line[1])
                    Draw_Base_Dialoge_Border(enemy, line[0], False)
                    now_text = pg.font.Font(None, 20);
                    text = now_text.render(vegeta.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                    screen.blit(text, (width / 20, height / 1.5));
                    pg.display.flip()
                    while True:
                        for event in pg.event.get():

                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_SPACE:
                                    line = file.readline().strip()
                                    if not line:
                                        break
                                    line = line.split('_')
                                    print(line[1])
                                    Draw_Base_Dialoge_Border(enemy, line[0], False)
                                    now_text = pg.font.Font(None, 20);
                                    if line[0] == 'NPC':
                                        text = now_text.render(enemy.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                                    else:
                                        text = now_text.render(vegeta.Name + ':' + ' ' + line[1], 1, (255, 255, 255));
                                    screen.blit(text, (width / 20, height / 1.5));
                                    pg.display.flip()
                        if not line:
                            break
                    file.close()
                    screen.fill(pg.Color('black'));
                    grass_group.update()
                    grass_group.draw(screen)
                    grass_group.update()
                    camera_group.custom_draw()
                    pg.display.flip()
                    Draw_Base_Dialoge_Border(enemy, 'Player', True)
                    Draw_Base_Dialoge_Text(enemy)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_4:
                    chek = 0


class Point:
    def __init__(self, x1, y1):
        self.x = x1;
        self.y = y1;

    def getPosition(self, delta_x=0, delta_y=0):
        return (self.x + delta_x, self.y + delta_y);

class Animation:
    def __init__(self, name: str):
        self.main = [load_image(name + r"\main\1.png"),
                     load_image(name + r"\run left\1.png"),
                     load_image(name + r"\run up\1.png"),
                     load_image(name + r"\run right\1.png")]
        self.fight_up = [load_image(name + r"\fight up\1.png")]
        self.fight_down = [load_image(name + r"\fight down\1.png")]
        self.fight_left = [load_image(name + r"\fight left\1.png")]
        self.fight_right = [load_image(name + r"\fight right\1.png")]

        self.aura = [load_image(name + r"\aura\base aura.png")]

        self.left = [load_image(name + r"\run left\1.png")]
        self.right = [load_image(name + r"\run right\1.png")]
        self.up = [load_image(name + r"\run up\1.png")]
        self.down = [load_image(name + r"\run down\1.png")]

        self.hud = [load_image(name + r"\hud\1.png")]

        self.dialog = [load_image(name + r"\hud\2.png")]

        self.superup = [load_image(name + r"\super up\1.png")]
        self.superdown = [load_image(name + r"\super down\1.png")]
        self.superleft = [load_image(name + r"\super left\1.png")]
        self.superfight = [load_image(name + r"\super right\1.png")]

class HUD:
    def __init__(self, player):
        self.rect_healt = pg.Rect
        self.rect_energy = pg.Rect
        self.stats = player.stats
        self.image = player.frames.hud[0]
        pg.draw.rect(screen, (25, 25, 25), pg.Rect(0, 0, 150, 107))
        self.image = pg.transform.scale(self.image,(150,90))
    def update(self):
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(150, 0, 252, 55), 5)
        pg.draw.rect(screen, (0, 0, 0), (150, 52, 252, 55), 5)
        self.rect_healt = pg.Rect(155, 5, (self.stats.health/self.stats.maxhealth)*250-8, 45)
        self.rect_energy = pg.Rect(155, 57, (self.stats.energy/self.stats.maxEnergy)*250-8, 45)

        pg.draw.rect(screen, (255,0,0), self.rect_healt)
        pg.draw.rect(screen, (0,0,255), self.rect_energy)
        energy = pg.font.Font(None, 20);
        text = energy.render(str(self.stats.energy)+r'/'+str(self.stats.maxEnergy), 1, (0, 0, 0));
        screen.blit(text, (250, 70));
        health = pg.font.Font(None, 20);
        text = energy.render(str(self.stats.health)+r'/'+str(self.stats.maxhealth), 1, (0, 0, 0));
        screen.blit(text, (250, 20));
        screen.blit(self.image, (0, 15))
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 101, 402, 60), 5)
        if vegeta.exp < vegeta.exp_nextLevel:
            pg.draw.rect(screen, (200,200,30), pg.Rect(5, 107, vegeta.exp/vegeta.exp_nextLevel*397-4, 49))
            text = energy.render(str(vegeta.exp)+r'/'+str(vegeta.exp_nextLevel), 1, (0, 0, 0));
        else:
            pg.draw.rect(screen, (200,200,30), pg.Rect(5, 107, 393, 49))
            text = energy.render(str(vegeta.exp)+r'/'+str(vegeta.exp_nextLevel), 1, (0, 0, 0));
        screen.blit(text, (250, 112));
        text = energy.render(str(vegeta.stats.level), 1, (255, 0, 0));
        screen.blit(text, (15, 11))
class Stats:
    def __init__(self, level1, maxhealth1, energy1, maxEnergy1, health1, attack1, speed1, kiAttack1, chargeEnergy1, defend1, basedefend1):
        self.level = level1
        self.maxhealth = maxhealth1
        self.energy = energy1;
        self.health = health1;
        self.attack = attack1;
        self.speed = speed1;
        self.kiAttack = kiAttack1;
        self.chargeEnergy = chargeEnergy1;
        self.defend = defend1;
        self.baseDefend = basedefend1;
        self.maxEnergy = maxEnergy1

class NPC(pg.sprite.Sprite):
    def __init__(self, ID, name, pos, scale, frame, stats1):
        super().__init__(camera_group, npc_group)
        self.id = ID
        self.Name = name
        self.position = pos;
        self.stats = stats1
        self.frames = frame;
        self.image = self.frames.main[0];
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.position.x*tile_width, self.position.y*tile_height);
        self.transform = scale;
        self.image = pg.transform.scale(self.image, (scale[0], scale[1]))
        self.cur_frame = 0;
        self.speed = 0;
        self.collide_rect = pg.Rect(0, 0, scale[0] // 2, scale[1] // 10)
        self.collide_fight = pg.Rect(0, 0, scale[0] // 2, scale[1] // 4)
        self.dialogie_rect = pg.Rect(self.rect.centerx, self.rect.centery, 200, 200)
        self.dialog = self.frames.dialog[0]
    def update(self):

        if self.stats.health <= 0:
            self.kill()


class ScriptEnemy(pg.sprite.Sprite):
    def __init__(self, id, name, pos: Point, scale: tuple, frame: Animation, stats1: Stats):
        super().__init__(player_group, all_sprites, camera_group, enemy_group)
        self.ID = id
        self.Name = name;
        self.position = pos;
        self.stats = stats1
        self.frames = frame;
        self.image = self.frames.main[0];
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.position.x * tile_width, self.position.y * tile_height);
        self.transform = scale;
        self.image = pg.transform.scale(self.image, (scale[0], scale[1]))
        self.cur_frame = 0;
        self.speed = 0;
        self.collide_rect = pg.Rect(0, 0, scale[0] // 3, scale[1] // 10)
        self.collide_fight = pg.Rect(0, 0, scale[0]*2, scale[1]*2)
        self.facing = 'down'
        self.direction = pg.math.Vector2(0, 0)
        self.aura = self.frames.aura[0]
        self.dialog = self.frames.dialog[0]
        self.collide_see = pg.Rect(self.rect.centerx, self.rect.centery, 500, 500)
        self.collide_see.center = self.rect.center
        self.collide_see = self.collide_see.inflate(500, 500)
        self.collide_rect.center = self.rect.center
        self.alpha = 0
        self.move_bool = True
        self.time_attack = 0

    def update(self):
        if self.stats.health <= 0:
            self.kill()
            vegeta.exp += 100
            eval("ScriptEnemy" + self.ID)(self)


        if self.time_attack == 0 or self.time_attack <= 250:
            self.getDirection()

        if self.time_attack == 0 and self.move_bool:

            self.rect.center += self.direction
            self.collide_see.center += self.direction

            self.collide_fight.x = self.rect.centerx
            self.collide_fight.y = self.rect.y + 50
            if self.facing == 'left':
                self.collide_fight = pg.Rect(0, 0, self.transform[0], self.transform[1] // 4)
                self.collide_fight.x = self.rect.centerx
                self.collide_fight.y = self.rect.centery

            elif self.facing == 'right':
                self.collide_fight = pg.Rect(0, 0, self.transform[0], self.transform[1] // 4)
                self.collide_fight.x = self.rect.centerx
                self.collide_fight.y = self.rect.centery

            elif self.facing == 'up':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] // 2)
                self.collide_fight.y = self.rect.y - 10
                self.collide_fight.x = self.rect.x

            elif self.facing == 'down':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] // 3)
                self.collide_fight.y = self.rect.y + tile_height
                self.collide_fight.x = self.rect.x


        else:
            if self.time_attack == 0:
                self.time_attack = 500
                if self.facing == 'left':
                    self.rect.move_ip(-10, 0)
                    self.image = self.frames.fight_left[0]

                    self.rect.move_ip(10, 0)


                elif self.facing == 'right':
                    self.image = self.frames.fight_right[0]

                elif self.facing == 'up':
                    self.image = self.frames.fight_up[0]

                elif self.facing == 'down':
                    self.image = self.frames.fight_down[0]
                self.hit(self.collide_fight, self.stats)
                self.image = pg.transform.scale(self.image, (self.transform[0], self.transform[1]))
            if self.time_attack > 0:
                self.time_attack -= self.stats.speed

        self.direction = pg.math.Vector2(0, 0)

    def getDirection(self):
        if self.collide_see.colliderect(vegeta.rect):

            start = pg.math.Vector2(self.rect.centerx, self.rect.centery)
            end = pg.math.Vector2(vegeta.rect.center)
            if not (start == end):
                self.direction = ((end - start).normalize() * 2);
                if self.direction.x > 1:
                    self.direction.x = 1
                elif self.direction.x < -1:
                    self.direction.x = -1
                if self.direction.y > 1:
                    self.direction.y = 1
                elif self.direction.y < -1:
                    self.direction.y = -1

                if self.direction.y == 1:
                    self.facing = 'down'
                    self.image = self.frames.down[0]
                elif self.direction.y == -1:
                    self.facing = 'up'
                    self.image = self.frames.up[0]
                elif self.direction.x == -1:
                    self.facing = 'left'
                    self.image = self.frames.left[0]
                elif self.direction.x == 1:
                    self.facing = 'right'
                    self.image = self.frames.right[0]
                self.image = pg.transform.scale(self.image, (self.transform[0], self.transform[1]))

        else:
            self.direction = pg.math.Vector2(0, 0)

        self.collide_rect.center = self.rect.center
        self.collide_rect.center += (self.direction * 2)
        if not (self.selfCollide(self.collide_rect)):
            self.move_bool = False
        else:
            self.move_bool = True

    def hit(self, a, stat):
        if a.colliderect(vegeta.rect):
            print(1)
            vegeta.stats.health -= stat.attack
        for block in block_group:

            if a.colliderect(block):
                block.health -= stat.attack
                break
        if stat == 'ki':
            for grass in grass_group:

                if a.colliderect(grass):
                    grass.health -= stat.attack
        for enemy in npc_group:
            if a.colliderect(enemy.rect):
                enemy.stats.health -= stat.attack

    def selfCollide(self, a):
        if a.colliderect(vegeta.rect):
            return False
        for block in block_group:
            if a.colliderect(block):
                return False
        for enemy in npc_group:
            if a.colliderect(enemy):
                return False
        for border in border_group:
            if a.colliderect((border.rect)):
                return False
        return True


class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2()
        self.half_w = width/2
        self.half_h = height/2
    def custom_draw(self):
        self.CenterPlayerCamera(vegeta)
        screen.fill(pg.Color("black"))
        for grass in grass_group:
            offset_pos = grass.rect.topleft - self.offset
            self.display_surface.blit(grass.image, offset_pos)
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
    def CenterPlayerCamera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h


camera_group = CameraGroup()


class Player(pg.sprite.Sprite):
    def __init__(self,name, pos: Point, scale: tuple, frame: Animation, stats1: Stats):
        super().__init__(player_group, all_sprites, camera_group)
        self.Name = name;
        self.position = pos;
        self.stats = stats1
        self.frames = frame;
        self.image = self.frames.main[0];
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0, 0);
        self.transform = scale;
        self.image = pg.transform.scale(self.image, (scale[0], scale[1]))
        self.cur_frame = 0;
        self.speed = 0;
        self.collide_rect = pg.Rect(0, 0, scale[0] // 2, scale[1] // 10)
        self.collide_fight = pg.Rect(0, 0, scale[0] // 2, scale[1] // 4)
        self.facing = 'down'
        self.aura = self.frames.aura[0]
        self.dialog = self.frames.dialog[0]
        self.quest_history = {}
        self.exp = 0
        self.exp_nextLevel = 500

    def levelUp(self):
        self.stats.maxhealth += 100
        self.stats.health = self.stats.maxhealth
        self.stats.maxEnergy += 100
        self.stats.energy = self.stats.maxEnergy
        self.stats.chargeEnergy += 100
    def update(self):

        if self.exp >= self.exp_nextLevel:
            self.stats.level += 1
            self.exp -= self.exp_nextLevel
            self.exp_nextLevel += 50
            self.levelUp()

        if self.stats.health <= 0:
            screen.fill('black');
            currentQuestText = pg.font.Font(None, 20);
            printText = (width / 2, height / 2)
            text = currentQuestText.render("Game Over", 1, (255, 0, 0));
            screen.blit(text, printText);

        keys = pg.key.get_pressed()
        tmp_aura = True;
        if keys[pg.K_z]:
            self.change_energy();
            tmp_aura = False;
        if tmp_aura:
            self.speed = 0;
            self.collide_fight.x = self.rect.x
            self.collide_fight.y = self.rect.y + 50
            if self.facing == 'left':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] // 4)
                self.collide_fight.x = self.rect.x - 20
                self.collide_fight.y = self.rect.y + 50

            elif self.facing == 'right':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] // 4)
                self.collide_fight.x = self.rect.x + 15
                self.collide_fight.y = self.rect.y + 50

            elif self.facing == 'up':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1]//2)
                self.collide_fight.y = self.rect.y +tile_height//4
                self.collide_fight.x = self.rect.x

            elif self.facing == 'down':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] //3)
                self.collide_fight.y = self.rect.y + tile_height
                self.collide_fight.x = self.rect.x

            self.collide_rect.x = self.rect.x
            self.collide_rect.y = self.rect.y + self.transform[1]//2+10

            if keys[pg.K_d] - keys[pg.K_a] > 0:
                self.image = self.frames.right[0]
                self.collide_rect.move_ip(5, 0)
                self.facing = 'right'

                if collide(self.collide_rect):
                    self.rect.x += keys[pg.K_d] - keys[pg.K_a] + self.stats.speed


            elif keys[pg.K_d] - keys[pg.K_a] < 0:
                self.image = self.frames.left[0]
                self.facing = 'left'
                self.collide_rect.move_ip(-5, 0)

                if collide(self.collide_rect):
                    self.collide_rect.move_ip(5, 0)
                    self.rect.x += keys[pg.K_d] - keys[pg.K_a] - self.stats.speed

            if keys[pg.K_s] - keys[pg.K_w] > 0:
                self.image = self.frames.down[0]
                self.facing = 'down'
                self.collide_rect.move_ip(0, 5)
                if collide(self.collide_rect):
                    self.rect.y += keys[pg.K_s] - keys[pg.K_w] + self.stats.speed


            elif keys[pg.K_s] - keys[pg.K_w] < 0:
                self.image = self.frames.up[0]
                self.facing = 'up'
                self.collide_rect.move_ip(0, -5)

                if collide(self.collide_rect):
                    self.rect.y += keys[pg.K_s] - keys[pg.K_w] - self.stats.speed

        self.speed += 1 * self.stats.speed
        self.image = pg.transform.scale(self.image, (self.transform[0], self.transform[1]))


    def change_energy(self):
        if self.stats.maxEnergy < self.stats.energy + self.stats.chargeEnergy:
            self.stats.energy = self.stats.maxEnergy
        elif self.stats.maxEnergy > self.stats.energy:
            self.stats.energy += self.stats.chargeEnergy
        self.aura = pg.transform.scale(self.aura, (self.transform[0] + 30, self.transform[1] + 50))
        rect = pg.Rect(self.rect.centerx, self.rect.centery, 200, 200)

        rect.centerx = self.rect.centerx
        rect.centery = self.rect.centery
        self.hit(rect, self.stats.chargeEnergy, 'ki')
        print(rect.x, self.rect.x, rect.y, self.rect.y)

        screen.blit(self.aura, (width/2.42, height/2.9))

    def hit(self, a, damage, stat):
        for enemy in enemy_group:
            if a.colliderect(enemy.rect):
                enemy.stats.health = -damage
                print(enemy.stats.health)


        for block in block_group:

            if a.colliderect(block):
                block.health -= damage
                break
        if stat == 'ki':
            for block in block_group:

                if a.colliderect(block):
                    block.health -= damage
            for grass in grass_group:

                if a.colliderect(grass):
                    grass.health -= damage
        for enemy in npc_group:
            if a.colliderect(enemy.rect):
                enemy.stats.health -= damage
class Enemy(pg.sprite.Sprite):
    def __init__(self,id, name, pos: Point, scale: tuple, frame: Animation, stats1: Stats):
        super().__init__(player_group, all_sprites, camera_group, enemy_group)
        self.ID = id
        self.Name = name;
        self.position = pos;
        self.stats = stats1
        self.frames = frame;
        self.image = self.frames.main[0];
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.position.x*tile_width, self.position.y*tile_height);
        self.transform = scale;
        self.image = pg.transform.scale(self.image, (scale[0], scale[1]))
        self.cur_frame = 0;
        self.speed = 0;
        self.collide_rect = pg.Rect(0, 0, scale[0] // 3, scale[1] // 10)
        self.collide_fight = pg.Rect(0, 0, scale[0], scale[1])
        self.facing = 'down'
        self.direction = pg.math.Vector2(0,0)
        self.aura = self.frames.aura[0]
        self.dialog = self.frames.dialog[0]
        self.collide_see = pg.Rect(self.rect.centerx, self.rect.centery, 500, 500)
        self.collide_see.center = self.rect.center
        self.collide_see = self.collide_see.inflate(500,500)
        self.collide_rect.center = self.rect.center
        self.alpha = 0
        self.move_bool = True
        self.time_attack = 0

    def update(self):
        if self.stats.health <= 0:
            self.kill()

        if self.time_attack == 0 or self.time_attack <= 250:
            self.getDirection()

        if self.time_attack==0 and self.move_bool:

            self.rect.center += self.direction
            self.collide_see.center += self.direction

            self.collide_fight.x = self.rect.centerx
            self.collide_fight.y = self.rect.y + 50
            if self.facing == 'left':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] // 4)
                self.collide_fight.x = self.rect.centerx
                self.collide_fight.y = self.rect.centery

            elif self.facing == 'right':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] // 4)
                self.collide_fight.x = self.rect.centerx
                self.collide_fight.y = self.rect.centery

            elif self.facing == 'up':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1]//2)
                self.collide_fight.y = self.rect.y-10
                self.collide_fight.x = self.rect.x

            elif self.facing == 'down':
                self.collide_fight = pg.Rect(0, 0, self.transform[0] // 2, self.transform[1] //3)
                self.collide_fight.y = self.rect.y + tile_height
                self.collide_fight.x = self.rect.x


        else:
            if self.time_attack==0 :
                self.time_attack = 500
                if self.facing == 'left':
                    self.rect.move_ip(-10, 0)
                    self.image = self.frames.fight_left[0]

                    self.rect.move_ip(10, 0)


                elif self.facing == 'right':
                    self.image = self.frames.fight_right[0]

                elif self.facing == 'up':
                    self.image = self.frames.fight_up[0]

                elif self.facing == 'down':
                    self.image = self.frames.fight_down[0]
                self.hit(self.collide_fight, self.stats)
                print(self.facing)
                self.image = pg.transform.scale(self.image, (self.transform[0], self.transform[1]))
            self.speed += self.stats.speed
            if self.time_attack > 0:
                self.time_attack -= self.stats.speed

        self.direction = pg.math.Vector2(0,0)
    def getDirection(self):
        tmp = (0,0)
        if self.collide_see.colliderect(vegeta.rect):

            start = pg.math.Vector2(self.rect.centerx, self.rect.centery)
            end = pg.math.Vector2(vegeta.rect.center)
            if not(start == end):
                self.direction = ((end-start).normalize()*2);
                if self.direction.x > 1:
                    self.direction.x = 1
                elif self.direction.x<-1:
                    self.direction.x =-1
                if self.direction.y > 1:
                    self.direction.y = 1
                elif self.direction.y < -1:
                    self.direction.y = -1

                if self.direction.y == 1:
                    self.facing ='down'
                    self.image = self.frames.down[0]
                elif self.direction.y == -1:
                    self.facing = 'up'
                    self.image = self.frames.up[0]
                elif self.direction.x == -1:
                    self.facing = 'left'
                    self.image=self.frames.left[0]
                elif self.direction.x == 1:
                    self.facing = 'right'
                    self.image=self.frames.right[0]
                self.image = pg.transform.scale(self.image, (self.transform[0], self.transform[1]))

        else:
            self.direction = pg.math.Vector2(0,0)

        self.collide_rect.center = self.rect.center
        self.collide_rect.center += (self.direction*2)
        if not(self.selfCollide(self.collide_rect)):
            self.move_bool = False
        else:
            self.move_bool = True

    def change_energy(self):
        if self.stats.maxEnergy < self.stats.energy + self.stats.chargeEnergy:
            self.stats.energy = self.stats.maxEnergy
        elif self.stats.maxEnergy > self.stats.energy:
            self.stats.energy += self.stats.chargeEnergy
        self.aura = pg.transform.scale(self.aura, (self.transform[0] + 30, self.transform[1] + 50))
        rect = self.aura.get_rect()
        rect.x = self.rect.x - 40
        rect.y = self.rect.y - 45
        #screen.blit(self.aura, (rect.x, rect.y))
        # pg.draw.rect(self.aura, (0,0,0), self.aura.get_rect())
        self.hit(rect, self.stats.chargeEnergy, 'ki')
        screen.blit(self.aura, (self.image.get_rect().x+160, self.image.get_rect().y+150))
        #screen.fill(pg.Color("green"))

        #pg.display.flip()
    def hit(self, a, stat):
        if a.colliderect(vegeta.rect):
            print(1)
            vegeta.stats.health -= stat.attack
        if a.colliderect(vegeta.collide_rect):
            print(1)
            vegeta.stats.health -= stat.attack
        for block in block_group:

            if a.colliderect(block):
                block.health -= stat.attack
                break
        if stat == 'ki':
            for grass in grass_group:

                if a.colliderect(grass):
                    grass.health -= stat.attack
        for enemy in npc_group:
            if a.colliderect(enemy.rect):
                enemy.stats.health -= stat.attack

    def selfCollide(self, a):
        if a.colliderect(vegeta.rect):
            return False
        for block in block_group:
            if a.colliderect(block):
                return False
        for enemy in npc_group:
            if a.colliderect(enemy):
                return False
        for border in border_group:
            if a.colliderect((border.rect)):
                return False
        return True

def load_level(filename):
    filename = "Level/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))



def collide(a):


    for block in block_group:
        if a.colliderect(block):
            return False
    for enemy in npc_group:
        if a.colliderect(enemy):
            return False
    for border in border_group:
        if a.colliderect((border.rect)):
            return False
    return True


def load_image(name, color_key=None):
    fullname = os.path.join('Sprite', name)
    try:
        image = pg.image.load(fullname).convert_alpha()
    except pg.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


box_images = {
    'Box1': load_image(r'StaticObject\Box1.png'),
    'Rocky1': load_image(r'StaticObject\Rocky1.png')
}
grass_images = {
    'Grass1': load_image(r'StaticObject\Grass1.png'),
    'Dirty1': load_image(r'StaticObject\Dirty1.png'),
    'Sand1': load_image(r'StaticObject\Sand1.png')
}


class Block(pg.sprite.Sprite):

    def __init__(self, name, pos_x, pos_y):
        super().__init__(block_group, all_sprites, camera_group)
        self.image = box_images[name]
        self.image = pg.transform.scale(self.image, (tile_width, tile_height)).convert_alpha()
        #self.image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.health = 1

    def update(self):
        for block in block_group:
            if block.health <= 0:
                Grass('Sand1', block.rect.x // tile_width, block.rect.y // tile_height);
                block.kill()

class Grass(pg.sprite.Sprite):

    def __init__(self, name, pos_x, pos_y):
        super().__init__( grass_group, all_sprites)
        self.image = grass_images[name]
        self.health = 1
        self.image = pg.transform.scale(self.image, (tile_width, tile_height))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def update(self):
        if self.health <= 0:
            #enemy.kill()
            Grass('Dirty1', self.rect.x // tile_width, self.rect.y // tile_height);

            self.kill()

class Border(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(border_group)
        self.image = grass_images['Grass1']

        self.image = pg.transform.scale(self.image, (tile_width, tile_height))

        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Grass('Sand1', x, y)
            elif level[y][x] == '#':
                Grass('Sand1', x, y)
                Block('Rocky1', x, y)
            elif level[y][x] == '@':
                Grass('Sand1', x, y)
                player = Player("Vegeta",Point(x, y), (tile_width, tile_height), Animation("Vegeta"),
                                Stats(10, 100000, 10000, 10000, 100000, 5000, 5, 10, 10, 10, 100))
                player.rect = player.image.get_rect().move(tile_width * x + 15, tile_height * y + 5)
            elif level[y][x] == 'n':
                Grass('Sand1', x, y)
                npc = NPC("00000", "Nappa",Point(x, y), (tile_width-5, tile_height-5), Animation(r"NPC\Nappa"),
                                Stats(10, 50000, 0, 10000, 50000, 100, 500, 100, 10, 10, 100))
                npc.rect = npc.image.get_rect().move(tile_width * x + 15, tile_height * y + 5)
            elif level[y][x] == 'b':
                Border(x,y)
            elif level[y][x] == 'g':
                Grass('Sand1', x, y)
                npc = NPC("00001", "Goku",Point(x, y), (tile_width-5, tile_height-5), Animation(r"NPC\Goku"),
                                Stats(10, 100000, 0, 10000, 100000, 100, 500, 100, 10, 10, 100))
                npc.rect = npc.image.get_rect().move(tile_width * x + 15, tile_height * y + 5)
    return player, x, y



def Main():
    screen.fill(pg.Color('black'));
    global vegeta
    vegeta,a,b = generate_level(load_level("Test.txt"));
    pg.display.flip()
    image_button_e = load_image(r"Button\E.png")
    image_button_e = pg.transform.scale(image_button_e, (75, 75))
    tmp_e = False
    tmp = 0
    image_tmp = None
    tmp_bool = False
    hud = HUD(vegeta);
    fps = 60;
    clock = pg.time.Clock()
    kiAttack = False
    running = 1;

    KiAttackPosition = 0
    CollideKiAttackPosition = 0


    while running:

        screen.fill(pg.Color('black'));
        grass_group.update()
        grass_group.draw(screen)
        grass_group.update()
        camera_group.custom_draw()
        if vegeta.stats.health <= 0:
            running = False
        hud = HUD(vegeta);
        hud.update()
        if not (tmp_bool):
            camera_group.update()
        npc_group.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                file = open("Save/CurrentQuest.txt",'w').close
                file = open("Save/CompleteQuest.txt",'w').close
                file = open("Quest/00000/Status.txt",'w').close

                running = False
            if event.type == pg.KEYDOWN:
                if event. key == pg.K_j:
                    chek = 1
                    screen.fill("black")
                    file1 = codecs.open("Save/AllQuest.txt", "r")
                    file2 = codecs.open("Save/CurrentQuest.txt", "r")
                    file3 = codecs.open("Save/CompleteQuest.txt", "r")
                    list1 = []
                    list2 = []
                    list3 = []
                    while True:
                        line = file1.readline().strip()
                        if not (line):
                            break
                        list1.append(line)
                    file1.close()
                    while True:
                        line = file2.readline().strip()
                        if not (line):
                            break
                        list2.append(line)
                    file2.close()
                    while True:
                        line = file3.readline().strip()
                        if not (line):
                            break
                        list3.append(line)
                    file3.close()
                    list11 = []
                    list22 = []
                    list33 = []
                    for read in list1:
                        list11.append(read.split('_'))
                    for read in list2:
                        list22.append(read.split('_'))
                    for read in list3:
                        list33.append(read.split('_'))
                    currentQuestText = pg.font.Font(None, 20);
                    printText =  (width/5, height/20)
                    text = currentQuestText.render("Current Quest", 1, (255, 255, 255));
                    screen.blit(text, printText);
                    printText = (width/15, height/25+height/15)
                    for i in list11:
                        for j in list22:

                            if str(i[0]) == j[0]:
                                text = currentQuestText.render(i[1], 1, (255, 255, 255));
                                screen.blit(text, printText)
                                text = currentQuestText.render(i[2], 1, (255, 255, 255));
                                screen.blit(text, (printText[0]+width/3, printText[1]))
                                printText = (printText[0], printText[1]+height/15)
                    printText = (width/5, printText[1])
                    completeQuestText = pg.font.Font(None, 20);
                    text = completeQuestText.render("Complete Quest", 1, (255, 255, 255));
                    screen.blit(text, printText)
                    printText = (width / 15, printText[1]+height/15)
                    for i in list11:
                        for j in list33:
                            if str(i[0]) == j[0]:
                                text = currentQuestText.render(i[1], 1, (255, 255, 255));
                                screen.blit(text, printText)
                                text = currentQuestText.render(i[2], 1, (255, 255, 255));
                                screen.blit(text, (printText[0]+width/3, printText[1]))

                                printText = (printText[0], printText[1]+height/15)
                    pg.display.flip()
                    while chek:
                        for event in pg.event.get():
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_j:
                                    chek = 0
                            if event.type == pg.QUIT:
                                file = open("Save/CurrentQuest.txt", 'w').close
                                file = open("Save/CompleteQuest.txt", 'w').close
                                file = open("Quest/00000/Status.txt", 'w').close
                                chek = False
                                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if tmp == 0:
                        image_tmp = vegeta.image
                        tmp_bool = True
                        if vegeta.facing == 'left':
                            vegeta.rect.move_ip(-10, 0)
                            vegeta.image = vegeta.frames.fight_left[0]

                            vegeta.rect.move_ip(10, 0)


                        elif vegeta.facing == 'right':
                            vegeta.image = vegeta.frames.fight_right[0]

                        elif vegeta.facing == 'up':
                            vegeta.image = vegeta.frames.fight_up[0]

                        elif vegeta.facing == 'down':
                            vegeta.image = vegeta.frames.fight_down[0]
                        vegeta.hit(vegeta.collide_fight, vegeta.stats.attack, 'base')
                        tmp = 100;
            if event.type == pg.KEYDOWN:
                #npc_group.update()
                if event.key == pg.K_r:
                    if vegeta.stats.energy >= 2000:
                        if tmp == 0:
                            vegeta.stats.energy -=2000
                            image_tmp = vegeta.image
                            rect2 = vegeta.collide_fight.copy()

                            tmp_bool = True
                            #rect1 = pg.image.load(r"Sprite\Vegeta\Garlik Gun\1.png")
                            #rect1 =
                            if vegeta.facing == 'down':
                                vegeta.image = vegeta.frames.superdown[0]
                                rect1 = pg.image.load(r"Sprite\Vegeta\Garlik Gun\1.png")
                                rect1 = pg.transform.rotate(rect1, 270)
                                rect1 = pg.transform.scale(rect1, (500,1000))
                                KiAttackPosition = (rect2.centerx-(camera_group.offset.x)-tile_width*2.2, rect2.centery-camera_group.offset.y-tile_width/3.2)
                                screen.blit(rect1, KiAttackPosition)
                                CollideKiAttackPosition =  pg.Rect(rect2.centerx-tile_width, rect2.centery, 200, 1000)
                                vegeta.hit(CollideKiAttackPosition, vegeta.stats.kiAttack, 'ki')

                            elif vegeta.facing == 'right':
                                vegeta.image = vegeta.frames.superfight[0]

                                rect1 = pg.image.load(r"Sprite\Vegeta\Garlik Gun\1.png")
                                rect1 = pg.transform.rotate(rect1, 0)
                                rect1 = pg.transform.scale(rect1, (1000,500))
                                KiAttackPosition =(rect2.centerx-(camera_group.offset.x)+tile_width/5, rect2.centery-camera_group.offset.y-tile_width*1.5)
                                screen.blit(rect1, KiAttackPosition)
                                CollideKiAttackPosition = pg.Rect(rect2.centerx - tile_width / 4, rect2.centery -tile_width, 1000, 200)
                                vegeta.hit(CollideKiAttackPosition, vegeta.stats.kiAttack, 'ki')

                            elif vegeta.facing == 'left':
                                vegeta.image = vegeta.frames.superleft[0]
                                rect1 = pg.image.load(r"Sprite\Vegeta\Garlik Gun\1.png")
                                rect1 = pg.transform.rotate(rect1, 180)
                                rect1 = pg.transform.scale(rect1, (1000, 500))
                                KiAttackPosition = (rect2.centerx - (camera_group.offset.x) - tile_width*7.9, rect2.centery - camera_group.offset.y - tile_width * 2)
                                screen.blit(rect1, KiAttackPosition)
                                CollideKiAttackPosition = pg.Rect(rect2.centerx - tile_width*8, rect2.centery - tile_width*0.5, 1000, 200)
                                vegeta.hit(CollideKiAttackPosition, vegeta.stats.kiAttack, 'ki')
                            elif vegeta.facing == 'up':
                                vegeta.image = vegeta.frames.superup[0]

                                rect1 = pg.image.load(r"Sprite\Vegeta\Garlik Gun\1.png")
                                rect1 = pg.transform.rotate(rect1, 90)
                                rect1 = pg.transform.scale(rect1, (500,1000))
                                KiAttackPosition = (rect2.centerx-(camera_group.offset.x)-tile_width*1.8, rect2.centery-camera_group.offset.y-tile_width*8)
                                screen.blit(rect1, KiAttackPosition)
                                CollideKiAttackPosition = pg.Rect(rect2.centerx-tile_width, rect2.centery-tile_width*8, 200, 1000)
                                vegeta.hit(CollideKiAttackPosition, vegeta.stats.kiAttack, 'ki')
                            kiAttack = True
                            pg.display.flip()
                            tmp = 1000

                        #print(rect1.get_rect().center)
                        #tmp = 0;
            for enemy in npc_group:
                if vegeta.rect.colliderect((enemy.dialogie_rect)):
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_e:
                            chek = 1
                            camera_group.custom_draw()
                            Dialogue(enemy)
                            break;

        if tmp_bool:
            tmp -= (vegeta.stats.speed)

            if kiAttack:
                vegeta.hit(CollideKiAttackPosition, vegeta.stats.kiAttack, 'ki')

                if (vegeta.facing == 'up'):
                    screen.blit(rect1, KiAttackPosition)
                    screen.blit(vegeta.image, (vegeta.rect.x-camera_group.offset.x, vegeta.rect.y-camera_group.offset.y))
                else:
                    screen.blit(rect1, KiAttackPosition)
                grass_group.update()
                block_group.update()
                enemy_group.update()
                pg.display.flip()
                if tmp <= 0:
                    tmp=0
                    vegeta.image = image_tmp
                    kiAttack = False
                    tmp_bool = False
            elif tmp <= 0:
                tmp = 0
                vegeta.image = image_tmp
                tmp_bool = False

        for enemy in npc_group:
            if not(kiAttack) and vegeta.rect.colliderect((enemy.dialogie_rect)):
                screen.blit(image_button_e, (enemy.rect.x-camera_group.offset.x, enemy.rect.y-camera_group.offset.y-tile_height/2))
        vegeta.image = pg.transform.scale(vegeta.image, (vegeta.transform[0], vegeta.transform[1]))
        enemy_group.update()
        pg.display.flip()
        clock.tick(fps)
    for i in range(500):
        pass
    file = open("Save/CurrentQuest.txt", 'w').close
    file = open("Save/CompleteQuest.txt", 'w').close
    file = open("Quest/00000/Status.txt", 'w').close
Main();