# -*- encoding: utf-8 -*-

import json
from glob import glob

from passangers import process

error_message = 'ERROR in file {}. Expected: "{}", got: "{}"'


def run_tests():
    i=0
    for filename in glob('tests/*.json'):
        i=i+1
        data = json.load(open(filename))
        trains, events, result = data['trains'], data['events'], data['result']
        print('test №', i, '\n', trains, '\n', events)
        got = process(trains, events, result['car'])
        expected = result['amount']
        print("expected: ",result)
        print(trains)
        if got != expected:
            print(error_message.format(filename, expected, got))
            return
    print("All tests passed!")


if __name__ == '__main__':
    run_tests()
