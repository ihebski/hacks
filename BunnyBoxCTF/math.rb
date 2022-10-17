#!/usr/bin/ruby
require 'socket'
hostname = '195.154.53.62'
port = 1337
s = TCPSocket.open(hostname, port)
raw = ''
res = nil
flag = false
while line = s.gets   # Read lines from the socket
    puts line.chop    # And print with platform line terminator
    raw += line
    if raw.match(/=$/) && flag == false
        calc = raw.match(/^([0-9]*) ([+\-%*\/]) ([0-9]*) =/)
        a = calc.captures[0].to_i
        oper = calc.captures[1]
        b = calc.captures[2].to_i
        if oper == '+'
            res = a + b
        elsif oper == '-'
            res = a - b
        elsif oper == '*'
            res = a * b
        elsif oper == '%'
            res = a % b
        elsif oper == '/'
            res = a / b
        else
            puts "That's not good..."
        end
        if res != nil
            puts res
            s.puts res
        end
        res = nil
        raw = ''
    end
end
s.close   