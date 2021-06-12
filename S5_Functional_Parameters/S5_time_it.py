import time
import math
pi = math.pi

def time_it(fn, *args, repetition=1, **kwargs):
    start = time.perf_counter()
    for i in range(repetition):
        values = fn(*args, **kwargs)
    end = time.perf_counter()
    time_taken = start - end
    return time_taken, values

def myprint(*args, **kwargs):
    sep = kwargs['sep']
    end = kwargs['end']
    result = ''
    for item in args:
        result += str(item) + str(sep)
    result += end
    return result

def squared_power_list(num, start, end):
    lst = []
    if start == end:
        raise Exception('Start and End cant be same')
    elif start > end:
        raise Exception('Start must be less than End')
    elif type(start) is not int or type(end) is not int:
        raise Exception('Start and End must be integers')
    elif start < 0 or end <0:
        raise Exception('-ve powers not allowed')

    for i in range(start, end+1):
        lst.append(num**i)
    return lst

def polygon_area(length, sides):
    if length <= 0:
        raise Exception('Length should be +ve')
    elif sides in [3,4,5,6]:
        area = round((length**2 * sides)/(4 * math.tan(pi/sides)), 2)
    else:
        raise Exception('Sides must 3,4,5 or 6')
    return area

def temp_converter(temp, temp_given_in):
    scale = temp_given_in.upper()
    if scale == 'F':
        temp_out = 5 / 9 * (temp - 32)
    elif scale == 'K':
        temp_out = temp - 273.15
    elif scale == 'C':
        temp_out = temp
    else:
        raise Exception('Scale must be c, f or k')

    return round(temp_out, 2)

def speed_converter(speed, dist='km', time='hr'):

    dist = dist.lower()
    time = time.lower()

    dist_dict = {'km': 1, 'm': 1000, 'yrd': 1093.61, 'ft': 3280.84}
    time_dict = {'day': 0.4167, 'hr': 1, 'min': 60, 's': 3600, 'ms': 3.6e+6}

    if speed <=0:
        raise Exception('Speed should be greater than 0')
    elif dist.lower() not in list(dist_dict.keys()):
        raise Exception(f'Speed must be in {list(dist_dict.keys())}')
    elif time.lower() not in list(time_dict.keys()):
        raise Exception(f'Time must be in {list(time_dict.keys())}')

    speed = speed * dist_dict[dist]/time_dict[time]

    return round(speed, 2)

time_t, values  = time_it(speed_converter, 100, dist='m', time='S', repetition=10)
print(values)
