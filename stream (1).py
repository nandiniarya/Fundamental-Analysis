#pip install streamlit
#pip install yfinance
#run the above code in jupyter terminal before running the streamlit file

import streamlit as st
import yfinance as yf
from llama_index.llms.ollama import Ollama

# Function to fetch financial ratios
def get_financial_ratios(ticker):
    try:
        stock = yf.Ticker(ticker)
        financials = stock.financials
        balance_sheet = stock.balance_sheet
        cashflow = stock.cashflow

        def get_value(df, key):
            return df.loc[key].iloc[0] if key in df.index else None

        revenue = get_value(financials, "Total Revenue")
        net_income = get_value(financials, "Net Income")
        total_assets = get_value(balance_sheet, "Total Assets")
        total_liabilities = get_value(balance_sheet, "Total Liabilities Net Minority Interest")
        stockholders_equity = get_value(balance_sheet, "Stockholders Equity")
        invested_capital = get_value(balance_sheet, "Invested Capital")
        ebit = get_value(financials, "EBIT")
        operating_cashflow = get_value(cashflow, "Operating Cash Flow")
        total_debt = get_value(balance_sheet, "Total Debt")
        current_assets = get_value(balance_sheet, "Current Assets")
        current_liabilities = get_value(balance_sheet, "Current Liabilities")

        ratios = {
            "ROIC (%)": (net_income / invested_capital) * 100 if net_income and invested_capital else "N/A",
            "ROA (%)": (net_income / total_assets) * 100 if net_income and total_assets else "N/A",
            "Debt-to-Equity": total_liabilities / stockholders_equity if total_liabilities and stockholders_equity else "N/A",
            "Current Ratio": current_assets / current_liabilities if current_assets and current_liabilities else "N/A",
            "EBIT Margin (%)": (ebit / revenue) * 100 if ebit and revenue else "N/A",
            "Operating Cash Flow to Debt": operating_cashflow / total_debt if operating_cashflow and total_debt else "N/A"
        }

        return ratios
    except Exception as e:
        return {"Error": str(e)}

# Function to analyze ratios with LLM
def analyze_ratios_with_llm(ratios):
    prompt = f'''
    Given the following financial ratios, analyze the company's financial health and provide an investment recommendation:

    - ROIC: {ratios.get("ROIC (%)", "N/A")}%
    - ROA: {ratios.get("ROA (%)", "N/A")}%
    - Debt-to-Equity: {ratios.get("Debt-to-Equity", "N/A")}
    - Current Ratio: {ratios.get("Current Ratio", "N/A")}
    - EBIT Margin: {ratios.get("EBIT Margin (%)", "N/A")}%
    - Operating Cash Flow to Debt: {ratios.get("Operating Cash Flow to Debt", "N/A")}

    Based on these metrics, should an investor consider buying, holding, or selling this stock? Provide a short justification.
    '''
    
    llm = Ollama(model="mistral")
    
    try:
        response = llm.complete(prompt)
        return response
    except Exception as e:
        return f"Error generating analysis: {str(e)}"

# Streamlit UI with enhanced design
st.set_page_config(page_title="Stock Analysis Dashboard", page_icon="📈", layout="wide")

# Sidebar for user input
with st.sidebar:
    st.header("🔍 Stock Selection")
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", key="stock_ticker").strip().upper()

# Main App Layout
st.title("📊 Stock Analysis Dashboard")
st.markdown("Gain insights into a company's financial health using AI-driven analysis.")

if ticker:
    st.subheader(f"📌 Fetching Financial Data for: **{ticker}**")

    ratios = get_financial_ratios(ticker)

    if "Error" in ratios:
        st.error(f"❌ Error fetching data: {ratios['Error']}")
    else:
        st.subheader("📈 Key Financial Ratios")
        styled_ratios = {k: f"📊 {v}" if isinstance(v, (int, float)) else v for k, v in ratios.items()}
        st.table(styled_ratios)

        st.subheader("🤖 AI Investment Recommendation")
        with st.spinner("Analyzing financial data with AI..."):
            recommendation = analyze_ratios_with_llm(ratios)
        st.success(recommendation)

# Footer
st.markdown("---")
st.markdown("🔹 *Developed by [Your Name]. Powered by Streamlit & AI.*")

