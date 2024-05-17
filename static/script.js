document.addEventListener('DOMContentLoaded', function() {
    fetch('/date')
        .then(response => response.json())
        .then(data => {
            document.getElementById('date-container').innerText = `Current Date: ${data.date}`;
        })
        .catch(error => {
            console.error('Error fetching date:', error);
            document.getElementById('date-container').innerText = 'Error loading date';
        });
});


