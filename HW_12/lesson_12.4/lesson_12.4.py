import configparser

config = configparser.ConfigParser()
# config.read('config.ini')
# print(config.sections())
# print(config['mariadb']['name'])
# print(config.get('mariadb', 'name'))

# config = configparser.ConfigParser()
# dict = {
#     "Default": {
#         "host": "localhost"
#     },
#     "mariadb": {
#         "name": "mariadb"
#     },
#     "redis": {
#         "port": 2313
#     }
# }

# config.read_dict(dict)
# print(config['mariadb']['name'])
# print(config.get('mariadb', 'name'))

# config['Default'] = {"host": "localhost"}

# with open('confignew.ini', 'w') as configFile:
#     config.write(configFile)

# config.read('confignew.ini')

# config['Default']['host'] = '1.2.2.3'

# with open('confignew.ini', 'w') as configFile:
#     config.write(configFile)

config.read('config.ini')
print(config.get('redis', 'dns'))
