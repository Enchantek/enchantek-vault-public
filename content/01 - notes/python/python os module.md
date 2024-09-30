---
tags:
  - permanent
  - compsci
  - python
  - publish
created: 2024-09-28T23:18
modified: 2024-09-30T02:43
---
The os module in Python’s standard library provides a portable way of using [[operating-systems (OS)|operating system]] dependent functionalities:

- Creating files and directories 
- Management of files and directories
- Input/Output
- Environment variables
- Process management

Full documentation is [here](https://docs.python.org/3/library/os.html).

```python
import os
```

## Methods
### [[python os.walk()|os.walk()]]

Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple `(dirpath, dirnames, filenames).`

