# Extract Sub-Domain + Domain from URL

```
=SUBSTITUTE(REPLACE(REPLACE(A2; 1; IFERROR(FIND("//"; A2)+1; 0); "")&"/"; FIND("/"; REPLACE(A2; 1; IFERROR(FIND("//"; A2)+1; 0); "")&"/"); LEN(A2); ""); "www."; "")
```
