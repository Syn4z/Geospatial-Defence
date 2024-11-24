import { useNavigate } from 'react-router-dom'
import logoImg from '../assets/icons/logo.png'
import settingsImg from '../assets/icons/settings.png'
import '../assets/css/Logo.css'

const Logo = () => {
  const navigate = useNavigate()

  const handleSettingsClick = () => {
    navigate('/userinfo')
  }

  return (
    <div className="logo-wrapper">
      <img className='logo-img' src={logoImg} alt="logo" />
      <h1 className='logo-title'>Agrofy</h1>
      <a href="#" onClick={handleSettingsClick}>
        <img className='setting-img' src={settingsImg} alt="settings" />
      </a>
    </div>
  )
}

export default Logo