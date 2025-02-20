import pygame as pg
from random import randint
 
pg.init()

WHITE =   (255, 255, 255)
BLACK =   (  0,   0,   0)
GRAY =    (202, 204, 203)
GREEN =   ( 12, 107,  31)
D_GREEN = ( 11,  84,  26)
RED =     (255,   0,   0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLOCK_SIZE = 20
MAX_X = SCREEN_WIDTH // BLOCK_SIZE - 1
MAX_Y = SCREEN_HEIGHT // BLOCK_SIZE - 1

# 게임 창의 이름 설정
pg.display.set_caption("Snake")

def draw_snake(screen, blocks):
    """ screen의 position 위치에 color 색으로 블록을 그립니다. """
    # blocks : [(y, x), ...]
    # pg.Rect 인스턴스 ((x, y), (w, h))
    head = pg.Rect((blocks[0][0]*BLOCK_SIZE, blocks[0][1]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pg.draw.rect(screen, D_GREEN, head)
    if len(blocks) > 1:
        for y, x in blocks[1:]:
            block = pg.Rect((y*BLOCK_SIZE, x*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(screen, GREEN, block)

def draw_apple(screen, block):
    """ screen의 position 위치에 color 색으로 블록을 그립니다. """
    # blocks : [(y, x), ...]
    # pg.Rect 인스턴스 ((x, y), (w, h))
    apple = pg.Rect((block[0][0]*BLOCK_SIZE, block[0][1]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pg.draw.rect(screen, RED, apple)

apple = []
extension = False
done = False
clock = pg.time.Clock()
# blocks = [[5, 5]]
snake = [[5, 5]]
last_block = snake[-1]
current_direction = None

font = pg.font.SysFont('comicsans', 20, True)

def get_apple_coord():
    x = randint(0, MAX_X)
    y = randint(0, MAX_Y)
    while [x, y] in snake:
        x = randint(0, MAX_X)
        y = randint(0, MAX_Y)
    # apple = pg.Rect((x, y), (BLOCK_SIZE, BLOCK_SIZE))
    # pg.draw.rect(screen, RED, apple)
    return [x, y]

def paint_score(snake, screen):
    score = len(snake)
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    screen.blit(text, (320, 10))


while not done:
    # 1초당 화면 출력 횟수 (10, 30 60 정도로 설정)
    clock.tick(10) 
    
    screen.fill(GRAY)
    # [y, x]

    # 아무 이벤트(키보드 입력)가 발생하지 않은 경우를 표시
    is_event = False

    
    # 게임 실행 중 발생하는 이벤트를 포착
    ## 게임 종료 이벤트가 발생하면 메인 루프 종료하도록 처리
    for event in pg.event.get():
        # 게임 실행 창의 종료 버튼 클릭시
        if event.type == pg.QUIT:
            done = True
        # 키보드가 눌렸다면
        elif event.type == pg.KEYDOWN:
            # 기존 진행방향의 반대 방향으로 키보드를 누른 경우가 아닌 경우
            if (not (current_direction == 'DOWN' and event.key == pg.K_UP)) and (not (current_direction == 'UP' and event.key == pg.K_DOWN)) and (not (current_direction == 'LEFT' and event.key == pg.K_RIGHT)) and (not (current_direction == 'RIGHT' and event.key == pg.K_LEFT)):
                last_block = snake[-1]
                is_event = True
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1][:]
                
                # 어떤 키보드가 눌렸는지에 따라
                if event.key == pg.K_UP:
                    current_direction = 'UP'
                    snake[0][1] -= 1
                elif event.key == pg.K_DOWN:
                    current_direction = 'DOWN'
                    snake[0][1] += 1
                elif event.key == pg.K_LEFT:
                    current_direction = 'LEFT'
                    snake[0][0] -= 1
                elif event.key == pg.K_RIGHT:
                    current_direction = 'RIGHT'
                    snake[0][0] += 1
            # 기존 진행방향의 반대 방향으로 키보드를 누른 경우에는 해당 이벤트를 무시
            else:
                last_block = snake[-1]
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1][:]
                        
                # 기존 진행방향에 따라
                if current_direction == 'UP':
                    snake[0][1] -= 1
                elif current_direction == 'DOWN':
                    snake[0][1] += 1
                elif current_direction == 'LEFT':
                    snake[0][0] -= 1
                elif current_direction == 'RIGHT':
                    snake[0][0] += 1
    
    # 아무 이벤트가 발생하지 않은 경우에는 기존 진행방향으로 진행
    if not is_event:
        last_block = snake[-1]
        for i in range(len(snake)-1, 0, -1):
            snake[i] = snake[i-1][:]
                
        # 기존 진행방향에 따라
        if current_direction == 'UP':
            snake[0][1] -= 1
        elif current_direction == 'DOWN':
            snake[0][1] += 1
        elif current_direction == 'LEFT':
            snake[0][0] -= 1
        elif current_direction == 'RIGHT':
            snake[0][0] += 1
        
            
    # 화면 밖으로 이동해서 게임오버
    if not (0 <= snake[0][0] <= MAX_X and 0 <= snake[0][1] <= MAX_Y):
        done = True
    # 몸통과 부딪혀서 게임오버
    if snake[0] in snake[1:]:
        done = True

    # 사과를 먹었을 때
    if apple and snake[0] == apple[0]:
        apple.clear()      
        snake.append(last_block)

    draw_snake(screen, snake)
    
    # screen에 사과가 없을 때에만 새로운 사과를 생성
    if not apple:
        apple.append(get_apple_coord())
    
    draw_apple(screen, apple)

    paint_score(snake, screen)

    # 메인 루프의 끝에 반드시 display.flip()을 통해 메인 루프에서 진행된 작업을 화면에 업데이트 해주어야 함
    pg.display.flip()

pg.quit()