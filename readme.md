# Intro 
A news sentiment Analysis app constructed by flask.

![Screenshot 2022-11-22 at 2 11 05 PM](https://user-images.githubusercontent.com/38517716/203431783-d9f79dba-9bd2-409a-92ba-b33a1971dc5f.png)
(Example: get sentiemnt analysis of today's news headlines.)

![Screenshot 2022-11-22 at 2 11 28 PM](https://user-images.githubusercontent.com/38517716/203431844-73c1c25e-26d8-49a9-b07c-20be1d3ae9cc.png)
(Example: get sentiment analysis by keyword "Elon Musk".)

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
