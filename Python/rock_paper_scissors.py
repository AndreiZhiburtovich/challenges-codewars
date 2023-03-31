# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"


def rps(p1, p2):
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if p1 not in beats and p2 not in beats:
        return "Error! Unacceptable arguments!"
    elif p1 == p2:
        return "Draw!"
    elif p1 in beats and beats[p1] == p2:
        return "Player 1 won!"
    elif p2 in beats and beats[p2] == p1:
        return "Player 2 won!"

    
print(rps('something', '!!!'))
print(rps('scissors', 'scissors'))
print(rps('rock', 'scissors'))
print(rps('scissors', 'rock'))
print(rps('paper', 'rock'))
print(rps('rock', 'paper'))
print(rps('scissors', 'paper'))
print(rps('paper', 'scissors'))


# import codewars_test as test
# from solution import rps

# @test.describe("rock paper scissors")
# def basic_tests():
#     @test.it("Player 1 wins")
#     def player_1():
#         test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
#     @test.it("Player 1 wins")
#     def player_1():
#         test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
#     @test.it("Draw")
#     def draw():
#         test.assert_equals(rps('rock', 'rock'), 'Draw!')
