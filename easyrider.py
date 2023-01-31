# Write your code here
import json
import re

SUFFIX = ["Avenue", "Boulevard", "Street", "Road"]
STOP_TYPE = ['', 'O', 'S', 'F']


def is_int(to_check):
    if isinstance(to_check, int):
        return True
    return False


def is_time(to_check):
    if isinstance(to_check, str):
        temp = to_check.split(':')
        if len(temp) != 2:
            return False
        else:
            h = temp[0]
            m = temp[1]
            if 0 <= int(h) < 24 and 0 <= int(m) < 60:
                return True
    return False


def is_name(to_check):
    if isinstance(to_check, str):
        temp = to_check.split(' ')
        if len(temp) < 2:
            return False
        else:
            regexp = r'[A-Z][a-z]*'
            suffix = temp[-1]
            if suffix not in SUFFIX:
                return False
            else:
                for name in temp[:-1]:
                    if not re.match(regexp, name):
                        return False
                return True
    return False


def main():
    error_dict = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0,
    }

    data = json.loads(input())
    for bus in data:

        if not is_int(bus["bus_id"]):
            error_dict["bus_id"] += 1
        if not is_int(bus["stop_id"]):
            error_dict["stop_id"] += 1
        if not is_name(bus["stop_name"]):
            print(bus["stop_name"])
            error_dict["stop_name"] += 1
        if not is_int(bus["next_stop"]):
            error_dict["next_stop"] += 1
        if bus["stop_type"] not in STOP_TYPE:
            error_dict["stop_type"] += 1
        if not is_time(bus["a_time"]):
            error_dict["a_time"] += 1

    all_error = 0
    for key in error_dict:
        all_error += error_dict[key]

    print(f'Type and required field validation: {all_error} errors')
    for key in error_dict:
        print(f'{key}: {error_dict[key]}')


if __name__ == '__main__':
    main()



