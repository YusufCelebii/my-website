document.addEventListener("DOMContentLoaded", function() {
    const toggleDarkMode = document.getElementById("toggleDarkMode");
    const content = document.querySelector(".content");
    const sunIcon = document.querySelector(".sun-icon");
    const moonIcon = document.querySelector(".moon-icon");

    const darkModePreference = localStorage.getItem("darkModeActive");

    if (darkModePreference === "true") {
        content.classList.add("dark-mode");
        toggleDarkMode.checked = true;
    }

    function updateIcons() {
        if (content.classList.contains("dark-mode")) {
            sunIcon.style.textShadow = "none";
            sunIcon.style.opacity = "0.3";
            moonIcon.style.textShadow = "0px 0px 20px rgba(255, 255, 150, 1)";
            moonIcon.style.opacity = "1";
        } else {
            sunIcon.style.textShadow = "0px 0px 20px rgba(255, 204, 0, 1)";
            sunIcon.style.opacity = "1";
            moonIcon.style.textShadow = "none";
            moonIcon.style.opacity = "0.3";
        }
    }

    toggleDarkMode.addEventListener("change", function() {
        content.classList.toggle("dark-mode");

        const isDarkModeActive = content.classList.contains("dark-mode");

        localStorage.setItem("darkModeActive", isDarkModeActive);

        updateIcons();
    });

    updateIcons();
});
