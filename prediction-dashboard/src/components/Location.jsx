import locationIcon from '../assets/icons/location.png'
import '../assets/css/Location.css'

const Location = ({ name }) => {
  return (
    <div className="location-wrapper">
      <img className='location-icon' src={locationIcon} alt="location_icon" />
      <h2 className='location-title'>{name}</h2>
    </div>
  )
}

export default Location