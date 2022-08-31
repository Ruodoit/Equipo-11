import './lista.css'
import { useState, useEffect } from 'react'
import BtnAgregar from '../../components/btnAgregar/BtnAgregar'
import ListaItem from '../../components/listaItem/ListaItem'

export default function Lista() {
  const [aire, setAire] = useState([])
  const getAire = async () => {
    const res = await fetch('/aires.json')
    let json = await res.json()
    setAire(json.Aires)
  }
  useEffect(() => {
    getAire()
  }, [])

  const [ventilador, setVentilador] = useState([])
  const getVentilador = async () => {
    const res = await fetch('/ventiladores.json')
    let json = await res.json()
    setVentilador(json.VENTILADORES)
  }
  useEffect(() => {
    getVentilador()
  }, [])

  return (
    <div className='lista'>
      <BtnAgregar></BtnAgregar>
      {aire.map((aire, index) => (
          <ListaItem dispositivo={aire} key={index} />
      ))}
      {ventilador.map((ventilador) => (
        <ListaItem dispositivo={ventilador} key={ventilador[0]} />
      ))}
    </div>
  )
}
