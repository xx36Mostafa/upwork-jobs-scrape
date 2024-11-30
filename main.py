import tls_client , sqlite3
from bs4 import BeautifulSoup

def insert_data(data):
    for key, value in data.items():
        link, tittle, date, price, description = value['link'], value['tittle'], value['date'], value['price'], value['description']
        
        cr.execute("SELECT 1 FROM articles WHERE link = ?", (link,))
        if cr.fetchone():
            print(f"[!] Link already exists, skipping: {link}")
            continue
        
        cr.execute("SELECT IFNULL(MAX(id), 0) + 1 FROM articles")
        new_id = cr.fetchone()[0]
        
        cr.execute(
            "INSERT INTO articles (id, date, tittle, price, description, link) VALUES (?, ?, ?, ?, ?, ?)",
            (new_id, date, tittle, price, description, link)
        )
    
        print('[+] Success Insert Articles In DataBase..')
    db.commit()

def scrape(topic):
    index = 1
    for i in range(1,13):
        URL = f'https://www.upwork.com/nx/search/jobs/?nbs=1&q={topic}&page={i}'
        headers = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language':'en-US,en;q=0.7',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }
        response = session.get(URL,headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            jobss = soup.find('section',{'data-ev-sublocation':'search_results'})
            for job in jobss:
                try:
                    x = str(job).strip()
                    if 'class' not in x: continue
                    published_date = job.find('small',{'data-test':'job-pubilshed-date'}).text
                    published_date = str(published_date).replace('Posted','').strip()

                    job_header = job.find('div',{'class':'air3-line-clamp is-clamped'})
                    job_link = 'https://www.upwork.com' + job_header.find('a',{'class':'up-n-link'})['href'] # https://www.upwork.com
                    job_tittle = job_header.find('a',{'class':'up-n-link'}).text
                    job_tile = job.find('ul', {'class':'job-tile-info-list text-base-sm mb-4'})
                    job_price_element = job_tile.find('li',{'data-test':'is-fixed-price'})

                    if job_price_element:
                        job_price = job_price_element.find_all('strong')[1].text.strip()

                    else:
                        job_element = job_tile.find('li',{'data-test':'job-type-label'})
                        job_price = job_element.find_all('strong')[0].text.strip()
                    JobDescription_element = job.find('div',{'class':'air3-line-clamp-wrapper clamp mb-3'})
                    job_description = JobDescription_element.find('p').text.strip()
                    jobs[index] = {'link':job_link,
                            'tittle':job_tittle,
                            'date':published_date,
                            'price':job_price,
                            'description':job_description}
                    index += 1
                except:
                    pass
        else:
            print('[!] Error To Bypass Security...')
            return 0
    print(jobs)
    insert_data(jobs)

if __name__ == '__main__':
    db = sqlite3.connect('jobs.db')
    cr = db.cursor()
    db.execute("CREATE TABLE if not exists articles (id integer,date TEXT, tittle TEXT, price TEXT, description TEXT, link TEXT)")
    jobs = {}
    topic = 'data scraping'
    session = tls_client.Session(client_identifier="chrome_118", random_tls_extension_order=True)
    scrape(topic)