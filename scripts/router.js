window.addEventListener("popstate", (e) => {
  var state = e.state;
  if (state !== null) {
    loadRouteDocument(state.route, state.title);
  }
});

function toggleDisplay(show = false, element) {
  if (show) {
    element.classList.remove("hidden");
  } else {
    element.classList.add("hidden");
  }
}

function toggleLoader(show = false) {
  const loader = document.getElementById("loader");
  if (loader) {
    toggleDisplay(show, loader);
  }
}

function loadRouteDocument(route, title) {
  const router = document.getElementById("router");
  toggleDisplay(false, router);
  toggleLoader(true);
  var r = new XMLHttpRequest();
  r.open("GET", route, true);
  r.responseType = "txt";
  r.onload = function () {
    if (r.readyState !== 4 || r.status !== 200) return;
    const doc = r.responseText;
    setTimeout(() => {
      toggleLoader(false);
      toggleDisplay(true, router);
      if (title) {
        setDocumentTitle(title);
      }
      router.innerHTML = doc;
      registerRoutes();
      document.getElementById("crumb").innerText = title;
    }, 500);
  };
  r.send();
}

function loadRoute(element) {
  const route = element.getAttribute("route");
  const title = element.getAttribute("routeTitle");
  if (route) {
    loadRouteDocument(route, title);
    window.history.pushState({ route, title }, title);
  }
}

function initDefaultRoute() {
  const element = document.querySelector("[defaultRoute]");
  loadRoute(element);
}

function registerRoutes() {
  document.querySelectorAll("[route]").forEach((element) => {
    const registered = element.hasAttribute("routeRegistered");
    if (!registered) {
      element.setAttribute("routeRegistered", "");
      element.addEventListener("click", (e) => {
        e.preventDefault();
        loadRoute(element);
      });
    }
  });
}

function initRoute() {
  initDefaultRoute();
  registerRoutes();
}

initRoute();
