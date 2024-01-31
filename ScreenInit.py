from waveshare_epd import *

import os
from dotenv import load_dotenv

class ScreenInit:
    
    
    ''' Below are the codes for each e-ink display type    
    1   1in02
    2   1in54
    3   1in54b
    4   1in54b
    5   1in54c
    6   1in54V2
    7   1in64g
    8   2in7
    9   2in7b
    10   2in7bV2
    11   2in7_V2
    12   2in9
    13   2in9bc
    14   2in9b_V3
    15   2in9d
    16   2in9_V2
    17   2in13
    18   2in13bc
    19   2in13b_V3
    20   2in13b_V4
    21   2in13d
    22   2in13g
    23   2in13_V2
    24   2in13_V3
    25   2in36g
    26   2in66
    27   2in66b
    28   3in0g
    29   3in7
    30   3in52
    31   4in01
    32   4in2
    33   4in2bc
    34   4in2b_V2
    35   4in37g
    36   5in65f
    37   5in83
    38   5in83bc
    39   5in83b_V2
    40   5in83_V2
    41   7in3f
    42   edp7in3g
    43   7in5
    44   7in5bc
    45   7in5b_HD
    46   7in5b_V2
    47   7in5_HD
    48   7in5_V2
    49   7in5_V2_fast
    '''
    
    
        
    
    def giveProperScreen(id):
        
        id = int(id)
        
        #check to see if proper ID is given
        if(id <= 0 or id > 49):
            raise ValueError("Improper ID given")
        
        #return the proper initialization given the ID
        if(id == 1):
            return epd1in02.EPD()
        elif(id == 2):
            return epd1in54.EPD()
        elif(id == 3):
            return epd1in54b.EPD()
        elif(id == 4):
            return epd1in54b_V2.EPD()
        elif(id == 5):
            return epd1in54c.EPD()
        elif(id == 6):
            return epd1in54_V2.EPD()
        elif(id == 7):
            return epd1in64g.EPD()
        elif(id == 8):
            return epd2in7.EPD()
        elif(id == 9):
            return epd2in7b.EPD()
        elif(id == 10):
            return epd2in7b_V2.EPD()
        elif(id == 11):
            return epd2in7_V2.EPD()
        elif(id == 12):
            return epd2in9.EPD()
        elif(id == 13):
            return epd2in9bc.EPD()
        elif(id == 14):
            return epd2in9b_V3.EPD()
        elif(id == 15):
            return epd2in9d.EPD()
        elif(id == 16):
            return epd2in9_V2.EPD()
        elif(id == 17):
            return epd2in13.EPD()
        elif(id == 18):
            return epd2in13bc.EPD()
        elif(id == 19):
            return epd2in13b_V3.EPD()
        elif(id == 20):
            return epd2in13b_V4.EPD()
        elif(id == 21):
            return epd2in13d.EPD()
        elif(id == 22):
            return epd2in13g.EPD()
        elif(id == 23):
            return epd2in13_V2.EPD()
        elif(id == 24):
            return epd2in13_V3.EPD()
        elif(id == 25):
            return epd2in36g.EPD()
        elif(id == 26):
            return epd2in66.EPD()
        elif(id == 27):
            return epd2in66b.EPD()
        elif(id == 28):
            return epd3in0g.EPD()
        elif(id == 29):
            return epd3in7.EPD()
        elif(id == 30):
            return epd3in52.EPD()
        elif(id == 31):
            return epd4in01f.EPD()
        elif(id == 32):
            return epd4in2.EPD()
        elif(id == 33):
            return epd4in2bc.EPD()
        elif(id == 34):
            return epd4in2b_V2.EPD()
        elif(id == 35):
            return epd4in37g.EPD()
        elif(id == 36):
            return epd5in65f.EPD()
        elif(id == 37):
            return epd5in83.EPD()
        elif(id == 38):
            return epd5in83bc.EPD()
        elif(id == 39):
            return epd5in83b_V2.EPD()
        elif(id == 40):
            return epd5in_V2.EDP()
        elif(id == 41):
            return epd7in3f.EPD()
        elif(id == 42):
            return epd7in3g.EPD()
        elif(id == 43):
            return epd7in5.EPD()
        elif(id == 44):
            return epd7in5bc.EPD()
        elif(id == 45):
            return epd7in5b_HD.EPD()
        elif(id == 46):
            return epd7in5b_V2.EPD()
        elif(id == 47):
            return epd7in5_HD.EPD()
        elif(id == 48):
            return epd7in5_V2.EPD()
        elif(id == 49):
            return epd7in5_V2_fast.EPD()