import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TariffList({ apiUrl }) {
  const [tariffs, setTariffs] = useState([]);
  const [country, setCountry] = useState('');
  const [hsCode, setHsCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(0);

  const fetchTariffs = async () => {
    setLoading(true);
    try {
      const params = {
        skip: page * 50,
        limit: 50
      };
      if (country) params.country = country;
      if (hsCode) params.hs_code = hsCode;

      const response = await axios.get(`${apiUrl}/api/tariffs`, { params });
      setTariffs(response.data.data);
    } catch (error) {
      console.error('Failed to fetch tariffs:', error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchTariffs();
  }, [country, hsCode, page]);

  return (
    <div className="tariff-list">
      <div className="filters">
        <div className="filter-group">
          <label>Country:</label>
          <select value={country} onChange={(e) => { setCountry(e.target.value); setPage(0); }}>
            <option value="">All</option>
            <option value="US">United States</option>
            <option value="China">China</option>
          </select>
        </div>
        <div className="filter-group">
          <label>HS Code:</label>
          <input 
            type="text" 
            value={hsCode}
            onChange={(e) => { setHsCode(e.target.value); setPage(0); }}
            placeholder="e.g., 6204.62.20"
          />
        </div>
        <button onClick={fetchTariffs} className="refresh-btn">🔄 Refresh</button>
      </div>

      {loading ? (
        <div className="loading">Loading...</div>
      ) : (
        <table className="tariff-table">
          <thead>
            <tr>
              <th>Country</th>
              <th>HS Code</th>
              <th>Product Description</th>
              <th>Tariff Rate (%)</th>
              <th>Last Updated</th>
            </tr>
          </thead>
          <tbody>
            {tariffs.map((tariff) => (
              <tr key={tariff.id}>
                <td>{tariff.country}</td>
                <td className="hs-code">{tariff.hs_code}</td>
                <td className="description">{tariff.product_description}</td>
                <td className="rate">{tariff.rate.toFixed(2)}%</td>
                <td>{new Date(tariff.last_updated).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      <div className="pagination">
        <button onClick={() => setPage(Math.max(0, page - 1))} disabled={page === 0}>← Previous</button>
        <span>Page {page + 1}</span>
        <button onClick={() => setPage(page + 1)} disabled={tariffs.length < 50}>Next →</button>
      </div>
    </div>
  );
}

export default TariffList;
