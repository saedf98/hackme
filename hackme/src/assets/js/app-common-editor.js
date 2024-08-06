const editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");


document.getElementById('language').addEventListener('change', function() {
    const language = this.value;
    const mode = language === 'python' ? 'ace/mode/python' : 'ace/mode/javascript';
    editor.session.setMode(mode);
});

function runCode() {
    const language = document.getElementById('language').value;
    const code = editor.getValue();
    const libraries = document.getElementById('libraries').value.split(',');

    fetch('/run-code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ language, code, libraries }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.output;
    })
    .catch(error => {
        document.getElementById('output').innerText = 'Error: ' + error;
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
