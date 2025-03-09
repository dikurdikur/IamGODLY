async function uploadFile() {
    let fileInput = document.getElementById("fileInput").files[0];
    let promptInput = document.getElementById("promptInput").value;
    let formData = new FormData();
    formData.append("file", fileInput);
    formData.append("prompt", promptInput);

    let response = await fetch("http://localhost:8000/analyze/", {
        method: "POST",
        body: formData
    });

    let result = await response.json();
    document.getElementById("output").innerText = JSON.stringify(result, null, 2);
}
