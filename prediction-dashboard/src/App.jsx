import './assets/css/App.css'
import Location from './components/Location'
import Logo from './components/Logo';
import MetricsList from './components/MetricsList';
import CorneliusMap from './components/CorneliusMap';

function App() {
  return (
    <main className="main-wrapper">
      <Logo />
      <Location name="Chișinău, Moldova" />
      <MetricsList />
      <CorneliusMap />
    </main>
  ) 
}

export default App
