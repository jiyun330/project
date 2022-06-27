from sqlalchemy import create_engine
import pandas as pd

df=pd.read_csv('/Users/jiyun/Desktop/Project3/data/Pokemon.csv')

df.columns = [c.lower() for c in df.columns]

engine = create_engine('postgresql://wloxatfz:bCC_dkMURSQzl7DvjlsAU90o0YduK7-4@castor.db.elephantsql.com/wloxatfz')

df.to_sql("pokemon", engine)