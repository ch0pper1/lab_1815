setLoadHandler();
setOverridePersonaShortcutHandler();

function setLoadHandler() {
	window.addEventListener("load", (event) => {
		definePersonaOverrideDialog();
	});
}

function setCookieValue(cookieName, value) {
	document.cookie = `${cookieName}=${value}`;
}

function setPersonaOverride(personaOverride) {
	setCookieValue(COOKIE_NAMES.personaOverride, personaOverride);
}

function removePersonaOverride() {
	document.cookie = `${COOKIE_NAMES.personaOverride}=; expires=Thu, 01 Jan 1970 00:00:00 GMT`;
}

function setOverridePersonaShortcutHandler() {
	document.addEventListener("keyup", function(event) {
		if (event.code === "KeyP" && event.ctrlKey && event.shiftKey) {
			document.querySelector("#cic-personaOverrideDialog").showModal();
		}
	});
}

function closeOverridePersonaDialog() {
	document.querySelector("#cic-personaOverrideDialog").close();
}

function definePersonaOverrideDialog() {
	const dialog = document.createElement("dialog");
	dialog.id = "cic-personaOverrideDialog";

	dialog.innerHTML = `
	<h3>Set/override your persona or remove the override and return to your normal persona.</h3>
	<h5>NOTE: If you are not running behind the IBM Reverse Proxy, you won't likely have a persona defined.<br/>Setting it with this tool will be the only way to assume a particular persona.</h5>
	<h5>After making your choice, the page will be refreshed.</h5>
	<br/>
	<br/>
	<div id="cic-personaOverrideDialog-buttonRow">
		<button class='firstRowButton' onclick='setPersonaOverride("ibmer"); location.reload()'>"ibmer"</button>
		<button class='firstRowButton' onclick='setPersonaOverride("partner"); location.reload()'>"partner"</button>
		<button class='firstRowButton' onclick='setPersonaOverride("unknown"); location.reload()'>"unknown"</button>
		<button class='secondRowButton firstColumnButton' onclick='removePersonaOverride(); location.reload()'>Remove Override</button>
		<button class='secondRowButton thirdColumnButton' onclick='closeOverridePersonaDialog()'>Close</button>
	</div>
	`;

	document.body.append(dialog);
}
