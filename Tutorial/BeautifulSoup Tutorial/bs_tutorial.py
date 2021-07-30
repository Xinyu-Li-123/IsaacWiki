# use lxml parser
"""
Module used: BeautifulSoup, requests, lxml

Tips:
1/ Try to avoid sending too much request too fast,
        o/w it will break others' websites.

2/ Look for user API first when scrapping big websites like YouTube,
        if they have one, they would prefer you using API to scrape info instead.
"""


from bs4 import BeautifulSoup
import requests
import csv
# use csv module to deal with csv file

def tutorial_1():
    with open('simple.html') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

    # print(soup.prettify())

    ''' Find content in html '''
    match = soup.title.text          # access an element of simple.html to get its content
    # print(match)

    article = soup.find('div', class_='article')
    print(article.text)

    for article in soup.find_all('div', class_='article'):
        headline = article.h2.a.text
        print(headline)
        summary = article.p.text
        print(summary)

def tutorial_2():
    # get all info from website
    source = requests.get('http://coreyms.com').text
    # request.get() returns a response object

    soup = BeautifulSoup(source, 'lxml')
    # parse the html text using lxml parser
    # print(soup.prettify())

    csv_file = open('cms_scrape.csv', 'w')
    # create a csv file

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'video_link'])
    # set up column / header name

    csv_writer = csv.writer(csv_file)


    # scrap info from website

    for article in soup.find_all('article'):

        headline = article.h2.a.text
        print(headline)

        summary = article.find('div', class_='entry-content').p.text
        print(summary)
        try:
            # access attributes using dict grammar
            vid_src = article.find('iframe', class_='youtube-player')['src']

            # parse youtube video id from the url
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            # ? in the link indicates the start of a query

            # create a youtube link using vid_id
            yt_link = f"https://youtube.com/watch?v={vid_id}"
            print(yt_link)
        except Exception as e:
            yt_link = None
            print(yt_link)
            print(f"(Error: {e})")

        print()

        # write info into csv file
        csv_writer.writerow([headline, summary, yt_link])

    csv_file.close()

        # save info into a csv file


tutorial_2()