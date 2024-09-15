document.addEventListener('DOMContentLoaded', () => {
    const apiUrl = "http://contactlist.us-east-1.elasticbeanstalk.com/contacts";
    
    // Fetch list of all contacts and show in a table
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const tableBody = document.querySelector('#dataTable tbody');
            data.forEach(contact => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${contact.contactId}</td>
                    <td>${contact.firstName}</td>
                    <td>${contact.lastName}</td>
                    <td>${contact.company}</td>
                    <td>${contact.phone}</td>
                    <td>${contact.email}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

    // Handle POST request to add new contact
    const addContactForm = document.getElementById('addContactForm');
    addContactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        const company = document.getElementById('company').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;

        fetch("http://contactlist.us-east-1.elasticbeanstalk.com/contact", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                firstName,
                lastName,
                company,
                phone,
                email
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(newContact => {
            // Add the new contact to the table
            const tableBody = document.querySelector('#dataTable tbody');
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${newContact.contactId}</td>
                <td>${newContact.firstName}</td>
                <td>${newContact.lastName}</td>
                <td>${newContact.company}</td>
                <td>${newContact.phone}</td>
                <td>${newContact.email}</td>
            `;
            tableBody.appendChild(row);

            // Reset the form
            addContactForm.reset();
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    });
});
