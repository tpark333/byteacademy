
def currency_exchange():
    with open('currency.txt', 'r') as file_obj:
        # Create Dictionary
        exchange_list = []
        exchange_dict = {}
        for line in file_obj:
            new_line = line.split()
            line_split = [i.split(' ',1)[0] for i in new_line]
        #new_line2 = line_split.replace('/n','')
            exchange_list.append(line_split)
        for currency_value in exchange_list:
            exchange_dict['symbol']=currency_value[0]
            exchange_dict['rate'] = float(currency_value[1])
                
    return exchange_dict

print(currency_exchange())