from os.path import exists


def load():
    if not exists("config.conf"):
        config_file = open("config.conf", 'w+')
        config_file.write("")
        config_file.close()
    config_file = open("config.conf", 'r')
    temp = config_file.readlines()
    config_file.close()
    configuration = {}
    for line in temp:
        splitted = line.replace("\n", "").split("=")
        configuration[splitted[0]] = splitted[1]

    return configuration


def save(configuration):
    config_file = open("config.conf", 'w+')
    for key in configuration.keys():
        config_file.write("%s=%s\n" % (key, configuration.get(key)))
    config_file.close()
