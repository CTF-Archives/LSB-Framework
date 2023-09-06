from func import logger

def byte2bin(data: str | int) -> str:
    """将 str|int 转换为二进制(字符串)

    Args:
        data (str | int): 需要转换的数据

    Returns:
        str: 二进制数据(去掉了"0b"头)
    """
    match str(type(data)):
        case "<class 'str'>":
            data_bin = " ".join(str(bin(ord(x)))[2:].zfill(8) for x in data)
            return data_bin
        case "<class 'int'>":
            data_bin = str(bin(data))[2:].zfill(8)
            return data_bin
        case _:
            logger.error("未被支持的输入变量类型: {}".format(type(data)))


def file2bin(filepath: str) -> str:
    """将文件转换为二进制(字符串)

    Args:
        filepath (str): 文件的绝对路径

    Returns:
        str: 二进制数据(去掉了"0b"头)
    """
    try:
        with open(filepath, "rb") as f:
            data = f.read()
    except:
        logger.error("{} 文件读取失败".format(filepath))