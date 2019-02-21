import time
import logging
'''
logging.basicConfig(filename='basicsloggers.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
'''
logging.basicConfig(filename='basicsloggers.log', filemode='a', format=' %(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
logging.warning('This will get logged to a file')