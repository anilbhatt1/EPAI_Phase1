import Generators_Assignment as GA
from collections import namedtuple

data_head  = ['Summons_Number' , 'Plate_ID', 'Registration_State', 'Plate_Type', 'Issue_Date', 'Violation_Code',
             'Vehicle_Body_Type', 'Vehicle_Make' ,'Violation_Description']

Tickets = namedtuple('Tickets', data_head)

ticket_path = r'C:\Users\anila\Desktop\AI\EPAI-Phase1\S15_Generators\nyc_parking_tickets_extract-1.csv'
ticket_gen = GA.car_tickets(ticket_path)

tickets_lst = [Tickets(*item) for item in ticket_gen]

def test_tickets_lst():
    assert len(tickets_lst) == 1000, 'Incorrect tickets list count'
    assert tickets_lst[1].Vehicle_Make == 'CHEVR', 'Incorrect Vehicle Make'

for item in tickets_lst:
    GA.ctr_dict(item.Vehicle_Make)()

def test_ctr_dict():
    assert GA.ticket_dict['BMW'] == 34, 'Incorrect ticket count for BMW'
    assert GA.ticket_dict['HYUND'] == 35, 'Incorrect ticket count for Hyundai'
