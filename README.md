# Rock-Paper-Scissors Game

## Project Description

This is a simple Python-based implementation of the classic **Rock-Paper-Scissors** game, where the user plays against the computer. The game runs in the command line, and the user can choose between **Rock**, **Paper**, or **Scissors** while the computer randomly picks its choice. The game keeps track of the score over multiple rounds and displays the final score when the user decides to quit.

## Features

- User can choose **Rock**, **Paper**, or **Scissors**.
- Computer randomly selects one of the three options.
- The game determines the winner of each round based on classic Rock-Paper-Scissors rules:
  - Rock beats Scissors.
  - Paper beats Rock.
  - Scissors beats Paper.
- The game tracks both the user's and the computer's win count.
- The user can play multiple rounds and view the final score upon quitting.

## Technologies Used

- **Python**: The game is entirely written in Python using built-in modules such as `random` for computer's random choices.

## How to Play

1. Clone or download this repository to your local machine.
2. Open a terminal (command prompt) and navigate to the project directory.
3. Run the `SecondProject.py` file using Python:
   ```bash
   python rock_paper_scissors.py
   ```
4. When prompted, choose one of the following options:
   - Type `0` for **Rock**
   - Type `1` for **Paper**
   - Type `2` for **Scissors**

5. The computer will make its choice, and the game will display the result.
6. You will be asked if you'd like to play again:
   - Type `y` to continue playing.
   - Type `q` to quit the game.

7. When you quit, the game will display the final scores showing how many rounds you won and how many rounds the computer won.

## Example Gameplay

```bash
Choose: 0 for Rock, 1 for Paper, 2 for Scissors: 1
You chose Paper, and the computer chose Rock.
You win!

Would you like to play again? Type 'y' to continue or 'q' to quit: y

Choose: 0 for Rock, 1 for Paper, 2 for Scissors: 0
You chose Rock, and the computer chose Scissors.
You win!

Would you like to play again? Type 'y' to continue or 'q' to quit: q
Final Scores:
You won 2 times
Computer won 0 times
Goodbye!
```

## Future Improvements

- Add a **Graphical User Interface (GUI)** using `Tkinter` for a more interactive experience.
- Refactor the game logic into a class-based structure for better code organization.
- Deploy the game as a simple web application using `Flask` or `Django`.
- Expand the game to include different levels of difficulty where the computer's choices are influenced by previous rounds.

## Contributing

If you would like to contribute to the project, feel free to submit pull requests or suggest features via the **Issues** tab. Contributions that add new features or improve the structure of the code are always welcome.
