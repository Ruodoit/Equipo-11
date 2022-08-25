import './listaItem.css'
import imgVentilador from '../../assets/statics/vent-rojo.png'
import imgAireGris from '../../assets/statics/aire-gris.png'

export default function CardApagado(props) {
  const { dispositivo } = props
  const handleEditar = () => {
    alert(dispositivo[8])
  }

  return (
    <>
      <div className='itemInactivo'>
        <div className='itemPrincipal'>
          <div className='contenedorImg'>
            {dispositivo[8] ? (
                
              <img src={imgAireGris} alt='' className='imgItem' />
            ) : (
              <img src={imgVentilador} alt='' className='imgItem' />
            )}
          </div>
          <div className='principalTxt'>
            <h2>{dispositivo[3]}</h2>
            {dispositivo[8] ? (
              <p className='infoTxt'>Aire Acondicionado</p>
            ) : (
              <p className='infoTxt'>Ventilador</p>
            )}
          </div>
          <span className='material-icons puntitos' onClick={handleEditar}>
            more_vert
          </span>
        </div>
        <div className='itemDetalles'>
          <div className='encendido'>
            <span className='material-icons'>power_settings_new</span>
            <p className='infoTxt'>OFF</p>
          </div>
        </div>
      </div>
    </>
  )
}
