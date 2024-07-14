# Print all permutation of a string
ip = 'abc'
op = ''
def print_permutation_of_string(ip, op):
    if ip == '':
        print(op)
        return
    for index in range(len(ip)):
        new_ip = ip[0:index] + ip[index+1:]
        new_op = op+ip[index]
        print_permutation_of_string(new_ip,new_op)


print_permutation_of_string(ip, op)