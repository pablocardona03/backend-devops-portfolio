document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('create-user-form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const submitButton = form.querySelector('button[type="submit"]');
    let editingUserId = null;

    // Handle form submit
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = nameInput.value.trim();
        const email = emailInput.value.trim();

        if (!name || !email) {
            alert('Please enter name and email.');
            return;
        }

        const url = editingUserId ? `/users/${editingUserId}` : '/users';
        const method = editingUserId ? 'PUT' : 'POST';

        const response = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email })
        });

        const result = await response.json();

        if (response.ok) {
            alert(result.message);
            window.location.reload();
        } else {
            alert(result.error);
        }
    });

    // Handle Edit buttons
    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', () => {
            const userId = button.dataset.id;
            const name = button.dataset.name;
            const email = button.dataset.email;

            nameInput.value = name;
            emailInput.value = email;
            editingUserId = userId;
            submitButton.textContent = 'Update User';
        });
    });

    // Handle Delete buttons
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', async () => {
            const userId = button.dataset.id;

            const confirmDelete = confirm('Are you sure you want to delete this user?');
            if (!confirmDelete) return;

            const response = await fetch(`/users/${userId}`, {
                method: 'DELETE'
            });

            const result = await response.json();

            if (response.ok) {
                alert(result.message);
                window.location.reload();
            } else {
                alert(result.error);
            }
        });
    });
});
