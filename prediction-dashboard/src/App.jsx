import './assets/css/App.css'
import Location from './components/Location'
import Logo from './components/Logo';
import Metric from './components/Metric'

function App() {
  const metrics = [
    { name: 'Flood Risk', label: 'Probability', value: 20, priority: 'low', imgPath: '/src/assets/icons/metrics/flood.png',
      unit: '%', info: 'Low flood risk. No immediate action required.'
    },
    { name: 'Drought Risk', label: 'Probability', value: 50, priority: 'high', imgPath: '/src/assets/icons/metrics/drought.png',
      unit: '%', info: 'High drought risk. Consider water-saving measures.'
    },
    { name: 'Soil Moisture', label: 'Index', value: 30, priority: 'medium', imgPath: '/src/assets/icons/metrics/soil.png',
      unit: '%', info: 'Soil moisture is low. Water plants accordingly.'
    },
    { name: 'Rainfall Accumulation', label: 'Volume', value: 0, priority: 'medium', imgPath: '/src/assets/icons/metrics/rainfall.png', 
      unit: 'mm', info: 'No rainfall accumulation. Monitor water sources.'
    }
  ];

  // Sort metrics by priority from high to low
  const sortedMetrics = metrics.sort((a, b) => {
    const priorityOrder = { high: 1, medium: 2, low: 3 };
    return priorityOrder[a.priority] - priorityOrder[b.priority];
  });

  return (
    <main className="main-wrapper">
      <Logo />
      <Location name="Chișinău, Moldova" />
      <div className="metrics-list">
        {sortedMetrics.map((metric, index) => (
          <Metric
            key={index}
            name={metric.name}
            label={metric.label}
            value={metric.value}
            priority={metric.priority}
            unit={metric.unit}
            info={metric.info}
            imgPath={metric.imgPath}
          />
        ))}
      </div>
    </main>
  ) 
}

export default App
