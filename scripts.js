document.addEventListener("DOMContentLoaded", function() {
  const blockedNumbersForm = document.getElementById("blockedNumbersForm");
  const blockedNumbersList = document.getElementById("numbers");

  blockedNumbersForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const numberInput = document.getElementById("number");
    const number = numberInput.value.trim();

    if (number !== "") {
      const listItem = document.createElement("li");
      listItem.textContent = number;
      blockedNumbersList.appendChild(listItem);
      numberInput.value = "";
    }
  });
});
