const videoElement = document.getElementById('webcam');
const captureButton = document.getElementById('captureButton');
const canvas = document.getElementById('capturedImage');
const ctx = canvas.getContext('2d');

async function startWebcam() {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoElement.srcObject = stream;
}

captureButton.addEventListener('click', () => {
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

    canvas.style.display = 'block';
});

startWebcam();
