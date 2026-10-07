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

  // Tag filter chips + "모집중만 보기" toggle.
  var chips = document.querySelectorAll(".chip[data-filter]");
  var cards = document.querySelectorAll(".card[data-tags]");
  var toggle = document.getElementById("open-only");
  var tag = "all";
  var OPEN = ["open", "soon", "always"];

  function apply() {
    cards.forEach(function (c) {
      var tagOk = tag === "all" || c.getAttribute("data-tags").split(" ").indexOf(tag) !== -1;
      var statusOk = !toggle || !toggle.checked || OPEN.indexOf(c.getAttribute("data-status")) !== -1;
      c.style.display = tagOk && statusOk ? "" : "none";
    });
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      tag = chip.getAttribute("data-filter");
      chips.forEach(function (c) { c.classList.toggle("on", c === chip); });
      apply();
    });
  });
  if (toggle) toggle.addEventListener("change", apply);
  // Browsers may restore a checked toggle on reload or history navigation
  // without emitting a change event.
  apply();
  window.addEventListener("pageshow", apply);
})();
