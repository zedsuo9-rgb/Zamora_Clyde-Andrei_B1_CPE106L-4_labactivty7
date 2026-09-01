import requests
import matplotlib.pyplot as plt

def fetch_and_plot_currency(base_currency, target_currency, start_date, end_date):
    """Fetches currency data and plots the trend."""
    # 1. Request structured data from the API
    url = f"https://api.frankfurter.app/{start_date}..{end_date}?from={base_currency}&to={target_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching data for {target_currency}")
        return

    # 2. Receive JSON and transform data
    data = response.json()
    rates = data.get("rates", {})
    
    # Extract dates (x-axis) and values (y-axis)
    dates = list(rates.keys())
    values = [rate[target_currency] for rate in rates.values()]

    # 3. Create a well-labeled visualization
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', linestyle='-', color='b')
    
    plt.title(f"Trend of {target_currency} against {base_currency} ({start_date} to {end_date})")
    plt.xlabel("Date")
    plt.ylabel(f"Exchange Rate ({target_currency})")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    
    # Save the plot as a screenshot for evidence
    filename = f"{base_currency}_to_{target_currency}_trend.png"
    plt.savefig(filename)
    print(f"Successfully generated and saved chart: {filename}")
    
    # Display the result
    plt.show()

if __name__ == "__main__":
    print("Lab Activity 7: Data Mining APIs and Visualization")
    print("Running 3 Test Cases...\n")

    # Test Case 1: USD to EUR for January 2023
    print("Test Case 1: USD to EUR")
    fetch_and_plot_currency("USD", "EUR", "2023-01-01", "2023-01-31")

    # Test Case 2: USD to GBP for February 2023
    print("Test Case 2: USD to GBP")
    fetch_and_plot_currency("USD", "GBP", "2023-02-01", "2023-02-28")

    # Test Case 3: USD to JPY for March 2023
    print("Test Case 3: USD to JPY")
    fetch_and_plot_currency("USD", "JPY", "2023-03-01", "2023-03-31")