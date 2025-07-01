import MapViewer from './components/MapViewer';
import SentinelDownload from './components/SentinelDownload';

function App() {
  return (
    <div>
      <h1>GeoRiskAI</h1>
      <SentinelDownload />
      <MapViewer />
    </div>
  );
}

export default App;