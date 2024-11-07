import React, { Component } from 'react';
import CardBox from './CardBox';

class FoundationPile extends Component {
    render() {
        const { cards } = this.props;
        return (
            <div className="foundation-pile">
                {cards.length === 0 ? null : cards.map((card, index) => (
                    <CardBox key={index} card={card} />
                ))}
            </div>
        );
    }
}

export default FoundationPile;