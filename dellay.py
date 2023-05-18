import argparse
from urllib.parse import unquote
from urllib.parse import urlparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-u", type=str, required=False, help="gets a single url")
parser.add_argument("-f", type=str, required=False, help="gets a file path to read urls")
parser.add_argument("-w", type=str, required=False, default="XSS",help="gets a keyword to put in url")
args = parser.parse_args()

def single():
    keyword = args.w
    #url decoding
    url = unquote(args.u)
    if (url[-1] == "/"):
        url = url.rstrip(url[-1])
    #url parsing
    url = urlparse(url)

    #getting url path
    path = url.path
    pathPart = url.path.split("/")
    pathPart.pop(0)

    loop_len = 0
    for vals in pathPart:
        print(url.scheme + "://" + url.netloc + path.replace(vals, vals + keyword, 1))
        loop_len += 1
        if loop_len == len(pathPart):
            print(url.scheme + "://" +url.netloc + url.path + "/" + keyword)

def multiple():
    #getting values
    file_path = args.f
    keyword = args.w
    #check file exist
    if os.path.isfile(file_path):
        
        f = open(file_path, "r")
        urls = f.read()
        urls = urls.split("\n")
        urls.pop(-1)
        for u in urls:
            
            url = unquote(u)
            if (url[-1] == "/"):
                url = url.rstrip(url[-1])
            #url parsing
            url = urlparse(url)

            #getting url path
            path = url.path
            pathPart = url.path.split("/")
            pathPart.pop(0)

            loop_len = 0
            for vals in pathPart:
                print(url.scheme + "://" + url.netloc + path.replace(vals, vals + keyword))
                loop_len += 1
                if loop_len == len(pathPart):
                    print(url.scheme + "://" +url.netloc + url.path + "/" + keyword)
    else:
        print("The file is not exist")

if args.u:
    single()
elif args.f:
    multiple()
else:
    exit()
