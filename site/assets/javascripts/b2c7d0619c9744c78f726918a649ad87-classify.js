setLoadHandler();

const COOKIE_NAMES = {
	personaOverride: "personaOverride",
	persona: "persona"
}

function setLoadHandler() {
	window.addEventListener("load", (event) => {
		setPersonaFromCookie();
	});

	if (document.readyState === "complete") {
		setPersonaFromCookie();
	}
}

function setPersonaFromCookie() {
	const personaOverrideCookieValue = getCookieValue("personaOverride");
	const personaCookieValue = getCookieValue("persona");

	const persona = personaOverrideCookieValue ? personaOverrideCookieValue : personaCookieValue;

	if (persona) {
		setPersona(persona);
	}
	else {
		console.error("The \"persona\" cookie does not have a value. Please seek support.");
		setPersonaToUnknown();
	}
}

function setPersona(persona) {
	document.body.setAttribute("persona", persona);
}

function setPersonaToUnknown() {
	setPersona("unknown");
}

function getCookieValue(cookieName) {
	return document.cookie
	  .split("; ")
	  .find((row) => row.startsWith(`${cookieName}=`))
	  ?.split("=")[1];
}
