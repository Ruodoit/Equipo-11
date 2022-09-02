import { useState } from 'react'
import styled from 'styled-components'
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
        /* lo puedo sacar, queda 20px por defecto*/
        padding={'20px'}
      >
        <Contenido>
          <h2>proximamente</h2>
          <p>nuevas funciones</p>
        </Contenido>
      </Modal>
    </>
  )
}

const Contenido = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;

  h1 {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 10px;
  }

  p {
    font-size: 18px;
    margin-bottom: 20px;
  }

  img {
    width: 100%;
    vertical-align: top;
    border-radius: 3px;
  }
`
