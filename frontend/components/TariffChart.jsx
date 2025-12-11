import React, { useState } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  ComposedChart,
  Area,
  AreaChart
} from 'recharts';

function TariffChart({ apiUrl }) {
  const [chartType, setChartType] = useState('line');
  const [country, setCountry] = useState('both');
  const [selectedHsCodes, setSelectedHsCodes] = useState(['6204.62.20', '8471.30.00']);

  // Sample historical data - in production, this would come from the API
  const historicalData = [
    { date: 'Jan 2018', us_general: 5, china_general: 3, us_china: 5, china_us: 5 },
    { date: 'Jun 2018', us_general: 8, china_general: 5, us_china: 8, china_us: 8 },
    { date: 'Jan 2019', us_general: 12, china_general: 8, us_china: 12, china_us: 12 },
    { date: 'Jun 2019', us_general: 15, china_general: 10, us_china: 15, china_us: 15 },
    { date: 'Jan 2020', us_general: 16.5, china_general: 12, us_china: 16.5, china_us: 16.5 },
    { date: 'Jun 2021', us_general: 16.5, china_general: 12, us_china: 16.5, china_us: 16.5 },
    { date: 'Jan 2023', us_general: 16.5, china_general: 12, us_china: 16.5, china_us: 16.5 },
    { date: 'Jun 2024', us_general: 20, china_general: 15, us_china: 20, china_us: 20 },
    { date: 'Sep 2024', us_general: 25, china_general: 18, us_china: 25, china_us: 25 },
    { date: 'Oct 2024', us_general: 35, china_general: 25, us_china: 35, china_us: 35 },
    { date: 'Nov 2025', us_general: 47.5, china_general: 31.9, us_china: 47.5, china_us: 31.9 }
  ];

  const tariffOptions = [
    { code: '6204.62.20', name: 'Women\'s Cotton Trousers' },
    { code: '8471.30.00', name: 'Data Processing Machines' },
    { code: '6109.10.00', name: 'Knit Shirts' },
    { code: '7326.90.00', name: 'Iron/Steel Articles' },
  ];

  const handleHsCodeToggle = (code) => {
    if (selectedHsCodes.includes(code)) {
      setSelectedHsCodes(selectedHsCodes.filter(c => c !== code));
    } else {
      setSelectedHsCodes([...selectedHsCodes, code]);
    }
  };

  return (
    <div className="tariff-chart">
      <div className="chart-controls">
        <div className="control-group">
          <label>Chart Type:</label>
          <select value={chartType} onChange={(e) => setChartType(e.target.value)}>
            <option value="line">Line Chart</option>
            <option value="area">Area Chart</option>
            <option value="combined">Combined</option>
          </select>
        </div>

        <div className="control-group">
          <label>View:</label>
          <select value={country} onChange={(e) => setCountry(e.target.value)}>
            <option value="both">US vs China</option>
            <option value="us">US Only</option>
            <option value="china">China Only</option>
          </select>
        </div>
      </div>

      <div className="chart-legend-section">
        <h3>📊 Tariff Rate Trends Over Time</h3>
        <p className="chart-subtitle">Historical average tariff rates for selected product categories</p>
      </div>

      <div className="chart-container">
        <ResponsiveContainer width="100%" height={400}>
          {chartType === 'line' ? (
            <LineChart data={historicalData} margin={{ top: 5, right: 30, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
              <XAxis 
                dataKey="date" 
                stroke="#999"
                style={{ fontSize: '12px' }}
              />
              <YAxis 
                label={{ value: 'Tariff Rate (%)', angle: -90, position: 'insideLeft' }}
                stroke="#999"
              />
              <Tooltip 
                contentStyle={{ backgroundColor: '#fff', border: '1px solid #ccc' }}
                formatter={(value) => `${value.toFixed(1)}%`}
              />
              <Legend />
              
              {(country === 'both' || country === 'us') && (
                <Line 
                  type="monotone" 
                  dataKey="us_general" 
                  stroke="#667eea" 
                  strokeWidth={3}
                  dot={{ fill: '#667eea', r: 4 }}
                  activeDot={{ r: 6 }}
                  name="US Tariff Rate"
                />
              )}
              {(country === 'both' || country === 'china') && (
                <Line 
                  type="monotone" 
                  dataKey="china_general" 
                  stroke="#e74c3c" 
                  strokeWidth={3}
                  dot={{ fill: '#e74c3c', r: 4 }}
                  activeDot={{ r: 6 }}
                  name="China Tariff Rate"
                />
              )}
              {country === 'both' && (
                <>
                  <Line 
                    type="monotone" 
                    dataKey="us_china" 
                    stroke="#f39c12" 
                    strokeWidth={2}
                    strokeDasharray="5 5"
                    dot={false}
                    name="US on Chinese"
                  />
                  <Line 
                    type="monotone" 
                    dataKey="china_us" 
                    stroke="#9b59b6" 
                    strokeWidth={2}
                    strokeDasharray="5 5"
                    dot={false}
                    name="China on US"
                  />
                </>
              )}
            </LineChart>
          ) : chartType === 'area' ? (
            <AreaChart data={historicalData} margin={{ top: 5, right: 30, left: 0, bottom: 5 }}>
              <defs>
                <linearGradient id="colorUs" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#667eea" stopOpacity={0.8}/>
                  <stop offset="95%" stopColor="#667eea" stopOpacity={0}/>
                </linearGradient>
                <linearGradient id="colorChina" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#e74c3c" stopOpacity={0.8}/>
                  <stop offset="95%" stopColor="#e74c3c" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
              <XAxis dataKey="date" stroke="#999" />
              <YAxis stroke="#999" />
              <Tooltip formatter={(value) => `${value.toFixed(1)}%`} />
              <Legend />
              {(country === 'both' || country === 'us') && (
                <Area 
                  type="monotone" 
                  dataKey="us_general" 
                  stroke="#667eea" 
                  fillOpacity={1} 
                  fill="url(#colorUs)"
                  name="US Tariff Rate"
                />
              )}
              {(country === 'both' || country === 'china') && (
                <Area 
                  type="monotone" 
                  dataKey="china_general" 
                  stroke="#e74c3c" 
                  fillOpacity={1} 
                  fill="url(#colorChina)"
                  name="China Tariff Rate"
                />
              )}
            </AreaChart>
          ) : (
            <ComposedChart data={historicalData} margin={{ top: 5, right: 30, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
              <XAxis dataKey="date" stroke="#999" />
              <YAxis stroke="#999" />
              <Tooltip formatter={(value) => `${value.toFixed(1)}%`} />
              <Legend />
              {(country === 'both' || country === 'us') && (
                <Area 
                  type="monotone" 
                  dataKey="us_general" 
                  fill="#667eea" 
                  stroke="#667eea" 
                  fillOpacity={0.3}
                  name="US Tariff Rate"
                />
              )}
              {(country === 'both' || country === 'china') && (
                <Line 
                  type="monotone" 
                  dataKey="china_general" 
                  stroke="#e74c3c" 
                  strokeWidth={3}
                  name="China Tariff Rate"
                />
              )}
            </ComposedChart>
          )}
        </ResponsiveContainer>
      </div>

      <div className="chart-stats">
        <div className="stat-box">
          <h4>Current US Rate</h4>
          <p className="stat-value">47.5%</p>
          <p className="stat-change">↑ +10.5% from Oct 2024</p>
        </div>
        <div className="stat-box">
          <h4>Current China Rate</h4>
          <p className="stat-value">31.9%</p>
          <p className="stat-change">↑ +6.9% from Oct 2024</p>
        </div>
        <div className="stat-box">
          <h4>Peak Rate</h4>
          <p className="stat-value">47.5%</p>
          <p className="stat-change">Reached Nov 2025</p>
        </div>
      </div>

      <div className="chart-info">
        <h3>📌 About This Chart</h3>
        <p>
          This chart shows the historical progression of tariff rates between the US and China 
          from January 2018 to the present. The data visualizes:
        </p>
        <ul>
          <li><strong>Blue line:</strong> US average tariff rates</li>
          <li><strong>Red line:</strong> China average tariff rates</li>
          <li><strong>Orange line (dashed):</strong> US tariffs on Chinese exports</li>
          <li><strong>Purple line (dashed):</strong> China tariffs on US exports</li>
        </ul>
        <p>
          <strong>Key Events:</strong> 2018 Trade War escalation → 2019 Rate Peak → 2020-2023 Stability → 2024-2025 Renewed escalation
        </p>
      </div>
    </div>
  );
}

export default TariffChart;
