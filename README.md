python3 -m venv .venv
source .venv/bin/activate
pip install google-adk
adk create factcheckeragent
adk run factcheckeragent
adk web factcheckeragent
