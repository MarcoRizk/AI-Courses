import pandas as pd

from model import MlModel

# make prediction for input csv
if __name__ == '__main__':
    model = MlModel('cov19model.joblib')
    df = pd.read_csv('/home/marco/Projects/Teaching/Data Science in Production/Session 1 Introduction/dataset.csv')
    for row in df.to_dict(orient='records'):
        print(model.predict(row))
