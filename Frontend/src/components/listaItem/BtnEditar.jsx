import { useState } from 'react'
import Modal from '../modal/Modal'

export default function BtnEditar() {
  const [estadoModal, setEstadoModal] = useState(false)

  return (
    <>
      <span
        className='material-icons puntitos'
        onClick={() => setEstadoModal(!estadoModal)}
      >
        more_vert
      </span>
      <Modal
        estado={estadoModal}
        setEstado={setEstadoModal}
        mostrarHeader={false}
        mostrarOverlay={true}
      >
        <div className='contenidoModal'>
          <h2>proximamente</h2>
          <p>nuevas funciones</p>
        </div>
      </Modal>
    </>
  )
}
