const myBtn = document.getElementsByClassName('confirm-purchase')


for(let i=0; i < myBtn.length ; i++){
    myBtn[i].addEventListener('click', () => {
        var productId = myBtn[i].dataset.product
        var action = myBtn[i].dataset.action

        updateUserOrder(productId, action)
    })
}

function updateUserOrder(productId, action){
    console.log('Sending data')

    var url = '/products/success/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action}),
    })

        .then((response) => {
            return response.json()
        })
    .then((data) => {
            console.log('data:', data)
        })
}