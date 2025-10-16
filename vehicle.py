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
        """
        The vehicle's initial to be used on the track
        Return:
            self._initial (str) : The initial of the vehicle
        """
        return self._initial

    @property
    def position(self):
        """
        The vehicle's position
        Return:
            self._position (int) : The vehicle's position
        """
        return self._position

    @property
    def energy(self):
        """
        The amount of energy the vehicle has
        Return:
            self._energy (int) : the vehicle's energy
        """
        return self._energy

    def fast(self, obs_loc):
        """
        passes in the location of the pair of obstacles. if the car has 5 energy, it can move fast. If the car will pass
        an obstacle crash into it. otherwise move that amount.
        If there was not sufficient energy, move 1 space.
        Sets the position to 100 if the car will finish the race.
        Args:
            obs_loc (list): position where obstruction is
        Return:
            formatted string of event that occurred with vehicle name and amount moved.
        """

        vehicle_speed = random.randint(self._speed - 1, self._speed + 1)
        vehicle_position = self._position

        if self._energy >= 5:

            self._energy -= 5

            if vehicle_position < obs_loc[0] <= vehicle_position + vehicle_speed:
                self._position = obs_loc[0] - 1
                return f"{self._name} has crashed into the obstacle!"

            elif vehicle_position <= obs_loc[1] <= vehicle_position + vehicle_speed:
                self._position = obs_loc[1] - 1
                return f"{self._name} has crashed into the obstacle!"

            elif vehicle_position <= 100 <= vehicle_position + vehicle_speed:
                self._position = 100
                return f"{self._name} has finished the race"
            else:
                self._position += vehicle_speed

        else:
            if self._position < 100:
                self._position += 1
            else:
                self._position = 100

        return f"{self._name} swiftly moves {vehicle_speed} spaces to {self._position}"

    def slow(self, obs_loc):
        """
        Vehicle moves at half speed +/- 1. Uses floor division to get half speed Ignores obstacles if there is one in
        the way.
        Args:
            obs_loc (int): passes in position of obstacle
        Return:
            formatted string of event that occurred with vehicle name and amount moved.
        """

        half_speed = self._speed // 2
        random_speed = random.randint(half_speed - 1, half_speed + 1)
        vehicle_position = self._position

        if self._position + random_speed >= 100:
            self._position = 100
            return f"{self._name} has finished the race"

        elif vehicle_position < obs_loc[0] <= vehicle_position + random_speed:
            self._position += random_speed
            return f"{self._name} has swerved around the obstacle!"

        elif vehicle_position <= obs_loc[1] <= vehicle_position + random_speed:
            self._position += random_speed
            return f"{self._name} has swerved around the obstacle!"
        else:
            self._position += random_speed

        return f"{self._name} slowly moves {random_speed} spaces to {self._position}"


    def __str__(self):
        """
        Description of vehicle with Name [Position - P Energy - E]
        Return:
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



