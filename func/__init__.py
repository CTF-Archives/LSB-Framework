import logging
import time
import os

logging.Formatter.converter = time.gmtime
logFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

BANNER = """
    ___  _____  ___      _            _     _                            
   / __\/__   \/ __\    /_\  _ __ ___| |__ (_)_   _____  ___             
  / /     / /\/ _\____ //_\\| '__/ __| '_ \| \ \ / / _ \/ __|            
 / /___  / / / /|_____/  _  \ | | (__| | | | |\ V /  __/\__ \            
 \____/  \/  \/       \_/ \_/_|  \___|_| |_|_| \_/ \___||___/            
                                                                         
   __  __    ___     ___                                            _    
  / / / _\  / __\   / __\ __ __ _ _ __ ___   _____      _____  _ __| | __
 / /  \ \  /__\//  / _\| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
/ /____\ \/ \/  \ / /  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
\____/\__/\_____/ \/   |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
                                                                         

                    Author:          Randark
                    Special thanks:  cheyenne
"""

print(BANNER)

def get_flag(debug: bool = False) -> str:
    """获取环境中的flag数据

    Returns:
        str: flag数据
    """
    with open("/flag", "r") as f:
        flag = f.read()
    if not debug:
        try:
            os.remove("/flag")
            logger.info("/flag 删除成功")
        except FileNotFoundError:
            logger.error("/flag 不存在")
        except PermissionError:
            logger.error("无权限删除 /flag")
        except OSError as e:
            logger.error(f"/flag 删除失败: {e}")
        else:
            logger.critical("/flag 文件处理失败")
    return flag