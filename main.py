import pandas as pd
import geopandas as gpd
def main():
    df = pd.read_csv('Housing_Data.csv')
    print(df.info())
    
    
if __name__ == "__main__":
    main()  