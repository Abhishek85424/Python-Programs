# # n =8
# # def sumall(n):
# #     if n ==1:
# #         return 1
# #     return n+sumall(n-1)
# # print(sumall(n))
# #
# #
#
# # def mygenerator(x):
# #     while x<5:
# #         yield x
# #         x += 1
# #
# # gen = mygenerator(1)
# # for item in gen:
# #     print(item)
# # from polling import poll
# # poll(lambda : print('hello'),step=1,timeout=5)
# lst = [0,1,-1,-2,2,3]
# # lst = [0,-1,-1,-2,2,3]
# # lst.reverse()
# print(lst)
# start = 0
# current_item = start+2
# # print(len(lst)-2)
# while start < len(lst)-2:
#     if lst[start]+lst[start+1]+lst[current_item] == 0:
#         print((lst[start],lst[start+1],lst[current_item]),lst[start]+lst[start+1]+lst[current_item])
#     current_item += 1
#     if current_item == len(lst):
#         current_item = 0
#         start += 1
#

def sumofdigit(n):
    if n == 0:
        return 0
    rem = n % 10
    n = n //10
    return rem + sumofdigit(n)


def sod(number: int) -> int:
    print(number,'Hi')
    return sumofdigit(number)


if __name__ == '__main__':
    print(sod(123456789))