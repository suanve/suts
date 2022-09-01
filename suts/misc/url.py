import urllib.parse


def urlencode(s,flag=1):
    """
    :param str:
    需要转义的字符串
    :param flag:
1 自动转义%0A为%0D%0A
    :return:
    """
    tmp = urllib.parse.quote(s)
    if flag:
        result = tmp.replace('%0A', '%0D%0A')
    return result