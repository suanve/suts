import suts

# print(suts.md5("huawei no.1"))
# print(suts.urlencode("huawei no.1 !@#%$#6457"))


str1 = "zMXHz#TOqhbWEv(hyw!LFq=="
# string1 = "ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/"
string1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*(+/="
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
print(suts.base_transform("b64",str1,string2,string1))

# print(suts.getip("1.1.1.1-2"))