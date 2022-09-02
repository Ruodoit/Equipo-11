import React from 'react'

export default function Timer() {
  return (
    <div>
		<div class="columns is-centered">
			<div class="column has-text-centered">
				<div id="contenedorInputs">
					<div class="field">
						<label class="label">Minutos</label>
						<div class="control">
							<input class="input" id="minutos" type="number" placeholder="Minutos"/>
						</div>
					</div>
					<div class="field">
						<label class="label">Segundos</label>
						<div class="control">
							<input class="input" id="segundos" type="number" placeholder="Segundos"/>
						</div>
					</div>
				</div>
				<h2 id="tiempoRestante">00:00.0</h2>
				<button id="btnIniciar" class="button is-success"><span class="mdi mdi-play"></span></button>
				<button id="btnPausar" class="button is-success"><span class="mdi mdi-pause"></span></button>
				<button id="btnDetener" class="button is-success"><span class="mdi mdi-stop"></span></button>
			</div>
		</div>
    </div>
  )
}
