import CircularSlider from '@fseehawer/react-circular-slider'

export default function Ruedita() {
  return (
    <CircularSlider
      onChange={(value) => {
        console.log(value)
      }}
    />
  )
}
