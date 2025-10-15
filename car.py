from vehicle import Vehicle
import random

class Car(Vehicle):

    def special_move(self, obs_loc):
        """
        The car spends 15 energy to use a special move. If the car has enough energy it moves 1.5x +/- 1 unit of its
        speed. If there is an obstruction in the way, it crashes. If it passes 100, it finishes the race. If it does not
        have enough energy, it moves 1 space forward
        Args:
            obs_loc (list): list of obstructions in the way
        Return:
             formatted string of the action
        """
        random_speed = int(self._speed * 1.5 + random.randint(-1, 1))

        if self._energy >= 15:
            self._energy -= 15

            if self._position + random_speed > obs_loc[0] > self._position:
                self._position = obs_loc[0] - 1
                return f"{self._name} has crashed into the obstacle!"

            elif self._position + random_speed > obs_loc[1] > self._position:
                self._position = obs_loc[1] - 1
                return f"{self._name} has crashed into the obstacle!"

            elif self._position + random_speed >= 100 >= self._position:
                self._position = 100
                return f"{self._name} has finished the race"

            else:
                self._position += random_speed
                return f"{self._name} boosts {random_speed} space to {self._position}"

        else:
            if self._position < 100:
                self._position += 1
                return f"{self._name} has failed to boost and moves 1 space to {self._position}"
            else:
                self._position = 100
                return f"{self._name} has finished the race"

