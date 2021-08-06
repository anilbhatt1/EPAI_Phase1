import datetime
from collections import namedtuple

def cast(type_, data):
    if type_ == 'DOUBLE':
        return float(data)
    elif type_ == 'INT':
        return int(data)
    elif type_ == 'DATE':
        data = datetime.datetime.strptime(data, '%m/%d/%Y')
        return data
    else:
        return str(data)

def cast_row(data_type, data_row):
    return [cast(type_, data)
            for type_, data in list(zip(data_type, data_row))]

data_type = ['INT', 'STRING', 'STRING', 'STRING', 'DATE', 'STRING', 'STRING', 'STRING', 'STRING' ]

def car_tickets(file_path):
    print('Reading file...')
    with open(file_path, 'r') as f:
        f.readline()                                                                               # This is to skip the header record
        ticket_data = yield from (cast_row(data_type, line.strip('\n').split(',')) for line in f)  # To take care of remaining records
    return ticket_data

ticket_dict = {}
def ctr_dict(vehicle_make)->str:
    def update():
        if not vehicle_make in ticket_dict.keys():
            ticket_dict[vehicle_make] = 0

        ticket_dict[vehicle_make] += 1
        return None

    return update