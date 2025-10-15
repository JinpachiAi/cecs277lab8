import check_input
from truck import Truck
from car import Car
from motorcycle import Motorcycle
import random

def vehicle_positions(vehicle_list, track, previous_positions):

    for i in range(len(vehicle_list)):
        vehicle_position = vehicle_list[i].position
        track[i][previous_positions[i]] = '*'
        if vehicle_position < 100:
            track[i][vehicle_position] = vehicle_list[i].initial
        elif vehicle_position >= 100:
            track[i][100] = vehicle_list[i].initial
        if vehicle_position <= 100:
            previous_positions[i] = vehicle_position

def obstruction_positions(obs_loc, player):

    positions = []
    for i in range(2):
        value = obs_loc[player - 1][i]
        positions.append(value)
    positions.sort()
    return positions

def npc_actions(npc, vehicle_list, obs_loc):

    for i in range(len(npc)):

        random_action = random.randint(1, 100)
        obs_pos = obstruction_positions(obs_loc, npc[i])

        if random_action <= 40:
            npc_choice = 2
            npc_action = choose_action(vehicle_list, npc[i], npc_choice, obs_pos)

        elif random_action <= 70:
            npc_choice = 1
            npc_action = choose_action(vehicle_list, npc[i], npc_choice, obs_pos)

        else:
            npc_choice = 3
            npc_action = choose_action(vehicle_list, npc[i], npc_choice, obs_pos)


    return npc_action

def print_track(track):

    for i in range(len(track)):
        for j in range(len(track[i])):
            print(track[i][j], end=' ')
        print()

def print_vehicles(vehicle_list):

    for i in range(len(vehicle_list)):
        print(vehicle_list[i])

def choose_action(vehicle_list, player_car, choice, obstacle_position):

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
    obs_loc = [
        [0, 0],
        [0, 0],
        [0, 0]
         ]

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
    player_car = check_input.get_int_range("Choose your vehicle (1-3) ", 1, 3)
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

    while(True):
        print_vehicles(vehicle_list)
        vehicle_positions(vehicle_list, track, previous_positions)
        print_track(track)
        player_choice = check_input.get_int_range("Choose Action (1. Fast, 2. Slow, 3. Special Move) : ", 1, 3)
        obs_pos = []
        obs_pos = obstruction_positions(obs_loc, player_car)
        action = choose_action(vehicle_list, player_car, player_choice, obs_pos)
        print(action)

        npc_action = npc_actions(npc, vehicle_list, obs_loc)
        print(npc_action)
        print(obs_pos)



if __name__ == "__main__":
    main()