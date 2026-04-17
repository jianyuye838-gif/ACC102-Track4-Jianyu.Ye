import wrds
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import statsmodels.api as sm

# -----------------------------
# WRDS连接（完全按你要求写）
# -----------------------------
username = "YOUR_WRDS_USERNAME"
db = wrds.Connection(wrds_username=username)


# -----------------------------
# 数据加载函数
# -----------------------------
@st.cache_data
def load_data(ticker):

    query = f"""
        SELECT a.date, a.ret, b.ticker
        FROM crsp.msf AS a
        JOIN crsp.msenames AS b
        ON a.permno = b.permno
        WHERE b.ticker = '{ticker}'
        AND a.date >= '2015-01-01'
    """

    df = db.raw_sql(query)

    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()

    return df


# -----------------------------
# Fama-French 数据（加分项）
# -----------------------------
@st.cache_data
def load_ff():

    ff = db.raw_sql("""
        SELECT date, mktrf, rf
        FROM ff.factors_monthly
    """)

    ff['date'] = pd.to_datetime(ff['date'])
    return ff


# -----------------------------
# Streamlit 页面
# -----------------------------
st.title("📊 Stock Risk & Return Analyzer (WRDS)")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL)", "AAPL")

if ticker:

    df = load_data(ticker)

    if df.empty:
        st.error("No data found.")
    else:
        st.success("Data Loaded Successfully!")

        # -----------------------------
        # 收益分析
        # -----------------------------
        df['cum_return'] = (1 + df['ret']).cumprod()

        st.subheader("📈 Cumulative Return")

        fig, ax = plt.subplots()
        ax.plot(df['date'], df['cum_return'])
        ax.set_title("Cumulative Return")
        st.pyplot(fig)

        # -----------------------------
        # 风险指标
        # -----------------------------
        avg_return = df['ret'].mean()
        volatility = df['ret'].std()
        sharpe = avg_return / volatility

        st.subheader("📊 Risk Metrics")
        st.write(f"Average Return: {avg_return:.4f}")
        st.write(f"Volatility: {volatility:.4f}")
        st.write(f"Sharpe Ratio: {sharpe:.4f}")

        # -----------------------------
        # CAPM（加分项）
        # -----------------------------
        try:
            ff = load_ff()

            merged = pd.merge(df, ff, on='date')
            merged['excess_ret'] = merged['ret'] - merged['rf']

            X = sm.add_constant(merged['mktrf'])
            y = merged['excess_ret']

            model = sm.OLS(y, X).fit()

            st.subheader("📊 CAPM Results")
            st.write(f"Alpha: {model.params['const']:.4f}")
            st.write(f"Beta: {model.params['mktrf']:.4f}")

        except:
            st.warning("CAPM analysis not available.")