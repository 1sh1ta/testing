import pygame
import time

pygame.init() # Initialize a Pygame class

#Define colours
yellow = (245, 224, 66)
black = (0, 0, 0)
red = (201, 64, 30)
blue = (47, 47, 235)

#Customize our screen
width, height = 1023, 495
pygame.display.set_caption("Pacman")
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("Pacman Icon.png")
pygame.display.set_icon(icon)

#Pacman moving functions
move_right = [pygame.transform.scale(pygame.image.load('open_right.png'), (33, 33)), pygame.transform.scale(pygame.image.load('closed_right.png'), (33, 33))]

move_left = [pygame.transform.scale(pygame.image.load('open_left.png'), (33, 33)), pygame.transform.scale(pygame.image.load('closed_left.png'), (33, 33))]

move_down = [pygame.transform.scale(pygame.image.load('open_down.png'), (33, 33)), pygame.transform.scale(pygame.image.load('closed_down.png'), (33, 33))]

move_up = [pygame.transform.scale(pygame.image.load('open_up.png'), (33, 33)), pygame.transform.scale(pygame.image.load('closed_up.png'), (33, 33))]

#Pacman Information
position = [500, 232]
direction = 'RIGHT'

left = False
right = False
up = False
down = False
walkCount = 0

#Create a clock object to control the frame rate
clock = pygame.time.Clock()

#these represent the horizontal lines in the map
horizontal_wall_list = [[[1, 1], [31, 1]], [[3, 3], [5, 3]], [[9, 3], [11, 3]], 
                        [[13, 3], [19, 3]], [[21, 3], [23, 3]], [[5, 5], [7, 5]],
                        [[11, 5], [14, 5]], [[18, 5], [21, 5]], [[25, 5], [27, 5]],
                        [[1, 6], [3, 6]], [[29, 6], [31, 6]], [[7, 7], [9, 7]],
                        [[13, 7], [15, 7]], [[17, 7], [19, 7]], [[23, 7], [25, 7]],
                        [[3, 8], [5, 8]], [[27, 8], [29, 8]], [[7, 9], [11, 9]],
                        [[23, 9], [25, 9]], [[1, 10], [3, 10]], [[29, 10], [31, 10]],
                        [[5, 11], [7, 11]], [[11, 11], [14, 11]], [[18, 11], [21, 11]],
                        [[25, 11], [27, 11]], [[9, 13], [11, 13]], [[13, 13], [19, 13]],
                        [[21, 13], [23, 13]], [[27, 13], [29, 13]], [[1, 15], [31, 15]],
                        [[13, 9], [19, 9]], [[27, 3], [29, 3]], [[3, 13], [5, 13]]]

#These represent the vertical lines in the map
vertical_wall_list = [[[1, 1], [1, 7]], [[3, 3], [3, 4]], [[5, 5], [5, 11]],
                      [[7, 3], [7, 7]], [[7, 13], [7, 15]], [[9, 3], [9, 7]],
                      [[9, 9], [9, 13]], [[11, 5], [11, 7]], [[11, 9], [11, 11]],
                      [[13, 7], [13, 9]], [[16, 3], [16, 5]], [[16, 9], [16, 13]],
                      [[18, 5], [18, 7]], [[19, 7], [19, 9]], [[21, 5], [21, 7]],
                      [[21, 9], [21, 11]], [[21, 13], [21, 15]], [[23, 3], [23, 4]],
                      [[23, 6], [23, 7]], [[23, 9], [23, 13]], [[25, 3], [25, 5]],
                      [[25, 13], [25, 15]], [[27, 5], [27, 11]], [[29, 12], [29, 13]],
                      [[31, 1], [31, 7]], [[3, 12], [3, 13]], [[29, 3], [29, 4]],
                      [[1, 9], [1, 15]], [[31, 9], [31, 15]]]

#this function takes input (which is a list of two coordinates)
# It multiplies each x and y value in the coordinates by 33 and subtract 16 to match the block's centre pixel
def wall_printer(inp):
    blue = (47, 47, 235)
    p1 = [(inp[0][0] * 33) - 16, (inp[0][1] * 33) - 16]
    p2 = [(inp[1][0] * 33) - 16, (inp[1][1] * 33) - 16]
    new = pygame.draw.line(screen, blue, p1, p2, 13)
    return new

def print_all_walls(): #Function to print all the walls
    for i in (vertical_wall_list):
        wall_printer(i)
    for i in (horizontal_wall_list):
        wall_printer(i)

def redraw_screen():
    global walkCount
    
    screen.fill(black) #Fill the screen with black
    print_all_walls()

    if walkCount + 1 >= 6: #If walkCount is greater than or equal to 6, which is the frame rate, reset it to 0
        walkCount = 0
    if right:
        screen.blit(move_right[walkCount//3], (position[0], position[1]))
    elif left:
        screen.blit(move_left[walkCount//3], (position[0], position[1]))
    elif up:
        screen.blit(move_up[walkCount//3], (position[0], position[1]))
    elif down:
        screen.blit(move_down[walkCount//3], (position[0], position[1]))
    else: 
        pygame.draw.circle(screen, yellow, (int(position[0] + 15), int(position[1] + 15)), 15)
        walkCount = 0 #Reset walkCount to 0

    time.sleep(1/100) #Sleep for 0.1 seconds to control the frame rate
    pygame.display.update()

def endgame(): #for when pacman gets eaten by a ghost or runs out of lives
    font = pygame.font.SysFont('impactms', 50)

    game_over_surface = font.render('GAME OVER', True, red)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.center = [(width/2), (height/2)]

    screen.blit(game_over_surface, game_over_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

wall_blacklist = []

def blacklist():
    for line in horizontal_wall_list:
        x1, y = line[0]
        x2, y = line[1]
        for i in range(x1, x2+1):
            wall_blacklist.append((i, y))
    for line in vertical_wall_list:
        x, y1 = line[0]
        x, y2 = line[1]
        for i in range (y1, y2+1):
            wall_blacklist.append((x, i))

blacklist()

def collide(inp):
    for i in wall_blacklist:
        if inp[0] < ((i[0] * 33) - 16) + 27: #right
            return True
        if inp[0] > ((i[0] * 33) - 16) - 27: #left
            return True
        if inp[1] < ((i[1] * 33) - 16) + 27: #down
            return True
        if inp[1] > ((i[1] * 33) - 16) - 27: #up
            return True
    return False

#Main running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Moving pacman
    keys = pygame.key.get_pressed() #Get the keys pressed
    if keys[pygame.K_RIGHT]:
        new_pos = [(position[0] + 11), position[1]]
        if not collide(new_pos):
            position[0] += 11
            right = True
            left = False
            up = False
            down = False
            walkCount += 1
        else:
            right = False
            left = False
            up = False
            down = False
            walkCount += 0
    elif keys[pygame.K_LEFT]:
        position[0] -= 11
        right = False
        left = True
        up = False
        down = False
        walkCount += 1

    elif keys[pygame.K_UP]:
        position[1] -= 11
        right = False
        left = False
        up = True
        down = False
        walkCount += 1

    elif keys[pygame.K_DOWN]:
        position[1] += 11
        right = False
        left = False
        up = False
        down = True
        walkCount += 1

    else:
        right = False
        left = False
        up = False
        down = False
        walkCount = 0

    #Create a clock
    clock = pygame.time.Clock()
    clock.tick(25)
    redraw_screen() #Redraw the screen

pygame.quit() #Quit pygame properly