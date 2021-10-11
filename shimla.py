import pygame
import random
import timeit
import random
start = timeit.timeit()
pygame.init()
pygame.mixer.init()
# display and caption
dw = 1000
dh = 600
WIN = pygame.display.set_mode((dw, dh))
pygame.display.set_caption('Abstruse')
# colors
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
pas = (63, 66, 69)
# fonts
game_name = pygame.font.Font('fonts\\font5.ttf', 70)
map_title = pygame.font.Font('fonts\\font5.ttf', 50)
confirmation = pygame.font.Font('fonts\\font1.ttf', 50)
story_font = pygame.font.Font('fonts\\chat_font.ttf', 20)
fps = 30
clock = pygame.time.Clock()

# backgrounds and images
home_bg = pygame.image.load('home_page\\2.jpg')
play_button = pygame.image.load('buttons\\play2.png')
quit_button = pygame.image.load('buttons\\quit2.png')
map_button = pygame.image.load('buttons\\map1.png')
mute_button = pygame.image.load('buttons\\mute2.png')
sound_button = pygame.image.load('buttons\\sound2.png')
map_image = pygame.image.load('map\\map1.jpg')
cross = pygame.image.load('map\\crucifix.png')
yes_button = pygame.image.load('buttons\\yes2.png')
no_button = pygame.image.load('buttons\\no2.png')
back_button = pygame.image.load('buttons\\back1.png')
control_button = pygame.image.load('buttons\\control1.png')
set_button = pygame.image.load('buttons\\setting2.png')
blood_hand = pygame.image.load('home_page\\bloodHand.png')
lock = pygame.image.load('objects\\lock.png')
unlock = pygame.image.load('objects\\unlock.png')
restart_button = pygame.image.load('buttons\\restart1.png')
resume_button = pygame.image.load('buttons\\resume1.png')
bg_s1 = pygame.image.load('hospital//wakeup3.png')
hos_win = pygame.image.load('hospital\\win_outside3.png')

# pointerImg = pygame.image.load('buttons\\pointer1.png')

# sound tracks
pygame.mixer.music.load("sounds\\home1.mp3")

# loop controllers
home = True
game_loop = True
maps = False
background_music = True
areYouSure = False
after_play_click = False
hospital_window = False
scene1_loop = True
hos_cup = False
hos_tv = False
scene2_loop = False
scene3_loop = False
scene6_loop = False
scene4_loop = False
scene5_loop = False
scene7_loop = False
# state save
map_key = False

# load player
walkRight = [pygame.image.load('charectors\\main_char\\r1.png'), pygame.image.load('charectors\\main_char\\r2.png'), pygame.image.load('charectors\\main_char\\r3.png'),
             pygame.image.load('charectors\\main_char\\r4.png'), pygame.image.load('charectors\\main_char\\r5.png'), pygame.image.load('charectors\\main_char\\r6.png'),
             pygame.image.load('charectors\\main_char\\r7.png'), pygame.image.load('charectors\\main_char\\r8.png'), pygame.image.load('charectors\\main_char\\r9.png'),
             pygame.image.load('charectors\\main_char\\r10.png'), pygame.image.load('charectors\\main_char\\r11.png'), pygame.image.load('charectors\\main_char\\r12.png')]

walkLeft = [pygame.image.load('charectors\\main_char\\l1.png'), pygame.image.load('charectors\\main_char\\l2.png'), pygame.image.load('charectors\\main_char\\l3.png'),
            pygame.image.load('charectors\\main_char\\l4.png'), pygame.image.load('charectors\\main_char\\l5.png'), pygame.image.load('charectors\\main_char\\l6.png'),
            pygame.image.load('charectors\\main_char\\l7.png'), pygame.image.load('charectors\\main_char\\l8.png'), pygame.image.load('charectors\\main_char\\l9.png'),
            pygame.image.load('charectors\\main_char\\l10.png'), pygame.image.load('charectors\\main_char\\l11.png'), pygame.image.load('charectors\\main_char\\l12.png')]

walkUp = [pygame.image.load('charectors\\main_char\\u1.png'), pygame.image.load('charectors\\main_char\\u2.png'), pygame.image.load('charectors\\main_char\\u3.png'),
          pygame.image.load('charectors\\main_char\\u4.png'), pygame.image.load('charectors\\main_char\\u5.png'), pygame.image.load('charectors\\main_char\\u6.png'),
          pygame.image.load('charectors\\main_char\\u7.png'), pygame.image.load('charectors\\main_char\\u8.png'), pygame.image.load('charectors\\main_char\\u9.png'),
          pygame.image.load('charectors\\main_char\\u10.png'), pygame.image.load('charectors\\main_char\\u11.png'), pygame.image.load('charectors\\main_char\\u12.png')]

walkDown = [pygame.image.load('charectors\\main_char\\D1.png'), pygame.image.load('charectors\\main_char\\D2.png'), pygame.image.load('charectors\\main_char\\D3.png'),
            pygame.image.load('charectors\\main_char\\D4.png'), pygame.image.load('charectors\\main_char\\D5.png'), pygame.image.load('charectors\\main_char\\D6.png'),
            pygame.image.load('charectors\\main_char\\D7.png'), pygame.image.load('charectors\\main_char\\D8.png'), pygame.image.load('charectors\\main_char\\D9.png'),
            pygame.image.load('charectors\\main_char\\D10.png'), pygame.image.load('charectors\\main_char\\D11.png'), pygame.image.load('charectors\\main_char\\D12.png')]


# image resize
bg_s1 = pygame.transform.scale(bg_s1, (dw, dh))
hos_win = pygame.transform.scale(hos_win, (dw, dh))
home_bg = pygame.transform.scale(home_bg, (dw, dh))
map_image = pygame.transform.scale(map_image, (dw, dh))
# pointerImg = pygame.transform.scale(pointerImg, (10, int(10*pointerImg.get_height()/pointerImg.get_width())))
r = play_button.get_height() / play_button.get_width()
play_button = pygame.transform.scale(play_button,
                                     (int(dw / 6), int(dw / 6 * r)))  # change the value
# of divisor to change button size
quit_button = pygame.transform.scale(quit_button, (int(dw / 6), int(dw / 6 * r)))
r = map_button.get_height() / map_button.get_width()
map_button = pygame.transform.scale(map_button, (int(dw / 30), int(dw / 30 * r)))
map_lock = pygame.transform.scale(lock, (
int(map_button.get_width() / 2), int(map_button.get_width() / 2 * lock.get_height() / lock.get_width())))
map_unlock = pygame.transform.scale(unlock, (
int(map_button.get_width() / 2), int(map_button.get_width() / 2 * unlock.get_height() / unlock.get_width())))
cross = pygame.transform.scale(cross, (50, int(50 * cross.get_height() / cross.get_width())))
mute_button = (pygame.transform.scale(mute_button, (int(map_button.get_width()),
                                                    int(map_button.get_width() * (
                                                            mute_button.get_height() / mute_button.get_width())))))
sound_button = (pygame.transform.scale(sound_button, (int(map_button.get_width()),
                                                      int(map_button.get_width() * (
                                                              sound_button.get_height() / sound_button.get_width())))))
yes_button = pygame.transform.scale(yes_button, (int(dw / 9),
                                                 int(dw / 8 * yes_button.get_height() / yes_button.get_width())))
no_button = pygame.transform.scale(no_button, (int(dw / 9),
                                               int(dw / 9 * no_button.get_height() / no_button.get_width())))

restart_button = pygame.transform.scale(restart_button, (int(dw / 9),
                                                         int(
                                                             dw / 9 * restart_button.get_height() / restart_button.get_width())))
resume_button = pygame.transform.scale(resume_button, (int(dw / 9),
                                                       int(
                                                           dw / 9 * resume_button.get_height() / resume_button.get_width())))

back_button = pygame.transform.scale(back_button, (int(dw / 7),
                                                   int(dw / 7 * back_button.get_height() / back_button.get_width())))
r = control_button.get_height() / control_button.get_width()
control_button = pygame.transform.scale(control_button, (int(dw / 6), int(dw / 6 * r)))

set_button = pygame.transform.scale(set_button, (int(map_button.get_width()),
                                                 int(map_button.get_width() * set_button.get_height() / set_button.get_width())))
blood_hand = pygame.transform.scale(blood_hand, (int(dw / 5),
                                                 int(dw / 5 * blood_hand.get_height() / blood_hand.get_width())))
blood_hand = pygame.transform.rotate(blood_hand, random.randint(-20, 30))
hand_xy = (random.randint(20, 40), random.randint(180, 250))
map_xy = (dw - 40, dh / 2 + 150)
sound_xy = (map_xy[0], map_xy[1] + 50)
setting_xy = (map_xy[0], sound_xy[1] + 50)
text_box = pygame.image.load('objects\\text_box.png')
text_box = pygame.transform.scale(text_box, (dw-100, dh//8))
close_box = pygame.image.load('objects\\down_box.png')
close_box = pygame.transform.scale(close_box, (30, int(30*close_box.get_height()/close_box.get_width())))
text_box_xy = ((dw-text_box.get_width())//2, dh-text_box.get_height())
close_box_xy = (int(text_box_xy[0]+(text_box.get_width()-close_box.get_width())/2), text_box_xy[1]+10)
text1 = True
win_text = False
text1_end = False
# bag of player
player_bag = {"key_for_room2": False, "key_for_room3": False, 'room1_closet_key': False, 'screwdriver': False, 'torch_flag': False, 'exit_door_key': False, 'fuel': False, 'van_key': False, 'med_file': False}

open_bag = False
unlock_room2 = False
unlock_room3 = False


# overlay function
def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def highlighter(color, rect):
    global WIN
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    WIN.blit(shape_surf, rect)


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        # self.isJump = False
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        # self.jumpCount = 10
        self.standing = True
        self.wl = []
        self.wr = []
        self.wu = []
        self.wd = []

        for images in walkLeft:
            images = pygame.transform.scale(images, (self.height*images.get_width()//images.get_height(), self.height))
            self.wl.append(images)
        for images in walkRight:
            images = pygame.transform.scale(images, (self.height*images.get_width()//images.get_height(), self.height))
            self.wr.append(images)
        for images in walkUp:
            images = pygame.transform.scale(images, (self.height*images.get_width()//images.get_height(), self.height))
            self.wu.append(images)
        for images in walkDown:
            images = pygame.transform.scale(images, (self.height*images.get_width()//images.get_height(), self.height))
            self.wd.append(images)

    def draw(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                WIN.blit(self.wl[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                WIN.blit(self.wr[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                WIN.blit(self.wu[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                WIN.blit(self.wd[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                WIN.blit(self.wr[4], (self.x, self.y))
            elif self.left:
                WIN.blit(self.wl[4], (self.x, self.y))
            elif self.up:
                WIN.blit(self.wu[4], (self.x, self.y))
            else:
                WIN.blit(self.wd[4], (self.x, self.y))


next_arrow_scene1 = pygame.image.load('buttons\\continue1.png')
next_arrow_scene1 = pygame.transform.scale(next_arrow_scene1, (dw//10, dw//10*next_arrow_scene1.get_height()//next_arrow_scene1.get_width()))


def scene1():
    global WIN, clock, bg_s1, open_bag, hospital_window, scene1_loop, hos_cup, hos_tv, background_music, maps, text1, win_text, text1_end, scene2_loop, Player
    bg = bg_s1

    while scene1_loop:
        clock.tick(36)
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        else:
            man.standing = True
            man.walkCount = 0

        WIN.blit(bg, (0, 0))
        WIN.blit(next_arrow_scene1, (dw-200, dh-50))
        # man.draw()
        # side icons
        WIN.blit(map_button, map_xy)
        if map_key:
            WIN.blit(map_unlock, (map_xy[0] - 10, map_xy[1] - 10))
        elif not map_key:
            WIN.blit(map_lock, (map_xy[0] - 10, map_xy[1] - 10))
        WIN.blit(set_button, setting_xy)
        if background_music:
            WIN.blit(sound_button, sound_xy)
        elif not background_music:
            WIN.blit(mute_button, sound_xy)

        # interactive object rectangles
        rect_dim_win = (583, 0, 187, 66)
        rect_dim_cub1 = (851, 0, 200, 190)
        rect_dim_cub2 = (851, 210, 200, 225)
        rect_dim_tv = (623, 68, 70, 85)
        next_dim_rect = (dw-200, dh-50, next_arrow_scene1.get_width(), next_arrow_scene1.get_height())
        if text1 and not text1_end:
            storytext('What is this place Where am I What happened to me and who i am')
        if pos[0] in range(rect_dim_win[0], rect_dim_win[0]+rect_dim_win[2]) and pos[1] in range(rect_dim_win[1], rect_dim_win[1]+rect_dim_win[3]):  # Interact to window
            highlighter((0, 0, 0, 128), rect_dim_win)
            # if text1_end:
            #     text1 = False
            # win_text = True
            # if win_text:
            mousetext("See Outside Window", pos)

        elif pos[0] in range(rect_dim_cub1[0], rect_dim_cub1[0]+rect_dim_cub1[2]) and pos[1] in range(rect_dim_cub1[1], rect_dim_cub1[1]+rect_dim_cub1[3]):  # Interact to window
            highlighter((0, 0, 0, 128), rect_dim_cub1)
            mousetext("Open closet", pos)

        elif pos[0] in range(rect_dim_cub2[0], rect_dim_cub2[0]+rect_dim_cub2[2]) and pos[1] in range(rect_dim_cub2[1], rect_dim_cub2[1]+rect_dim_cub2[3]):  # Interact to window
            highlighter((0, 0, 0, 128), rect_dim_cub2)
            mousetext("Open closet", pos)

        elif pos[0] in range(rect_dim_tv[0], rect_dim_tv[0]+rect_dim_tv[2]) and pos[1] in range(rect_dim_tv[1], rect_dim_tv[1]+rect_dim_tv[3]):  # Interact to window
            highlighter((0, 0, 0, 128), rect_dim_tv)
            # if text1_end:
            #     text1 = False
            # # cub_text = False
            # tv_text = True
            # if tv_text:
            mousetext("See monitor", pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene1_loop = False
            elif event.type == pygame.MOUSEBUTTONUP and pos[0] in range(rect_dim_win[0], rect_dim_win[0]+rect_dim_win[2]) and pos[1] in range(rect_dim_win[1], rect_dim_win[1]+rect_dim_win[3]):
                hospital_window = True
                win_text = False
                text1_end = False
                hospital_window_scene()
            elif event.type == pygame.MOUSEBUTTONUP and pos[0] in range(rect_dim_cub1[0], rect_dim_cub1[0]+rect_dim_cub1[2]) and pos[1] in range(rect_dim_cub1[1], rect_dim_cub1[1]+rect_dim_cub1[3]):
                # cupboard_loop = True
                # cub_text = False
                hos_cup = True
                cupboard()
            elif event.type == pygame.MOUSEBUTTONUP and pos[0] in range(rect_dim_cub2[0], rect_dim_cub2[0]+rect_dim_cub2[2]) and pos[1] in range(rect_dim_cub2[1], rect_dim_cub2[1]+rect_dim_cub2[3]):
                # cupboard_loop = True
                # cub_text = False
                if player_bag['room1_closet_key']:
                    open_bag = True
                    unlock_closet_room1 = bag('room1_closet_keyr')
                    if unlock_closet_room1 == 1:
                        hos_cup = True
                        cupboard(1)
                else:
                    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
                    instruction('You need key')
            elif event.type == pygame.MOUSEBUTTONUP and pos[0] in range(rect_dim_tv[0], rect_dim_tv[0]+rect_dim_tv[2]) and pos[1] in range(rect_dim_tv[1], rect_dim_tv[1]+rect_dim_tv[3]):
                # cupboard_loop = True
                # cub_text = False
                hos_tv = True
                hos_monitor()
            elif event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(map_xy[0]), int(map_xy[0] + map_button.get_width())) and pos[1] in range(
                        int(map_xy[1]), int(map_xy[1] + map_button.get_height())) and map_key:

                    maps = True
                    game_map()

                # click on sound
                elif pos[0] in range(int(sound_xy[0]), int(sound_xy[0] + sound_button.get_width())) and pos[1] in range(
                        int(sound_xy[1]), int(sound_xy[1] + sound_button.get_height())):
                    if background_music:
                        pygame.mixer.music.pause()
                        background_music = False
                    elif not background_music:
                        pygame.mixer.music.unpause()
                        background_music = True
                # if pos[0] in range(int(close_box_xy[0]), int(close_box_xy[0] + close_box.get_width())) and pos[
                #     1] in range(
                #         int(close_box_xy[1]), int(close_box_xy[1] + close_box.get_height())):
                #     text1_end = True
                if pos[0] in range(next_dim_rect[0], next_dim_rect[0]+next_dim_rect[2]) and pos[1] in range(next_dim_rect[1], next_dim_rect[1]+next_dim_rect[3]):
                    scene1_loop = False
                    scene2_loop = True

                    scene2()
        pygame.display.update()

    pygame.quit()


def hos_monitor():
    global hos_tv, scene1_loop
    tv = pygame.image.load('hospital\\display.jpg')
    hr = pygame.image.load('hospital\\heart_rate.png')
    disp = pygame.font.Font('fonts\\dis_font.otf', 40)
    num = disp.render('PATIENT 18', True, blue)
    tv = pygame.transform.scale(tv, (dw//3, dw//3*tv.get_height()//tv.get_width()))
    hr = pygame.transform.scale(hr, (tv.get_width()-50, (tv.get_width()-50)*hr.get_height()//hr.get_width()))
    tv_xy = ((dw - tv.get_width()) // 2, (dh - tv.get_height()) // 2)

    draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))
    while hos_tv:
        pos = pygame.mouse.get_pos()
        WIN.blit(tv, tv_xy)
        WIN.blit(hr, (tv_xy[0]+10, tv_xy[1]+(tv.get_height()-hr.get_height())//2))
        WIN.blit(num, [tv_xy[0]+(tv.get_width()-num.get_width())//2, tv_xy[1]+30])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hos_tv = False
                scene1_loop = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if pos[0] not in range(tv_xy[0], tv_xy[0]+tv.get_width()) or pos[1] not in range(tv_xy[1], tv_xy[1]+tv.get_height()):
                    hos_tv = False
        pygame.display.update()


def bag(request=None):
    global open_bag, player_bag
    bag_image = pygame.image.load('objects\\bag.png')
    bag_image = pygame.transform.scale(bag_image, (dw//3, dw//3*bag_image.get_height()//bag_image.get_width()))
    bag_xy = (2 * dw // 3, (dh - bag_image.get_height()) // 2)

    # elements in bag
    door_key1 = pygame.image.load('hospital\\key.png')
    door_key2 = door_key1
    screwdriver_map = pygame.image.load('objects\\screwdriver.png')
    room1_ck = pygame.image.load('objects\\room1_closet_key.png')
    torch = pygame.image.load('objects\\torch.png')
    exit_key = pygame.image.load('objects\\exit_door_key.png')
    vehicle_key = pygame.image.load('objects\\van_key.png')
    file_image = pygame.image.load('objects\\med_file.png')
    # room 2 key
    object_list_temp = [door_key1, door_key2, screwdriver_map, room1_ck, torch, exit_key, vehicle_key, file_image]
    object_list = []
    object_rect = []
    for objects in object_list_temp:
        objects = pygame.transform.scale(objects, (bag_image.get_width() // 4, bag_image.get_width() // 4 * objects.get_height() // objects.get_width()))
        object_list.append(objects)
    del object_list_temp
    count = 0
    # hover rectangle
    for o in object_list:
        count += 1
        if count <= 4:
            object_rect.append((dw//3, 70*count, o.get_width(), o.get_height()))
        elif 4 < count <= 8:
            object_rect.append((dw // 6, 70 * (count-4), o.get_width(), o.get_height()))

    # overlay
    draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))

    # add all the player_bag flags here
    object_list.append('key_for_room2')
    object_list.append('key_for_room3')
    object_list.append('screwdriver')
    object_list.append('room1_closet_key')
    object_list.append('torch_flag')
    object_list.append('exit_door_key')
    object_list.append('van_key')
    object_list.append('med_file')
    while open_bag:
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        # WIN.blit(bag_texture, (dw//5, (dh-bag_texture.get_height())//2))
        WIN.blit(bag_image, bag_xy)
        # blit objects
        for i in range(0, len(object_list)//2):
            if player_bag[object_list[i+len(object_list)//2]]:
                WIN.blit(object_list[i], (object_rect[i][0], object_rect[i][1]))
        # clicks and events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif keys[pygame.K_x]:
                open_bag = False
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(0, len(object_list) // 2):
                    if pos[0] in range(object_rect[i][0], object_rect[i][0]+object_rect[i][2]) and pos[1] in range(object_rect[i][1], object_rect[i][1]+object_rect[i][3]) and request == object_list[i+len(object_list)//2]+'r':
                        instruction('unlocked')
                        open_bag = False
                        return 1
                    if object_list[i+len(object_list)//2] == 'med_file':
                        if pos[0] in range(object_rect[i][0], object_rect[i][0] + object_rect[i][2]) and pos[1] in range(object_rect[i][1], object_rect[i][1] + object_rect[i][3]):
                            report()
                            open_bag = False
        pygame.display.update()
    return 0


def report(img='objects\\med_file.png'):
    med = pygame.image.load(img)
    med = pygame.transform.scale(med, (int(4*dw/5), int((4*dw/5)*med.get_height()/med.get_width())))
    loop = True
    while loop:
        pos = pygame.mouse.get_pos()
        WIN.blit(med, ((dw-med.get_width())//2, (dh-med.get_height())//2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] not in range((dw-med.get_width())//2, (dw-med.get_width())//2+med.get_width()) or pos[1] not in range((dh-med.get_height())//2, (dh-med.get_height())//2+med.get_height()):
                    loop = False
        pygame.display.update()


def cupboard(choice=0):
    global hos_cup, scene1_loop, player_bag
    cup_open = pygame.image.load('hospital\\cup_inside.jpg')
    door_key = pygame.image.load('hospital\\key.png')
    key_hover = pygame.image.load('hospital\\key_light.png')
    torch_image = pygame.image.load('objects\\torch.png')

    cup_open = pygame.transform.scale(cup_open, (dw//3, dw//3*cup_open.get_height()//cup_open.get_width()))
    door_key = pygame.transform.scale(door_key, (cup_open.get_width()//3, cup_open.get_width()//3*door_key.get_height()//door_key.get_width()))
    key_hover = pygame.transform.scale(key_hover, (int(cup_open.get_width() / 2.5), int(cup_open.get_width() / 2.5 * key_hover.get_height() // key_hover.get_width())))
    torch_image = pygame.transform.scale(torch_image, (cup_open.get_width() // 3, cup_open.get_width() // 3 * torch_image.get_height() // torch_image.get_width()))
    cup_xy = ((dw-cup_open.get_width())//2, (dh-cup_open.get_height())//2)
    draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))
    door_key_xy = (cup_xy[0]+50, cup_xy[1]+30)
    disp_key = door_key
    hover_rect = (door_key_xy[0], door_key_xy[1] + 15, 50, 50)
    while hos_cup:
        pos = pygame.mouse.get_pos()
        WIN.blit(cup_open, cup_xy)
        if choice == 0:
            if not player_bag["key_for_room2"]:
                WIN.blit(disp_key, door_key_xy)
            if pos[0] in range(door_key_xy[0], door_key_xy[0]+50) and pos[1] in range(door_key_xy[1], door_key_xy[1]+50):
                disp_key = key_hover
            else:
                disp_key = door_key
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hos_cup = False
                    scene1_loop = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if pos[0] in range(hover_rect[0], hover_rect[0] + hover_rect[2]) and pos[1] in range(hover_rect[1],
                                                                                                         hover_rect[1] +
                                                                                                         hover_rect[3]):
                        instruction('Item collected in bag')
                        player_bag["key_for_room2"] = True
                    if pos[0] not in range(cup_xy[0], cup_xy[0] + cup_open.get_width()) or pos[1] not in range(
                            cup_xy[1], cup_xy[1] + cup_open.get_height()):
                        hos_cup = False
        elif choice == 1:
            if not player_bag["torch_flag"]:
                WIN.blit(torch_image, door_key_xy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hos_cup = False
                    scene1_loop = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if pos[0] in range(hover_rect[0], hover_rect[0] + hover_rect[2]) and pos[1] in range(hover_rect[1],
                                                                                                         hover_rect[1] +
                                                                                                         hover_rect[3]):
                        instruction('Item collected in bag')
                        player_bag["torch_flag"] = True
                    if pos[0] not in range(cup_xy[0], cup_xy[0] + cup_open.get_width()) or pos[1] not in range(
                            cup_xy[1], cup_xy[1] + cup_open.get_height()):
                        hos_cup = False

        pygame.display.update()


def drawer(items, no=0, img='open_drawer'):
    loop = True
    drawer_bg = pygame.image.load('objects\\'+str(img)+'.png')
    drawer_bg = pygame.transform.scale(drawer_bg, (dw//2, dw//2*drawer_bg.get_height()//drawer_bg.get_width()))
    drawer_xy = ((dw - drawer_bg.get_width()) // 2, (dh - drawer_bg.get_height()) // 2)
    item_images = []
    for item in items:
        i = pygame.image.load('objects\\'+item+'.png')
        i = pygame.transform.scale(i, (drawer_bg.get_width()//3, int(drawer_bg.get_width()/3*i.get_height()/i.get_width())))
        item_images.append(i)

    draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))
    while loop:
        item_rect = []
        pos = pygame.mouse.get_pos()
        WIN.blit(drawer_bg, drawer_xy)
        count = 0
        for images in item_images:
            count += 1
            if count == 1 or count == 2:
                xy = (drawer_xy[0]+count*drawer_bg.get_height()//3-30, drawer_xy[1]+20)
                WIN.blit(images, xy)
                item_rect.append((xy[0], xy[1], images.get_width(), images.get_height()))
            elif count == 3 or count == 4:
                xy = (drawer_xy[0] + (count-2) * drawer_bg.get_width() // 3 - 30, drawer_xy[1] + drawer_bg.get_height() - images.get_height() - 20)
                WIN.blit(images, xy)
                item_rect.append((xy[0], xy[1], images.get_width(), images.get_height()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] not in range(drawer_xy[0], drawer_xy[0]+drawer_bg.get_width()) or pos[1] not in range(drawer_xy[1], drawer_xy[1]+drawer_bg.get_height()):
                    loop = False
                for i in range(0, len(item_images)):
                    if pos[0] in range(item_rect[i][0], item_rect[i][0]+item_rect[i][2]) and pos[1] in range(item_rect[i][1], item_rect[i][1]+item_rect[i][3]):
                        # if item[i] in player_bag:
                        if items[i] in player_bag.keys():
                            instruction('Item collected in bag')
                            player_bag[items[i]] = True
                            if no != 0:
                                drawer_items[no-1].remove(items[i])
                            del item_images[i]
                            del item_rect[i]

        del item_rect
        pygame.display.update()


def storytext(story, color=red):
    global text1_end
    line = story_font.render(story, True, color)
    if not text1_end:
        draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
    while not text1_end:
        pos = pygame.mouse.get_pos()
        WIN.blit(text_box, text_box_xy)
        WIN.blit(line, [text_box_xy[0]+(text_box.get_width()-line.get_width())//2, text_box_xy[1]+(text_box.get_height()-line.get_height())//2])
        WIN.blit(close_box, close_box_xy)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(close_box_xy[0]), int(close_box_xy[0] + close_box.get_width())) and pos[
                    1] in range(
                    int(close_box_xy[1]), int(close_box_xy[1] + close_box.get_height())):
                    text1_end = True
        pygame.display.update()

def mousetext(text, pos, color=red):
    at = [0, 0]
    mouse_font = pygame.font.Font('fonts\\chat_font.ttf', 10)
    msg = mouse_font.render(text, True, color)
    if pos[0]+msg.get_width() <= dw:
        at[0] = pos[0]+10
    elif pos[0]+msg.get_width() > dw:
        at[0] = pos[0]-(pos[0]+msg.get_width()-dw)
    if pos[1]+msg.get_height() <= dh:
        at[1] = pos[1]+10
    elif pos[1]+msg.get_height() > dh:
        at[1] = pos[1]-(pos[1]+msg.get_height()-dh)
    WIN.blit(msg, at)



def hospital_window_scene():
    global hospital_window, scene1_loop, text1_end
    while hospital_window:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hospital_window = False
                scene1_loop = False
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(10), int(10 + back_button.get_width())) \
                        and pos[1] in range(int(50), int(50 + back_button.get_height())):
                    hospital_window = False

        WIN.blit(hos_win, (0, (dh - hos_win.get_height()) // 2))
        WIN.blit(back_button, [10, 50])

        storytext("whoaa mountains looks like I am in trouble")
        pygame.display.update()


def home_page():
    global home, maps, background_music, areYouSure, blood_hand, map_key, after_play_click
    pygame.mixer.music.play()
    name = game_name.render('ABSTRUSE', True, red)
    w = name.get_width()

    play_xy = ((dw - play_button.get_width()) / 2, dh / 2 + 50)
    control_xy = ((dw - control_button.get_width()) / 2, play_xy[1] + 80)
    quit_xy = ((dw - quit_button.get_width()) / 2, control_xy[1] + 80)

    while home:

        # WIN.blit(pointerImg, (pos[0], pos[1]))
        WIN.blit(home_bg, (0, 0))
        draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
        WIN.blit(name, [(dw - w) / 2, dh / 7])
        # display buttons
        WIN.blit(play_button, play_xy)
        WIN.blit(quit_button, quit_xy)
        WIN.blit(control_button, control_xy)
        WIN.blit(blood_hand, hand_xy)
        # side icons from here
        pos = pygame.mouse.get_pos()
        WIN.blit(map_button, map_xy)
        if map_key:
            WIN.blit(map_unlock, (map_xy[0] - 10, map_xy[1] - 10))
        elif not map_key:
            WIN.blit(map_lock, (map_xy[0] - 10, map_xy[1] - 10))
        WIN.blit(set_button, setting_xy)
        if background_music:
            WIN.blit(sound_button, sound_xy)
        elif not background_music:
            WIN.blit(mute_button, sound_xy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(quit_xy[0]), int(quit_xy[0] + quit_button.get_width())) and pos[1] in range(
                        int(quit_xy[1]), int(quit_xy[1] + quit_button.get_height())):
                    home = False
                    areYouSure = True
                    sure()
                elif pos[0] in range(int(map_xy[0]), int(map_xy[0] + map_button.get_width())) and pos[1] in range(
                        int(map_xy[1]), int(map_xy[1] + map_button.get_height())) and map_key:

                    maps = True
                    game_map()
                elif pos[0] in range(int(map_xy[0]), int(map_xy[0] + map_button.get_width())) and pos[1] in range(
                        int(map_xy[1]), int(map_xy[1] + map_button.get_height())) and not map_key:
                    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
                    instruction("You need to find map")

                # click on sound
                elif pos[0] in range(int(sound_xy[0]), int(sound_xy[0] + sound_button.get_width())) and pos[1] in range(
                        int(sound_xy[1]), int(sound_xy[1] + sound_button.get_height())):
                    if background_music:
                        pygame.mixer.music.pause()
                        background_music = False
                    elif not background_music:
                        pygame.mixer.music.unpause()
                        background_music = True
                elif pos[0] in range(int(play_xy[0]), int(play_xy[0] + play_button.get_width())) and pos[1] in range(
                        int(play_xy[1]), int(play_xy[1] + play_button.get_height())):
                    home = False
                    after_play_click = True
                    play_options()
        pygame.display.update()


def sure():
    global areYouSure, home, maps, background_music
    ques = confirmation.render('Are you sure', True, blue)
    ques_xy = ((dw - ques.get_width()) / 2, (dh - ques.get_height()) / 2)
    yes_xy = (ques_xy[0]-30, ques_xy[1] + 100)
    no_xy = (ques_xy[0] + ques.get_width() - no_button.get_width()+30, ques_xy[1] + 100)
    back_x = 10
    back_y = 10
    while areYouSure:
        pos = pygame.mouse.get_pos()
        # WIN.blit(pointerImg, (pos[0], pos[1]))
        WIN.blit(home_bg, (0, 0))
        draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))
        # draw_rect_alpha(WIN, (0, 0, 0, 128), ((dw-w)/2, (dh-h) / 2, w, h))
        WIN.blit(ques, ques_xy)
        WIN.blit(yes_button, yes_xy)
        WIN.blit(no_button, no_xy)
        WIN.blit(back_button, [back_x, back_y])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                areYouSure = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(yes_xy[0]), int(yes_xy[0] + yes_button.get_width())) and pos[1] in range(
                        int(yes_xy[1]), int(yes_xy[1] + yes_button.get_height())):
                    areYouSure = False
                elif pos[0] in range(int(no_xy[0]), int(no_xy[0] + no_button.get_width())) and pos[1] in range(
                        int(no_xy[1]), int(no_xy[1] + no_button.get_height())) or pos[0] in range(int(back_x), int(
                    back_x + back_button.get_width())) \
                        and pos[1] in range(int(back_y), int(back_y + back_button.get_height())):
                    areYouSure = False
                    home = True
                    home_page()
        pygame.display.update()


def play_options():
    global after_play_click, home
    back_x = 10
    back_y = 10
    ques = confirmation.render('Play Options', True, blue)
    ques_xy = ((dw - ques.get_width()) / 2, (dh - ques.get_height()) / 2)
    restart_xy = (ques_xy[0], ques_xy[1] + 100)
    resume_xy = (ques_xy[0] + ques.get_width() - resume_button.get_width(), ques_xy[1] + 100)
    while after_play_click:
        pos = pygame.mouse.get_pos()
        WIN.blit(home_bg, (0, 0))
        draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))
        WIN.blit(ques, ques_xy)
        WIN.blit(restart_button, restart_xy)
        WIN.blit(resume_button, resume_xy)
        WIN.blit(back_button, [back_x, back_y])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                after_play_click = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(restart_xy[0]), int(restart_xy[0] + restart_button.get_width())) and pos[
                    1] in range(
                        int(restart_xy[1]), int(restart_xy[1] + restart_button.get_height())):
                    after_play_click = False
                    instruction('Remember to explore each corner')
                    scene1()
                if pos[0] in range(int(back_x), int(back_x + back_button.get_width())) \
                        and pos[1] in range(int(back_y), int(back_y + back_button.get_height())):
                    after_play_click = False
                    home = True
                    home_page()
                    after_play_click = False
                elif pos[0] in range(int(resume_xy[0]), int(resume_xy[0] + resume_button.get_width())) and pos[
                    1] in range(
                        int(resume_xy[1]), int(resume_xy[1] + resume_button.get_height())):
                    after_play_click = False
                    scene1()
                    after_play_click = False
        pygame.display.update()


def game_map(choice=0):
    global maps, home, scene1_loop
    back_x = 10
    back_y = 10
    cross_x = 300
    cross_y = 300
    while maps:
        pos = pygame.mouse.get_pos()
        map_name = map_title.render('SHIMLA', True, yellow)
        w = map_name.get_width()
        WIN.blit(map_image, (0, 0))
        WIN.blit(map_name, [(dw - w) / 2, 10])
        WIN.blit(back_button, [back_x, back_y])
        WIN.blit(cross, [cross_x, cross_y])
        WIN.blit(back_button, [back_x, back_y])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                maps = False
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(back_x), int(back_x + back_button.get_width())) \
                        and pos[1] in range(int(back_y), int(back_y + back_button.get_height())):
                    maps = False
                    # if choice == 1:
                    #     scene1_loop = True
                    # elif choice == 0:

                    home_page()


# scene 2 variables
bg_scene2 = pygame.image.load('hospital\\corridor.jpg')
map_hover = pygame.image.load('objects\\frame.png')
map_hover_rect = (453, 256, 84, 115)
map_hover = pygame.transform.scale(map_hover, (map_hover_rect[2], map_hover_rect[3]))
bg_scene2 = pygame.transform.scale(bg_scene2, (dw, dh))
man = Player(20, 2*dh/3, 50, 110)
rect_dim_room2 = (dw*0.18, dh*0.475, dw*0.1, dh//3)
rect_dim_room3 = (dw*0.84, dh*0.475, dw*0.1, dh//3)


def scene2(spawn=1):
    global scene2_loop, Player, scene1_loop, open_bag, scene3_loop, scene7_loop, unlock_room2, unlock_room3, open_bag, scene5_loop, map_key, maps, background_music, scene4_loop, text1_end,scene7_loop
    if spawn == 2:
        man.x = dw - man.width - 100
        man.y = 2*dh/3+100
    elif spawn == 1:
        man.x = 100
        man.y = 2*dh/3+100

    while scene2_loop:
        clock.tick(36)
        WIN.blit(bg_scene2, (0, 0))
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        WIN.blit(map_button, map_xy)
        if map_key:
            WIN.blit(map_unlock, (map_xy[0] - 10, map_xy[1] - 10))
        elif not map_key:
            WIN.blit(map_lock, (map_xy[0] - 10, map_xy[1] - 10))
        WIN.blit(set_button, setting_xy)
        if background_music:
            WIN.blit(sound_button, sound_xy)
        elif not background_music:
            WIN.blit(mute_button, sound_xy)

        if pos[0] in range(int(rect_dim_room2[0]), int(rect_dim_room2[0]+rect_dim_room2[2])) and pos[1] in range(int(rect_dim_room2[1]), int(rect_dim_room2[1]+rect_dim_room2[3])) and man.x in range(int(rect_dim_room2[0]), int(rect_dim_room2[0]+rect_dim_room2[2])):  # Interact to window
            highlighter((0, 0, 0, 128), rect_dim_room2)
            mousetext("Open Room", pos)

        elif pos[0] in range(int(rect_dim_room3[0]), int(rect_dim_room3[0]+rect_dim_room3[2])) and pos[1] in range(int(rect_dim_room3[1]), int(rect_dim_room3[1]+rect_dim_room3[3])) and man.x in range(int(rect_dim_room3[0]), int(rect_dim_room3[0]+rect_dim_room3[2])):  # Interact to window
            highlighter((0, 0, 0, 128), rect_dim_room3)
            mousetext("Open Room", pos)

        elif pos[0] in range(map_hover_rect[0], map_hover_rect[0]+map_hover_rect[2]) and pos[1] in range(map_hover_rect[1], map_hover_rect[1]+map_hover_rect[3]) and man.x in range(map_hover_rect[0], map_hover_rect[0]+map_hover_rect[2]):
            WIN.blit(map_hover, (map_hover_rect[0], map_hover_rect[1]))
            mousetext('See photo', pos)

        if keys[pygame.K_LEFT]:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
            man.up = False
            man.down = False
        elif keys[pygame.K_RIGHT] and man.x < dw - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
            man.up = False
            man.down = False

        elif keys[pygame.K_UP] and man.y > 385:
            man.y -= man.vel
            man.up = True
            man.right = False
            man.left = False
            man.standing = False
            man.down = False
        elif keys[pygame.K_DOWN] and man.y < dh - man.height - man.vel + 30:
            man.y += man.vel
            man.down = True
            man.right = False
            man.left = False
            man.standing = False
            man.up = False
        elif keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        else:
            man.standing = True
            man.walkCount = 0

        man.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene2_loop = False

            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(int(map_xy[0]), int(map_xy[0] + map_button.get_width())) and pos[1] in range(
                        int(map_xy[1]), int(map_xy[1] + map_button.get_height())) and map_key:
                    maps = True
                    game_map()
                elif pos[0] in range(int(map_xy[0]), int(map_xy[0] + map_button.get_width())) and pos[1] in range(
                        int(map_xy[1]), int(map_xy[1] + map_button.get_height())) and not map_key:
                    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
                    instruction("You need to find map")

                # click on sound
                elif pos[0] in range(int(sound_xy[0]), int(sound_xy[0] + sound_button.get_width())) and pos[1] in range(
                        int(sound_xy[1]), int(sound_xy[1] + sound_button.get_height())):
                    if background_music:
                        pygame.mixer.music.pause()
                        background_music = False
                    elif not background_music:
                        pygame.mixer.music.unpause()
                        background_music = True
                if pos[0] in range(int(rect_dim_room2[0]), int(rect_dim_room2[0]+rect_dim_room2[2])) and pos[1] in range(int(rect_dim_room2[1]), int(rect_dim_room2[1]+rect_dim_room2[3])) and man.x in range(int(rect_dim_room2[0]), int(rect_dim_room2[0]+rect_dim_room2[2])):  # Interact to window

                    if not player_bag["key_for_room2"]:
                        instruction("You need key")
                    else:
                        open_bag = True
                        unlock_room2 = bag('key_for_room2r')
                        if unlock_room2:
                            scene3_loop = True
                            scene3()

                elif pos[0] in range(int(rect_dim_room3[0]), int(rect_dim_room3[0]+rect_dim_room3[2])) and pos[1] in range(int(rect_dim_room3[1]), int(rect_dim_room3[1]+rect_dim_room3[3])) and man.x in range(int(rect_dim_room3[0]), int(rect_dim_room3[0]+rect_dim_room3[2])):  # Interact to window

                    if not player_bag["key_for_room3"]:
                        instruction("You need key")
                    else:
                        open_bag = True
                        unlock_room3 = bag('key_for_room3r')
                        if unlock_room3:
                            scene4_loop = True
                            scene4()
                elif pos[0] in range(map_hover_rect[0], map_hover_rect[0]+map_hover_rect[2]) and pos[1] in range(map_hover_rect[1], map_hover_rect[1]+map_hover_rect[3]) and man.x in range(map_hover_rect[0], map_hover_rect[0]+map_hover_rect[2]):
                    map_photo = pygame.transform.scale(map_image, (2*map_hover_rect[2], 2*map_hover_rect[3]))
                    unscrew = pygame.image.load('objects\\unscrew1.png')
                    unscrew_hover = pygame.image.load('objects\\unscrew2.png')
                    unscrew = pygame.transform.scale(unscrew, (dw//20, int(dw/20*unscrew.get_height()/unscrew.get_width())))
                    unscrew_hover = pygame.transform.scale(unscrew_hover, (dw // 20, int(dw / 20 * unscrew_hover.get_height() / unscrew_hover.get_width())))
                    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
                    run = True
                    unscrew_xy = ((dw - unscrew.get_width())//2, (dh - unscrew.get_height())//2+150)
                    while run:
                        pos = pygame.mouse.get_pos()
                        WIN.blit(map_photo, ((dw-map_photo.get_width())//2, (dh-map_photo.get_height())//2))
                        if player_bag['screwdriver']:
                            if pos[0] in range(unscrew_xy[0], unscrew_xy[0] + unscrew.get_width()) and pos[1] in range(unscrew_xy[1], unscrew_xy[1]+unscrew.get_height()):
                                WIN.blit(unscrew_hover, unscrew_xy)
                            else:
                                WIN.blit(unscrew, unscrew_xy)
                        for events in pygame.event.get():
                            if events.type == pygame.MOUSEBUTTONUP:
                                if pos[0] not in range(int((dw-map_photo.get_width())//2), int((dw-map_photo.get_width())//2+map_photo.get_width())) or pos[1] not in range(int((dh-map_photo.get_height())//2), int((dh-map_photo.get_height())//2+map_photo.get_height())):
                                    run = False
                                if pos[0] in range(unscrew_xy[0], unscrew_xy[0] + unscrew.get_width()) and pos[1] in range(unscrew_xy[1], unscrew_xy[1]+unscrew.get_height()) and player_bag['screwdriver']:
                                    map_key = True
                                    text1_end = False
                                    storytext('I see I am in shimla, do I live here, i don\'t know')
                                    instruction('map icon unlocked!')
                                    run = False

                        pygame.display.update()

        if man.x < 10:
            scene2_loop = False
            scene1_loop = True
            scene1()
        elif man.x > dw-100:
            scene5_loop = True
            scene5()
            man.x = dw-200
            man.y = 2*dh/3
        pygame.display.update()


def instruction(msg, color=blue):
    bar = pygame.image.load("objects\\instruction_bar.png")
    ok = pygame.image.load('buttons\\ok.png')
    ins_font = pygame.font.Font('fonts\\chat_font.ttf', 15)
    text = ins_font.render(msg, True, color)
    bar = pygame.transform.scale(bar, ((text.get_width()+300), int(dw/6*bar.get_height()/bar.get_width())))
    ok = pygame.transform.scale(ok, (dw//20, int(dw/20*ok.get_height()/ok.get_width())))
    bar_xy = ((dw-bar.get_width())//2, (dh-bar.get_height())//2)
    ok_xy = ((dw-ok.get_width())//2, (dh-ok.get_height())//2+bar.get_height()+50)

    loop = True
    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
    while loop:
        pos = pygame.mouse.get_pos()
        WIN.blit(bar, bar_xy)
        WIN.blit(ok, ok_xy)
        WIN.blit(text, [bar_xy[0]+(bar.get_width()-text.get_width()-50)//2, bar_xy[1]+(bar.get_height()-text.get_height())//2])
        pygame.display.update()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP and pos[0] in range(ok_xy[0], ok_xy[0]+ok.get_width()) and pos[1] in range(ok_xy[1], ok_xy[1]+ok.get_height()):
                loop = False


drawer_items = [['screwdriver'], ['exit_door_key'], ['key_for_room3']]


def scene3():
    global scene3_loop, open_bag, drawer_items
    d1_rect = (715, 378, 83, 42) # x,y,l,b
    d2_rect = (715, 417, 83, 42)
    d3_rect = (715, 465, 83, 44)
    bg = pygame.image.load('hospital\\room2.png')
    bg = pygame.transform.scale(bg, (dw, dh))
    while scene3_loop:
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(bg, (0, 0))
        if pos[0] in range(d1_rect[0], d1_rect[0]+d1_rect[2]) and pos[1] in range(d1_rect[1], d1_rect[1]+d1_rect[3]):
            mousetext("open drawer 1", pos)
        elif pos[0] in range(d2_rect[0], d2_rect[0]+d2_rect[2]) and pos[1] in range(d2_rect[1], d2_rect[1]+d2_rect[3]):
            mousetext("open drawer 2", pos)
        elif pos[0] in range(d3_rect[0], d3_rect[0]+d3_rect[2]) and pos[1] in range(d3_rect[1], d3_rect[1]+d3_rect[3]):
            mousetext("open drawer 3", pos)
        if keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if keys[pygame.K_e]:
                scene3_loop = False
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(d1_rect[0], d1_rect[0] + d1_rect[2]) and pos[1] in range(d1_rect[1], d1_rect[1] + d1_rect[3]):
                    drawer(drawer_items[0], 1)
                elif pos[0] in range(d2_rect[0], d2_rect[0] + d2_rect[2]) and pos[1] in range(d2_rect[1], d2_rect[1] + d2_rect[3]):
                    drawer(drawer_items[1], 2)
                elif pos[0] in range(d3_rect[0], d3_rect[0] + d3_rect[2]) and pos[1] in range(d3_rect[1], d3_rect[1] + d3_rect[3]):
                    drawer(drawer_items[2], 3)

        pygame.display.update()


scene6_bg = pygame.image.load('hospital\\hos_exit.jpg')
scene6_bg = pygame.transform.scale(scene6_bg, (dw, dh))


def scene6():
    global scene6_loop, open_bag, dh, dw, scene7_loop
    man.x = dw//2
    man.y = dh - 20 - man.height
    door_rect = (418, 178, 117, 240)
    prev_height = man.height
    man.height = 120
    while scene6_loop:
        pos = pygame.mouse.get_pos()
        clock.tick(36)
        WIN.blit(scene6_bg, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and man.y > 316:
            man.y -= man.vel
            man.up = True
            man.right = False
            man.left = False
            man.standing = False
            man.down = False
        elif keys[pygame.K_DOWN]:
            man.y += man.vel
            man.down = True
            man.right = False
            man.left = False
            man.standing = False
            man.up = False
        elif keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        else:
            man.standing = True
            man.walkCount = 0
        if pos[0] in range(door_rect[0], door_rect[0]+door_rect[2]) and pos[1] in range(door_rect[1], door_rect[1]+door_rect[3]) and man.y in range(0 , door_rect[1]+door_rect[3]-man.height+50):
            draw_rect_alpha(WIN, (0, 0, 0, 128), door_rect)
            mousetext('Open Exit', pos)

        man.draw()
        if man.y > dh - man.height:
            man.height = prev_height
            scene6_loop = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(door_rect[0], door_rect[0]+door_rect[2]) and pos[1] in range(door_rect[1], door_rect[1]+door_rect[3]) and man.y in range(0, door_rect[1]+door_rect[3]-man.height+50):
                    if player_bag['exit_door_key']:
                        open_bag = True
                        next_scene = bag('exit_door_keyr')
                        if next_scene:
                            scene7_loop = True
                            scene7()
                    else:
                        instruction("You need key")

        pygame.display.update()


scene4_bg = pygame.image.load('hospital\\final_room.png')
scene4_bg = pygame.transform.scale(scene4_bg, (dw, dh))


def scene4():
    global scene2_loop, scene4_loop, open_bag, dh, dw
    # hover_line = pygame.image.load('objects\\yellow_line.png')
    # hover_line = pygame.transform.scale(hover_line, (60, int(60*hover_line.get_height()/hover_line.get_width()+10)))
    cipher_rect = (609, 240, 180, 70)


    while scene4_loop:
        pos = pygame.mouse.get_pos()
        WIN.blit(scene4_bg, (0, 0))
        if pos[0] in range(510, 565) and pos[1] in range(360, 390):
            # WIN.blit(hover_line, (510, 374))
            mousetext('See', pos)
        if pos[0] in range(cipher_rect[0], cipher_rect[0]+cipher_rect[2]) and pos[1] in range(cipher_rect[1], cipher_rect[1]+cipher_rect[3]):
            # highlighter((0, 0, 0, 128), cipher_rect)
            mousetext('See', pos)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        if keys[pygame.K_e]:
            scene4_loop = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(510, 565) and pos[1] in range(360, 390):
                    if not player_bag['room1_closet_key']:
                        drawer(['glass', 'mug', 'room1_closet_key'], 0, 'table_top')
                    else:
                        drawer(['glass', 'mug'], 0, 'table_top')
                if pos[0] in range(cipher_rect[0], cipher_rect[0]+cipher_rect[2]) and pos[1] in range(cipher_rect[1], cipher_rect[1]+cipher_rect[3]):
                    cipher()

        pygame.display.update()


scene5_bg_light = pygame.image.load('hospital\\scene5_light.png')
scene5_bg_light = pygame.transform.scale(scene5_bg_light, (dw, dh))

scene5_bg_dark = pygame.image.load('hospital\\scene5_dark.png')
scene5_bg_dark = pygame.transform.scale(scene5_bg_dark, (dw, dh))


def scene5():
    global scene2_loop, scene5_loop, open_bag, dh, dw, open_bag, scene6_loop, player_bag
    state = False
    frame = pygame.image.load('objects\\frame.png')
    exit_rect = (683, 165, 89, 25)
    counter_rect = (451, 280, 121, 70)
    dark_rect = (832, 212, 82, 78)

    frame = pygame.transform.scale(frame, (exit_rect[2], exit_rect[3]))
    while scene5_loop:
        pos = pygame.mouse.get_pos()
        if state:
            WIN.blit(scene5_bg_light, (0, 0))
        else:
            draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
            WIN.blit(scene5_bg_dark, (0, 0))
        keys = pygame.key.get_pressed()
        if pos[0] in range(counter_rect[0], counter_rect[0]+counter_rect[2]) and pos[1] in range(counter_rect[1], counter_rect[1]+counter_rect[3]):
            mousetext('See counter', pos)
        elif pos[0] in range(exit_rect[0], exit_rect[0]+exit_rect[2]) and pos[1] in range(exit_rect[1], exit_rect[1]+exit_rect[3]):
            WIN.blit(frame, (exit_rect[0], exit_rect[1]))
        elif pos[0] in range(dark_rect[0], dark_rect[0]+dark_rect[2]) and pos[1] in range(dark_rect[1], dark_rect[1]+dark_rect[3]):
            if not state:
                mousetext('its very dark', pos)
            if state:
                mousetext('See Here', pos)
        if keys[pygame.K_b] and not open_bag:
            open_bag = True
            state = bag('torch_flagr')
        if keys[pygame.K_e]:
            scene5_loop = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(exit_rect[0], exit_rect[0]+exit_rect[2]) and pos[1] in range(exit_rect[1], exit_rect[1]+exit_rect[3]):
                    scene6_loop = True
                    scene6()
                if pos[0] in range(counter_rect[0], counter_rect[0] + counter_rect[2]) and pos[1] in range(counter_rect[1], counter_rect[1] + counter_rect[3]):
                    if not player_bag['med_file']:
                        drawer(['med_file'], 0, 'marbel_bg')
                    else:
                        drawer([], 0, 'marbel_bg')
                if pos[0] in range(dark_rect[0], dark_rect[0]+dark_rect[2]) and pos[1] in range(dark_rect[1], dark_rect[1]+dark_rect[3]):
                    if state:
                        if not player_bag['van_key']:
                            drawer(['van_key'], 0, 'grey_wall')
                        else:
                            drawer([], 0, 'grey_wall')
                    else:
                        instruction('Find illumination')


        pygame.display.update()


def cipher():
    loop = True
    cipher_imageL = pygame.image.load('hospital\\cipherL.png')
    cipher_imageR = pygame.image.load('hospital\\cipherR.png')
    cipher_imageL = pygame.transform.scale(cipher_imageL, (dw//3, int(dw/3*cipher_imageL.get_height()/cipher_imageL.get_width())))
    cipher_imageR = pygame.transform.scale(cipher_imageR, (dw // 3, int(dw / 3 * cipher_imageR.get_height() / cipher_imageR.get_width())))

    dial1 = pygame.image.load('objects\\dial1.png')
    dial1 = pygame.transform.scale(dial1, (cipher_imageL.get_height(), cipher_imageL.get_height()))
    dial2 = pygame.transform.rotate(dial1, 90)
    dial3 = pygame.transform.rotate(dial2, 90)
    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
    while loop:
        pos = pygame.mouse.get_pos()
        WIN.blit(dial1, ((dw-dial1.get_width())//2, (dh-dial1.get_height())//2))
        WIN.blit(dial2, (int(dw/2-1.5*dial1.get_width()), (dh-dial1.get_height())//2))
        WIN.blit(dial3, ((dw+dial1.get_width())//2, (dh-dial1.get_height())//2))
        WIN.blit(cipher_imageL, (int(dw/2-1.5*dial1.get_width()-cipher_imageL.get_width()), (dh-cipher_imageL.get_height())//2))
        WIN.blit(cipher_imageR, (int(dw / 2 + 1.5 * dial1.get_width()), (dh - cipher_imageR.get_height()) // 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] not in range(int(dw/2-1.5*dial1.get_width()-cipher_imageL.get_width()), int(dw / 2 + 1.5 * dial1.get_width() + cipher_imageR.get_width())) or pos[1] not in range((dh - cipher_imageR.get_height()) // 2, (dh - cipher_imageR.get_height()) // 2+cipher_imageR.get_height()):
                    loop = False
        pygame.display.update()


man_out = Player(319, 500, 30, 60)


def scene7():
    global scene7_loop, player_bag, open_bag, Player
    scene7_bg = pygame.image.load('hospital\\hos_out.png')
    scene7_bg = pygame.transform.scale(scene7_bg, (dw, dh))

    no_entry = (196, 0, 585, 475)
    van_rect = (530, 375, 225, 100)
    fuel_rect = (293, 106, 22, 20)
    entry_rect = (277, 394, 100, 52)
    spawn_xy = (319, 500)
    man_out.x = spawn_xy[0]
    man_out.y = spawn_xy[1]

    while scene7_loop:
        a = man_out.x in range(no_entry[0], no_entry[0] + no_entry[2])
        b = man_out.y in range(no_entry[1], no_entry[1] + no_entry[3])
        clock.tick(36)
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(scene7_bg, (0, 0))
        if keys[pygame.K_LEFT] and not (a and b):
            man_out.x -= man_out.vel
            man_out.left = True
            man_out.right = False
            man_out.standing = False
            man_out.up = False
            man_out.down = False
        elif keys[pygame.K_RIGHT] and man_out.x < dw - man_out.width - man_out.vel and not (a and b):
            man_out.x += man.vel
            man_out.right = True
            man_out.left = False
            man_out.standing = False
            man_out.up = False
            man_out.down = False

        elif keys[pygame.K_UP] and man_out.y > man_out.height + man_out.vel and not (a and b):
            man_out.y -= man.vel
            man_out.up = True
            man_out.right = False
            man_out.left = False
            man_out.standing = False
            man_out.down = False
        elif keys[pygame.K_DOWN] and man_out.y < dh - man_out.height - man_out.vel - 30 and not (a and b):
            man_out.y += man.vel
            man_out.down = True
            man_out.right = False
            man_out.left = False
            man_out.standing = False
            man_out.up = False
        elif keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        elif a and b:
            if man_out.y >= no_entry[3]-man_out.vel-man_out.height:
                man_out.y += man_out.vel
            elif man_out.x >= no_entry[0] and man_out.x < no_entry[0] + 100:
                man_out.x -= 2*man_out.vel
            elif man_out.x <= no_entry[0]+no_entry[2]:
                man_out.x += 2*man_out.vel
            else:
                man_out.x = spawn_xy[0]
                man_out.y = spawn_xy[1]

        else:
            man_out.standing = True
            man_out.walkCount = 0

        man_out.draw()
        if pos[0] in range(van_rect[0], van_rect[0]+van_rect[2]) and pos[1] in range(van_rect[1], van_rect[1]+van_rect[3]) and man_out.x in range(van_rect[0], van_rect[0]+van_rect[2]):
            mousetext('See Ambulance', pos)
        elif pos[0] in range(entry_rect[0], entry_rect[0]+entry_rect[2]) and pos[1] in range(entry_rect[1], entry_rect[1]+entry_rect[3]) and man_out.x in range(entry_rect[0], entry_rect[0]+entry_rect[2]):
            mousetext('Enter Hospital', pos)
        elif pos[0] in range(fuel_rect[0], fuel_rect[0]+fuel_rect[2]) and pos[1] in range(fuel_rect[1], fuel_rect[1]+fuel_rect[3]) and man_out.y in range(fuel_rect[1]-100, fuel_rect[1]+fuel_rect[3]+100):
            mousetext('Pick Fuel Tank', pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(van_rect[0], van_rect[0]+van_rect[2]) and pos[1] in range(van_rect[1], van_rect[1]+van_rect[3]) and man_out.x in range(van_rect[0], van_rect[0]+van_rect[2]):
                    open_bag = True
                    unlock_van = bag('van_keyr')
                    if unlock_van == 1:
                        if player_bag['fuel']:
                            vehicle()
                        else:
                            instruction('No fuel')
                    else:
                        instruction('Find key')
                elif pos[0] in range(fuel_rect[0], fuel_rect[0]+fuel_rect[2]) and pos[1] in range(fuel_rect[1], fuel_rect[1]+fuel_rect[3]) and man_out.y in range(fuel_rect[1]-100, fuel_rect[1]+fuel_rect[3]+100):
                    if not player_bag['fuel']:
                        player_bag['fuel'] = True
                        instruction('Fuel collected')
                elif pos[0] in range(entry_rect[0], entry_rect[0]+entry_rect[2]) and pos[1] in range(entry_rect[1], entry_rect[1]+entry_rect[3]) and man_out.x in range(entry_rect[0], entry_rect[0]+entry_rect[2]):
                    scene7_loop = False

        pygame.display.update()


def vehicle():
    loop = True
    van = pygame.image.load('hospital\\vehicle.jpg')
    van = pygame.transform.scale(van, (dw, dh))
    gps_rect = (434, 318, 130, 70)
    while loop:
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(van, (0, 0))
        if keys[pygame.K_e]:
            loop = False
        if pos[0] in range(gps_rect[0], gps_rect[0]+gps_rect[2]) and pos[1] in range(gps_rect[1], gps_rect[1]+gps_rect[3]):
            mousetext('Enter home address', pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(gps_rect[0], gps_rect[0] + gps_rect[2]) and pos[1] in range(gps_rect[1],gps_rect[1] + gps_rect[3]):
                    if map_key:
                        user_text = gps()
                        if user_text.lower() == 'charleville mansion':
                            instruction('Way to home')
                            mansion_scene1()
                        else:
                            instruction('Wrong address')
                    else:
                        instruction('Map is needed')

        pygame.display.update()


def gps(rect=((dw-200)//2, (dh-32)//2, 100, 32)):
    # instruction('Enter text in the command prompt: ')
    # text = input('Enter here: ')
    # return text
    base_font = pygame.font.Font('fonts\\chat_font.ttf', 20)
    user_text = ''
    input_rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
    color_active = pygame.Color(white)
    color_passive = pygame.Color(pas)
    color = color_passive
    active = False
    loop = True
    draw_rect_alpha(WIN, (0, 0, 0, 80), (0, 0, dw, dh))
    while loop:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] in range(rect[0], rect[0]+rect[2]) and pos[1] in range(rect[1], rect[1]+rect[3]):
                    active = True
                else:
                    active = False
                if pos[0] not in range(input_rect[0], input_rect[0]+input_rect[2]) or pos[1] not in range(input_rect[1], input_rect[1]+input_rect[3]):
                    # loop = False
                    return user_text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(WIN, color, input_rect)

        text_surface = base_font.render(user_text, True, (0, 0, 0))
        WIN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()

        # clock.tick(60)
#********************************** location 2 *********************************

conti_button = pygame.image.load('buttons\\continue1.png')
conti_button = pygame.transform.scale(conti_button, (dw//10, int(dw/10*conti_button.get_height()/conti_button.get_width())))
mansion_out = pygame.image.load('mansion_photos\\mansion_out.png')
mansion_out = pygame.transform.scale(mansion_out, (dw, dh))


def mansion_scene1():
    loop = True
    welcome_font = confirmation.render('charleville mansion'.upper(), True, white)

    WIN.blit(mansion_out, (0, 0))
    draw_rect_alpha(WIN, (0, 0, 0, 150), (0, 0, dw, dh))
    conti_xy = (dw-conti_button.get_width()-40, dh-conti_button.get_height()-20)
    while loop:
        pos = pygame.mouse.get_pos()
        WIN.blit(welcome_font, [(dw-welcome_font.get_width())//2, (dh//5)])
        WIN.blit(conti_button, conti_xy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(conti_xy[0], conti_xy[0] + conti_button.get_width()) and pos[1] in range(conti_xy[1], conti_xy[1] + conti_button.get_height()):
                    # instruction('Enter code to get in next level')
                    # next_level_code = gps()
                    # if next_level_code.lower() == 'jakhoo temple':
                    #     loop = False
                    #     mansion_scene2()
                    # else:
                    #     instruction('Wrong code')
                    loop = False
                    mansion_scene2()
        pygame.display.update()


mansion_gate = pygame.image.load('mansion_photos\\mansion_gate.png')
mansion_gate = pygame.transform.scale(mansion_gate, (dw, dh))
ladder = pygame.image.load('mansion_objects\\ladder.png')
ladder = pygame.transform.scale(ladder, (int(dh/3*ladder.get_width()/ladder.get_height()), dh//3))
ladder = pygame.transform.rotate(ladder, 90)


def mansion_scene2():

    global open_bag
    loop = True
    gate_rect = (287, 292, 191, 250)
    man.x = 20
    man.y = dh-man.height-man.vel
    while loop:
        clock.tick(36)
        WIN.blit(mansion_gate, (0, 0))
        WIN.blit(ladder, (dw-ladder.get_width(), dh-ladder.get_height()))
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if pos[0] in range(gate_rect[0], gate_rect[0]+gate_rect[2]) and pos[1] in range(gate_rect[1], gate_rect[1]+gate_rect[3]) and man.x in range(gate_rect[0], gate_rect[0]+gate_rect[2]):
            mousetext('Open Gate', pos)
        if pos[0] in range(dw-ladder.get_width(), dw-ladder.get_width()+ladder.get_width()) and pos[1] in range(dh-ladder.get_height(), dh-ladder.get_height()+ladder.get_height()) and man.x in range(dw-ladder.get_width(), dw-ladder.get_width()+ladder.get_width()):
            mousetext('Ladder', pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(gate_rect[0], gate_rect[0] + gate_rect[2]) and pos[1] in range(gate_rect[1], gate_rect[1]+gate_rect[3]) and man.x in range(gate_rect[0], gate_rect[0]+gate_rect[2]):
                    instruction('Locked!')
                if pos[0] in range(dw - ladder.get_width(), dw - ladder.get_width() + ladder.get_width()) and pos[1] in range(dh - ladder.get_height(), dh - ladder.get_height() + ladder.get_height()) and man.x in range(dw-ladder.get_width(), dw-ladder.get_width()+ladder.get_width()):
                    instruction('Use Ladder')
                    loop = False
                    mansion_scene3()
        if keys[pygame.K_LEFT] and man.x > man.width + man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
            man.up = False
            man.down = False
        elif keys[pygame.K_RIGHT] and man.x < dw - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
            man.up = False
            man.down = False

        elif keys[pygame.K_UP] and man.y > 460:
            man.y -= man.vel
            man.up = True
            man.right = False
            man.left = False
            man.standing = False
            man.down = False
        elif keys[pygame.K_DOWN] and man.y < dh - man.height - man.vel + 30:
            man.y += man.vel
            man.down = True
            man.right = False
            man.left = False
            man.standing = False
            man.up = False
        elif keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        else:
            man.standing = True
            man.walkCount = 0

        man.draw()
        pygame.display.update()

# player_bag_hos = player_bag
# del player_bag



def mansion_scene3():
    global open_bag, player_bag, open_bag_man, Player, man_out
    loop = True
    man_out.x = man_out.width + man_out.vel + 30
    man_out.y = dh - man_out.height - man_out.vel - 10
    main_door_rect = (353, 483, 82, 69)
    mystery_door_rect = (567, 529, 48, 46)
    while loop:
        clock.tick(36)
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(mansion_out, (0, 0))
        draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(main_door_rect[0], main_door_rect[0] + main_door_rect[2]) and pos[1] in range(
                    main_door_rect[1], main_door_rect[1]+main_door_rect[3]) and man_out.x in range(main_door_rect[0], main_door_rect[0] + main_door_rect[2]):
                    password = door_puzzle()
                    if str(password) == str(3):
                        instruction('Door Unlocked')
                        mansion_scene4()
                    else:
                        instruction('Incorrect password')
                elif pos[0] in range(mystery_door_rect[0], mystery_door_rect[0] + mystery_door_rect[2]) and pos[
                    1] in range(mystery_door_rect[1],
                                mystery_door_rect[1] + mystery_door_rect[3]) and man_out.x in range(
                    mystery_door_rect[0], mystery_door_rect[0] + mystery_door_rect[2]):
                    if player_bag_man['fp1']:
                        open_bag_man = True
                        req = bag_man('fp1r')
                        if req:
                            instruction('Door Unlocked')
                            mansion_scene6()
                    else:
                        instruction('Need fingerprint to unlock')

        if pos[0] in range(main_door_rect[0], main_door_rect[0] + main_door_rect[2]) and pos[1] in range(main_door_rect[1], main_door_rect[1]+main_door_rect[3]) and man_out.x in range(main_door_rect[0], main_door_rect[0] + main_door_rect[2]):
            mousetext('Open door', pos)
        elif pos[0] in range(mystery_door_rect[0], mystery_door_rect[0]+mystery_door_rect[2]) and pos[1] in range(mystery_door_rect[1], mystery_door_rect[1]+mystery_door_rect[3]) and man_out.x in range(mystery_door_rect[0], mystery_door_rect[0]+mystery_door_rect[2]):
            mousetext('Mystery room', pos)
        if keys[pygame.K_LEFT] and man_out.x > man_out.width + man_out.vel:
            man_out.x -= man_out.vel
            man_out.left = True
            man_out.right = False
            man_out.standing = False
            man_out.up = False
            man_out.down = False
        elif keys[pygame.K_RIGHT] and man_out.x < dw - man_out.width - man_out.vel:
            man_out.x += man_out.vel
            man_out.right = True
            man_out.left = False
            man_out.standing = False
            man_out.up = False
            man_out.down = False

        elif keys[pygame.K_b] and not open_bag:
            open_bag = True
            bag()
        else:
            man_out.standing = True
            man_out.walkCount = 0

        man_out.draw()
        pygame.display.update()


def door_puzzle():
    # print('Enter text in command prompt')
    # text = input('Enter here')
    # return text
    base_font = pygame.font.Font('fonts\\chat_font.ttf', 20)
    user_text = ''
    input_rect = pygame.Rect((dw-100)//2, dh-150, 100, 32)
    color_active = pygame.Color(white)
    color_passive = pygame.Color(pas)
    color = color_passive
    active = False
    puzzle = pygame.image.load('mansion_photos\\puzzle.png')
    puzzle = pygame.transform.scale(puzzle, (int(4*dh/5*puzzle.get_width()/puzzle.get_height()), 4*dh//5))
    loop = True
    draw_rect_alpha(WIN, (0, 0, 0, 100), (0, 0, dw, dh))
    while loop:
        WIN.blit(puzzle, ((dw-puzzle.get_width())//2, (dh-puzzle.get_height())//2))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if pos[0] not in range(input_rect[0], input_rect[0]+input_rect[2]) or pos[1] not in range(input_rect[1], input_rect[1]+input_rect[3]):
                    # loop = False
                    return user_text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(WIN, color, input_rect)

        text_surface = base_font.render(user_text, True, (0, 0, 0))
        WIN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()

        # clock.tick(60)


entrance = pygame.image.load('mansion_photos\\entrance.png')
entrance = pygame.transform.scale(entrance, (dw,dh))
bobbypin = pygame.image.load('mansion_objects\\bbp.png')
bobbypin = pygame.transform.scale(bobbypin, (100, 100*bobbypin.get_height()//bobbypin.get_width()))

player_bag_man = {'fp1': False, 'fp2': False, 'fp3': False, 'fp4': False, 'bbp': False, 'tape': False, 'brush': False,
                  'powder': False, 'p1': False, 'p2': False, 'p3': False, 'p4': False, 'p5': False, 'p6': False, 'p7': False, 'p8': False, 'p9': False, 'room3_key': False, 'pc_pass': False, 'cello_tape': False, 'taser': False, 'crowbar': False, 'id': False}
open_bag_man = False


def mansion_scene4():
    global open_bag_man
    loop = True
    upstairs_rect = (50, 43, 140, 70)
    shirt_rect = (69, 431, 49, dh-431)
    photo_door_rect = (709, 120, 38, 23)
    photo_tab_rect = (543, 459, 67, 51)
    frame_rect = (275, 201, 60, 159)
    room1_rect = (375, 226, 131, 230)
    exit_rect = (832, 100, 168, 300)
    p_rect = (651, 400, 30, 35)
    while loop:
        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        WIN.blit(entrance, (0, 0))
        if pos[0] in range(upstairs_rect[0], upstairs_rect[0]+upstairs_rect[2]) and pos[1] in range(upstairs_rect[1], upstairs_rect[1]+upstairs_rect[3]):
            mousetext('Upstairs', pos)
        if pos[0] in range(shirt_rect[0], shirt_rect[0]+shirt_rect[2]) and pos[1] in range(shirt_rect[1], shirt_rect[1]+shirt_rect[3]):
            mousetext('Check Pocket', pos)
        if pos[0] in range(photo_door_rect[0], photo_door_rect[0]+photo_door_rect[2]) and pos[1] in range(photo_door_rect[1], photo_door_rect[1]+photo_door_rect[3]):
            mousetext('See photo', pos)
        if pos[0] in range(photo_tab_rect[0], photo_tab_rect[0]+photo_tab_rect[2]) and pos[1] in range(photo_tab_rect[1], photo_tab_rect[1]+photo_tab_rect[3]):
            mousetext('See photo', pos)
        if pos[0] in range(frame_rect[0], frame_rect[0]+frame_rect[2]) and pos[1] in range(frame_rect[1], frame_rect[1]+frame_rect[3]):
            mousetext('See frames', pos)
        if pos[0] in range(room1_rect[0], room1_rect[0]+room1_rect[2]) and pos[1] in range(room1_rect[1], room1_rect[1]+room1_rect[3]):
            mousetext('Go in room', pos)
        if pos[0] in range(exit_rect[0], exit_rect[0]+exit_rect[2]) and pos[1] in range(exit_rect[1], exit_rect[1]+exit_rect[3]):
            mousetext('Exit', pos)
        if pos[0] in range(p_rect[0], p_rect[0]+p_rect[2]) and pos[1] in range(p_rect[1], p_rect[1]+p_rect[3]):
            mousetext('See photo', pos)
        if keys[pygame.K_b]:
            open_bag_man = True
            bag_man()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(shirt_rect[0], shirt_rect[0] + shirt_rect[2]) and pos[1] in range(shirt_rect[1],shirt_rect[1]+shirt_rect[3]):
                    if not player_bag_man['bbp']:
                        drawer_man(['bbp'], 0, 'cloth')
                    else:
                        drawer_man([], 0, 'cloth')
                if pos[0] in range(photo_door_rect[0], photo_door_rect[0] + photo_door_rect[2]) and pos[1] in range(photo_door_rect[1], photo_door_rect[1] + photo_door_rect[3]):
                    if not player_bag_man['p1']:
                        drawer_man(['p1'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
                if pos[0] in range(photo_tab_rect[0], photo_tab_rect[0] + photo_tab_rect[2]) and pos[1] in range(photo_tab_rect[1], photo_tab_rect[1] + photo_tab_rect[3]):
                    if not player_bag_man['p2']:
                        drawer_man(['p2'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
                if pos[0] in range(p_rect[0], p_rect[0] + p_rect[2]) and pos[1] in range(p_rect[1],p_rect[1] + p_rect[3]):
                    if not player_bag_man['p9']:
                        drawer_man(['p9'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
                if pos[0] in range(frame_rect[0], frame_rect[0] + frame_rect[2]) and pos[1] in range(frame_rect[1],frame_rect[1] + frame_rect[3]):
                    # instruction('Wall frame')
                    wall_frame()
                if pos[0] in range(upstairs_rect[0], upstairs_rect[0] + upstairs_rect[2]) and pos[1] in range(
                    upstairs_rect[1], upstairs_rect[1] + upstairs_rect[3]):
                    mansion_scene5()
                if pos[0] in range(room1_rect[0], room1_rect[0] + room1_rect[2]) and pos[1] in range(room1_rect[1],room1_rect[1] +room1_rect[3]):
                    mansion_scene8()
                if pos[0] in range(exit_rect[0], exit_rect[0] + exit_rect[2]) and pos[1] in range(exit_rect[1],exit_rect[1] +exit_rect[3]):
                    loop = False

        pygame.display.update()
pc_pass_flag = True

def bag_man(request=None):
    global open_bag_man, player_bag_man, pc_pass_flag
    bag_image = pygame.image.load('objects\\bag.png')
    bag_image = pygame.transform.scale(bag_image, (dw//3, dw//3*bag_image.get_height()//bag_image.get_width()))
    bag_xy = (2 * dw // 3, (dh - bag_image.get_height()) // 2)
    photos = []
    # elements in bag change 1
    pin = pygame.image.load('mansion_objects\\bbp.png')
    r3_key = pygame.image.load('mansion_objects\\room3_key.png')
    pcPass = pygame.image.load('mansion_objects\\pc_pass.png')
    cello = pygame.image.load('mansion_objects\\cello_tape.png')
    gun = pygame.image.load('mansion_objects\\taser.png')
    f1 = pygame.image.load('mansion_objects\\fp1.png')
    f2 = pygame.image.load('mansion_objects\\fp2.png')
    f3 = pygame.image.load('mansion_objects\\fp3.png')
    f4 = pygame.image.load('mansion_objects\\fp4.png')
    crow = pygame.image.load('mansion_objects\\crowbar.png')
    pow = pygame.image.load('mansion_objects\\powder.png')
    bru = pygame.image.load('mansion_objects\\brush.png')
    ids = pygame.image.load('mansion_objects\\id.png')
    for i in range(1, 10):
        img = pygame.image.load('mansion_objects\\p'+str(i)+'.png')
        photos.append(img)
    #  add all objects here change 2
    object_list_temp = [pin, r3_key, pcPass, cello, gun, f1, f2, f3, f4, crow, pow, bru, ids]
    for i in range(1, 10):
        object_list_temp.append(photos[i-1])
    object_list = []
    object_rect = []
    for objects in object_list_temp:
        objects = pygame.transform.scale(objects, (bag_image.get_width() // 4, bag_image.get_width() // 4 * objects.get_height() // objects.get_width()))
        object_list.append(objects)
    del object_list_temp
    count = 0
    # hover rectangle
    for o in object_list:
        count += 1
        if count <= 4:
            object_rect.append((dw//3, 75*count, o.get_width(), o.get_height()))
        elif 4 < count <= 8:
            object_rect.append((dw // 6, 35 * (count-4), o.get_width(), o.get_height()))
        elif 8 < count <= 12:
            object_rect.append((dw // 9, 35 * (count-8), o.get_width(), o.get_height()))
        elif count > 12:
            object_rect.append((dw // 12, 35 * (count-12), o.get_width(), o.get_height()))
        elif count > 18:
            object_rect.append((dw // 12, 35 * (count - 18), o.get_width(), o.get_height()))
    # overlay
    draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))

    # add all the player_bag_man flags here request must same as flag name change 3
    object_list.append('bbp')
    object_list.append('room3_key')
    object_list.append('pc_pass')
    object_list.append('cello_tape')
    object_list.append('taser')
    object_list.append('fp1')
    object_list.append('fp2')
    object_list.append('fp3')
    object_list.append('fp4')
    object_list.append('crowbar')
    object_list.append('powder')
    object_list.append('brush')
    object_list.append('id')
    # object_list.extend(['bbp', 'room3_key', 'pc_pass', 'cello_tape', 'taser', 'fp1', 'fp2', 'fp3', 'fp4'])
    for i in range(1, 10):
        object_list.append('p'+str(i))

    while open_bag_man:
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(bag_image, bag_xy)
        # blit objects
        for i in range(0, len(object_list)//2):
            count = 0
            if player_bag_man[object_list[i+len(object_list)//2]]:
                for ps in frame_display_list:
                    if ('p'+str(ps)) == object_list[i+len(object_list)//2]:
                        count += 1
                if not count:
                    WIN.blit(object_list[i], (object_rect[i][0], object_rect[i][1]))
        # clicks and events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif keys[pygame.K_x]:
                open_bag_man = False
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(0, len(object_list) // 2):
                    try:
                        if pos[0] in range(object_rect[i][0], object_rect[i][0]+object_rect[i][2]) and pos[1] in range(object_rect[i][1], object_rect[i][1]+object_rect[i][3]) and request == object_list[i+len(object_list)//2]+'r':
                            instruction('unlocked')
                            open_bag_man = False
                            return 1
                    except IndexError:
                        open_bag_man = False
                    if object_list[i+len(object_list)//2] == 'pc_pass' and pc_pass_flag:
                        if pos[0] in range(object_rect[i][0], object_rect[i][0] + object_rect[i][2]) and pos[1] in range(object_rect[i][1], object_rect[i][1] + object_rect[i][3]):
                            report('mansion_objects\\pc_pass.png')
                            open_bag_man = False
        pygame.display.update()
    return 0


def drawer_man(items, no=0, img='open_drawer'):
    global player_bag_man
    loop = True
    drawer_bg = pygame.image.load('mansion_objects\\'+str(img)+'.png')
    drawer_bg = pygame.transform.scale(drawer_bg, (dw//2, dw//2*drawer_bg.get_height()//drawer_bg.get_width()))
    drawer_xy = ((dw - drawer_bg.get_width()) // 2, (dh - drawer_bg.get_height()) // 2)
    item_images = []
    for item in items:
        if 'fp' in item and not(player_bag_man['cello_tape'] and player_bag_man['brush'] and player_bag_man['powder']):
            instruction('You need powder,tape and brush to collect fingerprints')
            loop = False
        else:
            i = pygame.image.load('mansion_objects\\'+item+'.png')
            i = pygame.transform.scale(i, (drawer_bg.get_width()//3, int(drawer_bg.get_width()/3*i.get_height()/i.get_width())))
            item_images.append(i)

    draw_rect_alpha(WIN, (0, 0, 0, 200), (0, 0, dw, dh))
    while loop:
        item_rect = []
        pos = pygame.mouse.get_pos()
        WIN.blit(drawer_bg, drawer_xy)
        count = 0
        if len(items) == 1:
            for image in item_images:
                xy = ((dw-image.get_width())//2, (dh-item_images[0].get_height())//2)
                WIN.blit(image, xy)
                item_rect.append((xy[0], xy[1], image.get_width(), image.get_height()))
        else:
            for images in item_images:
                count += 1
                if count == 1 or count == 2:
                    xy = (drawer_xy[0]+count*drawer_bg.get_height()//3-30, drawer_xy[1]+20)
                    WIN.blit(images, xy)
                    item_rect.append((xy[0], xy[1], images.get_width(), images.get_height()))
                elif count == 3 or count == 4:
                    xy = (drawer_xy[0] + (count-2) * drawer_bg.get_width() // 3 - 30, drawer_xy[1] + drawer_bg.get_height() - images.get_height() - 20)
                    WIN.blit(images, xy)
                    item_rect.append((xy[0], xy[1], images.get_width(), images.get_height()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if pos[0] not in range(drawer_xy[0], drawer_xy[0]+drawer_bg.get_width()) or pos[1] not in range(drawer_xy[1], drawer_xy[1]+drawer_bg.get_height()):
                    loop = False
                for i in range(0, len(item_images)):
                    if pos[0] in range(item_rect[i][0], item_rect[i][0]+item_rect[i][2]) and pos[1] in range(item_rect[i][1], item_rect[i][1]+item_rect[i][3]):
                        # if item[i] in player_bag_man:
                        instruction('Item collected in bag')
                        if items[i] in player_bag_man.keys():
                            player_bag_man[items[i]] = True
                            if no != 0:
                                drawer_items[no-1].remove(items[i])
                            del item_images[i]
                            del item_rect[i]

        del item_rect
        pygame.display.update()

frame_display_list = []


def wall_frame():
    global frame_display_list, open_bag_man
    loop = True
    photos = []
    frame_rect = [(110, 109, 120, 115), (283, 106, 265, 190), (608, 126, 100, 139), (771, 138, 104, 100), (110, 263, 115, 94), (288, 383, 105, 80), (471, 349, 157, 147), (695, 355, 168, 121), (132, 399, 81, 89)]
    for i in range(1, 10):
        img = pygame.image.load('mansion_objects\\p'+str(i)+'.png')
        img = pygame.transform.scale(img, (80, 80*img.get_height()//img.get_width()))
        photos.append(img)

    frame = pygame.image.load('mansion_photos\\wall_frame.png')
    frame = pygame.transform.scale(frame, (int(4*dh/5*frame.get_width()/frame.get_height()), 4*dh//5))
    frame_xy = ((dw-frame.get_width())//2, (dh-frame.get_height())//2)
    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
    instruction('select frames to insert photos')
    while loop:
        pos = pygame.mouse.get_pos()
        WIN.blit(frame, frame_xy)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] not in range(frame_xy[0], frame_xy[0]+frame.get_width()) or pos[1] not in range(frame_xy[1], frame_xy[1]+frame.get_height()):
                    if len(frame_display_list) == 9:
                        instruction('ooh, is this my family, now I can  remember somethings')
                        instruction('Find the Mystery Room Basement')
                    loop = False
                for i in range(0, len(frame_rect)):
                    if pos[0] in range(frame_rect[i][0], frame_rect[i][0] + frame_rect[i][2]) and pos[1] in range(
                            frame_rect[i][1], frame_rect[i][1] + frame_rect[i][3]):
                        open_bag_man = True
                        if player_bag_man['p'+str(i+1)]:
                            clicked = bag_man('p'+str(i+1)+'r')
                            if clicked:
                                frame_display_list.append(i+1)
                        else:
                            instruction('Image missing')
        for i in frame_display_list:
            WIN.blit(photos[i-1], (frame_rect[i-1][0]+(frame_rect[i-1][2]-photos[i-1].get_width())//2, frame_rect[i-1][1]+(frame_rect[i-1][3]-photos[i-1].get_height())//2))

        pygame.display.update()


def mansion_scene5():
    global open_bag_man, player_bag_man
    loop = True
    room3 = pygame.image.load('mansion_photos\\mansion_room3.png')
    room3 = pygame.transform.scale(room3, (dw, dh))
    sofa_rect = (105, 473, 91, 100)
    fireplace_rect = (347, 234, 44, 123)
    fp_rect = (334, 155, 24, 44)
    drawer_rect = (875, 324, 56, 39)
    cup_rect = (707, 324, 47, 70)
    pc_rect = (780, 213, 84, 64)
    door_rect = (51, 95, 110, 266)
    photo_rect = (794, 158, 52, 45)
    photo2_rect = (413, 550, 70, 50)
    photo3_rect = (576, 431, 75, 50)
    while loop:
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(room3, (0, 0))
        if pos[0] in range(sofa_rect[0], sofa_rect[0]+sofa_rect[2]) and pos[1] in range(sofa_rect[1], sofa_rect[1]+sofa_rect[3]):
            mousetext('See', pos)
        if pos[0] in range(fireplace_rect[0], fireplace_rect[0]+fireplace_rect[2]) and pos[1] in range(fireplace_rect[1], fireplace_rect[1]+fireplace_rect[3]):
            mousetext('See', pos)
        if pos[0] in range(fp_rect[0], fp_rect[0]+fp_rect[2]) and pos[1] in range(fp_rect[1], fp_rect[1]+fp_rect[3]):
            mousetext('See', pos)
        if pos[0] in range(drawer_rect[0], drawer_rect[0]+drawer_rect[2]) and pos[1] in range(drawer_rect[1], drawer_rect[1]+drawer_rect[3]):
            mousetext('open drawer', pos)
        if pos[0] in range(pc_rect[0], pc_rect[0]+pc_rect[2]) and pos[1] in range(pc_rect[1], pc_rect[1]+pc_rect[3]):
            mousetext('Check PC', pos)
        if pos[0] in range(cup_rect[0], cup_rect[0]+cup_rect[2]) and pos[1] in range(cup_rect[1], cup_rect[1]+cup_rect[3]):
            mousetext('See', pos)
        if pos[0] in range(door_rect[0], door_rect[0]+door_rect[2]) and pos[1] in range(door_rect[1], door_rect[1]+door_rect[3]):
            mousetext('See', pos)
        if pos[0] in range(photo_rect[0], photo_rect[0]+photo_rect[2]) and pos[1] in range(photo_rect[1], photo_rect[1]+photo_rect[3]):
            mousetext('See', pos)
        if pos[0] in range(photo2_rect[0], photo2_rect[0]+photo2_rect[2]) and pos[1] in range(photo2_rect[1], photo2_rect[1]+photo2_rect[3]):
            mousetext('See', pos)
        if pos[0] in range(photo3_rect[0], photo3_rect[0]+photo3_rect[2]) and pos[1] in range(photo3_rect[1], photo3_rect[1]+photo3_rect[3]):
            mousetext('See', pos)
        elif keys[pygame.K_b]:
            open_bag_man = True
            bag_man()
        elif keys[pygame.K_e]:
            loop = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(sofa_rect[0], sofa_rect[0] + sofa_rect[2]) and pos[1] in range(sofa_rect[1],sofa_rect[1] +sofa_rect[3]):
                    if not player_bag_man['room3_key']:
                        drawer_man(['room3_key'], 0, 'sofa_mat')
                    else:
                        drawer_man([], 0, 'sofa_mat')
                if pos[0] in range(drawer_rect[0], drawer_rect[0] + drawer_rect[2]) and pos[1] in range(drawer_rect[1],drawer_rect[1] + drawer_rect[3]):
                    if player_bag_man['room3_key']:
                        open_bag_man = True
                        select = bag_man('room3_keyr')
                        if select:
                            if not player_bag_man['pc_pass']:
                                drawer_man(['pc_pass'])
                            else:
                                drawer_man([])
                    else:
                        instruction('Need key')
                if pos[0] in range(pc_rect[0], pc_rect[0] + pc_rect[2]) and pos[1] in range(pc_rect[1],pc_rect[1] + pc_rect[3]):
                    desktop()
                if pos[0] in range(fireplace_rect[0], fireplace_rect[0] + fireplace_rect[2]) and pos[1] in range(
                    fireplace_rect[1], fireplace_rect[1] + fireplace_rect[3]):
                    instruction('there is a hidden safe')
                    instruction('Enter pin to open')
                    pin = gps()
                    if pin == '7355':
                        if not player_bag_man['taser']:
                            drawer_man(['taser'], 0, 'safe_bg')
                        else:
                            drawer_man([], 0, 'safe_bg')
                    else:
                        instruction('wrong pin')
                if pos[0] in range(cup_rect[0], cup_rect[0] + cup_rect[2]) and pos[1] in range(cup_rect[1],cup_rect[1] + cup_rect[3]):
                    if not player_bag_man['cello_tape']:
                        drawer_man(['cello_tape'])
                    else:
                        drawer_man([])
                if pos[0] in range(fp_rect[0], fp_rect[0] + fp_rect[2]) and pos[1] in range(fp_rect[1],fp_rect[1] + fp_rect[3]):
                    if not player_bag_man['fp1']:
                        drawer_man(['fp1'], 0, 'dirty_bg')
                    else:
                        drawer_man([], 0, 'dirty_bg')
                if pos[0] in range(door_rect[0], door_rect[0] + door_rect[2]) and pos[1] in range(door_rect[1],door_rect[1] +door_rect[3]):
                    mansion_scene7()
                if pos[0] in range(photo_rect[0], photo_rect[0] + photo_rect[2]) and pos[1] in range(photo_rect[1],photo_rect[1] +photo_rect[3]):
                    if not player_bag_man['p5']:
                        drawer_man(['p5'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
                if pos[0] in range(photo2_rect[0], photo2_rect[0] + photo2_rect[2]) and pos[1] in range(photo2_rect[1],photo2_rect[1] +photo2_rect[3]):
                    if not player_bag_man['p7']:
                        drawer_man(['p7'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
                if pos[0] in range(photo3_rect[0], photo3_rect[0] + photo3_rect[2]) and pos[1] in range(photo3_rect[1],photo3_rect[1] +photo3_rect[3]):
                    if not player_bag_man['p8']:
                        drawer_man(['p8'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
        pygame.display.update()


def desktop():
    loop = True
    pc_lock = pygame.image.load('mansion_objects\\pc_lock.png')
    pc_lock = pygame.transform.scale(pc_lock, (dw-200, dh-100))
    pc_desk = pygame.image.load('mansion_objects\\pc_desk.png')
    pc_desk = pygame.transform.scale(pc_desk, (dw-200, dh-100))
    game_img = pygame.image.load('mansion_objects\\game.png')
    game_img = pygame.transform.scale(game_img, (dw-200, dh-100))
    game_rect = (148, 80, 48, 63)
    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
    password = 0
    desk = False
    game = False
    flag = True
    while loop:
        pos = pygame.mouse.get_pos()
        if desk:
            WIN.blit(pc_desk, (100, 50))
        else:
            WIN.blit(pc_lock, (100, 50))
        if not desk:
            password = gps((dw//2-90, dh//2+35, 100, 25))
        if password == '1096':
            desk = True
        elif password == '7':
            instruction('7355 is the password')
            loop = False
        else:
            instruction('Wrong PIN!')
            loop = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP and desk:
                if pos[0] in range(game_rect[0], game_rect[0]+game_rect[2]) and pos[1] in range(game_rect[1], game_rect[1]+game_rect[3]):
                    game = True
                if pos[0] not in range(100, dw - 100) or pos[1] not in range(50, dh - 50):
                    loop = False
        if game:
            WIN.blit(game_img, (100, 50))
            if flag:
                instruction('Enter total number of differences in the lock screen to get safe code')
                flag = False

        pygame.display.update()

def mansion_scene7():
    global open_bag_man, player_bag_man
    loop = True
    bg = pygame.image.load('mansion_photos\\mansion_room2.jpg')
    bg = pygame.transform.scale(bg, (dw, dh))
    drawer_rect = (60, 490, 107, 86)
    rack_rect = (622, 100, 100, 42)
    id_rect = (35, 60, 130, 190)
    photo_rect =  (590, 260, 122, 60)
    while loop:
        WIN.blit(bg, (0, 0))
        pos = pygame.mouse.get_pos()
        if pos[0] in range(drawer_rect[0], drawer_rect[0] + drawer_rect[2]) and pos[1] in range(drawer_rect[1], drawer_rect[1] + drawer_rect[3]):
            mousetext('Check', pos)
        if pos[0] in range(rack_rect[0], rack_rect[0] + rack_rect[2]) and pos[1] in range(rack_rect[1], rack_rect[1] + rack_rect[3]):
            mousetext('Check', pos)
        if pos[0] in range(id_rect[0], id_rect[0] + id_rect[2]) and pos[1] in range(id_rect[1], id_rect[1] + id_rect[3]):
            mousetext('Check', pos)
        if pos[0] in range(photo_rect[0], photo_rect[0] + photo_rect[2]) and pos[1] in range(photo_rect[1], photo_rect[1] + photo_rect[3]):
            mousetext('Check', pos)
        keys = pygame.key.get_pressed()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(drawer_rect[0], drawer_rect[0] + drawer_rect[2]) and pos[1] in range(drawer_rect[1],drawer_rect[1] +drawer_rect[3]):
                    if player_bag_man['crowbar']:
                        open_bag_man = True
                        req = bag_man('crowbarr')
                        if req:
                            if not player_bag_man['powder']:
                                drawer_man(['powder'])
                            else:
                                drawer([])
                    else:
                        instruction('Locked')
                if pos[0] in range(rack_rect[0], rack_rect[0] + rack_rect[2]) and pos[1] in range(rack_rect[1],rack_rect[1] + rack_rect[3]):
                    if not player_bag_man['crowbar']:
                        drawer_man(['crowbar'])
                    else:
                        drawer_man([])
                if pos[0] in range(id_rect[0], id_rect[0] + id_rect[2]) and pos[1] in range(id_rect[1],id_rect[1] + id_rect[3]):
                    if not player_bag_man['id']:
                        drawer_man(['id'], 0, 'table_top')
                    else:
                        drawer_man([], 0, 'table_top')
                if pos[0] in range(photo_rect[0], photo_rect[0] + photo_rect[2]) and pos[1] in range(photo_rect[1],photo_rect[1] + photo_rect[3]):
                    if not player_bag_man['p4']:
                        drawer_man(['p4'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
        if keys[pygame.K_e]:
            loop = False
        elif keys[pygame.K_b]:
            open_bag_man = True
            bag_man()
        pygame.display.update()



def mansion_scene8():
    global open_bag_man, player_bag_man
    loop = True
    bg = pygame.image.load('mansion_photos\\mansion_room1.png')
    bg = pygame.transform.scale(bg, (dw, dh))
    piano_rect = (114, 337, 156, 73)
    clock_rect = (440, 253, 75, 95)
    trunk_rect = (544, 410, 126, 100)
    while loop:
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(bg, (0, 0))
        if pos[0] in range(piano_rect[0], piano_rect[0]+piano_rect[2]) and pos[1] in range(piano_rect[1], piano_rect[1]+piano_rect[3]):
            mousetext('Look', pos)
        if pos[0] in range(clock_rect[0], clock_rect[0]+clock_rect[2]) and pos[1] in range(clock_rect[1], clock_rect[1]+clock_rect[3]):
            mousetext('Look', pos)
        if pos[0] in range(trunk_rect[0], trunk_rect[0]+trunk_rect[2]) and pos[1] in range(trunk_rect[1], trunk_rect[1]+trunk_rect[3]):
            mousetext('Open', pos)
        if keys[pygame.K_b]:
            open_bag_man = True
            bag_man()
        elif keys[pygame.K_e]:
            loop = False
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(piano_rect[0], piano_rect[0] + piano_rect[2]) and pos[1] in range(piano_rect[1],piano_rect[1] +piano_rect[3]):
                    if not player_bag_man['p3']:
                        drawer_man(['p3'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
                if pos[0] in range(clock_rect[0], clock_rect[0] + clock_rect[2]) and pos[1] in range(clock_rect[1],clock_rect[1] +clock_rect[3]):
                    if not player_bag_man['p6']:
                        drawer_man(['p6'], 0, 'frame_bg')
                    else:
                        drawer_man([], 0, 'frame_bg')
                if pos[0] in range(trunk_rect[0], trunk_rect[0] + trunk_rect[2]) and pos[1] in range(trunk_rect[1],trunk_rect[1] +trunk_rect[3]):
                    if player_bag_man['bbp']:
                        open_bag_man = True
                        req = bag_man('bbpr')
                        if req:
                            if not player_bag_man['brush']:
                                drawer_man(['brush'], 0, 'table_top')
                            else:
                                drawer_man([], 0, 'table_top')

                    else:
                        instruction('Locked')

        pygame.display.update()


def mansion_scene6():
    global start
    loop = True
    bg = pygame.image.load('mansion_photos\\basement.png')
    bg = pygame.transform.scale(bg, (dw, dh))
    body_rect = (521, 410, 223, 158)
    while loop:
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        WIN.blit(bg, (0, 0))
        if keys[pygame.K_e]:
            loop = False
        if pos[0] in range(body_rect[0], body_rect[0] + body_rect[2]) and pos[1] in range(body_rect[1],body_rect[1] + body_rect[3]):
            mousetext('WHAT', pos)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONUP:
                if pos[0] in range(body_rect[0], body_rect[0] + body_rect[2]) and pos[1] in range(body_rect[1], body_rect[1] +body_rect[3]):
                    instruction('There\'s something in his pocket. A photo? It can\'t be.')
                    instruction('Can he be the reason for all this? What did even happen here?')
                    instruction('There is a lot of things I don\'t understand')
                    instruction('Story will be revealed in season 2')
                    end = timeit.timeit()
                    with open('send.txt', 'w') as f:
                        txt = random.choice(['sdfsaf', 'dfgaweg', 'fghterdf', 'iyrewyy', 'jioh'])
                        f.write(txt)
                        f.write(str(end - start))
                        txt = random.choice(['sdfsaf', 'dfgaweg', 'fghterdf', 'iyrewyy', 'jioh'])
                        f.write(txt)
                        f.write('121.5456')
                    thank_you()
        pygame.display.update()


def thank_you():
    loop = True
    draw_rect_alpha(WIN, (0, 0, 0, 128), (0, 0, dw, dh))
    text = game_name.render('Thank You For Playing', True, red)
    credits = pygame.font.Font('fonts\\font5.ttf', 50)
    credits1 = pygame.font.Font('fonts\\font5.ttf', 40)
    credits2 = pygame.font.Font('fonts\\font5.ttf', 40)
    cred_text = credits.render('CREDITS:', True, yellow)
    storyline = credits1.render('STORYLINE AND GRAPHICS:', True, white)
    program = credits2.render('PROGRAMMED BY:', True, white)
    names = pygame.font.Font('fonts\\font5.ttf', 30)
    name1 = names.render('Special Thanks to: Isha, Ishita, Deepankar, Gunjan, Mohnish', True, blue)
    name2 = names.render('Harshit Singh', True, blue)
    while loop:
        WIN.blit(home_bg, (0, 0))
        WIN.blit(text, [(dw-text.get_width())//2, 50])
        WIN.blit(cred_text, [(dw-cred_text.get_width())//2, 150])
        WIN.blit(storyline, [(dw-storyline.get_width())//2, 250])
        WIN.blit(name1, [(dw-name1.get_width())//2, 350])
        WIN.blit(program, [(dw-program.get_width())//2, 450])
        WIN.blit(name2, [(dw-name2.get_width())//2, 550])
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()


# mansion_scene1()
home_page()
# thank_you()
pygame.quit()

