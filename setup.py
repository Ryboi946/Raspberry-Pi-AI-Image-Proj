import os


from dotenv import load_dotenv, dotenv_values, set_key




#setup.py will only need to be run when you first install the repository
#prompts user to enter screen size and return size
def screenSizes():
    #declare sizes
    sizes = ["1in02", "1in54", "1in54b", "1in54b", "1in54c", "1in54V2", "1in64g", "2in7", "2in7b", "2in7bV2", "2in7_V2", "2in9", "2in9bc", "2in9b_V3", "2in9d", "2in9_V2", "2in13", "2in13bc", "2in13b_V3", "2in13b_V4", "2in13d", "2in13g", "2in13_V2", "2in13_V3", "2in36g", "2in66", "2in66b", "3in0g", "3in7", "3in52", "4in01", "4in2", "4in2bc", "4in2b_V2", "4in37g", "5in65f", "5in83", "5in83bc", "5in83b_V2", "5in83_V2", "7in3f", "edp7in3g", "7in5", "7in5bc", "7in5b_HD", "7in5b_V2", "7in5_HD", "7in5_V2","7in5_V2_fast"]
    
    print("Select the type of waveshare e-ink display you have: ")
    size = -1
    #print sizes
    while(int(size) < 1 or int(size) > 49) :
        for i in range(0,len(sizes)):
            print((i+1)," ",sizes[i])    
        size = input("Select your size (needs to be from a number 1-49): ")
    
    
    
    
    
    return size

#create .env file(if it does not exist and prompt user to enter API_KEY/screen type   

def getValues():
    #ask user if they would like to edit api key
    print("Would you like to add or edit an API Key entry? If yes type 'y': ")
    result = input()
    result = result.lower()
    #get api key add to .env file
    if(result == 'y'):
        API_KEY = input("Enter the API Key: ")
        print(API_KEY)
        set_key(".env", "API_KEY", API_KEY)
    
    
    #ask user to enter waveshare screen size
    size = input("Would you like to enter your waveshares screen size. If so type 'y': ")
    size = size.lower()
    if(size == 'y'):
        #get better logic to input screen size(should be from a list of choices
        ScreenSize  = screenSizes()
        set_key(".env", "ScreenSize", ScreenSize)
        
        
#driver code
if __name__ == '__main__':
    
    
    #try to open .env file, if it doesnt exist, create it
    try:
        load_dotenv()
    except DotenvError as e:
        with open(".env", "w") as fp:
            fp.write("API_KEY=\nScreenSize=\n")
            
    vars = dotenv_values()
    
    if(not ("API_KEY" in vars and "ScreenSize" in vars)):
        with open(".env", "w") as fp:
            fp.write("API_KEY=\nScreenSize=\n")
    getValues()
