// src/App.tsx

import React from "react";
import { foodCategories } from "./data";

const App: React.FC = () => {
  return (
    <div>
      <h1>Food Categories and Dishes</h1>
      {foodCategories.map((category) => (
        <div key={category.name}>
          <h2>{category.name}</h2>
          <ul>
            {category.dishes.map((dish) => (
              <li key={dish.name}>{dish.name}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default App;
