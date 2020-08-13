from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import sys

engine = create_engine('postgresql://postgres:zdxzdxzdx@192.168.1.8/make_model')
line = sys.argv[1]

df_reader = pd.read_sas('ma_private_'+line+'_uniq.sas7bdat', chunksize=10000)
for df in df_reader:
    str_df=df.select_dtypes([np.object])
    try:
        str_df=str_df.stack().str.decode('gb2312').unstack()
        for col in str_df:
            df[col]=str_df[col]

        df.to_sql(f'ma_pri_{line[:3]}_uniq', con=engine, if_exists='append')
    except Exception as e:
        print('Oooops...! Lets goon')
