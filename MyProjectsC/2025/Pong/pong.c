#include <stdio.h>
// показывает поле 
void show_field(int x_ball, int y_ball, int y_pl1, int y_pl2, int score_1, int score_2);
// выводит текущиую сторону попадание шара
int current_side_ball(int x_ball, int y_ball, int y_pl1, int y_pl2);
// ввод числа
char input_ch(int player);
// обработка действий игрока_1
int action_processing_player1(int rocket_1_y, char input);
// обработка действий игрока_2
int action_processing_player2(int rocket_2_y, char input);
// изменение направления мяча по вертикали
int vertical_delta(int side, int delta_y);
// изменение направления мяча по горизонтали
int gorizont_delta(int side, int delta_x);
// условия выигрыша
void Winner(int score_1, int score_2);

int main() {
    int player = 0;  // определяет игрока
    int score_1 = 0; 
    int score_2 = 0; 
    int delta_x = -1; 
    int delta_y = 1;
    int rocket_1_y = 5;
    int rocket_2_y = 5;
    int ball_x = 39;
    int ball_y = 12;
    while (score_1 < 21 && score_2 < 21) { // основной код программы

        show_field(ball_x, ball_y, rocket_1_y, rocket_2_y, score_1, score_2);
        char input = input_ch(player); // проверяет на правильный ввод игрока
        if (input == ' ') {
            player = (player == 1) ? 0 : 1;
        }
        else if (player == 0) 
        {
            rocket_1_y = action_processing_player1(rocket_1_y, input);
        } else {
            rocket_2_y = action_processing_player2(rocket_2_y, input);
        }

        int side = current_side_ball(ball_x, ball_y, rocket_1_y, rocket_2_y);
        delta_y = vertical_delta(side, delta_y);
        delta_x = gorizont_delta(side, delta_x);
        if (side == 0) {
            score_2++;
            ball_x = 40;
            ball_y = 12;
        } else if (side == 1) {
            score_1++;
            ball_x = 40;
            ball_y = 12;
        }
        ball_x += delta_x;
        ball_y += delta_y;
        if (input != ' ')
        {
            player = (player == 1) ? 0 : 1;
        }
    }
    Winner(score_1, score_2);
}

void show_field(int x_ball, int y_ball, int y_pl1, int y_pl2, int score_1, int score_2) {
    printf("\033[H\033[J");

    printf("%30d%20d\n", score_1, score_2);

    for (int i = 0; i <= 25; i++) {
        for (int j = 0; j < 80; j++) {
            if (i == 0 || i == 25) {
                printf("-");
            }
            else if (j == 0 || j == 79 || (j == 5 && i >= y_pl1 - 1 && i <= y_pl1 + 1) ||
                    (j == 74 && i >= y_pl2 - 1 && i <= y_pl2 + 1)) {
                printf("|");
            }
            else if (i == y_ball && j == x_ball) {
                printf("0");
            }
            else
            {
                printf(" ");
            }

        }
        printf("\n");
    }
}

int current_side_ball(int x_ball, int y_ball, int y_pl1, int y_pl2)
{
    int side = 5;
    if (x_ball == 0) {
        side = 0;
    }

    if (x_ball == 79) {
        side = 1;
    }

    if (y_ball == 1) {
        side = 2;
    }

    if (y_ball == 24) {
        side = 3;
    }
    if ((x_ball == 6 && y_ball >= y_pl1 - 1 && y_ball <= y_pl1 + 1) ||
        (x_ball == 73 && y_ball >= y_pl2 - 1 && y_ball <= y_pl2 + 1)) {
        side = 4;
    }
    return side;
}

char input_ch(int player)
{
    char input = 'q';
    while (1) {
        fflush(stdin);
        input = getchar();
        char c1 = getchar();
        if (((input == ' ' || input == 'k' || input == 'K' || input == 'm' || input == 'M') && player == 1 && c1 == '\n') || 
            ((input == ' ' || input == 'a' || input ==  'A' || input == 'z' || input == 'Z') && player == 0 && c1 == '\n'))
        {
            break;
        }
    }
    return input;
}

int action_processing_player1(int rocket_1_y, char input)
{
    if (input == 'a' || input == 'A') {
        if (rocket_1_y - 3 > 0) {
            rocket_1_y -= 2;
        } else if (rocket_1_y == 3) {
            rocket_1_y -= 1;
        }
    } else if (input == 'z' || input == 'Z') {
        if (rocket_1_y + 3 < 25) {
            rocket_1_y += 2;
        } else if (rocket_1_y == 22) {
            rocket_1_y += 1;
        }
        
    }
    return rocket_1_y;
}
int action_processing_player2(int rocket_2_y, char input)
{
    if (input == 'k' || input == 'K') {
        if (rocket_2_y - 3 > 0) {
            rocket_2_y -= 2;
        } else if (rocket_2_y == 3) {
            rocket_2_y -= 1;
        }
    } else if (input == 'm' || input == 'M') {
        if (rocket_2_y + 3 < 25) {
            rocket_2_y += 2;
        } else if (rocket_2_y == 22) {
            rocket_2_y += 1;
        }
    }
    return rocket_2_y;
}

int vertical_delta(int side, int delta_y)
{
    if (side == 2 || side == 3) 
    {
        delta_y *= (-1);
    }
    return delta_y;
}

int gorizont_delta(int side, int delta_x)
{
    if (side == 4) 
    {
        delta_x *= (-1);
    } 
    else if (side == 0)
    {
        delta_x = -1;
    }
    else if (side == 1)
    {
        delta_x = 1;
    }
    return delta_x;
}

void Winner(int score_1, int score_2)
{
    if (score_1 == 21) {
        printf("Player_1 Win!!!");
    } else if (score_2 == 21) {
        printf("Player_2 Win!!!");
    }
}