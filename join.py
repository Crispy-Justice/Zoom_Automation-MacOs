from info import *
from tabulate import tabulate

meetingid = ""
meetingpass = ""
subject = ""


class join:
    
    def math(sub, id, pswd):
        meetingid = math_meetingid
        meetingpass = math_pswd
        subject = 'math'
        return (subject, meetingid, meetingpass)
    
    def chemistry(sub, id, pswd):
        meetingid = chemistry_meetingid
        meetingpass = chemistry_pswd
        subject = 'chemistry'
        return (subject, meetingid, meetingpass)
    
    def physics(sub, id, pswd):
        meetingid = physics_meetingid
        meetingpass = physics_pswd
        subject = 'physics'
        return (subject, meetingid, meetingpass)
    
    def biology(sub, id, pswd):
        meetingid = biology_meetingid
        meetingpass = biology_pswd
        subject = 'biology'
        return (subject, meetingid, meetingpass)
    
    def history(sub, id, pswd):
        meetingid = history_meetingid
        meetingpass = history_pswd
        subject = 'history'
        return (subject, meetingid, meetingpass)
    
    def geography(sub, id, pswd):
        meetingid = geography_meetingid
        meetingpass = geography_pswd
        subject = 'geogarphy'
        return (subject, meetingid, meetingpass)

    def english(sub, id, pswd):
        meetingid = english_meetingid
        meetingpass = english_pswd
        subject = 'english'
        return (subject, meetingid, meetingpass)
    
    def _help():
        print(data_help)
    
    def timetable():
        print('\n')
        print(tabulate(data_timetable, headers=["TIMINGS", "MON", "TUES", "WED", "THURS", "FRI", "SAT"]))
        print('\n')