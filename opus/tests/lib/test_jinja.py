from jinja2 import Environment

from lib.jinja import join_attribute, is_pair


def test_is_pair():
    assert is_pair(2) is False
    assert is_pair((2, 3)) is False
    assert is_pair({'hello': 'friend'}) is False
    assert is_pair(('key', 'value')) is True
    assert is_pair(('key', 5)) is True


def test_join_attributes_pair():
    att = join_attribute(('key', 'value'), delimeter='=')
    assert att == 'key="value"'


def test_join_attributes_dict():
    d = {'first': 'value1', 'second': 'value2'}
    expected_str = 'first="value1" second="value2"'
    actual_str = join_attribute(d, delimeter='=', separator=' ')
    assert actual_str == expected_str


def test_join_attributes_iterable():
    d = [('first', 'value1'), ('second', 'value2')]
    expected_str = 'first="value1" second="value2"'
    actual_str = join_attribute(d, delimeter='=', separator=' ')
    assert actual_str == expected_str


def test_join_attributes_template():
    env = Environment()
    env.filters['join_attribute'] = join_attribute
    temp = env.from_string(
        "{% set d = {'first': 'value1', 'second': 'value2'} %}"
        "{{ d | join_attribute }}")
    expected_str = 'first="value1" second="value2"'
    actual_str = temp.render()
    assert actual_str == expected_str
