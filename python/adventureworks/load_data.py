# %%
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")



#dialect+driver://username:password@host:port/database
engine = create_engine(f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres_sandbox:5432/{POSTGRES_DATABASE}")



df = pd.read_csv('/home/data/adventureworks/customers.csv')

df.head()

# %%

try:
    df.to_sql('class', engine, if_exists= 'replace', index= False)

except:
    print("Sorry, some error has occurred!")

finally:
    engine.dispose()

