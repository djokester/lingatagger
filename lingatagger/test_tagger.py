from . import tagger 
input_str = 'नीरजः हाँ माता जी! स्कूल ख़त्म होते सीधा घर आऊँगा'
def test_numericTagger():
    lst = ["1", "2", "3", "4"]
    string = "०१२३४५६७८९ ०१२३"
    assert tagger.numericTagger(lst) == [('1', 'num'), ('2', 'num'), ('3', 'num'), ('4', 'num')]
    assert tagger.numericTagger(string) == [('०१२३४५६७८९', 'num'), ('०१२३', 'num')]

def test_defaultTagger():
    lst = ["1", "2", "3", "4"]
    string = "०१२३४५६७८९ ०१२३"
    assert tagger.defaultTagger(lst) == [('1', 'any'), ('2', 'any'), ('3', 'any'), ('4', 'any')]
    assert tagger.defaultTagger(string) == [('०१२३४५६७८९', 'any'), ('०१२३', 'any')]

if __name__ == '__main__':
    test_numericTagger()
    test_defaultTagger()