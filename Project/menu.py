import tkinter
from tkinter import *
import tkinter.font as font
import random
import json
from functools import partial

window = Tk()
window.title('Random Quiz')
window.geometry("800x500+10+20")
window['background'] = '#00c781'
myFont = font.Font(family='Showcard Gothic', size=15, weight='bold')
myFont_Choices = font.Font(family='Arial', size=15, weight='bold')
count = 0
score = 0

with open('./HighScore.json', encoding="utf8") as f:
    HIGH_SCORE = json.load(f)
    f.close()

with open('./data.json', encoding="utf8") as f:
    data = json.load(f)
    f.close()


# function
def menu_to_play():
    l.destroy()
    btn_play.destroy()
    btn_high.destroy()
    Play_page()

def newQuestion(ans):
    global data, score, count
    select = True

    Counter.destroy()
    Score_text.destroy()
    Question.destroy()
    Choices1.destroy()
    Choices2.destroy()
    Choices3.destroy()
    Choices4.destroy()

    answer = data[n]["answer"]
    if (int(answer) == int(ans)):
        score += 10

    data.pop(n)
    if select and count < 10:
        Play_page()
    else:
        with open('./data.json', encoding="utf8") as f:
            data = json.load(f)
            f.close()
        count = 0
        End_page()


def high_to_menu():
    highScore_text.destroy()
    ScoreList.destroy()
    btn_menu.destroy()
    Menu_page()


def menu_to_high():
    l.destroy()
    btn_play.destroy()
    btn_high.destroy()
    High_page()


def Save():
    global HIGH_SCORE
    HIGH_SCORE.append({
        "name": inputName.get(),
        "score": score
    })
    HIGH_SCORE = sorted(HIGH_SCORE, key=lambda k: k['score'], reverse=True)
    json_object = json.dumps(HIGH_SCORE, indent=4)
    with open('HighScore.json', 'w') as outfile:
        outfile.write(json_object)
        outfile.close()

    End_to_High()


def End_to_High():
    total_text.destroy()
    total_text.destroy()
    total.destroy()
    playAgain.destroy()
    btn_menu.destroy()
    inputName.destroy()
    btn_save.destroy()
    High_page()


def End_to_Play():
    total_text.destroy()
    total_text.destroy()
    total.destroy()
    playAgain.destroy()
    btn_menu.destroy()
    inputName.destroy()
    btn_save.destroy()
    Play_page()


def End_to_Menu():
    total_text.destroy()
    total_text.destroy()
    total.destroy()
    playAgain.destroy()
    btn_menu.destroy()
    Menu_page()


def Menu_page():
    global l, btn_play, btn_high
    l = Label(window, text="Random Quiz", font=("Showcard Gothic", 40), bg='#00c781')
    l.pack(pady=30)
    # button play
    btn_play = tkinter.Button(window,
                              text="Play",
                              bg='#ff1a53',
                              fg="#ffffff",
                              width=30,
                              height=3,
                              activebackground='#ff0040',
                              activeforeground="#ffffff",
                              command=menu_to_play)
    btn_play['font'] = myFont
    btn_play.pack(pady=10)
    # button high score
    btn_high = tkinter.Button(window,
                              text="High Score",
                              bg='#fff70a',
                              fg="#000000",
                              width=30,
                              height=3,
                              activebackground='#d1ca00',
                              command=menu_to_high)
    btn_high['font'] = myFont
    btn_high.pack()


def Play_page():
    window['background'] = '#d6d0f7'
    global count, score, Counter, Score_text, Question, Choices1, Choices2, Choices3, Choices4, select
    global data, n
    select = False
    if count == 0:
        score = 0
    l.destroy()
    btn_play.destroy()
    btn_high.destroy()
    count = count + 1

    n = random.randint(0, len(data) - 1)
    question = data[n]["question"]
    choice1 = data[n]["choice1"]
    choice2 = data[n]["choice2"]
    choice3 = data[n]["choice3"]
    choice4 = data[n]["choice4"]

    # Counter Text
    Counter = Label(window, text="Question " + str(count), font=("Showcard Gothic", 14), bg='#d6d0f7', fg='#4c39a7')
    Score_text = Label(window, text="Score\n  " + str(score), font=("Showcard Gothic", 20), bg='#d6d0f7', fg='#4c39a7')

    # Question
    Question = Label(window, text=str(question), font=("Showcard Gothic", 32), bg='#d6d0f7', fg='#4c39a7')

    # Choices
    Choices1 = tkinter.Button(window,
                              text=" 1 " + str(choice1),
                              bg='#523eb7',
                              fg="#ffffff",
                              width=30,
                              height=1,
                              anchor='w',
                              activebackground='#413190',
                              activeforeground="#ffffff",
                              command=partial(newQuestion, 1))

    Choices1['font'] = myFont_Choices

    Choices2 = tkinter.Button(window,
                              text=" 2 " + str(choice2),
                              bg='#523eb7',
                              fg="#ffffff",
                              width=30,
                              height=1,
                              anchor='w',
                              activebackground='#413190',
                              activeforeground="#ffffff",
                              command=partial(newQuestion, 2))
    Choices2['font'] = myFont_Choices
    Choices3 = tkinter.Button(window,
                              text=" 3 " + str(choice3),
                              bg='#523eb7',
                              fg="#ffffff",
                              width=30,
                              height=1,
                              anchor='w',
                              activebackground='#413190',
                              activeforeground="#ffffff",
                              command=partial(newQuestion, 3))
    Choices3['font'] = myFont_Choices
    Choices4 = tkinter.Button(window,
                              text=" 4 " + str(choice4),
                              bg='#523eb7',
                              fg="#ffffff",
                              width=30,
                              height=1,
                              anchor='w',
                              activebackground='#413190',
                              activeforeground="#ffffff",
                              command=partial(newQuestion, 4))
    Choices4['font'] = myFont_Choices

    Counter.pack(side="left", anchor='n', padx=20, pady=20)
    Score_text.pack(side="right", anchor='n', padx=20, pady=20)
    Question.pack(pady=(100, 0))
    Choices1.pack(pady=(15, 0))
    Choices2.pack(pady=(5, 0))
    Choices3.pack(pady=(5, 0))
    Choices4.pack(pady=(5, 0))


def High_page():
    window['background'] = '#00c781'
    global highScore_text, ScoreList, btn_menu
    highScore_text = Label(window, text="Leader Board")
    highScore_text.config(font=("Showcard Gothic", 30), bg='#00c781', fg='#ffffff')
    highScore_text.pack(pady=(50, 0))
    # Score List
    ScoreList = Listbox(window, bg="#00c781", bd=0, fg="#ffffff", justify='center',
                        font=("Showcard Gothic", 20), height=7)
    for i in range(5):
        if len(HIGH_SCORE) > i:
            show = str(HIGH_SCORE[i]['name']) + " - " + str(HIGH_SCORE[i]['score'])
            ScoreList.insert(int(i + 1), show)

    ScoreList.pack(pady=(20, 10))
    # Button Menu
    btn_menu = tkinter.Button(window,
                              text="Back",
                              bg='#ff9900',
                              fg="#ffffff",
                              width=20,
                              height=2,
                              activebackground='#b86e00',
                              command=high_to_menu)
    btn_menu['font'] = myFont
    btn_menu.pack(pady=10)


def End_page():
    window['background'] = '#00c781'
    global count, total_text, total_text, total, playAgain, btn_menu, inputName, btn_save, score

    total_text = Label(window, text="Score", font=("Showcard Gothic", 45), bg='#00c781', fg='#4c39a7')
    total_text.pack(pady=(50, 0))

    total = Label(window, text=str(score), font=("Showcard Gothic", 35), bg='#00c781', fg='#4c39a7')
    total.pack(pady=10)

    # input Name
    inputName = Entry(window, width=24, font=("Showcard Gothic", 15))
    inputName.pack(pady=5)

    # Button Save
    btn_save = tkinter.Button(window,
                              text="Save",
                              bg='#125cff',
                              fg="#ffffff",
                              width=20,
                              height=2,
                              activebackground='#003ab8',
                              activeforeground="#ffffff",
                              command=Save
                              )
    btn_save['font'] = myFont
    btn_save.pack(pady=5)

    # Button Plaay Again
    playAgain = tkinter.Button(window,
                               text="Play Again",
                               bg='#ff1a53',
                               fg="#ffffff",
                               width=20,
                               height=2,
                               activebackground='#ff0040',
                               activeforeground="#ffffff",
                               command=End_to_Play)
    playAgain['font'] = myFont
    playAgain.pack(pady=5)

    # Button Menu
    btn_menu = tkinter.Button(window,
                              text="Menu",
                              bg='#fff70a',
                              fg="#000000",
                              width=20,
                              height=2,
                              activebackground='#d1ca00',
                              command=End_to_Menu)
    btn_menu['font'] = myFont
    btn_menu.pack()


Menu_page()
window.mainloop()
