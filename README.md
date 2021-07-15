## Concept

Mapping chess data to sound behavior
Multiple mappings are possible
The final idea is to make a tool and make people compose music using chess
But it's a too big project, so to publish already something we make a smaller version, no tool, just tracks and the explanation of the different possible mappings.

We have a description of the mappings
We have an archive of the mappings
We have a description of the process (simple version -> complex one)

## Mappings

- Note
  - Cell moved to
  - All the cells during the piece movement
  - Starting cell of the piece moved
- Note Length

  - Absolute value of Centipawn score
  - Number of cells moved
  - Time taken by the player to move

- Distance between notes
  Distance between moves by player (in seconds)
  Works best with bullets but if time is scaled also with normal games

## How to install

```bash
python3 -m venv .venv
```

Then select python interpreter (in VSCODE)

```bash
pip install chess
```
