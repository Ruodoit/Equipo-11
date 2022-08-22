import './btnAgregar.css'

export default function BtnAgregar() {
  const handleClick = () => {
    alert('Aca se abrira el modal para agregar dispositivos')
  }
  return (
    <div className='divBtnAgregar' onClick={handleClick}>
      <span class='material-icons btnAgregar'>add_circle_outline</span>
    </div>
  )
}
