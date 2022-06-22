
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from create_html import create_html


def main():

    keyword = str(input('What are you searching for? '))
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(get_url(keyword))

    soup = BeautifulSoup(driver.page_source,'lxml')
    blocks = soup.findAll('div', {'data-component-type': 's-search-result'})

    products = []
    for item in blocks:
        if item.find('span', 'a-price'):
            product = {}
            atag = item.h2.a
            product['Name'] = atag.text.strip()
            product['Url'] = 'https://www.amazon.es/' + atag.get('href')
            price_parent = item.find('span', 'a-price')
            product['Price'] = float(price_parent.find('span', 'a-price-whole').text.replace('.','').replace(',','.'))
            product['Img'] = item.find('img', class_='s-image').get('src')
            products.append(product)

    products = sort(products)

    create_html(products)

    print('Done! Look at results.html for results')


def get_url(keyword):
    template = 'https://www.amazon.es/s?k={}&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'
    keyword = keyword.replace(' ', '+')
    return template.format(keyword)

def sort(array):
    for i in range(len(array)- 1):
        for j in range(len(array) - i - 1):
            if array[j]['Price'] > array[j+1]['Price']:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff

    return array


if __name__ == '__main__':
    main()