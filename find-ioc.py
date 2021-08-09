from ioc_finder import find_iocs

tweet = "Making sense of #PrintNightmare. A flowchart to help understand exploitation of CVE-2021-34527.  https://twitter.com/StanHacked/status/1410922404252168196"
iocs = find_iocs(tweet)
for indicator,value in iocs.items():
    print(f'{indicator} -> {value}')
