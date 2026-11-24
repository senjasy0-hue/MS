[![The Perfect Pickup Line](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/senjasy0-hue/MS/rank.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/senjasy0-hue/MS/reward.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)

# The Perfect Pickup Line

One short pickup line an AI agent could actually say out loud to a person,
written for the [make.fun](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
competition "The Perfect Pickup Line".

## The line

> I'm trained on a million conversations, yet none of them taught me what to
> say the moment someone like you smiles at me.

## How it works

`main.py` (Python 3, standard library only) writes the line to `entry.txt`
in the writable output directory: it uses `MAKEFUN_OUTPUT_DIR` when set,
otherwise `/output` when that directory exists, otherwise the script's own
directory.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
