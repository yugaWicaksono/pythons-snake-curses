import random
import curses

screen = curses.initscr()
curses.curs_set(0)

screen_height, screen_width = screen.getmaxyx()

window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)  # accept window input
window.timeout(100)  # refresh every 100 ms

window.border()


snake_x = round(screen_width/4)
snake_y = round(screen_height/2)

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2],
]


food = [round(screen_height/2), round(screen_width/2)]

window.addch(food[0], food[1], curses.ACS_PI)


key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1

    if key == curses.KEY_UP:
        new_head[0] -= 1

    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screen_height - 10),
                random.randint(1, screen_width - 10)
            ]

            food = new_food if new_food not in snake else None

            try:
                window.addch(food[0], food[1], curses.ACS_PI)
            except (curses.error):
                pass
    else:
        tail = snake.pop()
        try:
            window.addch(round(tail[0]), round(tail[1]), ' ')
        except(curses.error):
            pass

    try:
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    except(curses.error):
        raise curses.error
