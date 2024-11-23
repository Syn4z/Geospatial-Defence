import '../assets/css/Metric.css'

const Metric = ({ name, value, label, info, priority, unit, imgPath }) => {
  let wrapperClass = 'metric-wrapper';
  if (priority === 'high') {
    wrapperClass += ' danger';
  } else if (priority === 'medium') {
    wrapperClass += ' warning';
  } else {
    wrapperClass += ' healthy';
  }

  return (
    <div className={wrapperClass}>
      <div className="metric-header">
        <img className='metric-icon' src={imgPath} alt={name} />
        <h3 className="metric-title">{name}</h3>
      </div>
      <div className="metric-body">
        <p className="metric-value">
          <span className="metric-label">{label}</span>:  {value} {unit}
        </p>
        <p className="metric-value">
          <span className='metric-label'>Status</span>: {info}
        </p>
      </div>
    </div>
  )
}

export default Metric