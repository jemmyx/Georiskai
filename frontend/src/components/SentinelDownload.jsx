import React, { useState } from 'react';
import axios from 'axios';

export default function SentinelDownload() {
  const [message, setMessage] = useState("");

  const handleDownload = async () => {
    setMessage("Téléchargement en cours...");
    try {
      const response = await axios.post('http://localhost:8000/download-sentinel', {
        min_lon: 6.6,
        min_lat: 46.5,
        max_lon: 6.7,
        max_lat: 46.6
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Erreur lors du téléchargement.");
    }
  };

  return (
    <div>
      <button onClick={handleDownload}>🛰️ Télécharger image Sentinel</button>
      <p>{message}</p>
    </div>
  );
}
