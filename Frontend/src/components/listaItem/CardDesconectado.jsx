import './listaItem.css'
import imgVentilador from '../../assets/statics/vent-rojo.png'
import imgAireGris from '../../assets/statics/aire-gris.png'

export default function CardDesconectado(props) {
    const { dispositivo } = props
    const handleEditar = () => {
        alert('Aca se abrira el modal con las configuraciones')
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
        <span className='material-icons puntitos' onClick={handleEditar}>
          more_vert
        </span>
      </div>
    </div>

    <div className='itemDetalles'>
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

