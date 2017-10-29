import app


def test_check_permutation():
    # Input 1
    assert app.SolutionOne('abcd', 'bacd')
    assert app.SolutionTwo('abcd', 'bacd')
    assert app.SolutionThree('abcd', 'bacd')

    # Input 2
    assert app.SolutionOne('3563476', '7334566')
    assert app.SolutionTwo('3563476', '7334566')
    assert app.SolutionThree('3563476', '7334566')

    # Input 3
    assert app.SolutionOne('wef34f', 'wffe34')
    assert app.SolutionTwo('wef34f', 'wffe34')
    assert app.SolutionThree('wef34f', 'wffe34')

    # Input 4
    assert not app.SolutionOne('abcd', 'd2cba')
    assert not app.SolutionTwo('abcd', 'd2cba')
    assert not app.SolutionThree('abcd', 'd2cba')

    # Input 5
    assert not app.SolutionOne('2354', '1234')
    assert not app.SolutionTwo('2354', '1234')
    assert not app.SolutionThree('2354', '1234')

    # Input 6
    assert not app.SolutionOne('dcw4f', 'dcw5f')
    assert not app.SolutionTwo('dcw4f', 'dcw5f')
    assert not app.SolutionThree('dcw4f', 'dcw5f')

    # Input 7
    assert not app.SolutionOne('adksdjfsl', 'akdjfalksd')
    assert not app.SolutionTwo('adksdjfsl', 'akdjfalksd')
    assert not app.SolutionThree('adksdjfsl', 'akdjfalksd')

    # Input 8
    assert not app.SolutionOne('ba', 'Ab')
    assert not app.SolutionTwo('ba', 'Ab')
    assert not app.SolutionThree('ba', 'Ab')

    # Input 9
    assert not app.SolutionOne('anne', 'annea')
    assert not app.SolutionTwo('anne', 'annea')
    assert not app.SolutionThree('anne', 'annea')

    # Input 10
    assert app.SolutionOne('IAMLORDVOLDEMORT', 'TOMMARVOLORIDDLE')
    assert app.SolutionTwo('IAMLORDVOLDEMORT', 'TOMMARVOLORIDDLE')
    assert app.SolutionThree('IAMLORDVOLDEMORT', 'TOMMARVOLORIDDLE')
