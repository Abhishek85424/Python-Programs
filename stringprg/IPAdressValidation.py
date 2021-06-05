import re

total_ip = int(input())


def validateIpV4(IP):
    # print(IP)
    try:
        return 0 <= int(IP) <= 255
    except:
        return False


def validateIpV6(IP):
    # print('IPV6')
    if re.match("\W", IP):
        return False
    try:
        int(IP, 16)
        return True
    except:
        return False


for index in range(total_ip):
    current_ip = input()
    if current_ip.find('.') >= 0 and len(current_ip.split('.')) == 4 and all(
            validateIpV4(item) for item in current_ip.split('.')):
        print('IPv4')
    elif current_ip.find(':') >= 0 and len(current_ip.split(':')) == 8 and all(
            validateIpV6(item) for item in current_ip.split(':')):
        print('IPv6')
    else:
        print('Neither')