import React from 'react';
import '../../static/css/index.css';

const CardBox = ({ card }) => {
    return (
        <div className="card-box">
            {card.rank} of {card.suit}
        </div>
    );
};

export default CardBox;