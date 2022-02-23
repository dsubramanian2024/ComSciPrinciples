READ ME File
Author: Divya Subramanian


Values: (Same as the chess values)
  pawn - ♟ - 1
  knight - ♞ - 3
  bishop - ♝ - 3
  rook - ♜ - 5
  queen - ♛ - 9
  king - ♚ - 100

Rules:
  1. This game asks the user for a number which will be the size of the square
  board.
  2. The board of the given size will be displayed with "?" to fill the position
  of the shapes
  3. The users will then be able to choose a row (from 0 to n - 1), column
  (from 0 to n - 1), or diagonal where 0 is / and 1 is \. The points received is
  displayed. The points is the sum of the values in the chosen line of the array.
  If there are n appearances of a certain shape in the chosen line, the score will
  add n * n * the value of the shape.
  4. The user is then shown the board and asked if they want to randomly switch out one of the
  elements in their chosen line. If they do so, the new sum is displayed. This
  can only be done once per game by each player.
  5. The program will continue asking for new users until anything other than
  'yes' is entered.
  6. Then, the board with randomly generated shapes will be displayed.
  7. The corresponding values of the shapes in the chosen row, column, or
  diagonal will be summed up and displayed.
  8. The player who has received the most points is the winner!
