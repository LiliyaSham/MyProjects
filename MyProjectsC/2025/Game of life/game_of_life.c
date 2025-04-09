#include <ncurses.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define WIDTH 80
#define HEIGHT 25

void initialize_field(int field[HEIGHT][WIDTH]);
void update_field(int field1[HEIGHT][WIDTH], int field2[HEIGHT][WIDTH]);
int count_neighbors(int field1[HEIGHT][WIDTH], int y, int x);
int decision(int neighbors, int condition);
void change_field(int field2[HEIGHT][WIDTH], int field1[HEIGHT][WIDTH]);
int check(int field1[HEIGHT][WIDTH], int field2[HEIGHT][WIDTH]);
int set_speed(char button, int *flag, int time_msec);
int count(int field[HEIGHT][WIDTH]);

int main() {
    int field1[HEIGHT][WIDTH] = {0};
    int field2[HEIGHT][WIDTH];
    int time_msec = 500;
    int stop = 0;

    initialize_field(field1);
    if (freopen("/dev/tty", "r", stdin)) initscr();

    nodelay(stdscr, true);

    while (stop != 1) {
        char button = getch();
        if (count(field1) == 0) {
            stop = 1;
        }
        time_msec = set_speed(button, &stop, time_msec);
        usleep(time_msec * 1000);
        clear();
        update_field(field1, field2);

        if (check(field1, field2) == 2000) {
            stop = 1;
        }
        change_field(field2, field1);
        // refresh();
    }
    endwin();
    return 0;
}

void initialize_field(int field[HEIGHT][WIDTH]) {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            char a;
            scanf("%c", &a);
            if (a == 'x') field[y][x] = 1;
            // field[y][x] = rand() % 2;
        }
    }
}

void update_field(int field1[HEIGHT][WIDTH], int field2[HEIGHT][WIDTH]) {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            field2[y][x] = decision(count_neighbors(field1, y, x), field1[y][x]);
            if (field2[y][x] == 1)
                printw("x");
            else
                printw(" ");
        }
        printw("\n");
    }
}

int count_neighbors(int field1[HEIGHT][WIDTH], int y, int x) {
    int sum = 0;
    int y_minus = y - 1, x_minus = x - 1, y_plus = y + 1, x_plus = x + 1;

    if (y_minus < 0) y_minus = HEIGHT - 1;
    if (x_minus < 0) x_minus = WIDTH - 1;
    if (y_plus > HEIGHT - 1) y_plus = y_plus % HEIGHT;
    if (x_plus > WIDTH - 1) x_plus = x_plus % WIDTH;

    sum += field1[y_minus][x_minus];
    sum += field1[y_minus][x];
    sum += field1[y_minus][x_plus];
    sum += field1[y][x_plus];
    sum += field1[y_plus][x_plus];
    sum += field1[y_plus][x];
    sum += field1[y_plus][x_minus];
    sum += field1[y][x_minus];

    return sum;
}

int decision(int neighbors, int condition) {
    int next_gen;
    if ((neighbors == 2 || neighbors == 3) && (condition == 1)) {
        next_gen = 1;
    } else if (neighbors == 3 && condition == 0) {
        next_gen = 1;
    } else {
        next_gen = 0;
    }

    return next_gen;
}

void change_field(int field2[HEIGHT][WIDTH], int field1[HEIGHT][WIDTH]) {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            field1[y][x] = field2[y][x];
        }
    }
}

int check(int field1[HEIGHT][WIDTH], int field2[HEIGHT][WIDTH]) {
    int i = 0;
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            if (field1[y][x] == field2[y][x]) i++;
        }
    }
    return i;
}

int set_speed(char button, int *flag, int time_msec) {
    if (button == '1')
        time_msec = 900;
    else if (button == '2')
        time_msec = 400;
    else if (button == '3')
        time_msec = 70;
    else if (button == 'q')
        *flag = 1;

    return time_msec;
}

int count(int field[HEIGHT][WIDTH]) {
    int sum = 0;
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            sum += field[y][x];
        }
    }
    return sum;
}
