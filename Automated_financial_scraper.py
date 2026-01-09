#GitHub Project 1
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt



def Stock_Analyzer():
    print('---------------------------------')
    print('      Python Stock Analyzer')
    print('---------------------------------')
    try:
        ticker=input('Enter ticker of stock (eg: AAPL for Apple): ').upper()          # .upper() is used as yfinance takes ticker values only in uppercase as arguments

        print(f'\nDownloading the ticker data for a period of 1 year of {ticker}...')
        data=yf.Ticker(ticker).history(period='1y')                                   # 'data' is now a Pandas DataFrame that has collected the ticker data for a period of 1 year

        if data.empty:                                                                # data.empty is a function only present in the Pandas module, it checks if the given DataFrame is empty (if it is empty it returns 'True' else returns 'False')
            print('Error: No such data exists or Invalid Ticker')
            exit()
    

        fh=f'{ticker}_prices.csv'                                                     # Creates a csv file of the data collected
        data.to_csv(fh)
        print(f'Price History Saved to {fh}') 

        

        data['Daily Return']= data['Close'].pct_change()       # .pct_change() calculates fractional change between elements in the DataFrame ((Current Element- Prior Element)/Prior Element. In our case: Daily Return= (Current closing price-Closing price of day before)/ Closing price of day before
        average_daily_return=data['Daily Return'].mean()*252   # Average daily return for a period of 252 trading days
        volatility= data['Daily Return'].std() * (252**0.5)    # Annualized volatility of a stock (measure of how much a stock's price fluctuates)       Functions used: .std gives standard deviation, multipled by square root of trading days (252 days= 1 trading year)
        latest_price=data['Close'].iloc[-1]                        # [-1] as we need the last entry in the DataFrame to give us the latest price
        Annualized_return=(1+data['Daily Return']).prod()**(252/len(data))-1  # .prod() returns the product of the values in the DataFrame. Here we are calculating the compounded annualized return of the stock

        data['MA50'] = data['Close'].rolling(50).mean()           # .rolling(num) means that a window of a specific size (num) will across the DataFrame, its a way to move through the data one step at a time to perform calculations on the data present in the window.
        d_MA50=data['MA50'].dropna()                              # .dropna() drops the rows where the DataFrame has no value so rows that have NaN, None or Null values are dropped
        data['MA200'] = data['Close'].rolling(200).mean()
        d_MA200=data['MA200'].dropna()

        data['Signal']=0
        data.loc[data['MA50'] > data['MA200'], 'Signal']=1          # .loc is used to access a group of rows and columns by labels or a boolean array. Here we are creating a new column 'Signal' in the DataFrame, where if the 50 day Moving Average is greater than the 200 day Moving Average, the value in the 'Signal' column will be 1
        data['Position']=data['Signal'].diff()                      # .diff() calculates the difference of a DataFrame element compared with another element in the DataFrame (default is the element in the previous row). Here we are creating a new column 'Position' in the DataFrame, where it calculates the difference between the current value in the 'Signal' column and the prior value in the 'Signal' column


        print('\n- - - - - - Analysis Summary - - - - - -\n')
        print(f'Latest Price: ${latest_price:.2f}')              # When .2f is written after the value to be printed in the {}, it specifies we need only the first 2 decimal places in the result
        print(f'Annualized returns: {average_daily_return*100:.2f}%')
        print(f'Annualized returns (compounded): {Annualized_return*100:.2f}%')
        print(f'Annualized volatility: {volatility*100:.2f}%')       # .3f represents only 3 decimal places to be printed
        print(f'50 day Moving Average: {d_MA50.iloc[-1]:.3f}')   # .iloc is specific to Pandas library and used for indexing of data in the DataFrame. Here [-1] represents the latest data in the DataFrame
        print(f'200 day Moving Average: {d_MA200.iloc[-1]:.3f}')




        #Chart

        fig,ax= plt.subplots(figsize=(12,6))
        fig.patch.set_facecolor('#212121')                                       # This is used to add color to the parts outside the graph
        ax.set_facecolor('#15181C')                                          # This is used to set the background colour of the graph
        
        ax.plot(data['Close'], label='Close Price', color='gray')                 # This the data displayed on the graph that represents the closing price
        ax.plot(data['MA50'], label= '50 day MA', color='purple', alpha=0.9)                   # This is also the data displayed on the graph but this time it is of the 50 day Moving Average
        ax.plot(data['MA200'], label='200 day MA', color='lightblue', alpha=0.9)                  # This is also the data displayed on the graph but this time it is of the 200 day Moving Average 
        ax.plot(data[data['Position']==1].index,data['MA50'][data['Position']==1],'^',markersize=5,color='g',label='Buy Signal' )                                             # This is used to plot the buy and sell signals on the graph, here '^' represents an upward pointing triangle (buy signal) and 'v' represents a downward pointing triangle (sell signal)
        ax.plot(data[data['Position']==-1].index,data['MA50'][data['Position']==-1],'v', markersize=5, color='r', label='Sell Signal')                                        # markersize is used to specify the size of the marker on the graph                                              
        
        ax.set_title(f'{ticker} Price Chart with Moving Averages', color='white')      # This is the title of the graph, whatver is the argument in the function, is what is displayed as the title
        ax.set_xlabel('Date', color='white')                                           # This is the label of the x axis
        ax.set_ylabel('Price ($)', color='white')                                    # This is the label of the y axis

        ax.legend(facecolor='#15181C', edgecolor='white', labelcolor='white')                                                 # Because we have 3 streams of data displaye on the graph, we need to differentiate them, this is done with the help of plt.legend() (different colours for different data)
        ax.tick_params(colors='white')
        ax.grid(True, color='#2a2e33',alpha=0.4)                                               # This brings up a grid on the graph 
        plt.show()                                                   # This shows us the graph

    except Exception as e:
        print(f'Error downloading data: {e}')
        exit()

Stock_Analyzer()