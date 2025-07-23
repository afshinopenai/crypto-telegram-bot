import ccxt
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from telegram import Bot
import config
import traceback

def fetch_ohlcv(symbol="BTC/USDT", timeframe="4h", limit=100):
    binance = ccxt.binance()
    data = binance.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(data, columns=["ts","open","high","low","close","volume"])
    df["ts"] = pd.to_datetime(df["ts"], unit="ms")
    return df

def plot_and_send(df):
    plt.figure(figsize=(10,6))
    plt.plot(df["ts"], df["close"], label="Close")
    plt.title("BTC/USDT - 4h")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    bot = Bot(token=config.TOKEN)
    bot.send_photo(chat_id=config.CHAT_ID, photo=buf)

def main():
    try:
        df = fetch_ohlcv()
        plot_and_send(df)
    except Exception:
        print("❌ خطا رخ داد:")
        traceback.print_exc()

if __name__ == "__main__":
    main()
