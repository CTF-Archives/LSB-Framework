# 感谢 cheyenne-八神 对此框架的贡献
from func import get_flag,logger
from func.ProcessData import *

# 在这里定义整体的附件生成流程
# 请注意：请勿在正式题目环境中启用任何debug参数!!!
if __name__ == "__main__":
    FLAG = get_flag(debug=True)
    logger.info("Successful get flag: {flag}".format(flag=FLAG))
    print(byte2bin("test"))