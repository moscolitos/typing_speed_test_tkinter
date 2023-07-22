
![typing speed test](https://github.com/moscolitos/typing_speed_test_tkinter/assets/51311462/e69bad4b-bac7-4edb-a00b-6ec3684c3cbe)

# Typing Speed Test Tkinter Application
This application is a typing speed test created using Python and Tkinter. The application allows users to test their typing speed by typing out a randomly selected sentence. It then calculates their speed in Words Per Minute (WPM) and their accuracy. A leaderboard system is also implemented to track top performers.

## Installation
Before running this application, ensure you have Python installed on your computer. If not, you can download it from here.

## Detailed Specifications
The Typing Speed Test application is a comprehensive tool developed using Python 3.x and Tkinter, aimed to assess a user's typing skills. The application comes with a user-friendly GUI that intuitively measures typing speed and accuracy, presenting the results in real-time.

## Technical Features
- Test Generation: The application randomly selects a sentence from a predefined list. The user's goal is to replicate this sentence as quickly and accurately as possible.

- Real-Time Assessment: The application begins recording the time as soon as the user starts typing and stops when they finish. The typing speed, computed in Words Per Minute (WPM), is the total number of words typed divided by the elapsed time, then multiplied by 60.

- Accuracy Calculation: The application computes typing accuracy by comparing the user's typed text with the original sentence. It checks for exact character matches, including punctuation and capitalization.

- Leaderboard: A leaderboard system is built into the application. It ranks users based on their WPM and accuracy. This data is managed using SQLite, offering a lightweight, serverless database solution.

- Interactive GUI: The application's GUI is designed using Tkinter, Python's standard GUI library. It features a clean, minimalistic design that is easy to navigate. The application offers customization options, such as color and font size changes, to enhance user experience.

## Technical Requirements
### Python: 

The application is written in Python 3.x. Ensure that Python 3.x is installed on your machine before running the application.

### Tkinter: 

Tkinter is used for creating the application's GUI. Tkinter comes pre-installed with Python, so you do not need to install it separately.

### SQLite: 

SQLite is used for managing the leaderboard data. It comes pre-installed with Python, so no separate installation is required.

## Running the Application
To run the application, execute the following command in the terminal in the directory containing the script:

python main.py

The application will then start, presenting you with a random sentence to type.

## Key Features
- Test your typing speed in real-time.
- Measures Words per Minute (WPM) and accuracy.
- Leaderboard system to track top performances.
- Reset function to start a new test.
- Presents a randomly selected sentence for each new test.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT
