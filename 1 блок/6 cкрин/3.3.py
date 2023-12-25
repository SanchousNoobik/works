from collections import Counter


def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]).most_common(3))
print(count_it('21213214100002221'))
print(count_it('123456555288776655353535353441111'))
print(count_it('6565256936478455'))