from vehicle import Vehicle
import random

class Truck(Vehicle):

    def special_move(self, obs_loc):
        """
        spends 15 energy to move at 2x speed. bashes through obstacles. if there isn't enough energy, move 1 space.
        :param obs_loc:
        :return:
        """
        if self._energy >= 15:
            self._energy -= 15
            random_speed = int(self._speed * 2 + random.randint(-1,1))

            if self._position + random_speed >= 100:
                self._position = 100
            else:
                self._position += random_speed

        else:
            self._position += 1