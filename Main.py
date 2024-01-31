#!/usr/bin/env python3

import openai
import random

import requests
from PIL import Image, ImageDraw, ImageFont
import shutil
import urllib

import os
from dotenv import load_dotenv
from waveshare_epd import epd5in65f

import signal
# from timeout_decorator import timeout

import setup
from ScreenInit import ScreenInit

#try to access .env file, if error print message and exit
try:
    # Load your API key from an environment variable or secret management service
    load_dotenv()
except DotenvError as e:
    print("Error. Either .env file does not exist, or the API_KEY and or ScreenSize Variables have not been initialized.")
    exit(1)
#Load your API Key
#maybe add exception so that specific error message can be printed(never ran setup.py)
openai.api_key = os.getenv("API_KEY")
print(openai.api_key)
#get screen type
screenType = os.getenv("ScreenSize")




#Declare picture types
ParadyMode = 1
FunnyMode = 2
ArtisticMode = 3
InspiringMode = 4





def handler(signum, frame):
    raise TimeoutError("Code execution took too long.")


#main code that will display image to eink display
def main():
    
    
    #Attempt to display image to e-ink display
    try:
        #initialize display
        #maybe add exception so that specific error message can be printed(never ran setup.py)
        
        epd_disp = ScreenInit.giveProperScreen(screenType)
        #epd_disp = epd5in65f.EPD()
        epd_disp.init()
    
        #clear display
        epd_disp.Clear()
    
        #define width and height
        w = epd_disp.width
        h = epd_disp.height
    
    
        #define and draw background
        image = Image.open('image.png')
        image = image.resize((w, h))
        ImageDraw.Draw(image)
        #output to e-ink display
        epd_disp.display(epd_disp.getbuffer(image))
    except IOError as e:
        print(e)






#Gets prompt to use in image generation

def getPrompt():
    #Get a random mode
    ChoseMode = random.choices([ParadyMode, FunnyMode, ArtisticMode, InspiringMode], [25,25,25,25])[0]
    SubImage = random.randint(1, 4)
    
    #Select random mode to give to Chat GPT
    Mode = 'Fill in the blanks where the * characters are located for an image idea, '
    
    if ChoseMode == ParadyMode:    
        if SubImage == 1 or SubImage == 2:
            Mode += 'A parody of the album cover * by *'
        elif SubImage == 3 or SubImage == 4:  
            Mode += 'A parody of the art piece * by *'
        
    elif ChoseMode == FunnyMode:
        if SubImage == 1:
            Mode += 'A *(animal) doing *(something funny)'
        elif SubImage == 2: 
            Mode += '*(famous person) on *(something historically or culturally significant)'
        elif SubImage == 3: 
            Mode += '*(famous person or figure) doing a campaign for *'
        elif SubImage == 4: 
            Mode += '*caricature drawing of *(someone famous)'
    elif ChoseMode == ArtisticMode:
        if SubImage == 1:
            Mode += 'A picture of a *(living thing) doing *(something cool)'
        elif SubImage == 2:
            Mode += 'A picture of *(beautiful area) with *(something that creativly makes it a good image)'
        elif SubImage == 3:
            Mode += 'A virbrant and colorful picture of *(something interesting and thought provoking)'
        elif SubImage == 4:
            Mode += 'A picture of *(an innovative idea for an art piece)'
    elif ChoseMode == InspiringMode:
        if SubImage == 1 or SubImage == 2:
            Mode += 'A picture of * doing *(something inspiring)'
        elif SubImage == 3 or SubImage == 4:
            Mode += 'A picture of *(an inspiring art piece)'
    
        
    
    
    #for debugging
    print(Mode)

   

    #get image idea
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      max_tokens=100,
      messages =[ {"role": "user", "content": Mode}
      ]
      )
    
    #set and print chat gpts image idea
    print(completion.choices[0].message.content)
    ImageIdea = completion.choices[0].message.content
   

    #Get the image
    Imageresponse = openai.Image.create(
        prompt=ImageIdea,
        n=1,
        size="512x512"
    )
    imageUrl = Imageresponse['data'][0]['url']
    print(imageUrl)
    
    #Get the url for the AI Generated image
    response = requests.get(imageUrl)
    #download image to folder under the name image.png
    if response.status_code:
        fp = open('image.png', 'wb')
        fp.write(response.content)
        fp.close()
    




#driver code


# Call the function to execute its code
#catch error, and keep running til there are no errors
signal.signal(signal.SIGALRM, handler)
signal.alarm(75)  # Set the alarm signal to be triggered after 75 seconds

try:
    while True:
        try:
            getPrompt()
            break
        
        except TimeoutError as e:
            print('Error1:', e)
            exit(1)
    
    main()

except TimeoutError as e:
    print("Error:", e)
    exit(1)
    
    
finally:
    # Cancel the alarm signal if there are no issues
    signal.alarm(0)
    
    
    
    
    
    
    
    
    
    
    


    
