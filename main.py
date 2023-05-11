import curses
import math


def main_loop(screen):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    while True:
        rows, cols = screen.getmaxyx()
        # top_border = "=" * cols
        stat_box = curses.newwin(math.floor(rows / 3), math.floor(cols / 3), 0, 0)
        stat_box.bkgd(' ', curses.color_pair(1))
        stat_box.addstr(1, 1, "This is a window", curses.color_pair(1))
        stat_box.border()

        system_box = curses.newwin(rows - math.floor(rows / 3), math.floor(cols / 3), math.ceil(rows / 3), 0)
        system_box.bkgd(' ', curses.color_pair(1))
        system_box.addstr(1, 1, "System Information", curses.color_pair(1))
        system_box.border()

        main_box = curses.newwin(rows, math.floor(cols / 3) * 2 , 0, math.ceil(cols / 3))
        main_box.bkgd(' ', curses.color_pair(1))
        main_box.addstr(1, 1, "Welcome to bla bla bla", curses.color_pair(1))
        main_box.border()

        stat_box.refresh()
        system_box.refresh()
        main_box.refresh()
        screen.refresh()

        screen.getch()


def init_screen():
    _screen = curses.initscr()
    return _screen


scr = init_screen()
curses.wrapper(main_loop)