const API_BASE = '/api/v1';
let currentToken = localStorage.getItem('vidyalaya_token');

async function handleLogin() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorEl = document.getElementById('auth-error');

    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);

    try {
        const response = await fetch(`${API_BASE}/login/access-token`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error('Invalid credentials');

        const { access_token } = await response.json();
        localStorage.setItem('vidyalaya_token', access_token);
        currentToken = access_token;
        document.getElementById('auth-overlay').style.display = 'none';
        initDashboard();
    } catch (err) {
        errorEl.textContent = err.message;
        errorEl.style.display = 'block';
    }
}

function handleLogout() {
    localStorage.removeItem('vidyalaya_token');
    location.reload();
}

async function fetchWithAuth(endpoint) {
    const res = await fetch(`${API_BASE}${endpoint}`, {
        headers: { 'Authorization': `Bearer ${currentToken}` }
    });
    if (res.status === 403 || res.status === 401) {
        document.getElementById('auth-overlay').style.display = 'flex';
        return null;
    }
    const json = await res.json();
    return json.data;
}

async function initDashboard() {
    if (!currentToken) {
        document.getElementById('auth-overlay').style.display = 'flex';
        return;
    }

    const user = await fetchWithAuth('/me');
    if (user) {
        document.getElementById('user-display').textContent = user.full_name || user.email;
        showSection('students');
    }
}

async function showSection(section) {
    const title = document.getElementById('section-title');
    const head = document.getElementById('table-head');
    const body = document.getElementById('table-body');
    
    // Update nav active state
    document.querySelectorAll('nav a').forEach(a => {
        a.classList.toggle('active', a.textContent.toLowerCase().includes(section.slice(0,3)));
    });

    head.innerHTML = '';
    body.innerHTML = '<tr><td colspan="5">Loading...</td></tr>';

    let data = [];
    switch(section) {
        case 'students':
            title.textContent = 'Students Registry';
            data = await fetchWithAuth('/students');
            if (!data) return;
            head.innerHTML = '<th>ID</th><th>Full Name</th><th>Nationality ID</th>';
            body.innerHTML = data.map(s => `
                <tr>
                    <td>${s.id}</td>
                    <td>${s.first_name} ${s.last_name}</td>
                    <td>${s.nationality_id}</td>
                </tr>
            `).join('');
            document.getElementById('stat-students').textContent = data.length;
            break;
        case 'academic':
            title.textContent = 'Academic Years';
            // Placeholder for other sections - standard API fetch would go here
            body.innerHTML = '<tr><td colspan="5">Academic year management coming soon.</td></tr>';
            break;
        default:
            body.innerHTML = '<tr><td colspan="5">Feature under development.</td></tr>';
    }
}

// Start
initDashboard();
