# are_we_vulnerable

Checking the recently disclosed vulnerabilities over the network.

  - BIG-IPF5_CVE(2020-5902) - https://github.com/yasserjanah/CVE-2020-5902
  - Citrix Application Delivery Controller and Citrix Gateway(CVE-2019-19781) - https://github.com/mpgn/CVE-2019-19781
  - Cisco Adaptive Security Appliance and Firepower Threat Defense (CVE-2020-3452) - https://raw.githubusercontent.com/RootUp/PersonalStuff/master/http-vuln-cve2020-3452.nse

## Usage

~~~
$ echo "host1 host2 host3" | ./scanner
~~~

Reading an input from a file

~~~
$ cat myservers.txt | ./scanner
~~~
