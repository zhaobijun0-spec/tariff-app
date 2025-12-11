import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import Dashboard from './components/Dashboard';
import TariffList from './components/TariffList';
import ChangeLog from './components/ChangeLog';
import TariffChart from './components/TariffChart';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [stats, setStats] = useState(null);
  const [activeTab, setActiveTab] = useState('dashboard');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();
    const interval = setInterval(fetchStats, 300000); // Refresh every 5 minutes
    return () => clearInterval(interval);
  }, []);

  const fetchStats = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/stats`);
      setStats(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Failed to fetch stats:', error);
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="header">
        <h1>📊 Tariff Dashboard</h1>
        <p>Track US and China tariff rates daily</p>
      </header>

      <nav className="tabs">
        <button 
          className={`tab ${activeTab === 'dashboard' ? 'active' : ''}`}
          onClick={() => setActiveTab('dashboard')}
        >
          Dashboard
        </button>
        <button 
          className={`tab ${activeTab === 'chart' ? 'active' : ''}`}
          onClick={() => setActiveTab('chart')}
        >
          📈 Trends
        </button>
        <button 
          className={`tab ${activeTab === 'tariffs' ? 'active' : ''}`}
          onClick={() => setActiveTab('tariffs')}
        >
          All Tariffs
        </button>
        <button 
          className={`tab ${activeTab === 'changes' ? 'active' : ''}`}
          onClick={() => setActiveTab('changes')}
        >
          Recent Changes
        </button>
      </nav>

      <main className="content">
        {loading ? (
          <div className="loading">Loading data...</div>
        ) : (
          <>
            {activeTab === 'dashboard' && <Dashboard stats={stats} />}
            {activeTab === 'chart' && <TariffChart apiUrl={API_URL} />}
            {activeTab === 'tariffs' && <TariffList apiUrl={API_URL} />}
            {activeTab === 'changes' && <ChangeLog apiUrl={API_URL} />}
          </>
        )}
      </main>

      <footer className="footer">
        <p>Data sources: US Customs, China Customs • Updates daily at 00:00 GMT</p>
      </footer>
    </div>
  );
}

export default App;
