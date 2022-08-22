import './lista.css'
import { useState, useEffect } from 'react'
import ListaItem from '../../components/listaItem/ListaItem'

export default function Lista() {
  const [aire, setAire] = useState([])
  const getAire = async () => {
    const res = await fetch('/aires2.json')
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
      {aire.map((aire) => (
        <ListaItem dispositivo={aire} key={aire[0]}/>
      ))}
            {ventilador.map((ventilador) => (
        <ListaItem dispositivo={ventilador} key={ventilador[0]}/>
      ))}

    </div>
  )
}
