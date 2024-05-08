import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get("common info","baseURL")
        return url

    @staticmethod
    def getUsername():
        username=config.get("common info","username")
        return username

    @staticmethod
    def getPassword():
        password=config.get("common info","password")
        return password
