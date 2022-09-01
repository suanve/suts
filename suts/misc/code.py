import hashlib
import base64
import string

def md5(s):
    """返回md5"""
    hl = hashlib.md5()
    hl.update(s.encode(encoding='utf-8'))
    return hl.hexdigest()


def base_transform(t,s,old,new):
    """
    Base全家通换表
    :param t:
    换表类型
    :param s:
    需要解码的字符串
    :param old:
    原码表
    :param new:
    新码表
    :return:
    """
    str1 = "x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q"

    string1 = "ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/"
    string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    types = {
        "b64": base64.b64decode,
        "b32": base64.b32decode,
        "b16": base64.b16decode,
    }
    return types[t](s.translate(str.maketrans(new,old)))