import './homeItemLista.css'

export default function HomeItemLista() {
  return (
    <>
      <div className='itemInactivo'>
        <div className='itemPrincipal'>
          <span class='material-icons itemImg'>image_search</span>
          <div>
            <h2>Aire 1</h2>
            <p className='infoTxt'>Aire Acondicionado</p>
          </div>
          <span class='material-icons'>more_vert</span>
        </div>
        <div className='itemDetalles'>
          <span class='material-icons'>power_settings_new</span>
        </div>
      </div>
      <div className='itemDesconectado'>
        <div className='itemPrincipal'>
          <span class='material-icons itemImg'>image_search</span>
          <div>
            <h2>Aire 1</h2>
            <p className='infoTxt'>Aire Acondicionado</p>
          </div>
          <span class='material-icons'>more_vert</span>
        </div>
        <div className='itemDetalles'>
          <span class='material-icons'>power_settings_new</span>
        </div>
      </div>
      <div className='itemActivo'>
        <div className='itemPrincipal'>
          <span class='material-icons itemImg'>image_search</span>
          <div>
            <h2>Aire 1</h2>
            <p className='infoTxt'>Aire Acondicionado</p>
          </div>
          <span class='material-icons puntitos'>more_vert</span>
        </div>
        <div className='itemActivoDetalles'>
          <span class='material-icons'>power_settings_new</span>
        </div>
      </div>

    </>
  )
}
