from vehicle import Vehicle
import random

class Car(Vehicle):

    def special_move(self, obs_loc):
        random_speed = int(self._speed * 1.5 + random.randint(-1, 1))
        if self._energy >= 15:

            if self._position + random_speed > obs_loc[0] > self._position:
                self._position = obs_loc[0] - 1
                return f"{self._name} has crashed!"
            elif self._position + random_speed > obs_loc[1] > self._position:
                self._position = obs_loc[1] - 1
                return f"{self._name} has crashed!"
            elif self._position + random_speed >= 100 >= self._position:
                self._position = 100
                return f"{self._name} has finished the race"
            else:
                self._position += random_speed
                return f"{self._name} boosts {random_speed} space to {self._position}"
        else:
            self._position += 1
            return f"{self._name} has failed to boost and moves 1 space to {self._position}"


