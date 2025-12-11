# 📈 Tariff Charts & Trends Guide

Your Tariff Dashboard now includes professional charting capabilities to visualize historical tariff trends.

## 🎨 Chart Features

### Multiple Chart Types
1. **Line Chart** - Track rate changes over time
2. **Area Chart** - Show growth/decline with filled areas
3. **Combined Chart** - Mix area and line for comparison

### Filtering Options
- **View by Country**: US Only, China Only, or US vs China
- **Time Range**: Configurable (default: 90 days)
- **Product Categories**: Filter by HS code

## 📊 What You Can See

### Chart Elements
```
47.5% ┌─────────────────┐
      │                 │  ← US Tariff Rate (Blue)
31.9% │  ╱╱╱╱╱╱        │  ← China Tariff Rate (Red)
      │ ╱     ╲        │
20%   │╱       ╲      │
      │         ╲╱╱╱│
 5%   └─────────────┘
      Jan 18  Jan 20  Jan 22  Jan 24  Nov 25
```

### Key Metrics Displayed
- **Current US Rate**: Latest tariff rate for US
- **Current China Rate**: Latest tariff rate for China
- **Peak Rate**: Highest rate in the period
- **Rate Changes**: Month-over-month comparisons

## 🚀 Using the Chart Tab

### 1. Access Charts
Click the **"📈 Trends"** tab in the navigation

### 2. Select Chart Type
```
Chart Type: [Line Chart ▼]
- Line Chart (best for trends)
- Area Chart (best for visual impact)
- Combined (best for comparison)
```

### 3. Filter by View
```
View: [US vs China ▼]
- US vs China (shows both)
- US Only (US tariffs only)
- China Only (China tariffs only)
```

### 4. Interpret the Data
- **Blue Line** = US average tariff rate
- **Red Line** = China average tariff rate
- **Orange Dashed** = US tariffs on Chinese exports
- **Purple Dashed** = China tariffs on US exports

## 📈 Sample Historical Data Included

The app comes with realistic sample data:

| Date | US Rate | China Rate | Event |
|------|---------|-----------|-------|
| Jan 2018 | 5% | 3% | Base rates |
| 2018-2019 | 5-12% | 5-10% | Trade war escalation |
| 2020-2023 | 16.5% | 12% | Plateau period |
| Sept 2024 | 25% | 18% | Rate increases |
| Nov 2025 | 47.5% | 31.9% | Current peak |

## 🔄 Real Data Integration

To connect real tariff data sources:

### 1. Update Scraper (`backend/scraper.py`)
```python
def fetch_us_tariffs(self, db: Session):
    # Replace placeholder with actual data source
    # Examples:
    # - usitc.gov API
    # - USTR.gov data
    # - Custom CSV/JSON files
```

### 2. Add Historical Data
```python
# Save to TariffTrend table
trend = TariffTrend(
    country="US",
    hs_code="6204.62.20",
    product_description="Women's Trousers",
    rate=16.5,
    record_date=datetime.utcnow()
)
db.add(trend)
db.commit()
```

### 3. Access via API
```bash
curl "http://localhost:8000/api/trends?country=US&days=90"
```

## 📊 API Endpoints for Charts

### Get Trend Data
```
GET /api/trends
Parameters:
  - country: "US" or "China" (optional)
  - hs_code: HS code filter (optional)
  - days: days back (default: 90)

Response:
{
  "country": "US",
  "days": 90,
  "data": [
    {
      "date": "2025-09-01",
      "us_rate": 25.0,
      "china_rate": 18.0,
      "rates": {...}
    }
  ]
}
```

### Example Requests
```bash
# All data for 90 days
curl http://localhost:8000/api/trends

# US only for 30 days
curl "http://localhost:8000/api/trends?country=US&days=30"

# Specific product for 365 days
curl "http://localhost:8000/api/trends?hs_code=6204.62.20&days=365"
```

## 🎯 Use Cases

### 1. Track Trade War Impact
- View long-term trends
- See spikes and plateaus
- Compare US vs China trends

### 2. Monitor Specific Products
- Filter by HS code
- Track individual product rates
- Identify volatile products

### 3. Analyze Historical Patterns
- Use area chart for visual trends
- Identify peaks and valleys
- Compare time periods

### 4. Generate Reports
- Export chart data
- Use for presentations
- Share with stakeholders

## 🛠️ Customization

### Change Chart Colors
Edit `frontend/components/TariffChart.jsx`:
```javascript
<Line 
  dataKey="us_general" 
  stroke="#667eea"  // Change this color
  strokeWidth={3}
  ...
/>
```

### Add More Data Points
Edit `frontend/components/TariffChart.jsx`:
```javascript
const historicalData = [
  { date: 'Jan 2018', us_general: 5, ... },
  // Add more entries here
];
```

### Change Update Frequency
Edit `backend/main.py`:
```python
# Change from daily to hourly
scheduler.add_job(daily_job, "cron", hour="*", minute=0)
```

## 📱 Mobile Experience

Charts are fully responsive:
- Auto-scales on smaller screens
- Touch-friendly interactive elements
- Readable on mobile devices
- Smooth animations

## ⚡ Performance Tips

1. **Limit Date Range**
   - Use `days=30` for faster loading
   - Default is 90 days

2. **Filter by Product**
   - Narrow results with `hs_code`
   - Reduces data points

3. **Cache Data**
   - Client-side caching built-in
   - Reduces API calls

4. **Database Indexes**
   - Already optimized
   - Fast queries on large datasets

## 🔔 Real Data Sources to Connect

### US Tariffs
- **USITC.gov** - Tariff data
- **USTR.gov** - Trade agreements
- **Census Bureau** - Trade statistics

### China Tariffs
- **cccn.customs.gov.cn** - China Customs
- **chinagate.org** - Trade data
- **WTO database** - International tariffs

## 🚀 Next Steps

### Immediate
1. ✅ Run app and view chart
2. ✅ Test different chart types
3. ✅ Explore sample data

### Short Term
1. 📌 Connect real data source
2. 📌 Add more product categories
3. 📌 Customize colors to match brand

### Medium Term
1. 🚀 Add export (CSV, PDF)
2. 🚀 Add alerts on price changes
3. 🚀 Create email reports

### Long Term
1. 💼 Predictive analysis
2. 💼 Machine learning alerts
3. 💼 Advanced analytics

## 📚 Libraries Used

- **Recharts** - Professional React charting
- **Chart.js** - Alternative for future use
- **Moment.js** - Date formatting

## 🎓 Learning Resources

### Recharts Documentation
- Line Charts: https://recharts.org/api/LineChart
- Area Charts: https://recharts.org/api/AreaChart
- Tooltips: https://recharts.org/api/Tooltip

### Trade Data Sources
- World Bank: https://wits.worldbank.org/
- USITC: https://www.usitc.gov/
- USTR: https://ustr.gov/

## ✨ Chart Showcase

### Example: Compare US vs China Trends
1. Open Trends tab
2. Select "US vs China" view
3. Choose "Line Chart"
4. See both lines clearly
5. Hover for exact values

### Example: Track Single Product
1. Open Trends tab
2. Filter by HS code: 6204.62.20
3. Use Area Chart
4. See growth over time
5. Identify peak rates

## 🆘 Troubleshooting

### Chart Not Loading
- Check browser console for errors
- Verify API endpoint: `http://localhost:8000/api/trends`
- Ensure sample data exists in database

### Lines Overlapping
- Use "US Only" or "China Only" view
- Choose different chart type
- Zoom into specific time period

### No Data Points
- Ensure database has trend records
- Check date range (days parameter)
- Verify country filter

---

**The chart is ready to use with sample data! 📊 Connect real tariff sources anytime.**
