import abc
import random

class Vehicle(abc.ABC):
    """
    A general vehicle class with abstract method

    Attributes:
        _name (str): the name of the vehicle
        _initial (str): the vehicle's label
        _speed (int): the vehicle's speed
        _position (int): the vehicle's position
        _energy (int): the amount of energy the vehicle has

    Parameters:
        <<get>> _initial: str
        <<get>> _position: int
        <<get>> _energy: int
    """

    def __init__(self, name, initial, speed):
        """
        Initialize the name, speed, initial, position and energy
        Args:
            name: the name of the vehicle
            initial: the label of the vehicle
            speed: the speed of the vehicle
        """
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100

    @property
    def initial(self):
        return self._initial

    @property
    def position(self):
        return self._position

    @property
    def energy(self):
        return self._energy

    def fast(self, obs_loc):
        """
        passes in the location of the next obstacle. If there is sufficient energy, +/- 1 speed for the spaces they will move.
        if the amount moved is less than distance to obstacle then move that amount.
        otherwise, crash and land on the obstacle space.
        If there was not sufficient energy, move 1 space.
        Args:
            obs_loc (list): position where obstruction is
        returns:
            formatted string of event that occurred with vehicle name and amount moved.
        """

        vehicle_speed = random.randint(self._speed - 1, self._speed + 1)
        vehicle_position = self._position

        if self._energy >= 5:

            self._energy -= 5

            if vehicle_position < obs_loc[0] <= vehicle_position + vehicle_speed:
                self._position = obs_loc[0] - 1
                return f"{self._name} has crashed!"
            elif vehicle_position <= obs_loc[1] <= vehicle_position + vehicle_speed:
                self._position = obs_loc[1] - 1
                return f"{self._name} has crashed!"
            elif vehicle_position <= 100 <= vehicle_position + vehicle_speed:
                self._position = 100
                return f"{self._name} has finished the race"
            else:
                self._position += vehicle_speed

        else:
            self._position += 1

        return f"{self._name} swiftly moves {vehicle_speed} spaces to {self._position}"

    def slow(self, obs_loc):
        """
        Vehicle moves at half speed +/- 1. Passes obstacles if there is one in the way.
        Args:
            obs_loc (int): passes in position of obstacle
        return:
            formatted string of event that occurred with vehicle name and amount moved.
        """

        half_speed = self._speed // 2
        random_speed = random.randint(half_speed - 1, half_speed + 1)
        position = self._position

        if self._position + random_speed >= 100:
            self._position = 100
        else:
            self._position += random_speed

        return f"{self._name} slowly moves {random_speed} spaces to {self._position}"


    def __str__(self):
        """
        Description of vehicle
        return:
            formatted string of the vehicle
        """

        return f"{self._name} [Position - {self._position} Energy- {self._energy}]"

    @abc.abstractmethod
    def special_move(self, obs_loc):
        """
        abstract method to make sure classes that inherit class Vehicle has one
        Args:
            obs_loc (int): location of obstruction

        """

        pass



