import logging

def logout():
    print (0)

def printlog():
# 开始打日志
    logging.debug("debug message")
    logging.info("info message")
    logging.warn("warn message")
    logging.error("error message")
    logging.critical("critical message")

if __name__=='__main__':
    logout()