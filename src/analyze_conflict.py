import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

israel_attack_iran = datetime(2025, 6, 13)
us_attack_iran = datetime(2025, 6, 22)
ceasefire = datetime(2025, 6, 24)
end = datetime(2025, 7, 1)

def analyze_and_plot(ticker, period):
    commodity_df = yf.download(ticker, start=israel_attack_iran - timedelta(days=period), end=end)

    events = [("Israel_attack_iran", israel_attack_iran),
              ("US_attack_iran", us_attack_iran),
              ("Ceasefire", ceasefire)]

    # Main Price Prediction Plot (Top)
    fig, axs = plt.subplots(2, 3, figsize=(21, 10))  # 2 rows: 1st for price prediction, 2nd for risk premium
    fig.suptitle(f"{ticker} Prices, Predictions & Risk Premiums", fontsize=16, fontweight='semibold')

    for i, (event_name, event_date) in enumerate(events):
        # Split train/test data
        trainingset_period1 = commodity_df[commodity_df.index < event_date]
        testingset_period1 = commodity_df.drop(trainingset_period1.index)

        X_train = np.arange(len(trainingset_period1)).reshape(-1, 1)
        Y_train = trainingset_period1["Close"].values
        X_test = np.arange(len(trainingset_period1), len(trainingset_period1) + len(testingset_period1)).reshape(-1, 1)
        Y_test = testingset_period1["Close"].values

        # Linear regression
        model = LinearRegression()
        model.fit(X_train, Y_train)
        Y_Pred_Train = model.predict(X_train)
        Y_Pred_Test = model.predict(X_test)

        # Statistics
        r2 = model.score(X_train, Y_train)
        slope = model.coef_.item()  # safe float
        rmse = np.sqrt(mean_squared_error(Y_test, Y_Pred_Test))

        # --- Plot 1: Actual & Predicted Prices ---
        axs[0, i].plot(commodity_df.index, commodity_df["Close"], label="Actual Close Price", color="black")
        axs[0, i].plot(testingset_period1.index, Y_Pred_Test.flatten(), linestyle='--', color="orange", label="Predicted Close Price")
        axs[0, i].plot(trainingset_period1.index, Y_Pred_Train, linestyle='--', color="blue", label="Fitted (Pre-event)")
        axs[0, i].axvline(x=event_date, color='red', linestyle=':', label=event_name)
        axs[0, i].set_xlabel("Date")
        axs[0, i].set_ylabel("Price (USD)")
        axs[0, i].legend()
        axs[0, i].xaxis.set_major_locator(plt.MaxNLocator(4))
        axs[0, i].grid(True)
        axs[0, i].set_title(f"{event_name}\nR² = {r2:.3f} | Slope = {slope:.2f} | RMSE = {rmse:.2f}", fontsize=10)

        # --- Plot 2: Risk Premium ---
        risk_premium = Y_test - Y_Pred_Test 
        avg_risk = np.mean(risk_premium)
        max_risk = np.max(risk_premium)
        min_risk = np.min(risk_premium)
        sd_risk = np.std(risk_premium)

        axs[1, i].plot(range(len(risk_premium)), risk_premium, color='black', label='Risk Premium')
        axs[1, i].axhline(y=0, color='orange', linestyle='-', alpha=0.5)
        axs[1, i].set_xlabel("Days After Event")
        axs[1, i].set_ylabel("Risk Premium (USD)")
        axs[1, i].grid(True, alpha=0.3)
        axs[1, i].set_title(f"Risk Premium\nAvg: {avg_risk:.2f} | Max: {max_risk:.2f} | Min: {min_risk:.2f} | SD: {sd_risk:.2f}", fontsize=10)

 

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    return commodity_df, fig
