import Metric from './Metric'

const MetricsList = ({ metrics }) => {
  // Sort metrics by priority from high to low
  const sortedMetrics = metrics.sort((a, b) => {
    const priorityOrder = { high: 1, medium: 2, low: 3 };
    return priorityOrder[a.priority] - priorityOrder[b.priority];
  });


  return (
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
  )
}

export default MetricsList