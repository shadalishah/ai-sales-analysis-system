# 📦 Amazon Sales Analysis Report

A comprehensive data analysis project examining Amazon sales performance across categories, regions, and fulfillment methods over a 3-month period (March–June 2022).

---

## 📊 Project Overview

This project analyzes Amazon sales data to uncover key performance trends, identify operational bottlenecks, and provide actionable business recommendations. The analysis was conducted using Python-based data processing and AI-assisted insights powered by **Google Gemini API (Google AI Studio)**.

---

## 📁 Dataset Summary

| Field | Value |
|---|---|
| **Date Range** | 2022-03-31 to 2022-06-29 |
| **Total Orders** | 128,975 |
| **Total Revenue** | Rs 78,592,678.30 |
| **Average Order Value** | Rs 648.56 |
| **Avg Items per Order** | 0.90 |
| **Max Order Size** | 15 items |

---

## 🏆 Key Performance Indicators

- **Effective Delivery Rate:** 22.31% ⚠️
- **Cancellation Rate:** 14.21%
- **Return Rate (Post-Delivery):** ~6.8%
- **Top Fulfillment Method:** Easy Ship
- **Top State:** Maharashtra (22,260 orders)
- **Top Category:** Set (50,284 orders)

---

## 🗂️ Order Status Breakdown

| Status | Orders |
|---|---|
| Shipped | 77,804 |
| Shipped - Delivered to Buyer | 28,769 |
| Cancelled | 18,332 |
| Shipped - Returned to Seller | 1,953 |
| Shipped - Picked Up | 973 |
| Pending | 658 |
| Pending - Waiting for Pick Up | 281 |
| Shipped - Returning to Seller | 145 |
| Shipped - Out for Delivery | 35 |
| Shipped - Rejected by Buyer | 11 |
| Shipping | 8 |
| Shipped - Lost in Transit | 5 |
| Shipped - Damaged | 1 |

---

## 🌍 Regional Insights

**Top 5 States by Orders:**

| Rank | State | Orders |
|---|---|---|
| 1 | Maharashtra | 22,260 |
| 2 | Karnataka | 17,326 |
| 3 | Tamil Nadu | 11,483 |
| 4 | Telangana | 11,330 |
| 5 | Uttar Pradesh | 10,638 |

---

## 🛍️ Category Breakdown

**Top 5 Categories by Orders:**

| Rank | Category | Orders |
|---|---|---|
| 1 | Set | 50,284 |
| 2 | Kurta | 49,877 |
| 3 | Western Dress | 15,500 |
| 4 | Top | 10,622 |
| 5 | Ethnic Dress | 1,159 |

---

## 🚨 Key Findings & Red Flags

### ⚠️ Critical Issues
- **77,804 orders stuck in "Shipped" status** with no final delivery confirmation — the single biggest operational black hole.
- **Low effective delivery rate (22.31%)** signals severe last-mile delivery or tracking issues.
- **High cancellation rate (14.21%)** likely linked to delayed fulfillment and poor delivery communication.

### ✅ Strengths
- Strong product-market fit in **Set** and **Kurta** categories.
- Clear regional dominance in **Maharashtra** and **Karnataka**.
- **Easy Ship** proves to be the most effective fulfillment method.

---

## 💡 Actionable Recommendations

1. **🔍 Audit "Shipped" Orders** — Investigate all 77,804 orders without final delivery status. Resolving this alone could push revenue up by 25%+.
2. **🚚 Optimize Last-Mile Delivery** — Partner with reliable logistics providers; proactively update customers to reduce cancellations.
3. **🛒 Implement Cross-Selling & Bundling** — Introduce "Complete the Look" combos and free-shipping thresholds to raise average order value.
4. **📍 Targeted Geographic Expansion** — Run localized campaigns in Tier 2/3 cities across top states, with a dedicated focus on Uttar Pradesh's untapped potential.
5. **🎨 Diversify within Top Categories** — Launch seasonal collections and limited editions in Set & Kurta to retain customers and capture market share.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas & NumPy** | Data cleaning and processing |
| **Matplotlib / Seaborn** | Data visualization |
| **Google Gemini API** | AI-powered insights & analysis |
| **Google AI Studio** | Gemini API development & testing |
| **Amazon Seller Central** | Data source |

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/shadalishah/amazon-sales-analysis.git

# Navigate to the project directory
cd amazon-sales-analysis

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY="your_api_key_here"

# Run the analysis
python ai_Amazon_sales_analysis_pipeline.py
```

> 💡 Get your free Gemini API key from [Google AI Studio](https://aistudio.google.com/)

---

## 📂 Project Structure

```
amazon-sales-analysis/
│
├── .sixth/                                   # Project config/environment folder
│
├── ai_Amazon_sales_analysis_pipeline.py      # Main AI pipeline script (Gemini API)
├── Amazon Sale Data.csv                      # Raw Amazon sales dataset (67 MB)
├── amazon_sales_analysis.png                 # Generated sales analysis chart/visualization
├── sales_analysis_report.txt                 # AI-generated sales analysis report (9 KB)
└── README.md                                 # Project documentation
```

---

## 📌 Notes

- Data covers a 3-month window; long-term trends require additional historical data.
- The "0 items" minimum order size is a data anomaly and should be cleaned before deeper modelling.
- All revenue figures are in **Indian Rupees (Rs)**.
- AI insights in this project are generated via the **Google Gemini API**.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Shad Ali Shah**
> MPhil Economics student at the School of Economics, Quaid-i-Azam University, Islamabad.
> Interested in Economics theory with Data Science and Machine Learning.

- 🐙 GitHub: [@shadalishah](https://github.com/shadalishah)
- 💼 LinkedIn: [Shad Ali Shah](https://www.linkedin.com/in/shad-ali-shah-6439ab339/)
