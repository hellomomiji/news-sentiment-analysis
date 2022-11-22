# Intro 
A news sentiment Analysis app constructed by flask.

![Image](https://user-images.githubusercontent.com/38517716/203186883-a7d1da68-c376-4a37-bcd3-f6c19178b743.png)
(Example: get sentiment analysis by keyword "Elon Musk")

# Get Started

## To run this app in your local server.
(Reference: [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)).

1. Prerequisites

   - python3 and python extension installed.

2. Create project environment for the Flask
    - use the following command to create and activate virtual environment named `.venv`
    ```
    # Linux
    sudo apt-get install python3-venv    # If needed
    python3 -m venv .venv
    source .venv/bin/activate

    # macOS
    python3 -m venv .venv
        source .venv/bin/activate

    # Windows
    py -3 -m venv .venv
    .venv\scripts\activate
    ```
3. Install dependencies `pip3 install -r requirements.txt`.
4. Change api key to your own api key in `src/getData.py `.
5. `flask run` or `python3 app.py`(debug on) to run the app on your local server.
