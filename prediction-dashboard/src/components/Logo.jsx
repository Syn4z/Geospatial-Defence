import logoImg from '../assets/icons/logo.png'
import '../assets/css/Logo.css'

const Logo = () => {
  return (
    <div className="logo-wrapper">
      <img className='logo-img' src={logoImg} alt="logo" />
      <h1 className='logo-title'>Agrofy</h1>
      <img className='logo-img' src={logoImg} alt="logo" />
    </div>
  )
}

export default Logo