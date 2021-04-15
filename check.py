sentence_list = {'A train is ___________ than a bus. (fast)': 'faster',
                 'This text is the ___________ of all. (difficult)': 'the most difficult',
                 'I was ill last week but today I am________ (good)': 'better',
                 'Park Street is _______ than Market Street. (wide)': 'wider',
                 'This jacket is small for me. Show me a ________ one. (big)': 'bigger',
                 'What is the __________ thing in life? (beautiful)': 'the most beautiful',
                 'A crocodile is _________ than a water snake. (big)': 'bigger',
                 'Helen is the ________ girl in our class (smart)': 'the smartest'}


def check(i, sentence: str):
    if len(sentence) < 1:  # если длина меньше 2, то ошибка
        raise ValueError('Sentence should have at least two words')
    elif not isinstance(sentence, str):
        # если тип данных не строка, то ошибка и выводим сообщение
        # ,что такой тип данных нельзя использовать
        raise TypeError(f'{type(sentence)} is not allowed')
    if sentence.strip().lower() != i[1]:
        print('You failed the test :(')
        exit()


def main():
    for i in sentence_list.items():
        print('\n'+i[0])
        input_sentence = input('Input your answer: ')
        check(i, input_sentence)


main()
print('You passed the test! :)')
