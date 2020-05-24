from yaml import safe_load


class YamlParser(object):

    def __init__(self, filename):
        file = open(filename, 'r')
        self.loaded = safe_load(file)
        file.close()

    def get(self, key):
        return self.loaded.get(key)
