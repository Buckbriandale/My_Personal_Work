import yfinance as yf
import pandas as pd

# Define the assets in the exact order wanted in the CSV
ticker_order = [
    "XLE", "VDE", "XLB", "VAW", "XLI", "VIS", "XLY", "VCR",
    "XLP", "KXI", "XLV", "IHI", "XLF", "IYF", "VGT", "IXN",
    "VOX", "FCOM", "XLU", "VPU", "VNQ", "IYR", "EMXC", "GLD",
    "SPY", "VTI", "GBTC", "PGHY", "VWEHX", "SHY", "TLT"
]

# Define the time period
start_date = "2021-9-01"
end_date = "2026-8-02"

# Download data
data = yf.download(
    ticker_order,
    start=start_date,
    end=end_date,
    interval="1mo"
)

# Keep the Close prices and put the assets in the exact order above
adjusted_close = data["Close"].reindex(columns=ticker_order)

# Display the data
print(adjusted_close)

# Save to CSV
adjusted_close.to_csv("lastonesQ32026_monthly_adjusted_close.csv")
