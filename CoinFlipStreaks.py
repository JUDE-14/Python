print('Name: Jude Andrew \nUSN: 1AY24AI049 \nSection: M\n ')

import random

def coin_flip_streaks():
    number_of_streaks = 0
    total_simulations = 10000

    for experiment in range(total_simulations):
        flips = []
        for i in range(100):
            if random.randint(0, 1) == 0:
                flips.append('H')
            else:
                flips.append('T')

        streak_count = 1
        for i in range(1, len(flips)):
            if flips[i] == flips[i - 1]:
                streak_count += 1
                if streak_count == 6:
                    number_of_streaks += 1
                    break  
            else:
                streak_count = 1

    print(f'Chance of a streak of 6 in 100 flips: {number_of_streaks / total_simulations * 100:.2f}%')

coin_flip_streaks()
