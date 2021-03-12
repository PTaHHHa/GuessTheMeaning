def get_key_by_value(value, dic):
    for k in dic.items():
        if value == k[1]:
            print(k[0])
            exit()


def main(sentence: str):
    if len(sentence) < 1:
        raise ValueError('Sentence should have at least two words')
    elif not isinstance(sentence, str):
        raise TypeError(f'{type(sentence)} is not allowed')

    dic = {'Power as nuclear': ['nuclear', 'fukushima', 'renewable',
                                'sources', 'plants', 'energy', 'solar', 'substances', 'electricity'],
           'Kanye West': ['Power']}

    split_sentence = sentence.replace(', ', '').lower().split(' ')

    for word in split_sentence:
        for meaning in dic.values():
            if str(word) in meaning:
                get_key_by_value(meaning, dic)


if __name__ == '__main__':
    input_sentence = input('Input a sentence\n')
    main(input_sentence)
