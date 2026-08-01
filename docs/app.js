const PAGE_SIZE = 24;

const state = {
  papers: [],
  filtered: [],
  visible: PAGE_SIZE,
};

const elements = {
  search: document.querySelector("#search"),
  stakeholder: document.querySelector("#stakeholder"),
  topic: document.querySelector("#topic"),
  year: document.querySelector("#year"),
  grid: document.querySelector("#paper-grid"),
  count: document.querySelector("#result-count"),
  heroCount: document.querySelector("#hero-paper-count"),
  clear: document.querySelector("#clear-filters"),
  empty: document.querySelector("#empty-state"),
  loadMore: document.querySelector("#load-more"),
  template: document.querySelector("#paper-template"),
};

const shortStakeholder = (value) => value
  .replace("Applications for ", "")
  .replace("the Sports Industry", "Sports Industry");

function uniqueSorted(values, compare = (a, b) => a.localeCompare(b)) {
  return [...new Set(values.filter(Boolean))].sort(compare);
}

function populateSelect(select, values, labeler = (value) => value) {
  values.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = labeler(value);
    select.append(option);
  });
}

function setupFilters() {
  const categories = state.papers.flatMap((paper) => paper.categories);
  populateSelect(
    elements.stakeholder,
    uniqueSorted(categories.map((item) => item.stakeholder)),
    shortStakeholder,
  );
  populateSelect(elements.topic, uniqueSorted(categories.map((item) => item.topic)));
  populateSelect(
    elements.year,
    uniqueSorted(state.papers.map((paper) => paper.year), (a, b) => b - a),
  );
}

function createLink(label, url) {
  const link = document.createElement("a");
  link.href = url;
  link.target = "_blank";
  link.rel = "noreferrer";
  link.textContent = `${label} ↗`;
  return link;
}

function renderCard(paper, index) {
  const card = elements.template.content.firstElementChild.cloneNode(true);
  card.style.animationDelay = `${Math.min(index, 12) * 28}ms`;
  card.querySelector(".paper-year").textContent = paper.year || "Year n/a";
  card.querySelector(".paper-number").textContent = String(index + 1).padStart(3, "0");
  card.querySelector("h3").textContent = paper.title;
  card.querySelector(".paper-venue").textContent = paper.venue || "Publication details unavailable";

  const tags = card.querySelector(".paper-tags");
  const tagValues = uniqueSorted(paper.categories.flatMap((item) => [shortStakeholder(item.stakeholder), item.topic]));
  tagValues.slice(0, 3).forEach((value) => {
    const tag = document.createElement("span");
    tag.textContent = value;
    tags.append(tag);
  });

  const links = card.querySelector(".paper-links");
  links.append(createLink("Paper", paper.paper));
  Object.entries(paper.resources).forEach(([kind, url]) => links.append(createLink(kind, url)));
  return card;
}

function render() {
  const visiblePapers = state.filtered.slice(0, state.visible);
  elements.grid.replaceChildren(...visiblePapers.map(renderCard));
  elements.count.textContent = state.filtered.length;
  elements.empty.hidden = state.filtered.length !== 0;
  elements.grid.hidden = state.filtered.length === 0;
  elements.loadMore.hidden = state.visible >= state.filtered.length;
}

function applyFilters() {
  const query = elements.search.value.trim().toLocaleLowerCase();
  const stakeholder = elements.stakeholder.value;
  const topic = elements.topic.value;
  const year = elements.year.value;

  state.filtered = state.papers.filter((paper) => {
    const haystack = [
      paper.title,
      paper.venue,
      ...paper.categories.flatMap((item) => [item.stakeholder, item.topic]),
    ].join(" ").toLocaleLowerCase();
    return (!query || haystack.includes(query))
      && (!stakeholder || paper.categories.some((item) => item.stakeholder === stakeholder))
      && (!topic || paper.categories.some((item) => item.topic === topic))
      && (!year || String(paper.year) === year);
  });

  state.visible = PAGE_SIZE;
  render();
}

function clearFilters() {
  elements.search.value = "";
  elements.stakeholder.value = "";
  elements.topic.value = "";
  elements.year.value = "";
  applyFilters();
}

async function init() {
  try {
    const response = await fetch("papers.json");
    if (!response.ok) throw new Error(`Catalog request failed: ${response.status}`);
    const payload = await response.json();
    state.papers = payload.papers.sort((a, b) => (b.year || 0) - (a.year || 0) || a.title.localeCompare(b.title));
    state.filtered = state.papers;
    elements.heroCount.textContent = payload.paper_count;
    setupFilters();
    render();
  } catch (error) {
    elements.grid.innerHTML = `<p class="catalog-error">The catalog could not be loaded. Please try again later.</p>`;
    console.error(error);
  }
}

[elements.search, elements.stakeholder, elements.topic, elements.year]
  .forEach((element) => element.addEventListener("input", applyFilters));
elements.clear.addEventListener("click", clearFilters);
document.querySelector("[data-clear]").addEventListener("click", clearFilters);
elements.loadMore.addEventListener("click", () => {
  state.visible += PAGE_SIZE;
  render();
});
document.addEventListener("keydown", (event) => {
  if (event.key === "/" && document.activeElement !== elements.search) {
    event.preventDefault();
    elements.search.focus();
  }
});

init();
