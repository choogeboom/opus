import typing
from collections.abc import Mapping

Pair = typing.Tuple[str, typing.Any]
PairMap = typing.Mapping[str, typing.Any]


def is_pair(t):
    """
    Check whether an object is a pair
    
    :param t: 
    :return: bool
    """
    return isinstance(t, tuple) and len(t) == 2 and isinstance(t[0], str)


def join_attribute(pair: typing.Union[Pair, typing.Iterable[Pair], PairMap],
                   delimeter='=',
                   separator=' '):
    """
    Join together name value pairs into name="value"
    
    :param pair:
    :param delimeter:
    :param separator:
    :return: The joined name value pair
    """
    if is_pair(pair):
        return '{}{}"{!s}"'.format(pair[0], delimeter, pair[1])
    elif hasattr(pair, '__iter__'):
        if isinstance(pair, Mapping):
            pair = pair.items()
        pairs = (join_attribute(p, delimeter) for p in pair)
        return separator.join(pairs)
    else:
        raise TypeError('Unable to join attributes. Invalid type')


