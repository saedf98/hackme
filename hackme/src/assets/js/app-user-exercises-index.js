const editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");


document.getElementById('language').addEventListener('change', function() {
    const language = this.value;
    const mode = language === 'python' ? 'ace/mode/python' : 'ace/mode/javascript';
    editor.session.setMode(mode);
});

function runCode() {
    const language = 'python';
    const code = editor.getValue();
    const libraries = "";

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
        if(data.output != ""){
          document.getElementById("submit-exercise").removeAttribute("disabled");
        }else{
          document.getElementById("submit-exercise").setAttribute("disabled", "true");
        }
    })
    .catch(error => {
        document.getElementById('output').innerText = 'Error: ' + error;
        document.getElementById("submit-exercise").setAttribute("disabled", "true");
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


document.getElementById("submit-exercise").addEventListener("click", (e) => {
  e.preventDefault();
  const form = e.target.closest("form");
  output =  document.getElementById('output').innerText;
  document.getElementById("solution_output").value = output
  document.getElementById("solution").value = editor.getValue()
  // alert(editor.getValue())
  // Submit the form after showing the alert
  if (form && output) {
    form.submit();
  }
})
