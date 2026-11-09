module.exports = async (params) => {
    const { obsidian, app } = params;
    const [REDACTED_SECRET_ASSIGNMENT]; // Replace with your key
    const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);
    if (!view) return;

    const input = view.editor.getSelection() || view.editor.getValue();
    if (!input) return;

    async function callModel(model, prompt) {
        const response = await obsidian.requestUrl({
            url: "https://openrouter.ai/api/v1/chat/completions",
            method: "POST",
            headers: {
                "Authorization": `Bearer ${apiKey}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                model: model,
                messages: [{ role: "user", content: prompt }]
            })wdym by highlight your task text in any note
        });
        return response.json.choices[0].message.content;
    }

    new obsidian.Notice("Ox Alpha planning...");
    const plan = await callModel("stealth/ox-alpha", `Plan this task for Justin:\n${input}`);

    new obsidian.Notice("GLM 5.2 formatting...");
    const formatted = await callModel("z-ai/glm-5.2:free", `Format this plan into clean Markdown with YAML frontmatter:\n${plan}`);

    new obsidian.Notice("Nemotron 3 auditing...");
    const audit = await callModel("nvidia/nemotron-3-ultra-550b-a55b:free", `Audit any code or logic in this request:\n${input}`);

    view.editor.replaceSelection(`${formatted}\n\n### Logic & Code Audit\n${audit}`);
    new obsidian.Notice("Pipeline finished!");
};