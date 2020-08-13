from sqlalchemy import create_engine
import pandas as pd
import numpy as np

engine = create_engine('postgresql://postgres:zdxzdxzdx@192.168.1.8/make_model')

df_reader = pd.read_csv('pol.txt', delimiter='|',  chunksize=50000, encoding='gb2312')
for df in df_reader:
    str_df=df.select_dtypes([np.object])
    try:
        str_df=str_df.stack().str.decode('gb2312').unstack()
        for col in str_df:
            df[col]=str_df[col]

        df.to_sql('pol_txt', con=engine, if_exists='append')
    except Exception as e:
        print('Oooops...! Lets move on...')
