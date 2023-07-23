alert("Hi, i am a script")

document.addEventListener("DOMContentLoaded", function () {
  const divContainer = document.createElement("div");
  divContainer.style.display = "flex";
  divContainer.style.justifyContent = "center";
  divContainer.style.alignItems = "center";
  divContainer.style.height = "100vh";

  const button = document.createElement("button");
  button.textContent = "Iniciar";
  button.onclick = function () {
    window.location.href = "index.html";
  };

  divContainer.appendChild(button);
  document.body.insertBefore(divContainer, document.body.firstChild);
});
