import requests
from bs4 import BeautifulSoup
from fractions import Fraction


class Data(object):
    def __init__(self):
        self.d = {
            'alt': '1',
            'fusing': '2',
            'alchemy': '3',
            'chaos': '4',
            'gcp': '5',
            'exalt': '6',
            'chrome': '7',
            'jeweler': '8',
            'Orb of Chance': '9',
            'chisel': '10',
            'Orb of Scouring':'11',
            'Blessed Orb': '12',
            'regret':'13',
            'regal': '14',
            'divine orb': '15',
            'vaal orb': '16',
            'Orb of Transmutation': '22',
            'Orb of Augmentation': '23',
            'Silver Coin': '35'
            # ,'Apprentice Cartographers Sextant': '45'
            # ,'Journeyman Cartographers Sextant': '46'
            # ,'Master Cartographers Sextant': '47'
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
        attr = ['data-ign', 'data-sellvalue', 'data-buyvalue']
        if a not in self.data or b not in self.data:
            raise KeyError
        url = 'http://currency.poe.trade/search?league='+league+'&online=x&want='+self.data[a]+'&have='+self.data[b]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="html5lib")
        results = [(eval(x[attr[1]]+'/'+x[attr[2]]),"@" + x[attr[0]] + " Hi, I'd like to buy your "
                    + str(int(eval(x[attr[1]]))) + " " + a + " for my "
                    + str(int(eval(x[attr[2]]))) + " " + b + " in Incursion.")
                   for x in soup.find_all("div", class_='displayoffer')]
        return results

    def find_profit(self, c='chaos', rate=1.0, num=5):
        for i in self.data:
            if self.data[i]!=self.data[c]:
                buy = self.search(c, i)[:num]
                sell = self.search(i, c)[:num]
                if buy[0][0]*sell[0][0]>rate:
                    for j in range(num):
                        for k in range(num):
                            if buy[j][0]*sell[k][0]>rate:
                                print(Fraction(buy[j][0]*sell[k][0]).limit_denominator(), buy[j][0]*sell[k][0])
                                print(buy[j][1])
                                print(sell[k][1])


if __name__=="__main__":
    m = Monitor()
    m.find_profit(rate=1.03)
