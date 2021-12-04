from common import get_input_of_day
import numpy as np
import math

def read_data(input_list):

    random_numbers = input_list[0].split(",")
    decks = []
    deck = []
    for row in input_list[2:]:
        if row.strip()=="":
            decks.append(np.asarray(deck))
            deck = []
        else:
            deck.append(row.split())

    decks = np.stack(decks,axis=2)
    played_flag = np.zeros(decks.shape)

    return random_numbers,decks,played_flag

def winning_board_score(decks,winning_deck_index,played_numbers):

    winning_board = decks[:,:,winning_deck_index]
    for number in played_numbers:
        winning_board[winning_board==number] =  0
    score =  int(np.sum(winning_board.astype(np.float)))

    return score*int(played_numbers[-1])

def solve_part1(input_list):

    random_numbers,decks,played_flag = read_data(input_list)
    played_numbers = []
    for number in random_numbers:
        played_numbers.append(number)
        played_flag[:,:,:] = np.logical_or(decks == number,played_flag)
        rows_sum_max = list(np.max(np.sum(played_flag,axis=0),axis=0))
        cols_sum_max = list(np.max(np.sum(played_flag,axis=1),axis=0))

        row_found = False
        col_found = False
        if 5 in rows_sum_max:
            row_deck_index = math.ceil(rows_sum_max.index(5)/5)
            row_found = True

        if 5 in cols_sum_max:
            column_deck_index = math.ceil(cols_sum_max.index(5))
            col_found = True

        if row_found and col_found:
             winning_deck_index= min(row_deck_index,column_deck_index)
             break
        elif row_found:
            winning_deck_index = row_deck_index
            break
        elif col_found:
            winning_deck_index = column_deck_index
            break

    return winning_board_score(decks,winning_deck_index,played_numbers)


def solve_part2(input_list):

    random_numbers,decks,played_flag = read_data(input_list)
    played_numbers = []
    for number in random_numbers:
        played_numbers.append(number)
        played_flag[:,:,:] = np.logical_or(decks == number,played_flag)

        rows_sum_max = list(np.max(np.sum(played_flag,axis=0),axis=0))
        cols_sum_max = list(np.max(np.sum(played_flag,axis=1),axis=0))

        deletions=0
        game_over = False
        for idx,val in enumerate(rows_sum_max):
            if val==5:
                if decks.shape[2] > 1:
                    index = idx-deletions
                    decks = np.delete(decks,index,2)
                    played_flag = np.delete(played_flag,index,2)
                    deletions+=1
                    del cols_sum_max[index]
                else:
                    game_over = True
                    break
        if game_over:
            break

        deletions=0
        for idx,val in enumerate(cols_sum_max):
            if val==5:
                if decks.shape[2] > 1:
                    index = idx-deletions
                    decks = np.delete(decks,index,2)
                    played_flag = np.delete(played_flag,index,2)
                    deletions+=1
                else:
                    break
        if game_over:
            break

    return winning_board_score(decks,0,played_numbers)


if __name__ == '__main__':

    print("Day 4 part 1 answer: {}".format(solve_part1(get_input_of_day(4))))
    print("Day 4 part 2 answer: {}".format(solve_part2(get_input_of_day(4))))
