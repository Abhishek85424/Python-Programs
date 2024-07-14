import sys
import os


def search_file():

    file_name = sys.argv[1]
    text = sys.argv[2]
    print(sys.argv[1])
    print(sys.argv[2])
    with open(os.getcwd()+"/file/"+file_name, 'r') as read_obj:
        line = read_obj.readline()
        while line:
            if text in line:
                print(line)
            line = read_obj.readline()


search_file()
