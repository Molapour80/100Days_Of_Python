import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# 1. Generate sample data (in practice you can use yfinance or other sources)
def generate_sample_data(days=365):
    np.random.seed(42)
    base_price = 100
    noise = np.random.normal(0, 2, days)
    trend = np.linspace(0, 50, days)
    seasonal = 10 * np.sin(np.linspace(0, 10*np.pi, days))
    prices = base_price + trend + seasonal + noise
    dates = pd.date_range(start='2022-01-01', periods=days)
    return pd.DataFrame(prices, index=dates, columns=['Close'])

# 2. Calculate moving averages
def calculate_moving_averages(data, windows=[20, 50]):
    for window in windows:
        data[f'MA_{window}'] = data['Close'].rolling(window=window).mean()
    return data

# 3. Forecast using moving average
def moving_average_forecast(data, forecast_days=5, ma_window=20):
    # Calculate the last moving average value
    last_ma = data['Close'].rolling(window=ma_window).mean().iloc[-1]
    
    # Simple forecast: use the last MA value for future days
    forecast_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=forecast_days)
    forecast_values = [last_ma] * forecast_days
    
    return pd.DataFrame(forecast_values, index=forecast_dates, columns=['Forecast'])

# 4. Evaluate the model
def evaluate_model(data, ma_window=20, train_ratio=0.8):
    train_size = int(len(data) * train_ratio)
    train, test = data.iloc[:train_size], data.iloc[train_size:]
    
    # Calculate moving average on training data
    train[f'MA_{ma_window}'] = train['Close'].rolling(window=ma_window).mean()
    
    # Make predictions on test data
    predictions = []
    for i in range(len(test)):
        if i < ma_window:
            # For initial days without enough data, use last training MA
            pred = train[f'MA_{ma_window}'].iloc[-1]
        else:
            # For subsequent days, use MA of previous window
            window_data = test['Close'].iloc[i-ma_window:i]
            pred = window_data.mean()
        predictions.append(pred)
    
    test['Prediction'] = predictions
    mse = mean_squared_error(test['Close'], test['Prediction'])
    print(f'MSE for MA({ma_window}): {mse:.2f}')
    
    return test

# Main execution
if __name__ == "__main__":
    # Generate data
    stock_data = generate_sample_data()
    
    # Calculate moving averages
    stock_data = calculate_moving_averages(stock_data, windows=[20, 50])
    
    # Make 5-day forecast
    forecast = moving_average_forecast(stock_data, forecast_days=5, ma_window=20)
    
    # Evaluate model
    evaluation = evaluate_model(stock_data, ma_window=20)
    
    # Plot results
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Close'], label='Actual Price', alpha=0.7)
    plt.plot(stock_data['MA_20'], label='20-day Moving Average', color='orange')
    plt.plot(stock_data['MA_50'], label='50-day Moving Average', color='green')
    plt.plot(forecast['Forecast'], label='5-day Forecast', color='red', linestyle='--', marker='o')
    plt.plot(evaluation['Prediction'], label='Test Predictions', color='purple', alpha=0.7)
    plt.title('Stock Price Prediction Using Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()