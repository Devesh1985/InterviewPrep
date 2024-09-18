dct = {'Sachin Tendulkar': '54', 'Rahul Dravid': '53', 'Sunil Gavaskar': '51', 'Virat Kohli': '49', 'VVS Laxman': '46', 'Virender Sehwag': '49',
       'Sourav Ganguly': '42', 'Cheteshwar Pujara': '44', 'Dilip Vengsarkar': '42', 'Mohammad Azharuddin': '45', 'Gundappa Viswanath': '42', 'Kapil Dev': '31',
       'Ajinkya Rahane': '38', 'MS Dhoni': '38', 'Mohinder Amarnath': '43', 'Gautam Gambhir': '42', 'Rohit Sharma': '45', 'Murali Vijay': '38', 'Ravi Shastri': '36', 'Polly Umrigar': '42'}


ss ={}
for player, score in dct.items():
    if dct[player] not in ss:
        ss[score]= [player]
    else:
        ss[score].append(player)

for score,player in ss.items():
    if len(player) >1:
        print(f"score {score} player {",".join(player)}")
