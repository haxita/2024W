import json
import numpy as np

from pig_lite.game.base import Node, Game


class TTTNode(Node):
    def key(self):
        return tuple(self.state.flatten().tolist() + [self.player])

    def __repr__(self):
        return '"TTTNode(\nid:{}\nparent:{}\nboard:\n{}\nplayer:\n{}\naction:\n{}\ndepth:{})"'.format(
            id(self),
            id(self.parent),
            # this needs to be printed transposed, so it fits together with
            # how matplotlib's 'imshow' renders images
            self.state.T,
            self.player,
            self.action,
            self.depth
        )


class TicTacToe(Game):
    def __init__(self, rng=None, depth=None):
        self.n_expands = 0
        self.play_randomly(rng, depth)

    def play_randomly(self, rng, depth):
        empty_board = np.zeros((3, 3), dtype=int)
        start_from_empty = TTTNode(None, empty_board, None, 1, 0)
        if rng is None or depth is None or depth == 0:
            self.start_node = start_from_empty
        else:
            # proceed playing randomly until either 'depth' is reached,
            # or the node is a terminal node
            nodes = []
            successors = [start_from_empty]
            while True:
                index = rng.randint(0, len(successors))
                current = successors[index]

                if current.depth == depth:
                    break

                nodes.append(current)
                terminal, winner = self.outcome(current)
                if terminal:
                    break
                successors = self.successors(current)

                for node in successors:
                    nodes.append(node)

            self.start_node = TTTNode(None, current.state, None, current.player, 0)

    def get_start_node(self):
        return self.start_node

    def outcome(self, node):
        board = node.state
        for player in [-1, 1]:
            # checks rows and columns
            for i in range(3):
                if (board[i, :] == player).all() or (board[:, i] == player).all():
                    return True, player

            # checks diagonals
            if (np.diag(board) == player).all() or (np.diag(np.rot90(board)) == player).all():
                return True, player

        # if board is full, and none of the conditions above are true,
        # nobody has won --- it's a draw
        if (board != 0).all():
            return True, None

        # else, continue
        return False, None

    def get_max_player(self):
        return 1

    def successor(self, node, action):
        board = node.state
        player = node.player

        next_board = board.copy()
        next_board[action] = player

        if player == 1:
            next_player = -1
        else:
            next_player = 1

        return TTTNode(
            node,
            next_board,
            action,
            next_player,
            node.depth + 1
        )

    def get_number_of_expanded_nodes(self):
        return self.n_expands

    def successors(self, node):
        self.n_expands += 1
        terminal, winner = self.outcome(node)

        if terminal:
            return []
        else:
            successor_nodes = []
            # iterate through all possible coordinates (==actions)
            for action in zip(*np.nonzero(node.state == 0)):
                successor_nodes.append(self.successor(node, action))
            return successor_nodes

    def to_json(self):
        return json.dumps(dict(
            type=self.__class__.__name__,
            start_state=self.start_node.state.tolist(),
            start_player=self.start_node.player
        ))

    @staticmethod
    def from_json(jsonstring):
        data = json.loads(jsonstring)

        ttt = TicTacToe()
        ttt.start_node = TTTNode(
            None,
            np.array(data['start_state'], dtype=int),
            None,
            data['start_player'],
            0
        )
        return ttt

    @staticmethod
    def from_dict(data):
        ttt = TicTacToe()
        ttt.start_node = TTTNode(
            None,
            np.array(data['start_state'], dtype=int),
            None,
            data['start_player'],
            0
        )
        return ttt

    @staticmethod
    def get_minimum_problem_size():
        return 0