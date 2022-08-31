import './home.css'
import Header from '../../components/header/Header'
import Menu from '../../components/menu/Menu'
import Lista from '../lista/Lista'

export default function Home() {
  return (
    <>
      <Header></Header>
      <Lista></Lista>
      <Menu></Menu>
    </>
  )
}
