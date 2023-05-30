let form = document.querySelector('form#add-ai');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    let nameValue = form.elements['name'].value;
    let urlValue = form.elements['url'].value;
    let taskValue = form.elements['tasks'].value;
    let fieldValue = form.elements['field'].value;
    let descValue = form.elements['desc'].value;

    if (!nameValue || !urlValue || !taskValue || !fieldValue || !descValue) {
        alert('Введите данные');
        return;
    }

    let data = {
        name: nameValue,
        url: urlValue,
        tasks: taskValue,
        field: fieldValue,
        desc: descValue,
    }

    fetch('/api/ai', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    }).then(res => {
        if (!res.ok) {
            res.json()
                .then(v => console.error(v))
                .catch(e => console.error(e))
        } else {
            res.json()
                .then(v => alert(v['msg']))
                .catch(e => console.error(e))
        }
    })
        .catch(err => console.error(err))

    location.href = '/'
});