(function () {
  // D-day and status badges: computed in the browser so the static site stays
  // accurate between builds (deadline passing, call opening, deadline approaching).
  var LABEL = { open: "모집중", soon: "마감임박", closed: "마감" };
  var today = new Date();
  today.setHours(0, 0, 0, 0);

  function setStatus(card, status) {
    card.setAttribute("data-status", status);
    var badge = card.querySelector(".badge");
    if (badge) {
      badge.textContent = LABEL[status];
      badge.className = "badge b-" + status;
    }
  }

  document.querySelectorAll("[data-deadline]").forEach(function (el) {
    var d = new Date(el.getAttribute("data-deadline") + "T00:00:00");
    if (isNaN(d)) return;
    var diff = Math.round((d - today) / 86400000);
    var card = el.closest("[data-status]");
    if (diff < 0) {
      el.textContent = "마감";
      el.classList.remove("hot");
      if (card) setStatus(card, "closed");
      return;
    }
    el.textContent = "D-" + diff;
    if (diff <= 14) el.classList.add("hot");
    if (!card) return;
    var status = card.getAttribute("data-status");
    var openAttr = card.getAttribute("data-open-date");
    if (status === "planned") {
      // Flip to open only when the announced opening date has arrived.
      if (openAttr && !(today < new Date(openAttr + "T00:00:00"))) {
        setStatus(card, diff <= 14 ? "soon" : "open");
      }
    } else if (status === "open" || status === "soon") {
      setStatus(card, diff <= 14 ? "soon" : "open");
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
