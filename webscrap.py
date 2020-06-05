import requests as rq
from bs4 import BeautifulSoup as soup
import csv
site_url="https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"

filename="laptop_product.csv"
f=open(filename,"w")
headers="Product_Name, Processor, RAM, OS, HDD, Display, Warrenty, Pricing, Ratings\n"
f.write(headers)

for i in range(1,11):
    site_url=site_url.format(i)
    site_html=rq.get(site_url).text
    html_content=soup(site_html,"lxml")

    containers=(html_content.findAll("div",{"class":"_1UoZlX"}))



    for container in containers:
        title=(container.findAll("div",{"class":"_3wU53n"})[0].text)
        
        con=(container.findAll("ul",{"class":"vFw0gD"})[0])
        features=[]
        for i in con:
            features.append((i.text))

        price=(container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})[0].text.strip())
        try:
            rating=(container.findAll("div",{"class":"hGSR34"})[0].text)
        except:
            rating="0"
        print(title.replace(",","|") + "," + features[0].replace(",","|") + "," + features[1].replace(",","|") + "," + features[2].replace(",","|") + "," + features[3].replace(",","|") + "," + features[4].replace(",","|") + "," + features[5].replace(",","|") + "," +  price.replace(",","") + "," + rating +"\n")
        f.write(title.replace(",","|") + "," + features[0].replace(",","|") + "," + features[1].replace(",","|") + "," + features[2].replace(",","|") + "," + features[3].replace(",","|") + "," + features[4].replace(",","|") + "," + features[5].replace(",","|") + "," +  price.replace(",","") + "," + rating +"\n")
f.close()
