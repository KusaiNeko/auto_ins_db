from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import sys

# read sas dt
# line='scratch' # scratch file is broken
# line='glass'
line = sys.argv[1]
df = pd.read_sas('ma_private_'+line+'_uniq.sas7bdat')

str_df=df.select_dtypes([np.object])
str_df=str_df.stack().str.decode('gb2312').unstack()
for col in str_df:
    df[col]=str_df[col]

engine = create_engine('postgresql://postgres:zdxzdxzdx@192.168.1.8/make_model')
df.to_sql(f'ma_pri_{line[:3]}_uniq', con=engine, if_exists='replace')
