document.body.addEventListener("htmx:afterSwap", (event) => {
	if (event.target.id === "contactList") {
		const form = document.getElementById("contactList");
		form.scrollIntoView({ behavior: "smooth", block: "end" });
	}
});
