'''
Web Scrapping tool to compare 
products from different ecommerce websites.
'''

# import module
import os
import eel
import requests
from bs4 import BeautifulSoup

# current file path
path = os.getcwd()

# initialize eel
eel.init(path)

# Web Scrapping Ecommerce sites

# scraping flipkart data


@eel.expose
def get_flipkart(item):
    url = f"https://www.flipkart.com/search?q={item}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        # image
        product_img = soup.find_all('img', class_="_396cs4 _3exPp9")
        # name -> View -> 4 items in 1 row
        product_name = soup.find_all('a', class_="s1Q9rs")
        # name -> View -> 1 items in 1 row
        product_name_1 = soup.find_all('div', class_="_4rR01T")
        # description
        product_desc = soup.find_all('div', class_="_3Djpdu")
        # rating
        product_rating = soup.find_all('div', class_="_3LWZlK")
        # price -> View -> 4 items in 1 row
        product_price = soup.find_all('div', class_="_30jeq3")
        # price -> View -> 1 items in 1 row
        product_price_1 = soup.find_all('div', class_="_30jeq3 _1_WHN1")
        # all product storing lists
        list1 = []  # img
        list2 = []  # name
        list3 = []  # desc
        list4 = []  # rating
        list5 = []  # price
        # checking for passing data into js
        # View -> 4 in 1 row
        if len(product_name) != 0 and len(product_price) != 0:
            # image
            for img in product_img:
                list1.append(img['src'])
            # name
            for name in product_name:
                list2.append(name.text)
            # description
            for desc in product_desc:
                list3.append(desc.text)
            # rating
            for rating in product_rating:
                list4.append(rating.text)
            # price
            for price in product_price:
                list5.append(price.text)
            # all info dictionary
            product = {'img': list1, 'name': list2,
                       'desc': list3, 'rating': list4, 'price': list5}
            return product
        # View -> 1 in 1 row
        elif len(product_name_1) != 0 and len(product_price_1) != 0:
            # image
            for img in product_img:
                list1.append(img['src'])
            # name
            for name in product_name:
                list2.append(name.text)
            # description
            for desc in product_desc:
                list3.append(desc.text)
            # rating
            for rating in product_rating:
                list4.append(rating.text)
            # price
            for price in product_price:
                list5.append(price.text)
            # all info dictionary
            product = {'img': list1, 'name': list2,
                       'desc': list3, 'rating': list4, 'price': list5}
            return product
    except Exception as e:
        print(e)


# Scraping Snapdeal data


@eel.expose
def get_snapdeal(item):
    # snapdeal website slug url
    url = f"https://www.snapdeal.com/search?keyword={item}&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # product image
    # product_img = soup.find_all()
    # product name
    product_name = soup.find_all("p", class_="product-title")
    # product price
    product_price = soup.find_all(
        "span", class_="lfloat product-desc-price strike")
    # product discount
    product_discount = soup.find_all(
        'div', class_="product-discount")
    print(product_discount)


# start eel
eel.start('index.html', size=(1100, 600))
