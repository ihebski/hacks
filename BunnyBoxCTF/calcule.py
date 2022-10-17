#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# some settings
TCP_IP = '92.222.90.84'
TCP_PORT = 5003
BUFFER_SIZE = 1024


def parse(data):
    """Parse the numbers and the operation to perform from the raw data received"""
    numbers = [int(n) for n in data[0].split()]
    op = data[1].split(" ")[3]
    print data
    return numbers, op


def get_data(s):
    """Get all the raw data (it can be longer than BUFFER_SIZE, so we need to loop)"""
    data = ''
    try:
        while 'numbers' not in data:  # try to guess the end of the data
            tmp = s.recv(BUFFER_SIZE)

            if tmp == '':  # no more data and still in the while, we got the flag \o/
                print data
                exit(0)

            data += tmp
    except socket.timeout:
        print 'You have a shitty connection.'
        exit(1)
    return data.split('\n')


def main():
    # connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.settimeout(1)

    while True:
        data = get_data(s)
        numbers, action = parse(data)
        print numbers

        print '%s of %d numbers' % (action, len(numbers))

        if action == 'min':
            ret = min(numbers)
        elif action == 'max':
            ret = max(numbers)
        elif action == 'sum':
            ret = sum(numbers)
        elif action == 'avg':
            ret = 1.0 * sum(numbers) / len(numbers)
        else:
            print 'No operation found.'
            exit(1)

        s.send(str(ret)+'\n')


if __name__ == '__main__':
    main()