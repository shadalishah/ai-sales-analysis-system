import pandas as pd

# Import the CSV file
csv_file = 'Amazon Sale Report.csv'
df = pd.read_csv(csv_file)

# Display basic information about the data
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nBasic statistics:")
print(df.describe())
import google.generativeai as genai
# Configure API (replace with your actual API key)
genai.configure(api_key="Your API Key Here")
# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")
# Prepare data summary for analysis
data_summary = f"""
Dataset Summary:
- Total Orders: {len(df)}
- Columns: {', '.join(df.columns.tolist())}
- Date Range: {df['Date'].min()} to {df['Date'].max()}
- Total Amount: {df['Amount'].sum()}
- Average Order Value: {df['Amount'].mean():.2f}
- Top 5 States: {df['ship-state'].value_counts().head().to_dict()}
- Top 5 Categories: {df['Category'].value_counts().head().to_dict()}
"""
# Get AI analysis
analysis_prompt = """Act as an e-commerce business analyst.
Based on the dataset below:
- Identify sales patterns
- Detect anomalies
- Suggest 3 strategies to increase revenue
Keep the answer short and clear.
Dataset Summary:
""" + data_summary
response = model.generate_content(analysis_prompt)
print("E-Commerce Business Analysis:")
print(response.text)

# Now Basic analysis is done, let's ask for specific insights
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import google.generativeai as genai
from datetime import datetime
import numpy as np
import warnings
warnings.filterwarnings('ignore')
# ===== DATA SETUP =====
csv_file = 'Amazon Sale Report.csv'
df = pd.read_csv(csv_file)
# Configure API
genai.configure(api_key="Your API Key Here")
model = genai.GenerativeModel("gemini-2.5-flash")

# Display dataset info
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# ===== DATA PREPROCESSING =====
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')
daily_sales = df.groupby('Date')['Amount'].sum().reset_index()
# 2. State-wise Performance
state_sales = df.groupby('ship-state').agg({
    'Amount': 'sum',
    'Order ID': 'count'
}).sort_values('Amount', ascending=False).head(10)
# 3. Category Performance
category_sales = df.groupby('Category').agg({
    'Amount': 'sum',
    'Order ID': 'count'
}).sort_values('Amount', ascending=False)

# 4. Status Distribution
status_dist = df['Status'].value_counts()

# 5. Fulfillment Distribution
fulfillment = df['Fulfilment'].value_counts()

# ===== CREATE BEAUTIFUL VISUALIZATIONS =====
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 12)

fig = plt.figure(figsize=(16, 12))

# Plot 1: Daily Sales Trend
ax1 = plt.subplot(3, 3, 1)
ax1.plot(daily_sales['Date'], daily_sales['Amount'], color='#2E86AB', linewidth=2)
ax1.fill_between(daily_sales['Date'], daily_sales['Amount'], alpha=0.3, color='#2E86AB')
ax1.set_title('Daily Sales Trend', fontsize=12, fontweight='bold')
ax1.set_xlabel('Date')
ax1.set_ylabel('Amount (₹)')
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Plot 2: Top 10 States
ax2 = plt.subplot(3, 3, 2)
state_sales['Amount'].plot(kind='barh', ax=ax2, color='#A23B72')
ax2.set_title('Top 10 States by Sales', fontsize=12, fontweight='bold')
ax2.set_xlabel('Total Amount (₹)')

# Plot 3: Top Categories
ax3 = plt.subplot(3, 3, 3)
category_sales['Amount'].head(8).plot(kind='bar', ax=ax3, color='#F18F01')
ax3.set_title('Top 8 Categories by Sales', fontsize=12, fontweight='bold')
ax3.set_ylabel('Amount (₹)')
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Plot 4: Status Distribution
ax4 = plt.subplot(3, 3, 4)
colors = sns.color_palette("husl", len(status_dist))
ax4.pie(status_dist.values, labels=status_dist.index, autopct='%1.1f%%', colors=colors, startangle=90)
ax4.set_title('Order Status Distribution', fontsize=12, fontweight='bold')

# Plot 5: Fulfillment Distribution
ax5 = plt.subplot(3, 3, 5)
fulfillment.plot(kind='bar', ax=ax5, color=['#06A77D', '#D62828', '#9D4EDD'])
ax5.set_title('Fulfillment Method Distribution', fontsize=12, fontweight='bold')
ax5.set_ylabel('Number of Orders')
plt.setp(ax5.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Plot 6: Average Order Value by Top States
ax6 = plt.subplot(3, 3, 6)
aov_by_state = df.groupby('ship-state')['Amount'].mean().sort_values(ascending=False).head(10)
aov_by_state.plot(kind='barh', ax=ax6, color='#219653')
ax6.set_title('Average Order Value - Top States', fontsize=12, fontweight='bold')
ax6.set_xlabel('Average Amount (₹)')

# Plot 7: Quantity Distribution
ax7 = plt.subplot(3, 3, 7)
quantity_dist = df['Qty'].value_counts().sort_index()
ax7.bar(quantity_dist.index, quantity_dist.values, color='#EB5757')
ax7.set_title('Order Quantity Distribution', fontsize=12, fontweight='bold')
ax7.set_xlabel('Quantity')
ax7.set_ylabel('Number of Orders')

# Plot 8: Sales by Fulfillment Channel
ax8 = plt.subplot(3, 3, 8)
fulfillment_sales = df.groupby('fulfilled-by')['Amount'].sum().sort_values(ascending=False).head(8)
fulfillment_sales.plot(kind='barh', ax=ax8, color='#6C5CE7')
ax8.set_title('Sales by Fulfillment Channel', fontsize=12, fontweight='bold')
ax8.set_xlabel('Total Amount (₹)')

# Plot 9: Sales Channel Distribution
ax9 = plt.subplot(3, 3, 9)
channel_sales = df['Sales Channel '].value_counts()
channel_sales.plot(kind='bar', ax=ax9, color=['#FF6B6B', '#4ECDC4'])
ax9.set_title('Sales by Channel', fontsize=12, fontweight='bold')
ax9.set_ylabel('Number of Orders')
plt.setp(ax9.xaxis.get_majorticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.savefig('amazon_sales_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'amazon_sales_analysis.png'")

# ===== PREPARE ANALYSIS DATA =====

analysis_data = f"""
COMPREHENSIVE SALES ANALYSIS DATA:

1. OVERALL METRICS:
   - Total Orders: {len(df):,}
   - Total Revenue: Rs {df['Amount'].sum():,.2f}
   - Average Order Value: Rs {df['Amount'].mean():,.2f}
   - Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}

2. TOP PERFORMERS:
   - Top State: {df['ship-state'].value_counts().index[0]} ({df['ship-state'].value_counts().values[0]} orders)
   - Top Category: {df['Category'].value_counts().index[0]} ({df['Category'].value_counts().values[0]} orders)
   - Best Fulfillment: {df['fulfilled-by'].value_counts().index[0]}

3. ORDER STATUS:
{status_dist.to_string()}

4. QUANTITY INSIGHTS:
   - Avg Items per Order: {df['Qty'].mean():.2f}
   - Max Order Size: {df['Qty'].max()} items
   - Min Order Size: {df['Qty'].min()} items

5. REGIONAL INSIGHTS:
   Top 5 States: {df['ship-state'].value_counts().head().to_dict()}

6. CATEGORY BREAKDOWN:
   Top 5 Categories: {df['Category'].value_counts().head().to_dict()}
"""

# ===== GET AI ANALYSIS =====

ai_prompt = f"""You are a senior e-commerce consultant. Analyze this comprehensive Amazon sales data and provide:

1. **Key Performance Indicators** - Highlight the most important metrics
2. **Sales Patterns** - What trends do you observe?
3. **Anomalies & Red Flags** - Any concerning issues?
4. **Geographic Opportunities** - Which regions have growth potential?
5. **Product Strategy** - Which categories to focus on?
6. **5 Actionable Recommendations** - How to increase revenue by 25%+

Keep analysis concise but insightful.

{analysis_data}"""

response = model.generate_content(ai_prompt)
print("\n" + "="*60)
print("AI-POWERED BUSINESS ANALYSIS")
print("="*60)
print(response.text)

# ===== SAVE REPORT WITH UTF-8 ENCODING =====

with open('sales_analysis_report.txt', 'w', encoding='utf-8') as f:
    f.write("AMAZON SALES ANALYSIS REPORT\n")
    f.write("="*60 + "\n")
    f.write(analysis_data)
    f.write("\n\nAI INSIGHTS:\n")
    f.write("="*60 + "\n")
    f.write(response.text)

print("\n✓ Report saved as 'sales_analysis_report.txt'")
print("✓ Analysis complete!")