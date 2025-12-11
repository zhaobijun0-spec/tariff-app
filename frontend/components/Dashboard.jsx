import React from 'react';

function Dashboard({ stats }) {
  if (!stats) return <div>No data available</div>;

  return (
    <div className="dashboard">
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-value">{stats.us_tariffs}</div>
          <div className="stat-label">US Tariffs</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">{stats.china_tariffs}</div>
          <div className="stat-label">China Tariffs</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">{stats.total_tariffs}</div>
          <div className="stat-label">Total Tariffs</div>
        </div>
        <div className="stat-card">
          <div className="stat-value">{stats.recent_changes_7d}</div>
          <div className="stat-label">Changes (7 days)</div>
        </div>
      </div>
      
      <div className="info-section">
        <h2>📌 About This Dashboard</h2>
        <p>This dashboard tracks tariff rate changes between the United States and China.</p>
        <ul>
          <li>Data updates automatically every 24 hours</li>
          <li>Sources: US Customs, China Customs</li>
          <li>Filter by country and HS code</li>
          <li>View historical changes over time</li>
        </ul>
      </div>
    </div>
  );
}

export default Dashboard;
