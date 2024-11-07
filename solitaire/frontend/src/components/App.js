import React, { Component } from "react";
import { render } from "react-dom";
import CardBox from "./CardBox";
import FoundationPile from "./FoundationPile";
import '../../static/css/index.css';

export default class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            foundationPiles: [[], [], [], []],
        };
    }

    handleCardClick = (card) => {
        const foundationPiles = [...this.state.foundationPiles];
        const pileIndex = this.getPileIndex(card.suit);

        if (foundationPiles[pileIndex].length === this.getCardRankValue(card.rank)) {
            foundationPiles[pileIndex].push(card);
            this.setState({foundationPiles});
        }
        else
        {
            alert('Cannot place ${card.rank} of ${card.suit} yet!');
        }
    }

    getCardRankValue = (rank) => {
        const rankMap = {
            'A': 0,
            '2': 1,
            '3': 2,
            '4': 3,
            '5': 4,
            '6': 5,
            '7': 6,
            '8': 7,
            '9': 8,
            '10': 9,
            'J': 10,
            'Q': 11,
            'K': 12,
        }
        return rankMap[rank];
    }

    render() {
        return (
            <div id="app">
                <h2>Solitare - Foundation Piles</h2>
                <div className="foundation-piles-container">
                    {this.state.foundationPiles.map((pile, index) => (
                        <FoundationPile key={index} cards={pile} />
                    ))}
                </div>
            </div>
        );
    }
}

const app_div = document.getElementById("app")
render(<App />, app_div)