#### This repository demonstrates how to build and debug agents without the boilerplate using Google’s open-source Agent Development Kit (ADK).
####  In this guide, you will learn how to:
####  Set up the ADK Python SDK.
####  Write a Gemini-powered fact-checking agent from scratch.
#### Test and debug your agent locally using the ADK’s built-in web playground.
####  Let's get started! 🚀
---
Steps: 
```
python3 -m venv .venv
source .venv/bin/activate
pip install google-adk
adk create factcheckeragent
adk run factcheckeragent
adk web factcheckeragent
```
---
Grab the key from https://aistudio.google.com/  - Gemini API Key and enter it when creating an agent using ADK command
---
<img width="1196" height="608" alt="Screenshot 2026-07-28 125232" src="https://github.com/user-attachments/assets/7282e57b-5b76-4332-92d3-9b76546e5075" />
<img width="1853" height="1152" alt="Screenshot 2026-07-28 125148" src="https://github.com/user-attachments/assets/16bcc808-374d-41b2-9954-834beef88a84" />
<img width="1891" height="1143" alt="Screenshot 2026-07-28 125518" src="https://github.com/user-attachments/assets/0df99790-0b52-4231-b092-7a435a714ca6" />
<img width="1897" height="1147" alt="Screenshot 2026-07-28 140725" src="https://github.com/user-attachments/assets/a2ab1dea-efa6-46cb-a25b-00e24abfe936" />
