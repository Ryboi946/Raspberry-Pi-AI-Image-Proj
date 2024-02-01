Original idea from Jess Farber(https://jezs00.medium.com/pycasso-how-to-build-a-picture-frame-to-show-you-random-ai-art-every-day-44a1d3d78237)

Hello! This project uses AI to generate some cool images for your E-Ink display! All you need is a Raspberry Pi, and a Waveshare E-Ink display. Once you configure the operating system for your Pi, and have aquired the E-Ink display, follow along with these steps:

1. Make sure you have Python on your machine, if you do not use commands: sudo apt-get update, sudo apt-get install python3

2. Clone the git repository onto your machine, use command: git clone https://github.com/Ryboi946/Raspberry-Pi-AI-Image-Proj.git

3. Connect Waveform E-Ink display to your Pi. This will be done using your GPIO pins. Follow Waveform's instructions for connecting the display to your Raspberry Pi Model.

4. Download the dependencies for the project, to do this navagate to the projects directory and run command: pip install -r requirements.txt

5. From here, run the setup.py file - use command: python3 setup.py

6. Enter your OpenAI API Key and the number corresponding to the type of Waveshare E-Ink display that you have.

7. Assuming your API_key and Waveshare E-Ink display type were correctly entered, you can run the main.py file, use command: python3 main.py

8. You should then see an AI generated image appear on your E-Ink display!
