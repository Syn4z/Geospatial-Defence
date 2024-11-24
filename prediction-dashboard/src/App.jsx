import './assets/css/App.css'
import Main from './components/Main'
import UserInfo from './components/UserInfo'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/userinfo" element={<UserInfo />} />
      </Routes>
    </Router>
  ) 
}

export default App
