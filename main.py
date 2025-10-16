import check_input
from truck import Truck
from car import Car
from motorcycle import Motorcycle
import random

def winner_list(vehicle_list, win_list):
    """
    Takes in the vehicle list and win_list. If a vehicle's position is greater than or equal to 100 (it finished the race),
    then add it to the win_list
    Args:
        vehicle_list (list) : A list of vehicle objects
        win_list (list) : list of players that have won the race. Also keeps track of who won first, second, and third
    Return:
        win_list (list) : updated win_list
    """
    for i in range(len(vehicle_list)):
        vehicle_position = vehicle_list[i].position
        if vehicle_position >= 100:
            if vehicle_list[i].initial not in win_list:
                win_list.append(vehicle_list[i].initial)

    return win_list

def vehicle_positions(vehicle_list, track, previous_positions):
    """
    For each vehicle in vehicle list, updates the vehicle's position in the track. Places the previous position in a list
    previous_positions.

    Args:
        vehicle_list (list) : list of vehicle objects
        track (list): 2D list 3 lanes, 100 units long
        previous_positions (list) : list that keeps track of the previous position the vehicle was in
    :return:
    """

    for i in range(len(vehicle_list)):

        vehicle_position = vehicle_list[i].position
        track[i][previous_positions[i]] = '*'

        if vehicle_position < 100:
            track[i][vehicle_position] = vehicle_list[i].initial
        elif vehicle_position >= 100:
            track[i][100] = vehicle_list[i].initial
        if vehicle_position <= 100:
            previous_positions[i] = vehicle_position
        else:
            previous_positions[i] = 100

def obstruction_positions(obs_loc, player):
    """
    Takes in list obs_loc and player. Returns a sorted list with the two obstructions generated for that player.
    Args:
        obs_loc (list) : a complete list of obstructions generated for each player
        player (int) :  the player we want the obstructions for
    Return:
        positions (list) : A sorted list of the locations of the two obstructions for the player
    """

    positions = []
    for i in range(2):
        value = obs_loc[player - 1][i]
        positions.append(value)
    positions.sort()
    return positions

def update_npc(npc, vehicle_list):
    """
    updates the npc list. removes npc from the list if they completed the race
    Args:
        npc (list) : list of npc players
        vehicle_list (list) : list of vehicles
    """
    if vehicle_list[0].position >= 100:
        if 1 in npc:
            npc.remove(1)
    elif vehicle_list[1].position >= 100:
        if 2 in npc:
            npc.remove(2)
    elif vehicle_list[2].position >= 100:
        if 3 in npc:
            npc.remove(3)

def npc_actions(npc, vehicle_list, obs_loc):
    """
    For each NonPlayerCharacter generates an action 1 - 100. 40% chance to go slow (choice 2), 30% chance to go fast
    (choice 1), and 30% chance to use special move. Uses function obstruction_position(obs_loc, npc[i]) to get appropriate
    list of obstructions.
    Args:
        npc (list) : list of NonPlayerCharacters
        vehicle_list (list) : full list of vehicles
        obs_loc (list) : full list of obstructions generated
    """

    for i in range(len(npc)):

        random_action = random.randint(1, 100)
        obs_pos = obstruction_positions(obs_loc, npc[i])

        if random_action <= 40:
            npc_choice = 2
            npc_action = choose_action(vehicle_list, npc[i], npc_choice, obs_pos)
            print(npc_action)

        elif random_action <= 70:
            npc_choice = 1
            npc_action = choose_action(vehicle_list, npc[i], npc_choice, obs_pos)
            print(npc_action)

        else:
            npc_choice = 3
            npc_action = choose_action(vehicle_list, npc[i], npc_choice, obs_pos)
            print(npc_action)



    # return npc_action

def print_track(track):
    """
    prints the track.
    Args:
        track (list) : list containing the track

    """
    for i in range(len(track)):
        for j in range(len(track[i])):
            print(track[i][j], end=' ')
        print()

def print_vehicles(vehicle_list):
    """
    prints list of vehicles in the game
    Args:
        vehicle_list (list) : List of vehicles competing in the game
    """

    for i in range(len(vehicle_list)):
        print(vehicle_list[i])

def choose_action(vehicle_list, player_car, choice, obstacle_position):
    """
    Takes in a player's car and the position's of it's obstacles. If choice is 1. car goes fast, 2. car goes slow. and
    3. performs a special move.
    Args:
        vehicle_list (list) : full list of vehicles
        player_car (int) : num 1 through 3. subtracts 1 because list starts at 0.
        choice (int) : num 1 through 3. selects an action to perform
        obstacle_position (list) : list of obstacle positions for the player_car
    Return:
        car_action (str) : formatted string of the car's action
    """

    if choice == 1:
        car_action = vehicle_list[player_car - 1].fast(obstacle_position)
    elif choice == 2:
        car_action = vehicle_list[player_car - 1].slow(obstacle_position)
    else:
        car_action = vehicle_list[player_car - 1].special_move(obstacle_position)

    return car_action


def main():
    rows = 3
    col = 101
    npc = [1, 2, 3]
    previous_positions = [0,0,0]

    track = [['-' for i in range(col)] for j in range(rows)]

    # initializes obstruction list. 2 obstructions per track
    obs_loc = [
        [0, 0],
        [0, 0],
        [0, 0]
         ]

    # creates obstacles makes sure they aren't at the start or finish
    for i in range(len(track)):
        for n in range(2):
            obstacle = random.randint(1, 99)
            track[i][obstacle] = 0
            obs_loc[i][n] = obstacle


    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash! \n"
          "1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed) \n"
          "2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out). \n"
          "3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")

    # finds npc
    player_car = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)
    npc.remove(player_car)

    # initializes vehicle list depending on player choice
    if player_car == 1:
        vehicle_list = [Car("Lightning Car", "P", 10), Motorcycle("Swift Bike", "M", 10),
                        Truck("Behemoth Truck", "T", 10)]
    elif player_car == 2:
        vehicle_list = [Car("Lightning Car", "C", 10), Motorcycle("Swift Bike", "P", 10),
                        Truck("Behemoth Truck", "T", 10)]
    else:
        vehicle_list = [Car("Lightning Car", "C", 10), Motorcycle("Swift Bike", "M", 10),
                        Truck("Behemoth Truck", "P", 10)]

    # list of players that completed the track
    win_list = []

    while len(win_list) < 3:
        # prints vehicles
        print_vehicles(vehicle_list)
        vehicle_positions(vehicle_list, track, previous_positions)

        # prints track
        print_track(track)

        if vehicle_list[player_car - 1].position < 100:

            #player character
            player_choice = check_input.get_int_range("Choose Action (1. Fast, 2. Slow, 3. Special Move) : ", 1, 3)
            obs_pos = obstruction_positions(obs_loc, player_car)
            action = choose_action(vehicle_list, player_car, player_choice, obs_pos)
            print()
            print(action)

        npc_actions(npc, vehicle_list, obs_loc)
        print()
        update_npc(npc, vehicle_list)

        win_list = winner_list(vehicle_list, win_list)



    for i in range(len(win_list)):
        for j in range(len(vehicle_list)):
            if vehicle_list[j].initial == win_list[i]:
                if i == 0:
                    print(f"1st Place is {vehicle_list[j]}")
                if i == 1:
                    print(f"2nd Place is {vehicle_list[j]}")
                if i == 2:
                    print(f"3rd Place is {vehicle_list[j]}")



if __name__ == "__main__":
    main()

# 1 C
# 2 Hoeffding's is only tighter than chernoff if n > 92
# 3 1/2
# 4