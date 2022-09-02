import CircularSlider from '@fseehawer/react-circular-slider'

export default function Ruedita() {
  return (
    <CircularSlider
      width={400}
      min={0}
      max={100}
      offsetAngle={-45}
      dataIndex={17}
      labelOffset={10}
      knobPosition='left'
      labelBottom='true'
      arcSize={270}
      valueFontSize='2rem'
      renderLabelValue={null}
      progressLineCap='flat'
      progressSize={24}
      trackColor='#eeeeee'
      trackSize={24}
      knobColor='blue'
      knobSize={56}
      onChange={(value) => {
        console.log(value)
      }}
    />
  )
}
