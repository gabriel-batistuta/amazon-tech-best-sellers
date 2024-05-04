import json
from tqdm import tqdm
import pandas as pd
import scraping as spider
from time import time

if __name__ == '__main__':
    URL = 'https://www.amazon.com.br/gp/bestsellers/computers/'
    
    start_time = time()
    spider.parse_page(URL)

    end_time = time()
    duration = (end_time - start_time) / 60
    print("Tempo decorrido: ", duration, "minutos")