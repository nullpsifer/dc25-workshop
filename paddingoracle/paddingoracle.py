import requests

class PaddingOracle:

    def __init__(self,url):
        self.url = url

    def check(self,ciphertext):
        response = requests.get(self.url,{'ctext':ciphertext})
        if response.status_code == 200 or response.status_code == 404:
            return True
        elif response.status_code == 403:
            return False
