Superstore Sales \& Profitability Analysis


 Project Overview



本專案以公開資料集 Superstore 為基礎，進行完整的銷售與獲利分析，從整體營運表現出發，逐步深入探討不同商品、折扣策略與交易之間的關係，挖掘銷售數據背後可能存在的獲利風險。



透過 Python、SQL 與資料視覺化進行分析，進一步拆解問題並驗證可能的原因，觀察商品銷售與利潤之間的關聯與異常交易，將分析結果轉化為具體的商業洞察與改善方向，作為後續決策討論的參考。



⸻
 Business Questions



本專案主要探討以下問題：



1\. 哪些商品類別具有較高的獲利風險？

2\. 折扣策略與商品利潤之間存在什麼關係？

3\. 客戶層級的獲利表現，是否能反映實際的虧損來源？

4\. 如何透過資料分析找出值得進一步關注的交易與商品？



⸻
Key Findings



1\. Furniture：銷售規模高，但獲利率偏低



Furniture 的銷售額約為 742K，但總利潤僅約 18K，Profit Margin 約為 2.49%。



相較於 Office Supplies 與 Technology，Furniture 雖然具有一定的銷售規模，但獲利效率明顯偏低。



進一步分析後發現，Furniture 中的 Tables 為主要虧損來源。



⸻



2\. Tables：高折扣與低利潤呈現明顯關聯



Tables 是整體資料中虧損最嚴重的 Sub-Category，總利潤約為 -17.7K。



進一步依 Discount 分組後，可以觀察到平均利潤隨折扣提高而明顯下降：



Discount	Average Profit

0%	184.39

20%	-4.28

30%	-63.01

40%	-215.83

45%	-226.65

50%	-239.32



此外，進一步比較同時出現 0% 與 40% 折扣的商品後，33 個商品皆呈現：



0% 折扣 → 累積獲利為正

40% 折扣 → 累積獲利為負



這顯示高折扣交易值得進一步檢視，但由於資料未包含完整成本與促銷資訊，本分析將其視為關聯性結果，而非直接判定因果關係。



⸻



3\. Transaction-level Analysis：客戶虧損可能集中於少數交易



部分客戶的整體虧損，並不代表其所有交易都沒有獲利。



以 Cindy Stewart 為例，其整體 Profit 約為 -6.6K，但主要虧損集中於一筆高折扣交易：



\* Product：Cubify CubeX 3D Printer

\* Discount：70%

\* Profit：約 -6.6K



其他交易則包含多筆獲利交易。



因此，若只觀察 Customer-level 的總 Profit，可能無法直接辨識真正的虧損來源；進一步進行 Transaction-level Analysis 能更有效定位異常交易。



⸻
Analysis Process



本專案採用以下分析流程：



Data → Exploration → Problem Identification → Drill-down Analysis → SQL Validation → Visualization → Business Insight



1\. Data Preparation



\* 資料讀取與格式整理

\* 日期欄位轉換

\* 基礎資料檢查



2\. Exploratory Data Analysis



\* Category Sales / Profit

\* Profit Margin

\* Sub-Category Profit

\* Discount \& Profit

\* Customer Profitability



3\. Problem Drill-down



針對初步發現的問題進一步拆解：



Furniture → Tables → Discount → Product → Transaction



4\. SQL Analysis



使用 SQLite 進行資料查詢與驗證，包括：



\* Category Sales \& Profit

\* Sub-Category Profit

\* Tables Discount \& Average Profit

\* Top Loss-making Transactions



5\. Visualization



使用 Python / Matplotlib 將分析結果視覺化，協助辨識：



\* 類別間獲利差異

\* 折扣與平均利潤的變化

\* 個別交易的獲利異常



⸻
Business Recommendations



根據本次分析結果，提出以下改善方向：



1\. 檢視高折扣商品的促銷策略



尤其是 Tables 等高風險商品，可進一步檢視高折扣是否真正帶來足夠的銷售或數量提升，避免折扣造成利潤大幅下降。



2\. 建立交易層級的獲利監控



除了觀察 Customer 或 Category 的整體績效，也應針對高折扣、高銷售但低利潤的交易進行監控。



3\. 不只追蹤 Sales，也應同時觀察 Profit Margin



高銷售額不一定代表高獲利，因此在評估商品績效時，可以同時觀察：



Sales → Profit → Profit Margin



以避免只追求營收而忽略實際獲利能力。



⸻
Limitations



本資料集主要包含銷售、折扣、數量與利潤等資訊，未提供完整的：



\* Product Cost

\* Inventory Cost

\* Shipping Cost

\* Marketing / Promotion Cost

\* Customer Acquisition Cost



因此，本專案可以觀察變數之間的關聯與異常，但無法僅透過目前資料直接證明因果關係。



若取得更完整的成本與營運資料，可進一步進行 Profitability、Promotion Effectiveness 或 Customer Lifetime Value 等分析。



⸻
Tools \& Skills



\* Python

&#x20;   \* Pandas

&#x20;   \* Matplotlib

\* SQL

&#x20;   \* SQLite

&#x20;   \* SQL Aggregation / GROUP BY / ORDER BY / Filtering

\* Data Analysis

&#x20;   \* Exploratory Data Analysis

&#x20;   \* Profitability Analysis

&#x20;   \* Discount Analysis

&#x20;   \* Transaction-level Analysis

\* Data Visualization

\* Business Insight \& Recommendation



⸻
Project Structure



Superstore\_Analytics\_Portfolio/

│

├── superstore\_analysis.py

├── superstore\_sql.py

├── sql\_category\_result.csv

└── README.md



Note: The original dataset and local SQLite database are not included in the repository.



⸻
 Presentation



完整分析結果與視覺化成果整理於 PowerPoint 簡報中，包含：



\* Business Questions

\* Analytical Process

\* Key Findings

\* Data Visualization

\* Business Recommendations

\* Limitations \& Next Analysis



⸻
 Project Purpose



This project was developed as a portfolio project to demonstrate my ability to use data analysis tools to identify business problems, investigate potential causes, validate findings, and translate analytical results into actionable business insights.

