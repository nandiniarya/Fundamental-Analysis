# AI-Powered Stock Analysis Dashboard

## Introduction
This project presents a real-time, AI-driven dashboard built with Streamlit, which allows users to evaluate any public company's financial health by simply entering a stock ticker. It combines fundamental ratio analysis with AI-generated investment insights, bridging finance and machine learning for smarter investing. #*

## Tech Stack & Tools
**Frontend**: Streamlit (Python)  
**Backend**: Yahoo Finance API (via yfinance)  
**AI Model**: Mistral (LLM), integrated locally using Ollama  
**Environment**: Jupyter Notebook + Terminal for setup #*

## Key Functionalities
✅ **User Input**: Accepts stock ticker (e.g., AAPL, TSLA)  
📊 **Auto-Fetched Data**: Retrieves financials, balance sheet, and cashflow  
🔍 **Calculated Ratios**:
- ROIC, ROA, EBIT Margin
- Current Ratio, Debt-to-Equity, Operating Cash Flow to Debt  
🤖 **AI Analysis**:
- Uses Mistral to provide an investment verdict (Buy / Hold / Sell)
- Adds reasoning for transparency  
🧠 **No Finance Knowledge Required**: AI simplifies interpretation for beginners #*

## How to Run
1. Install Packages:
```bash
pip install streamlit yfinance

2. 🚀 Run Ollama (to start Mistral)
bash
Copy
Edit
ollama run mistral
3. ▶️ Launch Streamlit App
bash
Copy
Edit
streamlit run your_filename.py
The dashboard will open in your browser. Input any valid stock ticker to begin!







Challenges Faced
One of the primary challenges encountered during the development of this project was the incomplete or inconsistent financial data available through the Yahoo Finance API. For some companies, key financial metrics such as EBIT, invested capital, or operating cash flow were missing or reported under different naming conventions, which necessitated robust exception handling and fallback logic in the code. This issue affected the accuracy of certain financial ratios and sometimes led to "N/A" outputs, reducing the completeness of the analysis.

Another significant hurdle was prompt engineering for the LLM (Mistral) to generate consistent and reliable recommendations. Since the model interprets financial ratios based on textual input, crafting a structured and informative prompt was essential. Small changes in wording often led to varied AI outputs, so the prompt had to be carefully optimized to extract meaningful, professional-grade investment advice each time.

Additionally, the financial data obtained from Yahoo Finance came in diverse formats and units, often requiring conversion or normalization. For example, values might appear in thousands or millions, which could affect ratio calculations if not standardized correctly. Managing these discrepancies across income statements, balance sheets, and cash flow reports added complexity to the data processing logic.

Finally, setting up the Ollama model (Mistral) locally introduced its own set of configuration challenges. Ensuring compatibility between the Ollama server, Python environment, and Streamlit required a thorough understanding of system dependencies and careful coordination to make the model run smoothly alongside the dashboard interface. #*

Limitations
Despite its functionality, the dashboard has certain limitations that users should be aware of. Firstly, the analysis is based entirely on historical financial data, and it does not account for real-time market sentiment, breaking news, or macroeconomic events that can significantly impact stock performance. This static nature means that while the analysis is grounded in fundamentals, it may lack the dynamism of real-world investing environments.

Secondly, the dashboard currently lacks technical charting capabilities, such as historical price trends, moving averages, or candlestick patterns. These technical indicators are important for investors who follow momentum or timing-based strategies and would be a valuable addition to complement the fundamental metrics.

Moreover, the AI-generated recommendations are qualitative in nature, meaning they rely solely on the LLM's interpretation of ratios without a quantitative decision-making model or predictive analytics. This limits the model's capacity to back-test or provide confidence scores, which are often required in professional investment settings.

Lastly, the current setup supports analysis of only one stock at a time. While this is sufficient for quick individual reviews, it restricts broader use cases such as portfolio analysis or peer benchmarking. A multi-ticker comparison feature is under consideration and would significantly enhance the tool's analytical power. #*

Future Enhancements
To elevate the dashboard's capabilities, several enhancements are planned. One major addition would be sentiment analysis based on live news feeds and social media platforms such as Twitter and Reddit. This will help capture public and investor sentiment, offering a more well-rounded evaluation of a company beyond numerical ratios.

Another critical upgrade will be the inclusion of technical indicators like EMA (Exponential Moving Average), RSI (Relative Strength Index), and MACD (Moving Average Convergence Divergence). These tools will allow users to assess stock trends and momentum, providing entry and exit signals based on historical price patterns.

The ability to export results as PDF or Excel files is also on the roadmap. This will empower users to save and share AI-generated recommendations and financial ratios, especially useful for professionals and students working on reports or investment case studies.

Introducing a multi-ticker comparison feature will enable users to evaluate multiple companies side by side, rank them based on selected metrics, and gain deeper market insights. This is particularly valuable for portfolio construction or sector-specific analysis.

Finally, plans are in place to deploy the application on Streamlit Cloud or another hosting platform, making it publicly accessible. This deployment will remove the dependency on local setups, allowing broader usage across devices and geographies with minimal friction. #*

Conclusion
This project is a strong example of the synergy between finance and artificial intelligence, demonstrating how complex data can be transformed into actionable insights using intuitive user interfaces and smart models. By combining real-time data extraction, financial ratio computation, and LLM-powered recommendations, the tool empowers users—whether seasoned analysts or curious beginners—to make informed investment decisions with minimal effort.

While the model has its limitations, its extensibility and adaptability make it a promising prototype for more advanced applications in the fintech space. With planned enhancements and ongoing improvements, this dashboard is not just a project, but a stepping stone towards building intelligent, automated investment assistants that democratize access to financial analysis. #*
