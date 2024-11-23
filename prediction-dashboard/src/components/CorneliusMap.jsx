import { useState } from 'react'
import soilMap from '../assets/maps/soil_map.mp4'
import moistureMap from '../assets/maps/moisture_map.mp4'
import '../assets/css/CorneliusMap.css'

const CorneliusMap = () => {
  const [activeMap, setActiveMap] = useState('soil')

  const handleButtonClick = (map) => {
    setActiveMap(map)
  }

  return (
    <div className='map-wrapper'>
      <h2 className="section-title">Map</h2>
      <div className="map-buttons">
        <button 
        className={`map-button ${activeMap === 'soil' ? 'active' : ''}`}
        onClick={() => handleButtonClick('soil')}
        >
          Soil
        </button>
        <button
        className={`map-button ${activeMap === 'moisture' ? 'active' : ''}`}
        onClick={() => handleButtonClick('moisture')}
        >
          Moisture
        </button>
      </div>
      <div className="video-wrapper">
        {activeMap === 'soil' ? (
          <video className='map-video' autoPlay loop muted key="soil">
            <source src={soilMap} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        ) : (
          <video className='map-video' autoPlay loop muted key="moisture">
            <source src={moistureMap} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        )}
      </div>
    </div>
  )
}

export default CorneliusMap