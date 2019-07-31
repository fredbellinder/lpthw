from nose.tools import *
from ex48 import parser
from ex48 import lexicon


def test_sentence():
    # assert_equal(parser.scan()
    result = lexicon.scan('go north to cabinet')
    parsed = parser.parse_sentence(result)
    assert_equal(type(parsed), parser.Sentence)


# def test_sentence2():
#     # assert_equal(parser.scan()
#     result = lexicon.scan('go north to kill the cabinet')
#     parsed = parser.parsery(result)
#     assert_equal(type(parsed), parser.Sentence)


def test_exception():
    assert_raises(parser.ParserError, parser.parse_sentence,
                  [('noun', 123123123123123)])

# def test_sentence3():
#     # assert_equal(parser.scan()
#     result = lexicon.scan('north north go north to kill the cabinet')
#     parsed = parser.parse_sentence(result)
#     assert_raises(parser.parserError, parse_sentence, parameters)
#     assert_equal((parsed), parser.Sentence)
