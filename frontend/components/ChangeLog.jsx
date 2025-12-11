import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ChangeLog({ apiUrl }) {
  const [changes, setChanges] = useState([]);
  const [country, setCountry] = useState('');
  const [days, setDays] = useState(7);
  const [loading, setLoading] = useState(false);

  const fetchChanges = async () => {
    setLoading(true);
    try {
      const params = { days };
      if (country) params.country = country;

      const response = await axios.get(`${apiUrl}/api/changes`, { params });
      setChanges(response.data.data);
    } catch (error) {
      console.error('Failed to fetch changes:', error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchChanges();
  }, [country, days]);

  return (
    <div className="change-log">
      <div className="filters">
        <div className="filter-group">
          <label>Country:</label>
          <select value={country} onChange={(e) => setCountry(e.target.value)}>
            <option value="">All</option>
            <option value="US">United States</option>
            <option value="China">China</option>
          </select>
        </div>
        <div className="filter-group">
          <label>Time Period:</label>
          <select value={days} onChange={(e) => setDays(Number(e.target.value))}>
            <option value={1}>Last 24 hours</option>
            <option value={7}>Last 7 days</option>
            <option value={30}>Last 30 days</option>
            <option value={90}>Last 90 days</option>
          </select>
        </div>
        <button onClick={fetchChanges} className="refresh-btn">🔄 Refresh</button>
      </div>

      {loading ? (
        <div className="loading">Loading...</div>
      ) : changes.length === 0 ? (
        <div className="no-data">No tariff changes in this period</div>
      ) : (
        <div className="changes-list">
          {changes.map((change) => (
            <div key={change.id} className="change-item">
              <div className="change-header">
                <span className="country-badge">{change.country}</span>
                <span className="hs-code">{change.hs_code}</span>
                <span className="date">{new Date(change.change_date).toLocaleDateString()}</span>
              </div>
              <div className="change-rates">
                <div className="old-rate">
                  <span>Old Rate:</span>
                  <span className="rate">{change.old_rate?.toFixed(2) || 'N/A'}%</span>
                </div>
                <span className="arrow">→</span>
                <div className="new-rate">
                  <span>New Rate:</span>
                  <span className="rate highlight">{change.new_rate.toFixed(2)}%</span>
                </div>
              </div>
              {change.change_reason && (
                <div className="reason">Reason: {change.change_reason}</div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ChangeLog;
