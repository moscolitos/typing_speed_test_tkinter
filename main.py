import tkinter as tk
import time
import random
import string
import sqlite3

class TypingTest:
    def __init__(self, master):
        self.master = master
        self.master.configure(background='black')
        self.start_time = None
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Hello, World!",
            'I love you',
            # Add more sentences as per your need.
        ]
        self.setup_ui()
        self.setup_db()

    def setup_ui(self):
        # Add widgets to your UI
        # Label to display sentence.
        self.name_label = tk.Label(self.master, text="Enter your name", bg="black", fg="blue", font=("Helvetica", 18))
        self.name_label.pack(pady=(50, 50))


        # Entry to enter username.
        self.username_entry = tk.Entry(self.master, fg="white", bg="black", font=("Helvetica", 16), width=60)
        self.username_entry.pack(pady=10)
        

        # Label to display sentence.
        self.sentence_label = tk.Label(self.master, text="", bg="black", fg="yellow", font=("Helvetica", 18))
        self.sentence_label.pack(pady=(50, 50))

        # Entry to type in.
        self.typing_entry = tk.Entry(self.master, fg="white", bg="black", font=("Helvetica", 16), width=60)
        self.typing_entry.pack(pady=10)
        self.typing_entry.bind("<Key>", self.start_timer)
        self.typing_entry.bind("<Return>", self.calculate_results)

        # Label to display result.
        self.result_label = tk.Label(self.master, text="", bg="black", fg="white", font=("Helvetica", 16))
        self.result_label.pack(pady=10)

        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_test, fg="white", bg="red", font=("Helvetica", 16))
        self.reset_button.pack(pady=(50, 200))
        
        self.leaderboard_button = tk.Button(self.master, text="Leaderboard", command=self.display_leaderboard, fg="white", bg="red", font=("Helvetica", 16))
        self.leaderboard_button.pack(pady=10)

        # Load the first sentence
        self.load_new_sentence()

    def setup_db(self):
        # Create a database connection
        self.conn = sqlite3.connect('leaderboard.db')

        # Create a cursor
        c = self.conn.cursor()

        # Create leaderboard table
        c.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            username TEXT,
            wpm REAL,
            accuracy REAL
        )
        ''')

        # Commit changes and close connection
        self.conn.commit()

    def start_timer(self, event):
        # If timer is not already started, start it
        if self.start_time is None:
            self.start_time = time.time()

    def end_timer(self):
        self.end_time = time.time()

    def calculate_results(self, event):
        self.end_timer()

        # Calculate time taken in minutes.
        time_taken = (self.end_time - self.start_time) / 60

        typed_text = self.typing_entry.get()

        # Calculate WPM.
        print(len(typed_text))
        print(len(typed_text)/5/time_taken)
        words = len(typed_text.split())
        wpm = words / time_taken

        # Normalize text to lowercase and remove punctuation.
        normalize = lambda text: "".join(ch.lower() for ch in text if ch not in string.punctuation)
        normalized_sentence = normalize(self.current_sentence)
        normalized_text = normalize(typed_text)

        # Calculate accuracy.
        longest_length = max(len(normalized_sentence), len(normalized_text))
        accuracy = sum(t1 == t2 for t1, t2 in zip(normalized_sentence.ljust(longest_length), normalized_text.ljust(longest_length))) / longest_length

        # Add entry to leaderboard
        self.add_to_leaderboard(self.username_entry.get(), wpm, accuracy)

        # Update result label.
        self.result_label.config(text=f"WPM: {wpm}\nAccuracy: {accuracy * 100}%")

    def reset_test(self):
        # Reset timer
        self.start_time = None
        # Clear text entry
        self.typing_entry.delete(0, tk.END)
        # Load new sentence
        self.load_new_sentence()
        # Reset result label
        self.result_label.config(text="")

    def load_new_sentence(self):
        # Select a new random sentence
        self.current_sentence = random.choice(self.sentences)
        # Update the sentence label
        self.sentence_label.config(text=self.current_sentence)

    def add_to_leaderboard(self, username, wpm, accuracy):
        # Open connection and create cursor
        self.conn = sqlite3.connect('leaderboard.db')
        c = self.conn.cursor()

        # Insert new entry
        c.execute("INSERT INTO leaderboard VALUES (?, ?, ?)", (username, wpm, accuracy))

        # Commit changes and close connection
        self.conn.commit()
        self.conn.close()

    def display_leaderboard(self):
        # Open connection and create cursor
        self.conn = sqlite3.connect('leaderboard.db')
        c = self.conn.cursor()

        # Fetch top 10 entries
        c.execute("SELECT * FROM leaderboard ORDER BY wpm DESC, accuracy DESC LIMIT 10")
        entries = c.fetchall()

        # Create new window
        leaderboard = tk.Toplevel(self.master)
        leaderboard.title("Leaderboard")

        # Create labels for each entry
        for i, (username, wpm, accuracy) in enumerate(entries, start=1):
            tk.Label(leaderboard, text=f"{i}. {username}: {wpm} WPM, {accuracy*100:.2f}% Accuracy").pack()

        # Close connection
        self.conn.close()
        print(f'{i}. {username}: {wpm} WPM, {accuracy*100:.2f}% Accuracy')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Typing Speed Test")

    # Get the width and height of the screen.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Set the size of the window to be the size of the screen.
    root.geometry(f"{screen_width}x{screen_height}")
    typing_test = TypingTest(root)
    root.mainloop()
