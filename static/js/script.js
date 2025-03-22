document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("donorForm")?.addEventListener("submit", function(event) {
        event.preventDefault();
        alert("Donor Registered Successfully!");
    });

    document.getElementById("requestForm")?.addEventListener("submit", function(event) {
        event.preventDefault();
        alert("Blood Request Submitted!");
    });
});
