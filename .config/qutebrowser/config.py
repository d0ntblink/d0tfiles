import dracula.draw
import adblock
import os, sys
# Load existing settings made via :set
config.load_autoconfig()

c.completion.web_history.max_items = 10000
c.content.default_encoding = "utf-8"
c.content.pdfjs = True
c.downloads.location.directory = os.path.expanduser("~/Downloads")
c.downloads.location.prompt = False
c.downloads.remove_finished = 30000
c.editor.command = ["em", "{}"]
c.hints.uppercase = True
c.keyhint.delay = 100
c.scrolling.smooth = True
c.tabs.padding = {"left": 5, "right": 5, "top": 2, "bottom": 2}
c.tabs.title.format = "{perc}{current_title}"
c.url.default_page = "https://news.ycombinator.com/"
c.zoom.default = 67

config.load_autoconfig()
config.source("bindings.py")
config.source("fonts.py")
config.source("search_engines.py")
sys.path.append(os.path.join(sys.path[0], 'jblock'))
config.source("jblock/jblock/integrations/qutebrowser.py")

js_whitelist = [
    "*://*.youtube.com/*",
    "*://127.0.0.1/*",
    "*://darksky.net/*",
    "*://deepl.com/*",
    "*://duckduckgo.com/*",
    "*://github.com/*",
    "*://linkedin.com/*",
    "*://localhost/*",
    "*://news.ycombinator.com/*",
    "*://reddit.com/*",
    "*://translate.google.com/*",
]

private_whitelist = os.path.expanduser(
    "~/.config/qutebrowser/private-whitelist"
)
if os.path.exists(private_whitelist):
    with open(private_whitelist) as f:
        js_whitelist += filter(lambda l: bool(l), f.read().split("\n"))

for website in js_whitelist:
    with config.pattern(website) as p:
        p.content.javascript.enabled = True

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})
