from vehicle import Vehicle
import random

class Truck(Vehicle):

    def special_move(self, obs_loc):
        """
        spends 15 energy to move at 2x speed. bashes through obstacles. if there isn't enough energy, move 1 space.
        Args:
            obs_loc (list) : list of obstacles in the lane
        Return:
            formatted string of action performed
        """
        if self._energy >= 15:
            self._energy -= 15
            random_speed = int(self._speed * 2 + random.randint(-1,1))
            vehicle_position = self._position


            if self._position + random_speed >= 100:
                self._position = 100
                return f"{self._name} has finished the race"
            elif vehicle_position < obs_loc[0] <= vehicle_position + random_speed:
                self._position += random_speed
                return f"{self._name} has bashed through the obstacle to {self._position}!"

            elif vehicle_position <= obs_loc[1] <= vehicle_position + random_speed:
                self._position += random_speed
                return f"{self._name} has bashed through the obstacle to {self._position}!"
            else:
                self._position += random_speed
                return f"{self._name} rams forward {random_speed} spaces to {self._position}"


        else:
            self._position += 1
            return f"{self._name} has failed to boost and moves 1 space to {self._position}"
