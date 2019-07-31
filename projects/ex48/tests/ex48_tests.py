from nose.tools import *
from ex48 import lexicon
from ex48 import parser


def test_directions():
    assert_equal(lexicon.scan('north'), [('direction', 'north')])
    result = lexicon.scan('north south east')
    assert_equal(result, [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east')])


def test_verbs():
    assert_equal(lexicon.scan('go'), [('verb', 'go')])
    result = lexicon.scan('go eat kill')
    assert_equal(result, [
        ('verb', 'go'),
        ('verb', 'eat'),
        ('verb', 'kill'),
    ])


def test_stops():
    assert_equal(lexicon.scan('the'), [('stop', 'the')])
    result = lexicon.scan('the in of')
    assert_equal(result, [
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of'),
    ])


def test_nouns():
    assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
    result = lexicon.scan('bear princess')
    assert_equal(result, [
        ('noun', 'bear'),
        ('noun', 'princess'),
    ])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])

    result = lexicon.scan("3 91234")
    assert_equal(result, [
        ('number', 3),
        ('number', 91234),
    ])


def test_errors():
    assert_equal(lexicon.scan("ASDASADAS"), [('error', 'ASDASADAS')])

    result = lexicon.scan("3 ASDASADAS princess")
    assert_equal(result, [
        ('number', 3),
        ('error', 'ASDASADAS'),
        ('noun', 'princess')
    ])


def test_sentence_creation():
    result = lexicon.scan("go to the north door")
    assert_equal(result, [
        ('verb', 'go'),
        ('error', 'to'),
        ('stop', 'the'),
        ('direction', 'north'),
        ('noun', 'door'),
    ])
