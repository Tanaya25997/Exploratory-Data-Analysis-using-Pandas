import pandas as pd


def preprocess_datacsv():

    df = pd.read_csv('data.csv') 
    
    print("\n ======================= Printing Data ================================== \n", df.to_string())
    
    print("\n ================================== Quick overview of data (first 5 rows) ================================== \n", df.head())
    
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df.info())
    
    
    ### dropping empty cells ###
    
    df_dropped = df.dropna()   
    print("\n ============ Printing Data after dropping empty cells  =============== \n", df_dropped.to_string())
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df_dropped.info())
    
    
    
    
    
    
    
    





if __name__ == '__main__':

    preprocess_datacsv()