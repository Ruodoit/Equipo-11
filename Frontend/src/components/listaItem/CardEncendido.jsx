import './listaItem.css'
import { Link } from 'react-router-dom'
import imgVentilador from '../../assets/statics/vent-rojo.png'
import imgAireGris from '../../assets/statics/aire-gris.png'

export default function CardEncendido(props) {
  const { dispositivo } = props
  const handleEditar = () => {
    alert('Aca se abrira el modal con las configuraciones')
  }

  return (
    <Link to={`/dispositivo/:${dispositivo[0]}`} className='link'>
      <div className='itemActivo'>
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
        <div className='itemActivoDetalles'>
          {dispositivo[8] ? (
            <button>frio/calor</button>
          ) : (
            <button>velocidad</button>
          )}

          <button>sleep</button>
          <div className='encendido'>
            <span className='material-icons'>power_settings_new</span>
            <p className='infoTxt'>ON</p>
          </div>
        </div>
      </div>
    </Link>
  )
}
