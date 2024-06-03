---
title: Adding hooks when accessing environment variables in Python
date: 2024-06-03T21:01:33+03:00
summary: How to add hooks to accessing environment variables in Python
description: How to add hooks to accessing environment variables in Python
tags:
- python
---

## Moving away from environment-variable based configuration

In my current project, I'm working on moving away from configuring a Python 
service using environment variables to loading the configuration from another, 
more structured source (say, a json file). 

As part of the migration, I wrote the service's configuration twice: I kept the
environment variables, and also wrote the configuration file. I then loaded the
configuration from both sources - and compared. I let that run for some time,
and after there was no difference between the configuration generated from the
two source, I thought I was done. 

The next step was to remove the environment variables from the service's
environment. After doing that, the service crashed in multiple ways. Turns out
that instead of loading the configuration in one central place, there were many
places which had something similar to:
```python3
my_config_attr = os.environ["MY_ENVVAR"]
```

## Better data on using environment variables in my service

Changing the approach, I had to assume that there are many places in the code
which are accessing environment variables, across multiple directories.
Therefore, a better solution would be to find all those places, replace the
`os.environ["MY_ENVVAR"]` calls with referencing the configuration structure
which was read from the file. Only then, remove the environment variables from
the service's environment (as they won't be accessed anymore). 

The question is: How to find all those callsites?

I have a list of all the environment variables I'm dumping to the service's
environment. This means I could do something when those environment variables
are being accessed. 

## Overriding `os.environ`

Eventually, I decided to override `os.environ` with a similar structure which
logs whenever a relevant environment variable is being accessed. Simplifying
this a little bit, the code looks something like this:


```python3
#!/usr/bin/env python3
# env_hooks.py

import logging
import os
from typing import Set

logger: logging.Logger = logging.getLogger(__name__)


class EnvAccessLoggingDict(os._Environ):
    _TRACKED_ENVVARS: Set[str] = {
        "EDITOR",
        "SHELL",
    }

    def __init__(
        self,
    ) -> None:
        super().__init__(
            data=os.environ,
            encodekey=lambda x: x,
            decodekey=lambda x: x,
            encodevalue=lambda x: x,
            decodevalue=lambda x: x,
        )

    def __getitem__(self, key: str) -> str:
        if key in self._TRACKED_ENVVARS:
            logger.info(f"Accessed {key}")
        return super().__getitem__(key)


def main():
    logging.basicConfig(level=logging.INFO)

    # Override os.environ
    os.environ = EnvAccessLoggingDict()

    # Testing the hook
    print(os.environ["USER"])
    print(os.environ["EDITOR"])


if __name__ == "__main__":
    main()
```

A few interesting things to note:
* I didn't expect that `os.environ` would be anything else but a `dict`, but it
  turned out to be something else (I needed to [dig into the python source
  code](https://github.com/python/cpython/blob/3.10/Lib/os.py#L667)
  to find that out).
* I decided to inherit from the `os._Environ` type to keep the interface the
  same. To make this work, I replaced the various key/value encoding/decoding 
  methods with no-op lambda functions, as the `data` member, the original 
  `os.environ` object, had the needed functionality. 

Running the code above yields the following output:
```bash
$ ./env_hooks.py
noam
INFO:__main__:Accessed EDITOR
/usr/bin/vim
```

You can see that accessing the `USER` environment variable doesn't trigger the
logging, but accessing the `EDITOR` environment variable does trigger the
logging. Obviously, the actual logging function is better is much better,
sending an event to an event system for easy aggregation across multiple
production workloads.

## And now?

Now I have better confidence in which environment variables are being accessed,
so I can follow up and replace those callsites.

