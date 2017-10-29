import app


def test_is_unique():
    # Input 1
    assert app.SolutionOne('abcd')
    assert app.SolutionTwo('abcd')
    assert app.SolutionThree('abcd')

    # Input 2
    assert app.SolutionOne('abcdefghijklmnopqrstuvwxyz'
                           '1234567890'
                           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           '!@#$%^&*()-_=+\\|[{;:\'"/?.>,<`~}]')
    assert app.SolutionTwo('abcdefghijklmnopqrstuvwxyz'
                           '1234567890'
                           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           '!@#$%^&*()-_=+\\|[{;:\'"/?.>,<`~}]')
    assert app.SolutionThree('abcdefghijklmnopqrstuvwxyz'
                             '1234567890'
                             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                             '!@#$%^&*()-_=+\\|[{;:\'"/?.>,<`~}]')

    # Input 3
    assert not app.SolutionOne('acvklzckvnzxcvzlxcvkzxcvn')
    assert not app.SolutionTwo('acvklzckvnzxcvzlxcvkzxcvn')
    assert not app.SolutionThree('acvklzckvnzxcvzlxcvkzxcvn')

    # Input 4
    assert not app.SolutionOne('zlvzncvzxlckvnzxcvlzxkcvn')
    assert not app.SolutionTwo('zlvzncvzxlckvnzxcvlzxkcvn')
    assert not app.SolutionThree('zlvzncvzxlckvnzxcvlzxkcvn')

    # Input 5
    assert app.SolutionOne('jkzcvnadewix')
    assert app.SolutionTwo('jkzcvnadewix')
    assert app.SolutionThree('jkzcvnadewix')
