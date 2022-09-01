
def get_cidr(file_name,mask=".1/24"):
    """用于获取ip对应的c段地址"""
    a = open(file_name)
    b  = set()
    for i in a.readlines():
        i = i.strip()
        s = ".".join(i.split('.')[:3])
        b.add(s)

    for i in range(len(b)):
        print(b.pop()+mask)