import './listaItem.css'

export default function ListaItem(props) {
  const { dispositivo } = props
  console.log(dispositivo[3])
  if (dispositivo[2] == null) {
    return (
      <div className='itemDesconectado'>
        <div className='itemPrincipal'>
          <span class='material-icons itemImg'>image_search</span>
          <div className='principalTxt'>
            <h2>{dispositivo[3]}</h2>
            {dispositivo[11] ? (
              <p className='infoTxt'>Aire Acondicionado</p>
            ) : (
              <p className='infoTxt'>Ventilador</p>
            )}
          </div>
          <span class='material-icons'>more_vert</span>
        </div>
        <div className='itemDetalles'>
          <div className='desconectado'>
            <span class='material-icons iconoDesconectado'>report_problem</span>
            <div className='desconectadoTxt'>
              <p className='infoTxt'>DISPOSITIVO NO ENCONTRADO.</p>
              <p className='infoTxt'>REVISE LA CONEXION</p>
            </div>
          </div>
        </div>
      </div>
    )
  } else if ((dispositivo[2] == 'conect') & (dispositivo[1] == 'on')) {
    return (
      <div className='itemActivo'>
        <div className='itemPrincipal'>
          <span class='material-icons itemImg'>image_search</span>
          <div className='principalTxt'>
            <h2>{dispositivo[3]}</h2>
            {dispositivo[11] ? (
              <p className='infoTxt'>Aire Acondicionado</p>
            ) : (
              <p className='infoTxt'>Ventilador</p>
            )}
          </div>
          <span class='material-icons puntitos'>more_vert</span>
        </div>
        <div className='itemActivoDetalles'>
          <div className='encendido'>
            <span class='material-icons'>power_settings_new</span>
            <p className='infoTxt'>ON</p>
          </div>
        </div>
      </div>
    )
  } else {
    return (
      <>
        <div className='itemInactivo'>
          <div className='itemPrincipal'>
            <span class='material-icons itemImg'>image_search</span>
            <div className='principalTxt'>
              <h2>{dispositivo[3]}</h2>
              {dispositivo[11] ? (
                <p className='infoTxt'>Aire Acondicionado</p>
              ) : (
                <p className='infoTxt'>Ventilador</p>
              )}
            </div>
            <span class='material-icons'>more_vert</span>
          </div>
          <div className='itemDetalles'>
            <div className='encendido'>
              <span class='material-icons'>power_settings_new</span>
              <p className='infoTxt'>ON</p>
            </div>
          </div>
        </div>
      </>
    )
  }
}
