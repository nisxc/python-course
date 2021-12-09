import random
import logging

FORMAT = '%(levelname)s %(message)s'


class BatterySimulator:
    def __init__(self, logger) -> None:
        self.__logger = logger

    def simulate_last_hr(self):
        for minute in range(1, 60 + 1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.__logger.debug('{0} C'.format(temperature))
            elif temperature > 30 and temperature <= 35:
                self.__logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.__logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('battery-handler.log', mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

simulation = BatterySimulator(logger)
simulation.simulate_last_hr()
