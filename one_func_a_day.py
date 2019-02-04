import random
import datetime
import argparse
from function_dict import get_list

random_num = random.randint(0, 31)
x = datetime.datetime.now()
day = x.strftime("%d")
month = x.strftime("%m")
current_function_list = get_list(int(month))

parser = argparse.ArgumentParser(description="One Function A Day")
parser.add_argument('-r', '--random', action='store_true', help='Show a random function')
args = parser.parse_args()

if __name__ == '__main__':
    #print(month)
    if args.random:
        if int(month) == 1:
            help(current_function_list.func[random_num])
        else:
            help(current_function_list.object_name + "." + current_function_list.func[random_num])
    else:
        if int(month) == 1:
            help(current_function_list.func[int(day)])
        else:
            help(current_function_list.object_name + "." + current_function_list.func[int(day)])