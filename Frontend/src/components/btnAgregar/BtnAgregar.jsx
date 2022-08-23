import './btnAgregar.css'

export default function BtnAgregar() {
  const handleClick = () => {
    alert('Aca se abrira el modal para agregar dispositivos')
  }
  return (
    <div className='divBtnAgregar' onClick={handleClick}>
      <svg
        width='116'
        height='116'
        viewBox='0 0 116 116'
        fill='none'
        xmlns='http://www.w3.org/2000/svg'
      >
        <g filter='url(#filter0_dd_284_7817)'>
          <circle cx='58' cy='58' r='28' fill='white' />
          <circle cx='58' cy='58' r='27.5' stroke='#264653' />
        </g>
        <g filter='url(#filter1_d_284_7817)'>
          <rect x='55' y='40' width='7' height='36' fill='#264653' />
          <rect
            x='40'
            y='62'
            width='7'
            height='36'
            transform='rotate(-90 40 62)'
            fill='#264653'
          />
        </g>
        <defs>
          <filter
            id='filter0_dd_284_7817'
            x='0'
            y='0'
            width='116'
            height='116'
            filterUnits='userSpaceOnUse'
            color-interpolation-filters='sRGB'
          >
            <feFlood flood-opacity='0' result='BackgroundImageFix' />
            <feColorMatrix
              in='SourceAlpha'
              type='matrix'
              values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'
              result='hardAlpha'
            />
            <feOffset dx='-10' dy='-10' />
            <feGaussianBlur stdDeviation='10' />
            <feComposite in2='hardAlpha' operator='out' />
            <feColorMatrix
              type='matrix'
              values='0 0 0 0 0.992157 0 0 0 0 0.980392 0 0 0 0 0.980392 0 0 0 0.1 0'
            />
            <feBlend
              mode='normal'
              in2='BackgroundImageFix'
              result='effect1_dropShadow_284_7817'
            />
            <feColorMatrix
              in='SourceAlpha'
              type='matrix'
              values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'
              result='hardAlpha'
            />
            <feOffset dx='10' dy='10' />
            <feGaussianBlur stdDeviation='10' />
            <feComposite in2='hardAlpha' operator='out' />
            <feColorMatrix
              type='matrix'
              values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1 0'
            />
            <feBlend
              mode='normal'
              in2='effect1_dropShadow_284_7817'
              result='effect2_dropShadow_284_7817'
            />
            <feBlend
              mode='normal'
              in='SourceGraphic'
              in2='effect2_dropShadow_284_7817'
              result='shape'
            />
          </filter>
          <filter
            id='filter1_d_284_7817'
            x='37'
            y='37'
            width='44'
            height='44'
            filterUnits='userSpaceOnUse'
            color-interpolation-filters='sRGB'
          >
            <feFlood flood-opacity='0' result='BackgroundImageFix' />
            <feColorMatrix
              in='SourceAlpha'
              type='matrix'
              values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'
              result='hardAlpha'
            />
            <feOffset dx='1' dy='1' />
            <feGaussianBlur stdDeviation='2' />
            <feComposite in2='hardAlpha' operator='out' />
            <feColorMatrix
              type='matrix'
              values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0'
            />
            <feBlend
              mode='normal'
              in2='BackgroundImageFix'
              result='effect1_dropShadow_284_7817'
            />
            <feBlend
              mode='normal'
              in='SourceGraphic'
              in2='effect1_dropShadow_284_7817'
              result='shape'
            />
          </filter>
        </defs>
      </svg>
      <h2>agregar nuevo dispositivo</h2>
    </div>
  )
}
