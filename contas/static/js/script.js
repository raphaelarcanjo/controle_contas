const excluir_conta = e => {
    let confirmed = confirm('Tem certeza que deseja excluir esta conta?')
    if (!confirmed) e.preventDefault()
}

const data_pagamento = el => {
    let pagamento = document.querySelector('input.pagamento')
    if (el.checked) {
        if (pagamento.value == '') {
            let data = new Date(Date.now())
            pagamento.value = data.toISOString().substring(0, 10)
        }
    } else {
        pagamento.value = ''
    }
}

document.querySelector('a.excluir').onclick = e => excluir_conta(e)