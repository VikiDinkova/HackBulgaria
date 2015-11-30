import time
import json

time_ = time.strftime("%d.%m.%Y")


def parse_command(command):

    return tuple(command.split(" "))


def is_command(command_tuple, command_string):

    return command_tuple[0] == command_string


def read_json():
    with open('calories.json', 'r') as f:
        data = json.load(f)

    return data


def write_calories(new_dict):
    data = read_json()
    data.update(new_dict)

    with open('calories.json', 'w') as f:
        json.dump(data, f)
    return new_dict


def meal(meal, calories):
    # filename = 'food_panda.txt'
    # data = open(filename, 'a')
    filename_cal = 'calories.json'
    data_cal = open(filename_cal, 'r')
    read_cal = json.load(data_cal)
    if meal not in read_cal:
        with open('calories.json', 'w') as data:
            json.dump(read_cal, data)
        read_cal[meal] = calories
        return calories
    else:
        return read_cal[meal]

    # data.write(time_ + ' ' + meal + '\n')
    # data.close()

    return 'Ok it is saved'


def list_(eat_time):
    filename = 'food_panda.txt'
    data = open(filename, 'r')
    contain = data.read()
    contain = contain.split('\n')
    ate = []

    for line in contain:
        line.split(' ')
        if eat_time in line:
            ate.append(line[10:])
        else:
            continue

    return ''.join(ate)


def main():
    print('Hello and Welcome!')
    print('Choose an option.')
    print('1. meal - to write what are you eating now.')
    print('2. list <dd.mm.yyyy> - lists all the meals that you ate that day,')

    command = input('Enter command>')
    command = parse_command(command)
    command_cal = input('How much have you eaten?>')
    command_cal = parse_command(command_cal)

    if is_command(command, 'meal'):

        return(meal(command[1]), command_cal[0])

    elif is_command(command, 'list'):

        return(list_(command[1]))


if __name__ == '__main__':
    print(main())
