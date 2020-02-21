package com.blackjack;

import java.util.Scanner;

class Blackjack {

    public static void main(String[] args) {

        // Welcome Message
        System.out.println("Welcome to Blackjack!");

        // Create our playing deck
        Deck playingDeck = new Deck();
        playingDeck.createFullDeck();
        playingDeck.shuffle();

        // Creating a deck for the player and dealer
        Deck playerDeck = new Deck();
        Deck dealerDeck = new Deck();

        double playerMoney = 100.00;

        Scanner userInput = new Scanner(System.in);

        // Game Loop
        while (playerMoney > 0) {
            // Plays on if player still has money
            // Take the players bet
            System.out.println("You have $" + playerMoney + ", how much would you like to bet?");
            double playerBet = userInput.nextDouble();
            if (playerBet > playerMoney) {
                System.out.println("You can't bet more money than what you have!");
                break;
            }

            boolean endRound = false;

            // Start dealing
            // Player gets two cards
            playerDeck.draw(playingDeck);
            playerDeck.draw(playingDeck);

            // Dealer gets two cards
            dealerDeck.draw(playingDeck);
            dealerDeck.draw(playingDeck);

            // Loop for hitting (drawing cards from dealer)
            while (true) {
                System.out.println("Your hand:");
                System.out.println(playerDeck.toString() + "\n");
                System.out.println("Your hand is:" + playerDeck.cardsValue());

                // Display Dealer hand
                System.out.println("Dealer Hand: " + dealerDeck.getCard(0).toString() + " and [HIDDEN]");

                // What does the player want to do?
                System.out.println("Would you like to (1)Hit or (2)Stand?");
                int response = userInput.nextInt();

                // They hit
                if (response == 1) {
                    playerDeck.draw(playingDeck);
                    System.out.println("You drew a " + playerDeck.getCard(playerDeck.deckSize() -1));
                    // Loses if over cards value over 21
                    if (playerDeck.cardsValue() > 21) {
                        System.out.println("You lose! Currently valued at: " + playerDeck.cardsValue());
                        playerMoney -= playerBet;
                        endRound = true;
                        break;
                    }
                }

                if (response == 2) {
                    break;
                }
            }

            // Reveal Dealer Cards
            System.out.println("Dealer Cards: " + dealerDeck.toString());
            // Checks to see if dealer's hand is greater than player's hand
            if (dealerDeck.cardsValue() > playerDeck.cardsValue() && endRound == false) {
                System.out.println("Dealer beats you!");
                playerMoney -= playerBet;
                endRound = true;
            }

            // Dealers draws at 16, stand at 17
            while (dealerDeck.cardsValue() < 17 && endRound == false) {
                dealerDeck.draw(playingDeck);
                System.out.println("Dealer draws: " + dealerDeck.getCard(dealerDeck.deckSize()-1).toString());
            }

            // Display total value of cards in Dealer's hand
            System.out.println("Dealer's hand is valued at: " + dealerDeck.cardsValue());

            // Determine if dealer loses
            if ((dealerDeck.cardsValue() > 21) && endRound == false) {
                System.out.println(("Dealer loses! You win!"));
                playerMoney += playerBet;
                endRound = true;
            }

            // Determine if push (means a tie in blackjack)
            if ((playerDeck.cardsValue() == dealerDeck.cardsValue()) && endRound == false) {
                System.out.println("Push");
                endRound = true;
            }

            if ((playerDeck.cardsValue() > dealerDeck.cardsValue()) && endRound == false) {
                System.out.println("You win!");
                playerMoney += playerBet;
                endRound = true;
            } else if (endRound == false) {
                System.out.println("You lose the game.");
                playerMoney -= playerBet;
                endRound = true;
            }

            playerDeck.moveAllToDeck(playingDeck);
            dealerDeck.moveAllToDeck(playingDeck);
            System.out.println("End of hand.");
        }

        System.out.println("Gamer Over! You are out of money.");
    }
}