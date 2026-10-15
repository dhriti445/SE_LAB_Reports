# Assignment Chat History

This file records the prompts and responses available in this chat. It is not
claimed to be a complete history of any earlier conversations that are not
available here.

## Entry 1 — 2026-10-15

### Prompt

> I am completing a Lab 4 VibeCoding assignment on a Python Sliding Puzzle. Before making any code changes, read the README.md and inspect main.py, game.py, and puzzle.py.
>
> Create a file named chat-history.md in the project root to maintain my assignment record. For each task, help me record my exact prompt, your response, the files changed, and the tests performed, in chronological order. Preserve previous entries and do not claim the history is complete if you cannot access all previous messages.
>
> Do not change the game code yet. First explain the existing project and identify its current bugs.
>
> [Tagged file: c:\Users\dhriti\Downloads\22_sliding_puzzle\puzzle.py (31 lines)]

### Response

The project is a terminal sliding puzzle:

- `main.py` creates a `SlidingPuzzle` and starts its `run()` loop.
- `game.py` handles the 4x4 game session, board display, move counting,
  elapsed-time display, valid command filtering, and quitting.
- `puzzle.py` stores the board, finds the blank tile, applies legal blank-space
  moves, and checks whether the board is solved.
- `README.md` defines four requested tasks: guaranteed-solvable starts,
  complete-puzzle lifecycle handling, 3x3/4x4/5x5 modes with consistent
  session tracking, and valid-action feedback. It also lists the required
  behavioural tests.

Current bugs and missing requirements:

1. **Unsolvable starting boards:** `puzzle.py` uses `random.shuffle()` on an
   arbitrary permutation. Some permutations have the wrong parity and cannot be
   reached from the solved board by legal moves.
2. **No requested size modes:** `game.py` always creates a 4x4 puzzle and has
   no 3x3 or 5x5 selection.
3. **Incomplete lifecycle features:** the current loop does detect a solved
   board before reading the next command and returns with `Solved!`, but there
   is no explicit completion state in the model/controller. The requested
   lifecycle behaviour still needs to be verified and strengthened when
   implementation begins.
4. **Move feedback is incomplete:** successful moves produce no success
   feedback; only failed moves print `That move is not possible.` The move
   count itself is incremented only when `Puzzle.move()` returns `True`.
5. **Direct invalid direction calls can raise an exception:** `Puzzle.move()`
   indexes a dictionary with `direction`, so a caller that passes a value
   outside `w`, `a`, `s`, or `d` receives `KeyError`. The interactive loop
   filters commands first, but the model method is not defensive.
6. **Required behaviour is not yet tested:** there is no test suite in the
   inspected project, and the required repeated-board, size, solve,
   impossible-move, move-count, timer, invalid-command, and quit checks have
   not yet been performed.

### Files changed

- `chat-history.md` — created to maintain this assignment record.
- No game code was changed.

### Tests performed

- Read `README.md`.
- Inspected `main.py`, `game.py`, and `puzzle.py`.
- Checked repository status and root contents.
- No runtime or automated tests were run; implementation has intentionally not
  started.

## Entry 2 — 2026-10-15

### Prompt

> Implement Task 1 of my Lab 4 Sliding Puzzle assignment: Guarantee Solvable Starting States.
>
> First inspect the README.md and existing implementation. In puzzle.py, the make_board() method currently creates the tiles and shuffles them randomly. This can produce an unsolvable puzzle.
>
> Modify the existing implementation so that:
>
> 1. The board begins in the solved arrangement.
> 2. The board is scrambled by performing a sequence of legal blank-tile moves.
> 3. Immediate reversal of the previous scramble move is avoided when possible.
> 4. Every generated board is reachable from the solved arrangement.
> 5. The existing Puzzle class, board representation, and movement controls are preserved.
> 6. The implementation can support the board sizes required by the assignment.
> Do not implement Tasks 2, 3, or 4 yet. Do not add unnecessary dependencies, databases, file persistence, or unrelated features.
>
> Explain the changes, identify the files modified, and run suitable tests. Verify that the generated boards remain solvable and that every scramble move is legal.
>
> After finishing, append this task's exact prompt, response, changes, and test results to chat-history.md without deleting previous entries.
>
> [Tagged file: c:\Users\dhriti\Downloads\22_sliding_puzzle\puzzle.py (31 lines)]

### Response

Task 1 was implemented without changing Tasks 2, 3, or 4.

`Puzzle.make_board()` now:

- Creates the solved board directly instead of using `random.shuffle()`.
- Scrambles the board by repeatedly selecting and applying a legal
  `w/a/s/d` blank-tile move.
- Avoids the opposite of the previous scramble move whenever another legal
  move is available.
- Uses a size-dependent number of scramble moves and works with the required
  3x3, 4x4, and 5x5 board dimensions.
- Ensures a board larger than 1x1 does not finish the scramble in the solved
  state.

The existing `Puzzle` class, nested-list board representation, movement
controls, and movement method were preserved. No dependencies, databases, or
persistent game state were added.

### Files changed

- `puzzle.py` — replaced arbitrary shuffling with legal blank-tile scrambling.
- `chat-history.md` — appended this chronological assignment entry.
- No changes were made to `main.py`, `game.py`, `README.md`, or
  `requirements.txt`.

### Tests performed

- Re-read `README.md` and inspected the existing `puzzle.py` before editing.
- Compiled `puzzle.py` with Python 3.12.10 using `py_compile`.
- Generated 100 boards for each of 3x3, 4x4, and 5x5.
- Verified every board had the expected dimensions and contained each tile
  exactly once.
- Instrumented `Puzzle.move()` to verify every scramble move returned
  `True`, proving each recorded move was legal.
- Verified consecutive scramble moves did not immediately reverse one another
  whenever more than one legal move was available.
- Verified all 300 generated boards were not solved after scrambling, so each
  board had a valid legal path from the solved arrangement and was solvable in
  principle.
