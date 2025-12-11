const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
const outputArea = document.getElementById('outputArea');

uploadBtn.addEventListener('click', function() {
    const file = fileInput.files[0];

    if (!file) {
        alert("გთხოვთ, ჯერ აირჩიოთ ფაილი!");
        return;
    }

    if (file.type && !file.type.startsWith('text/')) {
        alert("გთხოვთ ატვირთოთ მხოლოდ ტექსტური ფაილი (.txt)");
        return;
    }

    const reader = new FileReader();

    reader.onload = function(e) {
        const content = e.target.result;
        outputArea.textContent = content;
        outputArea.classList.remove('hidden');
    };

    reader.readAsText(file);
});