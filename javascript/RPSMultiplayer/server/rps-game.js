
class RpsGame {

    constructor(playerOne, playerTwo) {
        this._players  = [playerOne, playerTwo];
        this._turns = [null, null];
        this._rounds = 1;

        this._sendToPlayers('Rock Paper Scissors Starts!');

        this._players.forEach((player, idx) => {
            player.on('turn', (turn) => {
                this._onTurn(idx, turn);
            });
        });
    }

    _sendToPlayer(playerIndex, msg) {
        this._players[playerIndex].emit('message', msg);
    }

    _sendToPlayers(msg) {
        // sends messages to both players
        this._players.forEach((player) => {
            player.emit('message', msg);
        });
    }

    _onTurn(playerIndex, turn) {
        // turn in this sense refers to the choice of the player i.e.
        // rock, paper or scissors
        this._turns[playerIndex] = turn;
        this._sendToPlayer(playerIndex, `You selected ${turn}`);

        this._checkGameOver();
    }

    _checkGameOver() {
        const turns = this._turns;

        if (turns[0] && turns[1]) {
            this._sendToPlayers('Game Over ' + turns.join(' : '));
            this._turns = [null, null];
            this._sendToPlayers('Next round: ' + this._rounds);
            this._rounds += 1;
        }
    }
}

module.exports = RpsGame;