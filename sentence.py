from bs4 import BeautifulSoup
import requests
import textwrap
from termcolor import colored, cprint
from colorama import init

init()

def sentence(wordToBeLookedUp):

	result=requests.get("http://sentence.yourdictionary.com/"+wordToBeLookedUp+"?direct_search_result=yes")
	soup=BeautifulSoup(result.content,"lxml")
	soup_sentence = soup.find_all(class_ = "li_content")

	for count, element in enumerate(soup_sentence):
            if count == 4:
                break
            else:
                print("{:>4}. {}".format(count + 1,textwrap.fill(element.get_text(),100, subsequent_indent="      ")))
                cprint("      "+"."*99,"yellow")
