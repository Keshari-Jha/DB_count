function processData() {
    let inputData = document.getElementById("dataInput").value;
    
    fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: inputData })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerHTML = `
            <p><strong>IMSI:</strong> ${data.IMSI}</p>
            <p><strong>DN:</strong> ${data.DN}</p>
            <p><strong>IMEI:</strong> ${data.IMEI}</p>
            <p><strong>Total:</strong> ${data.Total}</p>
            <p><strong>Calculation:</strong> ${data.Calculation}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
}
