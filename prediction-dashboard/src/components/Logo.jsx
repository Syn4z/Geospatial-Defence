import logoImg from '../assets/icons/logo.png'
import settingsImg from '../assets/icons/settings.png'
import '../assets/css/Logo.css'

const Logo = () => {
  return (
    <div className="logo-wrapper">
      <img className='logo-img' src={logoImg} alt="logo" />
      <h1 className='logo-title'>Agrofy</h1>
      <img className='setting-img' src={settingsImg} alt="settings" />
    </div>
  )
}

export default Logo