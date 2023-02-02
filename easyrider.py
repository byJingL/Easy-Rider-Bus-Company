# Write your code here
import json
import re
from collections import Counter
from datetime import datetime

STOP_TYPE = ['', 'O', 'S', 'F']


def is_int(to_check):
    """Return True if the given object is an integer."""
    if isinstance(to_check, int):
        return True
    return False


def is_time(to_check):
    """Return True if the given time conform to the format 'HH:MM (24 hours date format)'."""
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
    """Return True if given name conform to the format of '[proper name][suffix]'."""
    if isinstance(to_check, str):
        # Must add '\Z', the end of the string
        template = r"([A-Z]\w* )+(Avenue|Boulevard|Street|Road)\Z"
        if re.match(template, to_check):
            return True
    return False


def error_detect(data):
    """
    Return a dictionary of the count of errors of each field.

    :param data: data with JSON format to check
    :return: dict = {
        field1: count1,
        field2: count2,
        ...,
    }
    """
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
    """
    Return a dictionary of the count of format errors for stop name, stop type and time.

    :param data: data with JSON format to check
    :return: dict = {
        "stop_name": count1,
        "stop_type": count2,
        "a_time": count3,
    }
    """
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
    """
    Return a dictionary of the all bus lines and the number of stops on each line.

    :param data: data with JSON format to check
    :return: dict = {
        line1: count1
        line2: count2
        ...
    }
    """
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
    """
    Return a dictionary of the all bus lines and start, finsh and other stops on each line.

    :param data:
    :return: dict = {
        line1: {
            'Start': [stop name1],
            'Finish': [stop name2],
            'Other': [stop name3, ...],
        }
        ...
    }
    """
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
    """
    Return start_stops, transfer_stops and finish_stops on all bus lines.

    :param stops: dictionary of all bus lines and start, finsh and other stops on each line
    :return: tuple = (
        start_stops set = {stop name1, ...},
        transfer_stops = [stop name2, ...],
        finish_stops set = {stop name3, ...},
    )
    """

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


def get_times(data):
    """
    Return a dictionary of the all bus lines and tuple of arrive times and stop on each line.

    :param data:
    :return:
    """
    times = {}
    for bus in data:
        line = bus["bus_id"]
        if line in times:
            times[line].append((bus["a_time"], bus["stop_name"]))
        else:
            times[line] = [(bus["a_time"], bus["stop_name"])]

    return times


def check_times(times_of_lines):
    """
    Return a list of error info on each bus line.

    :param times_of_lines: dictionary of the all bus lines and tuple of arrive times and stop on each line
    :return: list = [
        (line1, stop name1),
        (line2, stop name2)
        ...
    ]
    """
    incorrect = []

    for line in times_of_lines:
        prev = datetime.strptime('00:00', '%M:%S')
        for (time, name) in times_of_lines[line]:
            if datetime.strptime(time, '%M:%S') > prev:
                prev = datetime.strptime(time, '%M:%S')
            else:
                incorrect.append((line, name))
                break

    return incorrect


def main():
    data = json.loads(input())

    error_dict = error_detect(data)
    format_error = format_error_detect(data)
    bus_lines = lines_check(data)
    stops = get_stops(data)
    separated_stops = separate_stops(stops)

    times = get_times(data)
    incorrect_times = check_times(times)

    print('Arrival time test:')
    if len(incorrect_times) == 0:
        print('OK')
    else:
        for (line, name) in incorrect_times:
            print(f"bus_id line {line}: wrong time on station {name}")


if __name__ == '__main__':
    main()



