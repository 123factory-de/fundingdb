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

  // Tag filter chips + "모집중만 보기" toggle + full-text search.
  var chips = document.querySelectorAll(".chip[data-filter]");
  var cards = document.querySelectorAll(".card[data-tags]");
  var toggle = document.getElementById("open-only");
  var input = document.getElementById("q");
  var noResults = document.querySelector(".no-results");
  var tag = "all";
  var OPEN = ["open", "soon", "always"];
  var query = "";          // current search string, lowercased
  // Search index (slug -> body+metadata text), fetched once from /index.json
  // the first time the visitor touches the search box. Until it arrives we
  // match against each card's own visible text, so title/subtitle search works
  // immediately and body search lights up as soon as the index loads.
  var index = null;
  var indexState = "idle"; // idle | loading | ready | error

  function loadIndex() {
    if (indexState !== "idle") return;
    indexState = "loading";
    fetch("/index.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        index = {};
        data.forEach(function (it) { index[it.slug] = it.text; });
        indexState = "ready";
        apply();
      })
      .catch(function () { indexState = "error"; });
  }

  function haystack(card) {
    var slug = card.getAttribute("data-slug");
    if (index && slug && index[slug] != null) return index[slug];
    return card.textContent.toLowerCase();
  }

  function apply() {
    var terms = query ? query.split(/\s+/) : [];
    var shown = 0;
    cards.forEach(function (c) {
      var tagOk = tag === "all" || c.getAttribute("data-tags").split(" ").indexOf(tag) !== -1;
      var statusOk = !toggle || !toggle.checked || OPEN.indexOf(c.getAttribute("data-status")) !== -1;
      var searchOk = true;
      if (terms.length) {
        var hay = haystack(c);
        for (var i = 0; i < terms.length; i++) {
          if (hay.indexOf(terms[i]) === -1) { searchOk = false; break; }
        }
      }
      var ok = tagOk && statusOk && searchOk;
      c.style.display = ok ? "" : "none";
      if (ok) shown++;
    });
    if (noResults) noResults.hidden = shown !== 0;
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      tag = chip.getAttribute("data-filter");
      chips.forEach(function (c) { c.classList.toggle("on", c === chip); });
      apply();
    });
  });
  if (toggle) toggle.addEventListener("change", apply);

  if (input) {
    var debounce;
    input.addEventListener("focus", loadIndex);
    input.addEventListener("input", function () {
      loadIndex();
      clearTimeout(debounce);
      debounce = setTimeout(function () {
        query = input.value.trim().toLowerCase();
        apply();
      }, 120);
    });
  }

  function syncFromControls() {
    // Browsers may restore a typed query or checked toggle on reload or history
    // navigation without emitting events.
    if (input) {
      query = input.value.trim().toLowerCase();
      if (query) loadIndex();
    }
    apply();
  }
  syncFromControls();
  window.addEventListener("pageshow", syncFromControls);
})();
