'''
Created on 09-Sep-2021

@author: prashantkumar
'''
import configparser

config = configparser.RawConfigParser()
config.read("configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getConfigValue(configKey):
        return config.get('common info', configKey)
