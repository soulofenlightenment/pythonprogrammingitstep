import socket
import requests
from concurrent.futures import ThreadPoolExecutor
import csv
import time
from os import chdir
chdir('exercise_18/homework 21')

urls = list()

with open('domains.csv') as f:
    reader = csv.reader(f)
    for url in reader:
        urls.append(url[1])

def fetch_data(url):
    try:
        start = time.perf_counter()
        requests.get('https://' + url, timeout = 5)
        final = time.perf_counter()
        response_time = round(final - start,3)
        try:
            ip = socket.gethostbyname('www.' + url)
        except socket.gaierror:
            response_time = 'N/A'
            ip = 'N/A'
            return [url,response_time,ip]
        return [url,response_time,ip]
    except requests.exceptions.RequestException:
        response_time = 'N/A'
        ip = 'N/A'
        return [url,response_time,ip]

with ThreadPoolExecutor(max_workers = 50) as th:
    data = list(th.map(fetch_data,urls))

with open('results.csv','w') as f:
    writer = csv.writer(f,delimiter = ',')
    headers = ['domain','response_time','ip_address']
    writer.writerow(headers)
    writer.writerows(data)




