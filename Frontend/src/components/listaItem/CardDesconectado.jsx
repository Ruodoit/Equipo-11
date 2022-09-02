import './listaItem.css'
import { useNavigate } from 'react-router-dom'
import BtnEditar from './BtnEditar'
import imgVentilador from '../../assets/statics/vent-rojo.png'
import imgAireGris from '../../assets/statics/aire-gris.png'

export default function CardDesconectado(props) {
  const { dispositivo } = props
  let direccion = useNavigate()
  const irADispositivo = () => {
    let ruta = `/dispositivo/:${dispositivo[0]}`
    direccion(ruta)
  }
  return (
    <div className='itemDesconectado'>
      <div>
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
          <BtnEditar></BtnEditar>
        </div>
      </div>

      <div className='itemDetalles' onClick={irADispositivo}>
        <div className='desconectado'>
          <span className='material-icons iconoDesconectado'>
            report_problem
          </span>
          <div className='desconectadoTxt'>
            <p className='infoTxt'>DISPOSITIVO NO ENCONTRADO.</p>
            <p className='infoTxt'>REVISE LA CONEXION</p>
          </div>
        </div>
      </div>
    </div>
  )
}
