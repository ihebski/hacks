# LaZyGenerat0r
lazy gen is python script that generate wordlist based on companies name,used basically for WPA/WPA2 bruteforcing attack.

# Raison to write such a script

During a long wireless pentesting exercise for multiple companies, I have noticed that the available wordlists are always failed against the customized passwords set by the company, In the most cases, passphrase includes the company name, date and sometimes symbol.What if we generate a list that includes all of that.

# How it works

Easy and nothing special :p <br />
possible generated strings <br />

lowercase+date<br />
lowercase+symble+date<br />
lowercase+date+symble<br />

uppercase+date<br />
uppercase+symble+date<br />
uppercase+date+symble<br />

## Exemple

company2014<br />
company$2014<br />
compay2014$<br />

COMPANY2014<br />
COMPANY2014<br />
COMPANY$2014<br />
COMPANY2014$<br />

Company2014 <br />
Company$2014<br />
Compay2014$<br />

# Contribute
I know its an ugly code ,work still in progress to add more and more cases ,fork and us to create a good wordlist generator