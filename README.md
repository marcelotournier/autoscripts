# autoscripts
Automatically install all scripts you put in the "./bin" folder of this repository

Works with any executable script with a shebang pattern in the first line: `!#/.........`

## Instructions:
Install with:
```
pip install git+https://github.com/marcelotournier/autoscripts.git
```

## Note: 
- ALWAYS add the shebang pattern in the first line, so `setup.py` can properly identify your script
- Remember that bash/sh scripts don't work in windows :)
