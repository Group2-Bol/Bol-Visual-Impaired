const imageInput = document.querySelector("#imageInput");
var uploadedImage = "";

imageInput.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        uploadedImage = reader.result;
        document.querySelector("#displayImage").style.backgroundImage = "url(" + uploadedImage + ")";
        document.querySelector("#displayImageText").style.display = "none";
    })
    reader.readAsDataURL(this.files[0]);
})