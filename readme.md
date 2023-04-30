# Python ChatGPT Conversation Implementation with GPTrim

This is just a simple test project, implementing GPTrim method to save tokens in using OpenAI API request. With this, all previous request content will be trimmed, and calculated to see how many tokens were saved.

To test this, follow this steps:
1. Git clone this repo
```bash
git clone https://github.com/haranobuhardo/ChatGPT-CLI-GPTrim
``` 
2. Change dir
```bash
cd ChatGPT-CLI-GPTrim
```
3. Create .env file with your OPENAI KEY stored as OPENAI_API_KEY (Change below XXX to your key)
```bash
echo OPENAI_API_KEY=XXX > .env
```
4. Run the main.py
```bash
python main.py
```

Check out [GPTrim](https://github.com/vlad-ds/gptrim)
