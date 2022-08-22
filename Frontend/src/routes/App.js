import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from '../components/layout/Layout' 
import Dispositivo from '../containers/dispositivo/Dispositivo'
import Home from '../containers/home/Home'
function App() {
  return (
    <>
      <BrowserRouter>
        <Layout>
          <Routes>
            <Route path='/' element={<Home/>}></Route>
            <Route path='/dispositivo' element={<Dispositivo/>}></Route>
          </Routes>
        </Layout>
      </BrowserRouter>
    </>
  )
}

export default App