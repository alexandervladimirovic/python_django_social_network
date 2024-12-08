document.addEventListener('DOMContentLoaded', () => {
    const postsDiv = document.getElementById('posts');

    fetch('/api/posts/')
        .then(response => response.json())
        .then(data => {
            data.forEach(post => {
                const postElement = document.createElement('div');
                postElement.innerHTML = `
                    <h3>${post.author_username}</h3>
                    <p>${post.content}</p>
                    <small>${new Date(post.created_at).toLocaleString()}</small>
                `;
                postsDiv.appendChild(postElement);
            });
        })
        .catch(error => console.error('Error:', error));
});