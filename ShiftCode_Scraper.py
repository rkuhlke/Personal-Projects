import csv
import bs4
import requests
import re


def Broderlands_1_Scraper():
    with open('Borderlands_Shift_Codes.csv', 'wt') as fi:
        url = 'https://mentalmars.com/game-news/borderlands-golden-keys/'
        resp = requests.get(url)
        html_text = resp.text
        soup = bs4.BeautifulSoup(html_text, features='html.parser')
        dates = soup.select('#codes')
        for date in dates:
            shift_date_text = date.getText()[37:]
            new_shift_date_text = re.sub('5 Golden Keys', '\n5 Golden Keys', shift_date_text)
            new_style = re.sub('PC/PS4/XB1', '\n\tPC/PS4/XB1', new_shift_date_text)
        writer = csv.writer(fi)
        row = (new_style,)
        writer.writerow(row)

def Borderlands_2_Scraper():
    with open('Borderlands_2_Shift_Codes.csv', 'wt') as fi:
        url = 'https://mentalmars.com/game-news/borderlands-2-golden-keys/'
        resp = requests.get(url)
        html_text = resp.text
        soup = bs4.BeautifulSoup(html_text, features='html.parser')
        dates = soup.select('#codes')
        for date in dates:
            shift_date_text = date.getText()[37:]
            new_shift_date_text = re.sub('5 Golden Keys', '\n5 Golden Keys', shift_date_text)
            Golden_Keys = re.sub('PC / Mac', '\n\tPC / Mac', new_shift_date_text)
            xbox = re.sub('Xbox 360', '\n\tXbox 360', Golden_Keys)
            xbox1 = re.sub('XB360', ' \n\tXB360', xbox)
            playstation = re.sub('PS3, PS4, PS Vita, and PSVR', '\n\tPS3, PS4, PS Vita, and PSVR', xbox1)
            playstation1 = re.sub('PS3/PS4/PS Vita/PSVR', '\n\tPS3/PS4/PS Vita/PSVR', playstation)
            Active = re.sub('\[Active', '\n\t\t[Active', playstation1)
        writer = csv.writer(fi)
        row = (Active,)
        writer.writerow(row)

def Borderlands_PreSeqaul_Scraper():
    with open('Borderlands_Pre-Sequal_Shift_Codes.csv', 'wt') as fi:
        url = 'https://mentalmars.com/game-news/bltps-golden-keys/'
        resp = requests.get(url)
        html_text = resp.text
        soup = bs4.BeautifulSoup(html_text, features='html.parser')
        dates = soup.select('#shift-codes')
        for date in dates:
            shift_date_text = date.getText()[37:]
            new_shift_date_text = re.sub('5 Golden Keys', '\n5 Golden Keys', shift_date_text)
            Golden_Keys = re.sub('PC / Mac / Linux', '\n\tPC / Mac / Linux', new_shift_date_text)
            xbox = re.sub('Xbox One or Xbox 360', '\n\tXbox One or Xbox 360', Golden_Keys)
            xbox1= re.sub('XBOne/XB360', '\n\tXBOne/XB360', xbox)
            playstation = re.sub('PlayStation 4 or PlayStation 3', '\n\tPlayStation 4 or PlayStation 3', xbox1)
            playstation1 = re.sub('PS4/PS3', '\n\tPS4/PS3', playstation)
            Active = re.sub('\[Active through', '\n\t\t[Active through', playstation1)
        writer = csv.writer(fi)
        row = (Active,)
        writer.writerow(row)

Broderlands_1_Scraper()
Borderlands_2_Scraper()
Borderlands_PreSeqaul_Scraper()