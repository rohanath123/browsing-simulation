import pandas as pd
import random

#read dataset, WARNING: many dropped due to parsing erros
df = pd.read_csv('/content/drive/MyDrive/Datasets/Book-Crossing-Dataset/BX-Books.csv', sep=';', error_bad_lines=False, engine = 'python')
df = df.drop(['Book-Title', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis = 1)

#randomly sample subset of items for quicker execution
subset = 10000
df = df.sample(n = subset)
num_users = random.randint(100, 1000)

def get_browsing_dataset(df, num_users):
  #get eligible publishers as those who have more than 10 books published in the dataset
  eligible_publishers = [publisher for publisher in list(df.Publisher.unique()) if len(df[df['Publisher'] == publisher]) >= 10]

  #get dataset consisting of only those rows with eligible publishers
  df = df.loc[df['Publisher'].isin(eligible_publishers)]

  #randomly set number of users
  
  #create first session to create new dataframe
  df_new = create_session(df, random.randint(1, 20))
  #create a session for each user 
  for i in range(num_users-1):
    #create random number of sessions for each user:
    num_sessions = random.randint(1, 5)
    for j in range(num_sessions-1):
      df_new = df_new.append(create_session(df, random.randint(1, 20)))


  df_new = df_new.sample(frac=1).reset_index(drop=True)

  return df_new


#create session
def create_session(df, n):
  #create subset
  df_sesh = df.sample(n)
  df_sesh = df_sesh.reset_index(drop = True)

  #set last item as final item
  final_item = df_sesh.iloc[len(df_sesh)-1]['ISBN']
  df_sesh['Final_Item'] = df_sesh['ISBN'] == final_item

  #set item considered before and after
  ISBNs = list(df_sesh['ISBN'])
  df_sesh['Considered_Before'] = ISBNs
  df_sesh['Considered_After'] = ISBNs
  df_sesh.at[0, 'Considered_Before'] = None
  df_sesh.at[len(df_sesh)-1, 'Considered_After'] = None

  #set time to transaction
  ttt = sorted(random.sample(range(10, 600), len(df_sesh)), reverse = True)
  df_sesh['Time_to_Transaction'] = ttt

  #set time considered for each item
  time_considered = [ttt[i]-ttt[i+1] for i in range(len(ttt)-1)]
  time_considered.append(ttt[len(ttt)-1])
  df_sesh['Time_Considered'] = time_considered

  return df_sesh


browsing_dataset = get_browsing_dataset(df, num_users)