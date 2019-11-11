# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 用于加密和解密的 base62 字符串
wl_key = 'OZpjoyVihJbBAfnEcWa82s4GwqHKuxe7SDm0tXk1639RITFQPdlrLYCvUMzN5g'
wl_num = 1987032511

api_key = 'YCvUMOnEcX82slrLzNRIpjoyBAfWaSDmuxe7Z0tTFQk16VihJb4GwqHK5g39Pd'
api_num = 32212254719


# base62加密函数
def wlencode(num, addcrc=None):
    try:
        num = wl_num * long(num) + 1
        ret = ''
        crc = wl_key[long(str(num)[-1]) * 6]
        while num != 0:
            ret = (wl_key[num % 62]) + ret
            num = long(num / 62)
        if addcrc:
            # 在末尾添加一位随机字符
            ret += crc
        return ret
    except Exception:
        return num

# base62解密函数
def wldecode(st, addcrc=None):
    if isinstance(st, basestring):
        ret, mult = 0, 1
        if addcrc:
            # 去掉最末一位的随机字符
            st = st[:-1]
        for c in reversed(st):
            ret += mult * wl_key.index(c)
            mult *= 62
        if (ret - 1) % wl_num == 0:
            return long((ret - 1) / wl_num)
    return ""


# base62加密函数  对外api使用
def apiencode(num, addcrc=None):
    try:
        num = api_num * long(num) + 1
        ret = ''
        crc = api_key[long(str(num)[-1]) * 6]
        while num != 0:
            ret = (api_key[num % 62]) + ret
            num = long(num / 62)
        if addcrc:
            # 在末尾添加一位随机字符
            ret += crc
        return ret
    except Exception:
        return num


# base62解密函数 对外api使用
def apidecode(st, addcrc=None):
    if isinstance(st, basestring):
        ret, mult = 0, 1
        if addcrc:
            # 去掉最末一位的随机字符
            st = st[:-1]
        for c in reversed(st):
            ret += mult * api_key.index(c)
            mult *= 62
        if (ret - 1) % api_num == 0:
            return long((ret - 1) / api_num)
    return ""
