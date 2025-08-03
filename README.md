# tshell

`tshell` is a lightweight command line tool that lets you talk to an AI model
from your terminal. It uses the OpenAI API if it is available and configured via
`OPENAI_API_KEY`. When the API is unavailable, a placeholder response is
returned instead.

```
$ tshell echo hello
[AI] Response for: echo hello
```

Run `tshell` without arguments to enter an interactive shell.
