# Corporate Financial Health Analyzer
ACC102 Track4 Interactive Data Analysis Tool

## 1. Problem & User
This tool helps students and researchers analyze the financial health of public companies
using real annual financial data. The target users are finance learners, accounting students,
and casual analysts who need quick, interactive, and visual financial ratio analysis.

## 2. Data Source
- Data: WRDS Compustat Fundamental Annual (comp.funda)
- Access Date: April 2026
- Key Fields: Revenue, Net Income, Total Assets, Current Assets, Liabilities, EPS, Cash

## 3. Methods
- Python data extraction via WRDS API
- Financial ratio calculation (Profit Margin, ROA, ROE, Current Ratio, Debt Ratio, etc.)
- Interactive visualization using Streamlit
- Dual-company comparison and automated analysis

## 4. Key Findings
- Users can compare profitability, liquidity, and solvency between two companies.
- Clear trend charts show performance changes over selected years.
- The tool automatically evaluates financial risk and gives suggestions.

## 5. How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the tool:
   streamlit run app.py
3. Enter your WRDS username and select companies and years.

## 6. Product & Demo
- Interactive Tool: Local Streamlit App
- Demo Video: [Your Video Link]

## 7. Limitations & Improvements
- Limited to companies listed in Compustat.
- Data is annual; no quarterly analysis.
- Future: Add quarterly data, peer group analysis, and export PDF reports.