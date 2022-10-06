from time import sleep
from threading import Thread

def extract_data_from_website(site):
    """open a website and extract data"""

    print(f"We are navigate at: {site}")

    for i in range(1, 40):
        print(f"Processing data - {i}/40")
        sleep(2)
    
    print(f'Data extract of website {site} finished!')


def download_files():
    """download the files that find on website"""
    for i in range(1, 60):
        print(f"Downloading file - {i}/60")
        sleep(2)
    
    print(f'Downloaded 60 files successully!')

new_thread = Thread(
        target=extract_data_from_website, 
        args=('https://github.com/Antonio-Gabriel',), 
        daemon=True # specify if the thread runs in first or second plain
    )

new_thread.start()
download_files()
new_thread.join()
