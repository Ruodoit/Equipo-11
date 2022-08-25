import './listaItem.css'
import CardDesconectado from './CardDesconectado'
import CardEncendido from './CardEncendido'
import CardApagado from './CardApagado'
export default function ListaItem(props) {
  const { dispositivo } = props

  if (dispositivo[2] === 'no') {
    return <CardDesconectado dispositivo={dispositivo}></CardDesconectado>
  } else if ((dispositivo[2] === 'si') & (dispositivo[1] === 'si')) {
    return <CardEncendido dispositivo={dispositivo}></CardEncendido>
  } else {
    return (
      <CardApagado dispositivo={dispositivo}></CardApagado>
    )
  }
}
