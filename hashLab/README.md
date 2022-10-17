# hashLab
Fast tiny tool for CTFs
### Usage
Exemple / Encode
```
python hashLab.py -e md5 -w "text"
```
Exemple / DEcode
```
python hashLab.py -d bin -w 11001110
```

Exemple / Reverse Text
```
python hashLab.py -r FLAG
```
### Supports
* Encode hash md5,sha1,sha224,sha256,sha384,sha512,base64,bin,hex
* Decode base64 ,bin ,hex , cesar
* Reverse text / option : -r