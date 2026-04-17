document.getElementById('form').addEventListener('submit', function(event) {
    const confirmed = confirm("Please make sure these are the correct details of the show.");
    if (!confirmed) {
        event.preventDefault();
    }
})