# Write your code here
import json
import re
from collections import Counter

STOP_TYPE = ['', 'O', 'S', 'F']


def is_int(to_check):
    if isinstance(to_check, int):
        return True
    return False


def is_time(to_check):
    if isinstance(to_check, str):
        temp = to_check.split(':')
        if len(temp) == 2:
            h = temp[0]
            m = temp[1]
            if 0 <= int(h) < 24 and 0 <= int(m) < 60:
                if int(h) > 9:
                    return True
                else:
                    regexp = r'0\d'
                    if re.match(regexp, h):
                        return True
    return False


def is_name(to_check):
    if isinstance(to_check, str):
        # Must add '\Z', the end of the string
        template = r"([A-Z]\w* )+(Avenue|Boulevard|Street|Road)\Z"
        if re.match(template, to_check):
            return True
    return False


def error_detect(data):
    all_dict = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0,
    }

    for bus in data:
        if not is_int(bus["bus_id"]):
            all_dict["bus_id"] += 1

        if not is_int(bus["stop_id"]):
            all_dict["stop_id"] += 1

        if not is_name(bus["stop_name"]):
            all_dict["stop_name"] += 1

        if not is_int(bus["next_stop"]):
            all_dict["next_stop"] += 1

        if bus["stop_type"] not in STOP_TYPE:
            all_dict["stop_type"] += 1

        if not is_time(bus["a_time"]):
            all_dict["a_time"] += 1

    return all_dict


def format_error_detect(data):
    format_dict = {
        "stop_name": 0,
        "stop_type": 0,
        "a_time": 0,
    }
    for bus in data:
        if not is_name(bus["stop_name"]):
            format_dict["stop_name"] += 1

        if bus["stop_type"] not in STOP_TYPE:
            format_dict["stop_type"] += 1

        if not is_time(bus["a_time"]):
            format_dict["a_time"] += 1

    return format_dict


def lines_check(data):
    lines = {}
    for bus in data:
        if not is_int(bus["bus_id"]):
            continue
        else:
            if bus["bus_id"] in lines:
                lines[bus["bus_id"]] += 1
            else:
                lines[bus["bus_id"]] = 1
    return lines


def get_stops(data):
    stops = {}

    for bus in data:
        line = bus["bus_id"]
        if line in stops:
            continue
        else:
            stops[line] = {
                'Start': [],
                'Finish': [],
                'Other': [],
            }

    for bus in data:
        line = bus["bus_id"]
        if bus["stop_type"] == 'S':
            stops[line]['Start'].append(bus["stop_name"])

        if bus["stop_type"] == 'F':
            stops[line]['Finish'].append(bus["stop_name"])

        if bus["stop_type"] == 'O' or bus["stop_type"] == '':
            stops[line]['Other'].append(bus["stop_name"])

    return stops


def separate_stops(stops):
    start_stops = set()
    finish_stops = set()
    all_stops = []

    for line in stops:
        start = stops[line]['Start']
        finish = stops[line]['Finish']
        other = stops[line]['Other']
        if not (len(start) == 1 and len(finish) == 1):
            print(f'There is no start or end stop for the line: {line}.')
            quit()
        else:
            start_stops.update(start)
            finish_stops.update(finish)
            all_stops.extend(start)
            all_stops.extend(finish)
            all_stops.extend(other)

    stop_counter = Counter(all_stops)
    transfer_stops = []
    for key in stop_counter:
        if stop_counter[key] > 1:
            transfer_stops.append(key)

    return start_stops, transfer_stops, finish_stops


def main():
    data = json.loads(input())

    error_dict = error_detect(data)
    format_error = format_error_detect(data)
    bus_lines = lines_check(data)
    stops = get_stops(data)

    # print(stops)
    separated_stops = separate_stops(stops)

    print(f'Start stops: {len(separated_stops[0])} {sorted(list(separated_stops[0]))}')
    print(f'Transfer stops: {len(separated_stops[1])} {sorted(separated_stops[1])}')
    print(f'Finish stops: {len(separated_stops[2])} {sorted(list(separated_stops[2]))}')

if __name__ == '__main__':
    main()



