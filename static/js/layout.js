document.addEventListener("DOMContentLoaded", function() {
    let alert = document.querySelectorAll('.alert')
    alert.forEach(function(alert) {
        setTimeout(function() {
            let bsAlert = new bootstrap.Alert(alert)
            bsAlert.close()
        }, 3000)
    })
})