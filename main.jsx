import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  const [url, setUrl] = useState('');
  const [output, setOutput] = useState('');

  const handleSubmit = async () => {
    const res = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ playlistUrl: url }),
    });
    const data = await res.json();
    setOutput(data.analysis);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Auralysis</h1>
      <input
        type="text"
        placeholder="Paste Spotify playlist URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: '300px', marginRight: '1rem' }}
      />
      <button onClick={handleSubmit}>Analyze</button>
      <pre style={{ marginTop: '2rem' }}>{output}</pre>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);