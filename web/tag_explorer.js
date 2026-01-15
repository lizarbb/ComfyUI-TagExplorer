import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "TagExplorer.Integration",

    async setup() {
        const style = document.createElement("style");
        style.textContent = `
            .tag-explorer-button {
                margin: 5px 0;
                padding: 8px 12px;
                background: #4a9eff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 13px;
                width: 100%;
            }
            .tag-explorer-button:hover {
                background: #3a8eef;
            }
            .tag-explorer-modal {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                display: none;
                z-index: 10000;
                align-items: center;
                justify-content: center;
            }
            .tag-explorer-modal.visible {
                display: flex;
            }
            .tag-explorer-iframe {
                width: 90%;
                height: 90%;
                border: none;
                border-radius: 8px;
                background: white;
            }
        `;
        document.head.appendChild(style);

        const modal = document.createElement("div");
        modal.className = "tag-explorer-modal";

        const iframe = document.createElement("iframe");
        iframe.className = "tag-explorer-iframe";
        iframe.src = "/tag_explorer_web/tag_explorer.html";

        modal.appendChild(iframe);
        document.body.appendChild(modal);

        modal.addEventListener("click", (e) => {
            if (e.target === modal) {
                modal.classList.remove("visible");
            }
        });

        window.addEventListener("message", (event) => {
            if (event.data.type === "tag_explorer_tags") {
                const nodes = app.graph._nodes;
                nodes.forEach(node => {
                    if (node.type === "TagExplorerNode") {
                        const tagsWidget = node.widgets.find(w => w.name === "tags");
                        if (tagsWidget) {
                            const currentTags = tagsWidget.value.trim();
                            if (currentTags) {
                                tagsWidget.value = currentTags + ", " + event.data.tags;
                            } else {
                                tagsWidget.value = event.data.tags;
                            }
                        }
                    }
                });
                modal.classList.remove("visible");
            }
        });

        window.openTagExplorer = () => {
            modal.classList.add("visible");
        };
    },

    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "TagExplorerNode") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                const result = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;

                const button = document.createElement("button");
                button.textContent = "Open Tag Explorer";
                button.className = "tag-explorer-button";
                button.onclick = () => {
                    window.openTagExplorer();
                };

                this.addDOMWidget("explorer_button", "button", button, {
                    serialize: false,
                });

                return result;
            };
        }
    }
});
