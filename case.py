import pandas as pd
'''Theory: With investments of more than 100k,
the probability of startup success is higher'''
df = pd.read_csv('investments_VC.csv')
print(df.info())
print(df["status"].value_counts())
def set_total_usd(installs):
  if installs == '0':
    return 0
  if installs == " -   ":
    return 0
  return int(installs[1 : -1].replace(',', ''))
df[' funding_total_usd '] = df[' funding_total_usd '].apply(set_total_usd)
df[' funding_total_usd '] = df[' funding_total_usd '].apply(int)
more_100k = df[df[' funding_total_usd '] > 100000]['status'].value_counts()
less_100k = temp = df[df[' funding_total_usd '] <= 100000]['status'].value_counts()
compared = more_100k['acquired'] / less_100k['closed']
if compared > 1.0:
  print("Confirmed")
else:
  print("Refuted")
print('More/less:',compared)
