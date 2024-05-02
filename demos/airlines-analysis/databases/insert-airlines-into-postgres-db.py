import pandas as pd
from sqlalchemy import create_engine

airlines = pd.read_csv("../data/airlines.csv", header=0)

engine = create_engine("postgresql://jetbrains:jetbrains@localhost/demo")
airlines.to_sql("airlines", con=engine)