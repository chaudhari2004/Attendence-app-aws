async function markAttendance() {
    const name = document.getElementById("name").value;

    const res = await fetch("http://YOUR-EC2-IP:5000/mark", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name })
    });

    const data = await res.json();

    const li = document.createElement("li");
    li.innerText = data.message;

    document.getElementById("list").appendChild(li);
}