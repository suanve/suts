import itertools

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

def getip(args):
    """
    输入1.1.1.1-1 获取对应的ip段
    :param args:
    输入1.1.1.1-1 获取对应的ip段
    :return:
    """
    gets = lambda x: ["%d.%d.%d.%d" % d for d in itertools.product(

        *[range(m, n + 1) for s in x.split(".") for m, n, *_ in [map(int, (s + "-" + s).split("-"))]])]
    return gets(args)