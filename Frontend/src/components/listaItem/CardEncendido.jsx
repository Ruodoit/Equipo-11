import './listaItem.css'
import { useNavigate } from 'react-router-dom'
import BtnEditar from './BtnEditar'
import imgVentilador from '../../assets/statics/vent-rojo.png'
import imgAireGris from '../../assets/statics/aire-gris.png'
import vel from '../../assets/vel.png'
import temp from '../../assets/temp.png'
import sleep from '../../assets/sleep.png'

export default function CardEncendido(props) {
  const { dispositivo } = props
  let direccion = useNavigate()
  const irADispositivo = () => {
    let ruta = `/dispositivo/:${dispositivo[0]}`
    direccion(ruta)
  }

  return (
    <div className='itemActivo'>
      <div className='itemPrincipal'>
        <div className='contenedorImg' onClick={irADispositivo}>
          {dispositivo[8] ? (
            <img src={imgAireGris} alt='' className='imgItem' />
          ) : (
            <img src={imgVentilador} alt='' className='imgItem' />
          )}
        </div>
        <div className='principalTxt' onClick={irADispositivo}>
          <h2>{dispositivo[3]}</h2>
          {dispositivo[8] ? (
            <p className='infoTxt'>Aire Acondicionado</p>
          ) : (
            <p className='infoTxt'>Ventilador</p>
          )}
        </div>
        <BtnEditar></BtnEditar>
      </div>
      <div className='itemActivoDetalles' onClick={irADispositivo}>
        {dispositivo[8] ? (
          <button>
            <img src={temp} alt='' />
            <p>{dispositivo[4]}°</p>
          </button>
        ) : (
          <button>
            <img src={vel} alt='' />
            <p>{dispositivo[4]}</p>
          </button>
        )}
        <button className='indicadorSleep'>
          <img src={sleep} alt='' />
          <p>{dispositivo[dispositivo.length - 1]}</p>
        </button>
        <div className='encendido'>
          <span className='material-icons'>power_settings_new</span>
          <p className='infoTxt'>ON</p>
        </div>
      </div>
    </div>
  )
}
