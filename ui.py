# This file is written for UI using tkinter.

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", width=8, height=3,
                                 font=("Arial", 10, "bold"), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question here", width=280,
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.get_true)
        self.right_button.grid(row=2, column=1)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.get_false)
        self.wrong_button.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.enable_buttons()
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f'"Thanks!! You got {self.quiz.score}/{len(self.quiz.question_list)}"')
            self.disable_buttons()

    def get_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def get_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        self.disable_buttons()
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def enable_buttons(self):
        self.wrong_button["state"] = "active"
        self.right_button.config(state="active")
        # self.right_button["state"] = "active"        THIS WAY OR ABOVE WAY. BOTH WAY IS POSSIBLE.

    def disable_buttons(self):
        self.right_button.config(state="disabled")
        self.wrong_button["state"] = "disabled"
