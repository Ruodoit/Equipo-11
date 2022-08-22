import './menu.css'

export default function Menu() {
  const handleClick = () => {
    alert('Aca se abrira el modal para agregar dispositivos')
  }
  const handleConfiguracion = () => {
    alert('Aca se abrira el modal con las configuraciones')
  }


  return (
    <div className='menu'>
      <button className='btnMenu'>
        <span class='material-icons'>horizontal_split</span>
        <p className='btnTxt'>DISPOSITIVOS</p>
      </button>
      <button className='btnMenu' onClick={handleClick}>
        <span class='material-icons'>add_circle_outline</span>
        <p className='btnTxt'>AGREGAR</p>
      </button>
      <button className='btnMenu'onClick={handleConfiguracion}>
        <span class='material-icons'>horizontal_split</span>
        <p className='btnTxt'>CONFIGURACION</p>
      </button>
    </div>
  )
}
