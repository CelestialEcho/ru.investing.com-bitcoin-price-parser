from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import datetime
import pytz
import time
import json
import requests

headers_randomuseragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.3; rv:112.0) Gecko/20100101 Firefox/112.0',
                            'Mozilla/5.0 (X11; Linux i686; rv:112. 0) Gecko/20100101 Firefox/112.0',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.3; rv:102.0) Gecko/20100101 Firefox/102.0',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/97.0.4719.17']
headers_randomreferer = ['https://www.yahoo.com', 'https://www.duckduckgo.com', 'https://www.google.com',
                         'https://www.bing.com']


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


random_user_agent = random.choice(headers_randomuseragents)
random_referer = random.choice(headers_randomreferer)
print(f'user-agent = {random_user_agent}\nreferer = {random_referer}')


chrome_options.add_argument(f'user-agent={random_user_agent}')
chrome_options.add_argument(f'referer={random_referer}')

driver = webdriver.Chrome(options=chrome_options)

url = 'https://ru.investing.com/crypto/currency-pairs'
main_data = {}


headers = {
    'User-Agent': random_user_agent,
    'Referer': random_referer,
}
request = requests.get(url, headers=headers)
request = str(request)
request = request.replace('<Response [', '').replace(']>', '')

if request == '200':
    print('Successful! (Response 200)')
elif request == '404':
    print("Can't connect to website! (Response 404)")
else:
    print(f"Response code: {request} wasn't expected!")

time.sleep(random.uniform(31, 67))


def __bitcoin__():
    driver.get(url)
    time.sleep(random.uniform(1, 30))
    bitcoin = driver.find_element('css selector', 'td.pid-1057391-last')
    print(f'Bitcoin price (USD): {bitcoin.text}')
    time_sleep = random.uniform(1, 30)
    time.sleep(time_sleep)
    bitcoin = str(bitcoin.text)
    bitcoin = bitcoin.replace('.', '').replace(',', '.')
    if bitcoin == '':
        return None
    else:
        currency = float(bitcoin)
        return currency


def add_dict(n1):
    us_tz = pytz.timezone('America/New_York')
    usa_current_time = datetime.datetime.now(us_tz)
    formatted_time = usa_current_time.strftime('%Y/%m/%d | %H:%M')
    main_data[formatted_time] = n1

    return main_data


while True:
    n = __bitcoin__()
    answer = add_dict(n)
    print(f'Added to dictionary:\n{answer}')
    with open("prices.json", 'w') as json_file:
        json.dump(main_data, json_file)
    time.sleep(random.uniform(60, 120))

