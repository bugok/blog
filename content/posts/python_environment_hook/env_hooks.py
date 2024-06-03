#!/usr/bin/env python3

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
