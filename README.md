# Easy Rider Bus Company
Find all the mistakes in the database for a bus company based on the documentation.

Supported Checking: required data, data format, all bus line information, all stops information, all arrive times, on-demand stops

## Main Skill
re module, time module, JSON file, different data structures: set, dictionary, list, tuple
## Theory
- Checking missing required data
- Ckecking incorrect data format for bus stop name, bus stop type and bus arrive time
- Checking the number of stops for each bus line
- Checking all start stops, transfer stops and finish stops
- Checking all arrive times 
- Checking on-demand stops
## Example Output
```
Type and required field validation: 8 errors
bus_id: 2
stop_id: 1
stop_name: 1
next_stop: 1
stop_type: 1
a_time: 2
```
```
Format validation: 9 errors
stop_name: 3
stop_type: 2
a_time: 4
```
```
Line names and number of stops:
bus_id: 128, stops: 4
bus_id: 256, stops: 4
bus_id: 512, stops: 2
```
```
Start stops: 3 ['Bourbon Street', 'Pilotow Street', 'Prospekt Avenue']
Transfer stops: 3 ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
Finish stops: 2 ['Sesame Street', 'Sunset Boulevard']
```
```
Arrival time test:
bus_id line 128: wrong time on station Fifth Avenue
bus_id line 256: wrong time on station Sunset Boulevard
```
```
On demand stops test:
Wrong stop type: ['Elm Street', 'Sunset Boulevard']
```

## Disclaimer
The original learning materials and project ideas are from [JetBrains Academy](https://www.jetbrains.com/academy/). All codes were written by myself.