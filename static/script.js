function calcularRuta() {
    fetch('/hill_climbing')
    .then(response => response.json())
    .then(data => {
        const resultadoDiv = document.getElementById('resultado');
        resultadoDiv.innerHTML = `
            <h2>Ruta Óptima</h2>
            <p>${data.ruta.join(' ➔ ')}</p>
            <h3>Distancia Total: ${data.distancia_total.toFixed(4)}</h3>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
