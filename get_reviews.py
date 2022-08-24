import pandas as pd

import requests

from bs4 import BeautifulSoup as bsp


def scrap_product_amazon_reviews_bsp(id_product):
    url='https://www.amazon.com/product-reviews/'+id_product+'/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
        
    response = requests.get('http://localhost:8050/render.html',params={'url':url,'wait':2})
    
    soup = bsp(response.text,'html.parser')
    
    reviews = soup.find_all('div',{'data-hook':'review'})
    
    r=[]
    
    if response.status_code == 200:
        
        for item in reviews :
                
            review={}
     
            review['title'] = item.find('a',{'data-hook':'review-title'}).text.strip().split('\n')    
             
            review['profils_review'] = item.find('span',class_="a-profile-name").text.split('\n')
               
            review['stars'] = item.find('i',{'data-hook':'review-star-rating'}).text.split('\n')
                
            review['body_reviews'] = item.find('span',{'data-hook':'review-body'}).text.split('\n')
                    
            review['dates'] = item.find('span',{'data-hook':'review-date'}).text.strip('Reviewed in').split('\n')
                
                
            r.append(review)
                
     
            df = pd.DataFrame(r,columns=['title','dates','profils_review','stars','body_reviews'])
        
        return df 
        
                
    else:
        return "failed"
    


print(scrap_product_amazon_reviews_bsp('B06XZTZ7GB'))