OK_FORMAT = True

test = {   'name': 'q5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib\n'
                                               '>>> x = hashlib.md5(str(48.75).encode()).hexdigest()\n'
                                               '>>> y = hashlib.md5(str(distance).encode()).hexdigest()\n'
                                               ">>> assert y == 'a7adb68bf3f2bcd697239e335dc8f6c5', 'Hint: Check if your answer makes sense in context. What are the units of your velocity and "
                                               "time?'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
