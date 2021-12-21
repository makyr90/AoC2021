from common import get_input_of_day
from itertools import product
from functools import lru_cache

def dice_roll(dice):

    dice_sum = 0
    for idx in range(3):
        dice = dice + 1 if dice < 100 else 1
        dice_sum += dice

    return dice_sum, dice

def solve_part1(player1_pos,player2_pos):

    player1_score = 0
    player2_score = 0
    dice = 0
    dice_rolls = 0
    while True:
        
        dice_rolls += 3
        dice_sum , dice = dice_roll(dice)
        player1_pos += dice_sum
        player1_pos = 10 if (player1_pos % 10 == 0) else player1_pos % 10
        player1_score += player1_pos
        if player1_score >= 1000:

            return player2_score * dice_rolls

        dice_rolls += 3
        dice_sum , dice = dice_roll(dice)
        player2_pos += dice_sum
        player2_pos = 10 if (player2_pos % 10 == 0) else player2_pos % 10
        player2_score += player2_pos
        if player2_score >= 1000:

            return player1_score * dice_rolls

@lru_cache(maxsize=None)
def universe_game(player1_pos,player2_pos,player1_score,player2_score):

    if player2_score >= 21:

        return 0,1

    else:
        p1_win_universes = 0
        total_universes = 0
        for q_roll in product((1,2,3),repeat=3):
            step_player_pos = player1_pos + sum(q_roll)
            step_player_pos = 10 if (step_player_pos % 10 == 0) else step_player_pos % 10
            step_player_score = player1_score + step_player_pos
            p2_win_universes, universes = universe_game(player2_pos,step_player_pos,player2_score,step_player_score)
            total_universes += universes
            p1_win_universes += (universes - p2_win_universes)

        return (p1_win_universes,total_universes)

def solve_part2(player1_pos,player2_pos):

    p1_win_universes, total_universes = universe_game(player1_pos,player2_pos,0,0)

    return max(p1_win_universes, total_universes - p1_win_universes)

if __name__ == '__main__':

    data = get_input_of_day(21,True).split("\n")
    player1_pos = int(data[0].split()[-1])
    player2_pos = int(data[1].split()[-1])
    print("Day 21 part 1 answer: {}".format(solve_part1(player1_pos,player2_pos)))
    print("Day 21 part 2 answer: {}".format(solve_part2(player1_pos,player2_pos)))
