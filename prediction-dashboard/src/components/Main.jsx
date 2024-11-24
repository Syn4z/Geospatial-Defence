import Logo from "./Logo"
import Location from "./Location"
import MetricsList from "./MetricsList"
import CorneliusMap from "./CorneliusMap"
import Footer from "./Footer"
import '../assets/css/Main.css'

const Main = () => {
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

  return (
    <main className="main-wrapper">
      <Logo />
      <Location name="Chișinău, Moldova" />
      <MetricsList metrics={metrics} />
      <CorneliusMap />
      <Footer />
    </main>
  )
}

export default Main