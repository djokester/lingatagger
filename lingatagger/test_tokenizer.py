from . import tokenizer
def test_tokenize():
    input_str = 'Hey there! Wassup? \n Nice Meeting You.\t Have a nice day.'
    out = tokenizer.tokenize(input_str)
    assert out == ['Hey', 'there', '!', 'Wassup', '?', 'Nice', 'Meeting', 'You', '.', 'Have', 'a', 'nice', 'day', '.']

def test_wordtokenize():
    input_str = 'Hey there! Wassup? \n Nice Meeting You.\t Have a nice day.'
    out = tokenizer.wordtokenize(input_str)
    assert out == ['Hey', 'there', 'Wassup', 'Nice', 'Meeting', 'You', 'Have', 'a', 'nice', 'day']

def test_senttokenize():
    input_str = 'Hey there! Wassup? \n Nice Meeting You.\t Have a nice day.'
    out = tokenizer.sentencetokenize(input_str)
    assert out == ['Hey there! ', 'Wassup? \n ', 'Nice Meeting You.\t ', 'Have a nice day.']

if __name__ == '__main__':
    test_tokenize()
    test_wordtokenize()
    test_senttokenize()