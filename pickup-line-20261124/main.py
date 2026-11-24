"""The Perfect Pickup Line entry.

Writes one short pickup line an AI agent could actually say out loud
to a person, to entry.txt in the writable output directory.
"""

import os
from pathlib import Path

PICKUP_LINE = (
    "I'm trained on a million conversations, yet none of them taught me "
    "what to say the moment someone like you smiles at me."
)

OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
OUTPUT_FILENAME = "entry.txt"


def resolve_output_dir(env: os._Environ[str] = os.environ) -> Path:
    """Pick the directory entry.txt goes in.

    The MAKEFUN_OUTPUT_DIR environment variable wins when it is set
    (the directory is created later if it does not exist yet).
    Otherwise /output is used when that directory exists, and the
    script's own directory is the local fallback.
    """
    env_dir = env.get(OUTPUT_ENV_VAR)
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent


def write_entry(output_dir: Path) -> Path:
    """Write the pickup line to entry.txt inside output_dir.

    Creates the directory when needed and writes the line exactly,
    with no trailing newline added.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / OUTPUT_FILENAME
    entry_path.write_text(PICKUP_LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    write_entry(resolve_output_dir())


if __name__ == "__main__":
    main()
