import requests
from bs4 import BeautifulSoup


class Data(object):
    def __init__(self):
        self.d = {
            'chaos': '4',
            'exalt': '6',
            'c': '4',
            'ex': '6'
        }

    def load(self):
        #TODO:
        # load database from file
        pass

class Monitor(object):
    def __init__(self):
        db = Data()
        self.data = db.d

    def search(self, a, b, league='Incursion'):
        if a not in self.data or b not in self.data:
            raise KeyError
        url = 'http://currency.poe.trade/search?league='+league+'&online=x&want='+self.data[a]+'&have='+self.data[b]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="html5lib")
        results = [x["data-ign"] for x in soup.find_all("div", class_='displayoffer')]
        return results


if __name__=="__main__":
    m = Monitor()
    res = m.search('c', 'ex')
    print(res)
