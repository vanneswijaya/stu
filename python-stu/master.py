import requests
import json
import numpy as np
import random

#per_28may_3pm
all_banks = {'bank_sell':{'Alpha': {'SGD':5.82700,
                                    'EUR':8.56320,
                                    'USD':7.91180},
                        'Beta': {'SGD':5.7770,
                                'EUR':8.5660,
                                'USD':7.8960},
                        'Gamma': {'SGD':5.81000,
                                'EUR':8.51000,
                                'USD':7.89000},
                        'Theta': {'SGD':5.78300,
                                'EUR':8.50000,
                                'USD':7.87900},
                        'Omega': {'SGD':5.78500,
                                'EUR':8.49000,
                                'USD':7.88500}},
                      
            'bank_buy':{'Alpha': {'SGD':5.65950,
                                'EUR':8.33340,
                                'USD':7.78500},
                        'Beta': {'SGD':5.6840,
                                'EUR':8.3360,
                                'USD':7.7720},
                        'Gamma': {'SGD':5.670000,
                                'EUR':8.360000,
                                'USD':7.810000},
                        'Theta': {'SGD':5.69200,
                                'EUR':8.3960,
                                'USD':7.82700},
                        'Omega': {'SGD':5.726,
                                'EUR':8.438,
                                'USD':7.840}
            }}

url_hist = "https://api.apilayer.com/exchangerates_data/timeseries?start_date=2021-04-27&end_date=2022-04-27&base=HKD&symbols=SGD,EUR,USD"
url_recom = "https://api.apilayer.com/exchangerates_data/timeseries?start_date=2022-04-27&end_date=2022-05-27&base=HKD&symbols=SGD,EUR,USD"

payload = {}
headers= {
  "apikey": "U6ySk29cNFc6m9Gg239lmUOB84kxYGUr"
}

response_hist = requests.request("GET", url_hist, headers=headers, data = payload)
status_code = response_hist.status_code
result_hist = json.loads(response_hist.text)

response_recom = requests.request("GET", url_recom, headers=headers, data = payload)
status_code = response_recom.status_code
result_recom = json.loads(response_recom.text)

class Convert:

    def __init__(self, currency, amount_hkd, amount_forex):

        self.currency = currency
        self.amount_hkd = amount_hkd
        self.amount_forex = amount_forex

    def find_min_rate(self):

        banks_pricelist = []
    
        if self.amount_forex == 0:

            for x in all_banks['bank_sell']:
                banks_pricelist.append(all_banks['bank_sell'][x][self.currency])

            index_min = min(range(len(banks_pricelist)), key=banks_pricelist.__getitem__)

            banks = []
            for x in all_banks['bank_sell']:
                banks.append(x)
        
        if self.amount_hkd == 0:

            for x in all_banks['bank_buy']:
                banks_pricelist.append(all_banks['bank_buy'][x][self.currency])

            index_min = min(range(len(banks_pricelist)), key=banks_pricelist.__getitem__)

            banks = []
            for x in all_banks['bank_buy']:
                banks.append(x)
        
        return banks_pricelist, banks[index_min]

    def count_output(self):
        rate = min(self.find_min_rate()[0])

        if self.amount_forex == 0:
            amount = self.amount_hkd / rate
        
        if self.amount_hkd == 0:
            amount = self.amount_forex * rate

        return amount
    
    def output_dict(self):
        output_amount = self.count_output()
        min_price = min(self.find_min_rate()[0])
        min_bank = self.find_min_rate()[1]


        if self.amount_forex == 0:
            # print(f'{output_amount} {self.currency}, {min_price}, {min_bank}')
            histories = []
    
            for date in result_hist['rates']:
                rate_hist = 1 / result_hist['rates'][date][self.currency]
                histories.append(rate_hist)
            margin = 2*np.std(histories)
            min_price = min(self.find_min_rate()[0])
            # recom_price = min_price - margin
            recom_price = float('{:.3f}'.format(min_price - margin))

            instant_dict = {'from': 'HKD',
                            'from_amt': self.amount_hkd,
                            'to': f'{self.currency}',
                            'to_amt': output_amount,
                            'rate_per_hkd': min_price,
                            'bank': f'{min_bank}',
                            'recom_price': recom_price}
        
        if self.amount_hkd == 0:
            # print(f'{output_amount} HKD, {min_price}, {min_bank}')

            instant_dict = {'from': f'{self.currency}',
                            'from_amt': self.amount_forex,
                            'to': 'HKD',
                            'to_amt': output_amount,
                            'rate_per_hkd': min_price,
                            'bank': f'{min_bank}' }
        
        return instant_dict

    # def recommend_target_price(self):

    #     histories = []
        
    #     for date in result_hist['rates']:
    #         rate_hist = 1 / result_hist['rates'][date][self.currency]
    #         histories.append(rate_hist)

    #     margin = 2*np.std(histories)
    #     min_price = min(self.find_min_rate()[0])
    #     recom_price = min_price - margin
    #     # print(recom_price)
    #     return recom_price
            
    def compare_real_price(self): #bank sell from HKD to forex

        base_price = []

        for date in result_recom['rates']:
            per_base = 1 / result_recom['rates'][date][self.currency]
            base_price.append(per_base)
        
        # print(base_price)

        banks = ['Alpha', 'Beta', 'Gamma', 'Theta', 'Omega']
        real_prices = []

        random_lower_bound = min(self.find_min_rate()[0])-base_price[0]
        random_upper_bound = max(self.find_min_rate()[0])-base_price[0]

        # print(random_lower_bound, random_upper_bound)

        for bank in banks:

            real_bank_price = []

            for rate in base_price:
                daily_price = rate + random.uniform(random_lower_bound, random_upper_bound)
                real_bank_price.append(daily_price)

            real_prices.append(real_bank_price)

        # print(real_prices)

        monthly_prices_allbanks = []
       
        index = 0
        
        for i in range(len(real_prices[0])):
     
            monthly_prices_allbanks.append([])
    
            for j in range(len(real_prices)):
               
                monthly_prices_allbanks[index].append(real_prices[j][index])
  
            index += 1
       
        # print(monthly_prices_allbanks)
        lowest_price_allbanks = {}

        for idx, price_date in enumerate(monthly_prices_allbanks):
            index_min_bank = min(range(len(price_date)), key=price_date.__getitem__)
            lowest_price_allbanks[idx] = [banks[index_min_bank], min(price_date)]

        return lowest_price_allbanks

    def cashback(self, input_tp):
        
        input_target_price = input_tp

        lowest_price_allbanks = self.compare_real_price()
        # print(lowest_price_allbanks)
        for day in lowest_price_allbanks:
            if lowest_price_allbanks[day][1] < input_target_price:
                
                cashback_rate = lowest_price_allbanks[day][1]
                cashback_bank = lowest_price_allbanks[day][0]
               
                # print(f'Execute Cashback at {date}')
                break
        
        cashback_amount = self.amount_hkd / cashback_rate

        cashback_dict = {'days': day,
                         'cashback_amt': cashback_amount,
                         'cashback_rate': cashback_rate,
                         'cashback_bank': cashback_bank }

        # print(f'on day {day}, receive {cashback_amount} HKD, at 1 {self.currency} = {cashback_rate} HKD, from Bank {cashback_bank}')

        return cashback_dict


        # for idx, price in enumerate(lowest_price_allbanks):
        #     if price < input_target_price:
        #         print(f'Execute Cashback at day {idx}')
        #         break

    # def execute_buy(self):

    #     planned_target_price = 5.70

    #     lowest_price_allbanks = self.compare_real_price()

    #     for idx, price in enumerate(lowest_price_allbanks):
    #         if price < planned_target_price:
    #             print(f'Execute Planned Buy at day {idx}')
    #             break