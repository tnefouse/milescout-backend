import requests
from bs4 import BeautifulSoup

def scrape_united():
    url = "https://shopping.mileageplus.com/"
    response = requests.get(url)
    print("🔍 United HTML Response:")
    print(response.text[:1000])  # print first 1000 characters of HTML for debugging

    soup = BeautifulSoup(response.text, 'html.parser')
    offers = []

    for merchant in soup.select('.merchant'):
        name_tag = merchant.select_one('.merchant-name')
        rate_tag = merchant.select_one('.merchant-rate')
        link_tag = merchant.find('a')

        if name_tag and rate_tag and link_tag:
            name = name_tag.text.strip()
            rate_text = rate_tag.text.strip()
            domain = link_tag['href'].split('/')[-1].lower() + ".com"
            miles = rate_text.split(' ')[0] + 'x'
            offers.append({
                "store": domain,
                "miles_per_dollar": miles
            })

    return offers
