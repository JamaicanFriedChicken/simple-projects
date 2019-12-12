
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
            this._sendToPlayers('Result: ' + turns.join(' : '));
            this._getGameResult();
            this._turns = [null, null];
            this._rounds += 1;
            this._sendToPlayers('Next! Round ' + this._rounds);
        }
    }

    _getGameResult() {

        const playerOne = this._decodeTurn(this._turns[0]);
        const playerTwo = this._decodeTurn(this._turns[1]);

        const distance = (playerOne - playerTwo + 3) % 3;

        switch (distance) {
            case 0:
                // tie
                this._sendToPlayers('Draw!');
                break;
            case 1:
                // playerOne won
                this._sendWinMessage(this._players[0], this._players[1]);
                break;
            case 2:
                // playerTwo won
                this._sendWinMessage(this._players[1], this._players[0]);
                break;
        }

    }

    _sendWinMessage(winner, loser) {
        winner.emit('message', 'You won!');
        loser.emit('message', 'You lost :(');
    }

    _decodeTurn(turn) {
        
        switch (turn) {
            case 'rock':
                return 0;
            case 'scissors':
                return 1;
            case 'paper':
                return 2;
            default:
                throw new Error(`Could not decode move ${turn}`);
        }
    }
}

module.exports = RpsGame;