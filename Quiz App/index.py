from Questions import Questions

questions = [
    'Name of Capital of Pakistan ? \n (a) Karachi \n (b) Islamabad \n (c) Punjab \n\n',
    'Name of Prime Minister of Pakistan ? \n (a) Imran Khan \n (b) Nawaz Sharif \n (c) Shahbaz Sharif \n\n',
    'Name of President of Pakistan ? \n (a) Zardari \n (b) Mamnoon Hussain \n (c) Dr.Arif Alvi \n\n',
]

questions_prompt = [
    Questions(questions[0], 'b'),
    Questions(questions[1], 'a'),
    Questions(questions[2], 'c'),
]


def runquiz(questionslist):
    score = 0
    for question in questionslist:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print('You Got ' + str(score) + '/' + str(len(questionslist)) + ' questions correct')


runquiz(questions_prompt)
