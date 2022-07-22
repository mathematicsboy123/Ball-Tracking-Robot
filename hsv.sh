# Written by Shreyans Daga
# Run code to update binary image
cd website/static && python3 img.py 2> /dev/null 1> /dev/null &
camera=$(ps aux | grep python3\ img.py | awk '{ print $2 }' | head -n 1)

# Start website
cd website
export FLASK_APP=website.py
flask run 

# Stop binary image updates on website
kill -9 $camera

# Start the Robot
cd ..
python3 controller.py
