

// --------------------------------
// LEAD FORM
// --------------------------------

const leadForm = document.getElementById("leadForm");
const formMessage = document.getElementById("formMessage");

if (leadForm) {

    leadForm.addEventListener("submit", function (event) {

        event.preventDefault();

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const phone = document.getElementById("phone").value.trim();


        // Basic validation

        if (name === "" || email === "" || phone === "") {

            formMessage.textContent =
                "Please fill in all the details.";

            return;
        }


        // Email validation

        const emailPattern =
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {

            formMessage.textContent =
                "Please enter a valid email address.";

            return;
        }


        // Phone validation

        const phoneDigits =
            phone.replace(/\D/g, "");

        if (phoneDigits.length < 10) {

            formMessage.textContent =
                "Please enter a valid WhatsApp number.";

            return;
        }


        // Success message

        formMessage.textContent =
            "Thank you, " + name +
            "! Your details have been received.";

        formMessage.style.color = "#ffd700";


        // Reset form

        leadForm.reset();

    });

}


// --------------------------------
// NAVIGATION
// --------------------------------

const navLinks =
    document.querySelectorAll(".navbar nav a");

navLinks.forEach(function (link) {

    link.addEventListener("click", function () {

        navLinks.forEach(function (item) {
            item.classList.remove("active");
        });

        link.classList.add("active");

    });

});


// --------------------------------
// BUTTON ANIMATION
// --------------------------------

const buttons =
    document.querySelectorAll(".primary-button, .secondary-button");

buttons.forEach(function (button) {

    button.addEventListener("click", function () {

        button.style.transform = "scale(0.97)";

        setTimeout(function () {

            button.style.transform = "";

        }, 120);

    });

});


// --------------------------------
// FAQ
// --------------------------------

const faqItems =
    document.querySelectorAll(".faq-list details");

faqItems.forEach(function (item) {

    item.addEventListener("toggle", function () {

        if (item.open) {

            faqItems.forEach(function (otherItem) {

                if (otherItem !== item) {
                    otherItem.removeAttribute("open");
                }

            });

        }

    });

});


// --------------------------------
// CONSOLE MESSAGE
// --------------------------------

console.log(
    "DIL Website loaded successfully."
);

console.log(
    "Digital Iconic Lions 🚀"
);

