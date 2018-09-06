# code:utf-8
def int2ip(int_value):
    s1 = int_value >> 24 & 0xff
    s2 = int_value >> 16 & 0xff
    s3 = int_value >> 8 & 0xff
    s4 = int_value & 0xff
    return '.'.join([str(s1), str(s2), str(s3), str(s4)])


def ip2int(ip):
    vals = ip.split('.')
    result = 0
    result |= int(vals[0]) << 24
    result |= int(vals[1]) << 16
    result |= int(vals[2]) << 8
    result |= int(vals[3])
    return result


print(int2ip(ip2int('192.168.71.69')))
print(0xff)
