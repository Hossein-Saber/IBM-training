from requests_html import HTMLSession
import re
from string import ascii_uppercase

def find_position(alphabet):
    return list(ascii_uppercase).index(alphabet)

def find_alphabet(Position):
    return list(ascii_uppercase)[Position]


s = HTMLSession()

resp = s.get('https://www.codal.ir/Reports/Decision.aspx?LetterSerial=nC4VEynq97ytoeGUQx30dw%3d%3d&rt=0&let=58&ct=0&ft=-1')

text = resp.html.find('script')[5].text
print(text)