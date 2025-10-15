from vehicle import Vehicle
import random

class Motorcycle(Vehicle):

    def slow(self, obs_loc):
        """
        Vehicle moves at 75%  speed +/- 1. Passes obstacles if there is one in the way.
        Args:
            obs_loc (int): passes in position of obstacle
        return:
            formatted string of event that occurred with vehicle name and amount moved.
        """

        three_fourths_speed = int(self._speed * .75)
        random_speed = random.randint(three_fourths_speed - 1, three_fourths_speed + 1)
        position = self._position
        obs_loc1 = obs_loc[0]

        if self._position + random_speed >= 100:
            self._position = 100
        else:
            self._position += random_speed

        return f"{self._name} slowly moves {random_speed} spaces to {self._position}"

    def special_move(self, obs_loc):
        """
        if energy is above 15, 75% chance to move at double speed. if there is an obstacle in the way, crash.
        if boost fails, move 1 space.
        Args:
            obs_loc (int): the location of the obstacle
        Return:

        """
        if self._energy >= 15:
            self._energy -= 15
            chance = random.randint(0,100)
            random_speed = self._speed * 2 + random.randint(-1,1)

            if chance <= 75:

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
            else:
                self._position += 1

        else:
            self._position += 1