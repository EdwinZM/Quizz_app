THEME_COLOR = "#375362"
import tkinter as tk

class QuizInterface:
    def __init__(self, question):
        self.question = question
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_image = tk.PhotoImage(file="./images/true.png")
        self.correct_button = tk.Button(image=self.true_image, highlightthickness=False)
        self.correct_button.grid(column=0, row=2)
        self.false_image = tk.PhotoImage(file="./images/false.png")
        self.correct_button = tk.Button(image=self.false_image, highlightthickness=False)
        self.correct_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        new_question = self.question.next_question()
        self.canvas.itemconfig(self.question_text, text=new_question)




