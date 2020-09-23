## Finger
Fingerprint port services after the naabu port scan.

Service list extracted from https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=1

## Usage
one liner style 
~~~bash
$ cat targets | naabu | python3 finger.py
$ echo 127.0.0.1:443 | python3 finger.py
~~~
