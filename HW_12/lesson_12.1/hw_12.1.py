import xml.etree.cElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celsius):
        return 9 / 5 * celsius + 32


class ForecastXMLParser:
    def __init__(self, converter):
        self.__converter = converter

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temp_celsius = int(child.find('temperature_in_celsius').text)
            fahrenheit = round(
                self.__converter.convert_celsius_to_fahrenheit(temp_celsius), 1)
            print('{0}: {1} Celsius {2} Fahrenheit'.format(
                day, temp_celsius, fahrenheit))


forecast_convert = TemperatureConverter()
forecst_parser = ForecastXMLParser(forecast_convert)
forecst_parser.parse('forecast.xml')
