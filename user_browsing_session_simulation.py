import pandas as pd
import random

df = pd.read_csv('/content/drive/MyDrive/Datasets/Book-Crossing-Dataset/BX-Books.csv', sep=';', error_bad_lines=False, engine = 'python')
df = df.drop(['Book-Title', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis = 1)


subset = 10000
df = df.sample(n = subset)

eligible_publishers = [publisher for publisher in list(df.Publisher.unique()) if len(df[df['Publisher'] == publisher]) >= 10]

df = df.loc[df['Publisher'].isin(eligible_publishers)]

def create_session(n):
  df_sesh = df.sample(n)
  df_sesh = df_sesh.reset_index(drop = True)
  final_item = df_sesh.iloc[len(df_sesh)-1]['ISBN']
  df_sesh['Final_Item'] = df_sesh['ISBN'] == final_item
  ISBNs = list(df_sesh['ISBN'])
  df_sesh['Considered_Before'] = ISBNs
  df_sesh['Considered_After'] = ISBNs
  df_sesh.at[0, 'Considered_Before'] = None
  df_sesh.at[len(df_sesh)-1, 'Considered_After'] = None
  ttt = sorted(random.sample(range(10, 600), len(df_sesh)), reverse = True)
  df_sesh['Time_to_Transaction'] = ttt
  time_considered = [ttt[i]-ttt[i+1] for i in range(len(ttt)-1)]
  time_considered.append(ttt[len(ttt)-1])
  df_sesh['Time_Considered'] = time_considered
  return df_sesh

num_users = random.randint(10, 100)

df_new = create_session(random.randint(1, 20))
for i in range(num_users-1):
  df_new = df_new.append(create_session(random.randint(1, 20)))

df_new = df_new.sample(frac=1).reset_index(drop=True)