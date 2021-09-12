'''
Created on 10-Sep-2021

@author: prashantkumar
'''
import logging

class LogGen:
    
    @staticmethod
    def loggen():
        logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', 
                    filename = "logs/automation.log")
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger