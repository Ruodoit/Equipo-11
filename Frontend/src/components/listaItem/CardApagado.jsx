import './listaItem.css'
import { Link } from 'react-router-dom'
import imgVentilador from '../../assets/statics/vent-rojo.png'
import imgAireGris from '../../assets/statics/aire-gris.png'
import vel from '../../assets/vel.png'
import temp from '../../assets/temp.png'
import sleep from '../../assets/sleep.png'
export default function CardApagado(props) {
  const { dispositivo } = props
  const handleEditar = () => {
    alert(dispositivo[8])
  }

  return (
    <>
      <Link to={`/dispositivo/:${dispositivo[0]}`} className='link'>
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
          <div className='itemActivoDetalles'>
            {dispositivo[8] ? (
              <button style={{ visibility: 'hidden' }}>
                {' '}
                <img src={temp} alt='' />
                <p>{dispositivo[4]}°</p>{' '}
              </button>
            ) : (
              <button style={{ visibility: 'hidden' }}>
                <img src={vel} alt='' />
                <p>{dispositivo[4]}</p>
              </button>
            )}

            <button className='indicadorSleep' style={{ visibility: 'hidden' }}>
              <img src={sleep} alt='' />
              <p>{dispositivo[dispositivo.length - 1]}</p>
            </button>
            <div className='encendido'>
              <span className='material-icons'>power_settings_new</span>
              <p className='infoTxt'>OFF</p>
            </div>
          </div>
        </div>
      </Link>
    </>
  )
}
