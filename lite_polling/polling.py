
from collections import namedtuple
from functools import reduce
from numbers import Real
from time import sleep

class SleepConfig(namedtuple('SleepConfig', ['minimum', 'maximum', 'scale_factor'])):
    """Parameters intended for control of the sleep interval during polling

    Args:

      minimum (Real): minimum time (seconds) to sleep after polling

      maximum (Real): maximum time (seconds) to sleep after polling

      scale_factor (Real): increas in the time to sleep after polling
    """
    def __init__(self, *args, **kwds):
        assert isinstance(self.minimum, Real)
        assert self.minimum >= 0

        assert isinstance(self.maximum, Real)
        assert self.maximum >= self.minimum

        assert isinstance(self.scale_factor, Real)
        assert self.scale_factor >= 1

DEFAULT_CONFIG = SleepConfig(
    minimum = 1.0e-6,
    maximum = 1.0e-1,
    scale_factor = 1.5)

class While(object):
    """Polling with increasing sleep duration between polls to reduce CPU overhead.

    Args:
    condition
    """
    def __init__(self, condition, *actions, config = DEFAULT_CONFIG ):

        assert callable(condition)
        assert reduce(lambda x, y: x and y, map(callable, actions), True)

        self.__condition = condition
        self.__actions = actions
        self.__config = config
        self.__done = False

        self.__run()

    def __updateSleepDuration(self, current):
        return min(self.__config.maximum, self.__config.scale_factor*current)

    def __run(self):
        sleep_duration = self.__config.minimum
        test_result = self.__condition()
        while test_result:
            for action in self.__actions:
                action()
            sleep_duration = self.__updateSleepDuration(sleep_duration)
            sleep(sleep_duration)

            test_result = self.__condition()

            assert isinstance(test_result, bool)
