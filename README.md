XPath is a tool that takes a URL with a keyword and makes it to a path-base XSS payload. You can use it in every path of web app to check the vulnerability.

# Installation 
You can install this tool by following these commands:
```
git clone https://github.com/aminsec/XPath.git
cd XPath
python3 dellay.py -h
```
# Usage
There is a simple usage of this tool: 
```
python3 dellay.py -u <url> -w <a random keyword>
```
Example: 
```
python3 dellay.py -u https://example.com/account/dashboard/profile -w XSS
```
Output: 
```
https://example.com/accountXSS/dashboard/profile
https://example.com/account/dashboardXSS/profile
https://example.com/account/dashboard/profileXSS
https://example.com/account/dashboard/profile/XSS
```

Or you can use ```-f``` flag to give more than one URL. This is content of ```urls.txt``` file: 
```
https://site.com/1/2/3/
https://example.com/1/2/3/
https://google.com/1/2/3
``` 
Command: 
```
python3 dellay.py -f urls.txt -w XSS
```
Output: 
```
https://site.com/1XSS/2/3
https://site.com/1/2XSS/3
https://site.com/1/2/3XSS
https://site.com/1/2/3/XSS
https://example.com/1XSS/2/3
https://example.com/1/2XSS/3
https://example.com/1/2/3XSS
https://example.com/1/2/3/XSS
https://google.com/1XSS/2/3
https://google.com/1/2XSS/3
https://google.com/1/2/3XSS
https://google.com/1/2/3/XSS
```

Happy hacking.


