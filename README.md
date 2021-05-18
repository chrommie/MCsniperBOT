<p align="center">
	<img
		width="500"
		alt="MCsniperPY"
		src="https://i.imgur.com/hl7h1ta.png?sanitize=true">
</p>

## Auto-Formatting
- pip install pre-commit
- pre-commit install

## Cogs
Cogs are separated into sub-directories to allow for features to be more organised

### Events
This cog sub-directory will be used for discord events such as "on_member_join" or "on_message_delete"

## Utils
The utils directory is used to save time when rewriting the same code repeatedly. It currently has:

### logs.py
For logging actions to either paste.gg or the logs channel specified on config.py

### responses.py
For responding to a command with either a success or error without recreating the same embed design repeatedly
