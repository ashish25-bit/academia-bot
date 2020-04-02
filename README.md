# Academia-Bot
Web Automation of academia which gives you the number of classes you can bunk in a respective subject.

To run : 

    download chromedriver and move to /usr/bin/local
    for linux users, you will need permissions to move the file.
    run the command : 
    sudo mv -f -i Downloads/chromediver_linux64/chromedriver /usr/local/bin
    (this will obtain all the permissions needed and move the file)
    
    In the terminal : 
    To set up the virtual environment : 
    1. virtualenv -p python3 .
    2. source bin/activate
    Then install selenium : 
    pip install selenium
    
    Run the program : 
    python academia.py
    Enter your username and password when asked in the terminal
