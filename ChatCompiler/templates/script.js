document.addEventListener("DOMContentLoaded", function () {
  const chatContainer = document.querySelector(".chat-container");
  const toggleButtons = document.querySelectorAll(".toggle-btn");

  toggleButtons.forEach((button) => {
    button.addEventListener("click", function () {
      toggleButtons.forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");
      const width = this.dataset.width;
      chatContainer.className = "chat-container " + width;
    });
  });

  // 默认激活宽屏按钮
  document.querySelector('.toggle-btn[data-width="medium"]').click();
});
