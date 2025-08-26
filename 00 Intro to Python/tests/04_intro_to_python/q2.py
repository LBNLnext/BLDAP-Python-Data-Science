OK_FORMAT = True

test = {   'name': 'q2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> for r, v in zip(radiuses, volumes):\n'
                                               "...     assert v / r ** 3 - 4 / 3 * math.pi < 1000000000.0, 'Are you sure you are using the right equation?'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
