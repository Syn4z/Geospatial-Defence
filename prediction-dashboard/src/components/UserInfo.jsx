import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import arrowIcon from '../assets/icons/arrow.png'
import '../assets/css/UserInfo.css'
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from '@mui/material/Button';
import MetricsList from './MetricsList';
import Footer from './Footer';

const UserInfo = () => {
  const [cropType, setCropType] = useState('');
  const [showResults, setShowResults] = useState(false);
  const navigate = useNavigate()

  const handleChange = (event) => {
    setCropType(event.target.value);
  };  

  const handleBackClick = () => {
    navigate('/')
  }

  const handleGetInsightsClick = () => {
    setShowResults(true);
  };

  const metrics = [
    { name: 'Crop yield', label: 'Amount', value: 30, priority: 'low', imgPath: '/src/assets/icons/metrics/success.jpg',
      unit: 'tons', info: 'Great crop yield. No immediate action required.'
    },
    { name: 'Low water supply', label: 'Volume', value: 10, priority: 'high', imgPath: '/src/assets/icons/metrics/drought.png',
      unit: 'm3', info: 'Low water supply. Consider water-saving measures.'
    },
    { name: 'Land productivity', label: 'Per unit', value: 83, priority: 'low', imgPath: '/src/assets/icons/metrics/soil.png',
      unit: '%', info: 'Amazing land productivity. No immediate action required.'
    },
    { name: 'Carbon footprint', label: 'CO2', value: 5, priority: 'medium', imgPath: '/src/assets/icons/metrics/co2.png', 
      unit: 'per ton', info: 'Medium carbon footprint. Monitor carbon emissions.'
    }
  ];

  return (
    <div className="user-info-wrapper">
      <button className="go-back-btn" type="button" onClick={handleBackClick}>
        <img className='go-back-img' src={arrowIcon} alt="go_back_button" />
      </button>

      <div className="user-inputs">
        <h2>Informations</h2>

        <TextField
            label="Water supply"
            id="outlined-start-adornment"
            sx={{ m: 1, width: '25ch' }}
            slotProps={{
              input: {
                startAdornment: <InputAdornment position="start">m3</InputAdornment>,
              },
            }}
          />

         <TextField
            label="Surface"
            id="outlined-start-adornment"
            sx={{ m: 1, width: '25ch' }}
            slotProps={{
              input: {
                startAdornment: <InputAdornment position="start">m2</InputAdornment>,
              },
            }}
          />

        <FormControl className='crop-type'>
          <InputLabel id="demo-simple-select-label">Crop type</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={cropType}
            label="Crop type"
            onChange={handleChange}
          >
            <MenuItem value={"Wheat"}>Wheat</MenuItem>
            <MenuItem value={"Corn"}>Corn</MenuItem>
            <MenuItem value={"Sunflower"}>Sunflower</MenuItem>
            <MenuItem value={"Grape"}>Grape</MenuItem>
            <MenuItem value={"Potatoes"}>Potatoes</MenuItem>
          </Select>
        </FormControl>

        <Button variant="contained" onClick={handleGetInsightsClick}>
          <b>Get insights</b>
        </Button>
      </div> 

      {showResults && (
        <>
          <div className="user-results">
            <h2>Results</h2>
            <MetricsList metrics={metrics} />
          </div>
          <Footer />
        </>
    )}

    </div>
  )
}

export default UserInfo