import sys
import logging
from lib.log import *
def main(system,page,function):
    logging.basicConfig(filename='result.log', level=logging.INFO)
    # logger = logging.getLogger("auto_api_test")
    # logger.setLevel(logging.DEBUG)
    # # 建立一个filehandler来把日志记录在文件里，级别为debug以上
    # fh = logging.FileHandler("result/spam.log")
    # fh.setLevel(logging.INFO)
    # # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.ERROR)
    # # 设置日志格式
    # formatter = logging.Formatter("[%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(message)s]")
    # ch.setFormatter(formatter)
    # fh.setFormatter(formatter)
    # #将相应的handler添加在logger对象中
    # logger.addHandler(ch)
    # logger.addHandler(fh)
    logging.info('进入系统')
    printlog()
    
if __name__=='__main__':



    if (len(sys.argv) == 4) :
        system = sys.argv[1]
        page = sys.argv[2]
        function = sys.argv[3]
        main(system,page,function)
    elif (len(sys.argv) == 1):
        main("all","all","all")
    else:
        logger.error("请输入正确的参数\n")