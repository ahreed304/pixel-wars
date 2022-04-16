const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const imgUrl = "https://images.unsplash.com/photo-1549740425-5e9ed4d8cd34?ixid=MXwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXwzOTU0NTB8fGVufDB8fHw%3D&ixlib=rb-1.2.1&w=1000&q=80";
const img = new Image();
const imgWidth = 100;

let html = "";
img.crossOrigin = "Anonymous";
img.onload = function() {
    canvas.width = imgWidth;
    canvas.height = (this.height * canvas.width) / this.width;
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    for (let i = 0; i < canvas.height; i++) {
        for (let j = 0; j < canvas.width; j++) {
            add(ctx.getImageData(j, i, 1, 1).data);
        }
        html += "<br />";
    }
    document.getElementById("final-image").innerHTML = html;
    canvas.parentNode.removeChild(canvas);
};

img.src = imgUrl;

function add(c) {
    html += `<span style="color: rgb(${c[0]}, ${c[1]}, ${c[2]});">&#9632;</span>`;
}



