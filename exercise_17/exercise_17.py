from os import chdir
import requests
import time
import json
from concurrent.futures import ThreadPoolExecutor
chdir('exercise_17')
start = time.perf_counter()
urls =  [f"https://jsonplaceholder.typicode.com/photos/{i}" for i in range(1,5001)]
def fetch(url):
    response = requests.get(url)
    return response.json()
with ThreadPoolExecutor(max_workers=50) as exe:
    fetched_data = list(exe.map(fetch,urls))

with open('photos.json', 'w') as f:
    json.dump(fetched_data,f, indent=5)
end = time.perf_counter()
final = end - start
print(f'code execution time is: {round(final)}s')
