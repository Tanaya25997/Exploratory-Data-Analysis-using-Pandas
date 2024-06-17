import pandas as pd
import matplotlib.pyplot as plt


def preprocess_datacsv():

    df = pd.read_csv('data.csv') 
    
    print("\n ======================= Printing Data ================================== \n", df.to_string())
    
    print("\n ================================== Quick overview of data (first 5 rows) ================================== \n", df.head())
    
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df.info())
    
    
    '''
    ### dropping empty cells ###
    
    df_dropped = df.dropna()   
    print("\n ============ Printing Data after dropping empty cells  =============== \n", df_dropped.to_string())
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df_dropped.info())
    '''
    
    ### empty cells in Date (object) and Calories (float). 
    ### filling empty cells in  Calories with mean
    ### dropping empty cells in Date 

    df = df.dropna(subset=['Date'])
    df['Calories'] = df['Calories'].fillna(df['Calories'].mean())
    print("\n ======================= Printing Data ================================== \n", df.to_string())
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df.info())
    
    #### changing wrong format 
    df['Date'] = pd.to_datetime(df['Date'])
    print("\n ======================= Printing Data ================================== \n", df.to_string())
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df.info())
    
    ### changing wrong data in 'Duration' with the Mode of the value 
    mode_duration = df['Duration'].mode()[0]
    for d in df.index:
        if df.loc[d,'Duration'] > 60:
            df.loc[d,'Duration'] = mode_duration
            
    print("\n ======================= Printing Data ================================== \n", df.to_string())
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df.info())
    
    
    ### Drop Duplicates 
    df.drop_duplicates(inplace=True)
    print("\n ======================= Printing Data ================================== \n", df.to_string())
    print("\n ================================== Quick net overview of data ================================== \n")
    print(df.info())
    
    ## Plot 
    print(df.corr())
    #df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
    #plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





if __name__ == '__main__':

    preprocess_datacsv()