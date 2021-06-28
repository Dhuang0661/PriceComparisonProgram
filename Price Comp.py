from bs4 import BeautifulSoup
import requests
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'}


ebay=''
amazon=''


def ebay(name):
    try:
        global ebay
        name1 = name.replace(" ","+")
        ebay=f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={name1}&_sacat=0'
        res = requests.get(ebay,headers=headers)
        print("\nSearching in ebay.....")
        soup = BeautifulSoup(res.text,'html.parser')
        length = soup.select('.s-item__price')
        ebayPageLength=int(len(length))
        for i in range (0,ebayPageLength):
            info = soup.select('.SECONDARY_INFO')[i].getText().strip()
            info = info.upper()
            if info=='BRAND NEW':
                ebayProduct = soup.select('.s-item__title')[i].getText().strip()
                name=name.upper()
                ebayProduct=ebayProduct.upper()
                if name in ebayProduct[:25]:
                    ebayPrice = soup.select('.s-item__price')[i].getText().strip()
                    ebayProduct = soup.select('.s-item__title')[i].getText().strip()
                    print("Ebay:")
                    print(ebayProduct)
                    print(ebayPrice)
                    print(info)
                    print("_______________________")
                    ebayPrice=ebayPrice[0:14]
                    break
                else:
                    i+=1
                    i=int(i)
                    if i==ebayPageLength:
                        print("Ebay: No product Found!")
                        print("_______________________")
                        ebayPrice = '0'
                        break

        return ebayPrice
    except:
        print("Ebay: No product Found!")
        print("_______________________")
        ebayPrice = '0'
    return ebayPrice


def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ","+")
        amazon=f'https://www.amazon.com/s?k={name1}'
        res = requests.get(amazon,headers=headers)
        print("\nSearching in amazon:")
        soup = BeautifulSoup(res.text,'html.parser')
        amazonPage = soup.select('.a-color-base.a-text-normal')
        amazonPageLength = int(len(amazonPage))
        for i in range(0,amazonPageLength):
            name = name.upper()
            amazonProduct = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            amazonProduct=amazonProduct.upper()
            if name in amazonProduct[0:20]:
                amazonProduct = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazonPrice = soup.select('.a-price-whole')[i].getText().strip().upper()
                print("Amazon:")
                print(amazonProduct)
                print("$"+amazonPrice)
                print("_______________________")
                break
            else:
                i+=1
                i=int(i)
                if i==amazonPageLength:
                    print("amazon : No product found!")
                    print("_______________________")
                    amazonPrice = '0'
                    break
        return amazonPrice
    except:
        print("amazon: No product found!")
        print("____________________")
        amazonPrice = '0'
    return amazonPrice


name=input("product name:\n")
ebayPrice=ebay(name)

amazonPrice=amazon(name)

print("__________________________________")
if ebayPrice== '0':
    print("Ebay: No Product found!")
else:
    print("Ebay price: $",ebayPrice)

if amazonPrice=='0':
    print("Amazon: No Product found!")
else:
    print("\namazon price: $",amazonPrice)
   
print("__________________________________")
time.sleep(2)




print("\nUrls:\n")
print("________________________________________________________________________")
print(ebay)
print(amazon)
print("________________________________________________________________________")
