
math_meetingid = 'meetingid' # Enter math meeting id here.
math_pswd = 'meetingpswd' # Enter math meeting password here.

chemistry_meetingid = 'meetingid' # Enter chemistry meeting id here.
chemistry_pswd = 'meetingpswd' # Enter chemistry meeting password here.

physics_meetingid = 'meetingid' # Enter physics meeting id here.
physics_pswd = 'meetingpswd' # Enter math physics password here.

biology_meetingid = 'meetingid' # Enter biology meeting id here.
biology_pswd = 'meetingpswd' # Enter math biology password here.

history_meetingid = 'meetingid' # Enter history meeting id here.
history_pswd = 'meetingpswd' # Enter math history password here.

geography_meetingid = 'meetingid' # Enter geography meeting id here.
geography_pswd = 'meetingpswd' # Enter math geography password here.

english_meetingid = 'meetingid' # Enter english meeting id here.
english_pswd = 'meetingpswd' # Enter math english password here.

# help info.
data_help = '''
help, -h                Show this help message.
help -tt, -h -tt        Show Timetable.
quit, -q                Exit.
--------------------------------------------------
math                    Join math meeting.
chemistry, chem         Join chemistry meeting.
physics, phy            Join physics meeting.
biology, bio            Join biology meeting.
english, eng            Join english meeting.
history, his            Join physics meeting.
geography, geo          Join history meeting.
    '''
    
# Timetable.
                    #time   #mon    #tues   #wed    #thurs   #fri    #sat   
data_timetable = [ ['6:00', 'GEO',  'MATH', 'PHY',  'CHEM', 'PHY',  'GEO'],
                 [  '7:00', 'HIS',  'GEO',  'MATH', 'ENG',  'ENG',  'CHEM'],
                 [  '8:00', 'BIO',  'PHY',  'CHEM', 'MATH', 'MATH', 'BIO'],
                 [  '9:00', 'MATH', 'ENG',  'HIS',  'BIO',  'HIS',  'MATH'] ]
