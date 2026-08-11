(function () {
  // D-day: computed in the browser so the static site stays accurate between builds.
  var today = new Date();
  today.setHours(0, 0, 0, 0);
  document.querySelectorAll("[data-deadline]").forEach(function (el) {
    var d = new Date(el.getAttribute("data-deadline") + "T00:00:00");
    if (isNaN(d)) return;
    var diff = Math.round((d - today) / 86400000);
    var card = el.closest("[data-status]");
    if (diff < 0) {
      el.textContent = "마감";
      el.classList.remove("hot");
      if (card) {
        card.setAttribute("data-status", "closed");
        var badge = card.querySelector(".badge");
        if (badge) {
          badge.textContent = "마감";
          badge.className = "badge b-closed";
        }
      }
    } else {
      el.textContent = "D-" + diff;
      if (diff <= 14) el.classList.add("hot");
    }
  });

  // Region filter chips + "모집중만 보기" toggle.
  var chips = document.querySelectorAll(".chip[data-filter]");
  var cards = document.querySelectorAll(".card[data-regions]");
  var toggle = document.getElementById("open-only");
  var region = "all";
  var OPEN = ["open", "soon", "always"];

  function apply() {
    cards.forEach(function (c) {
      var regionOk = region === "all" || c.getAttribute("data-regions").split(" ").indexOf(region) !== -1;
      var statusOk = !toggle || !toggle.checked || OPEN.indexOf(c.getAttribute("data-status")) !== -1;
      c.style.display = regionOk && statusOk ? "" : "none";
    });
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      region = chip.getAttribute("data-filter");
      chips.forEach(function (c) { c.classList.toggle("on", c === chip); });
      apply();
    });
  });
  if (toggle) toggle.addEventListener("change", apply);
})();
