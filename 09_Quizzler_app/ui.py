from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # Le pasamos de parámetro un objeto de tipo QuizBrain para trabajar con sus métodos
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.windows = Tk()
        self.windows.title('Quizzler')
        self.windows.config(pady=20, padx=20, background=THEME_COLOR)

        self.score = Label(text='Score: 0', background=THEME_COLOR, fg='white', justify='center')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.text = self.canvas.create_text(150,
                                            125,
                                            text="Questions",
                                            fill=THEME_COLOR,
                                            font=("Arial", 20, "italic"),
                                            width=280)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_img, background=THEME_COLOR, highlightthickness=0, command=self.check_true)
        self.button_true.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_img, background=THEME_COLOR, highlightthickness=0)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):  # Recogemos la pregunta y la presentamos en el canvas
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.text, text=q_text)
        else:
            self.canvas.itemconfigure(self.text, text=f"Has terminado la partida. Score: {self.quiz.score}")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_true(self):  # Para pasarle el string a la función check_answer() al pulsar el botón
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):  # Si es true o false, cambiamos el fondo 1 segundo y pasamos siguiente pregunta.
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.windows.after(1000, self.get_next_question)



