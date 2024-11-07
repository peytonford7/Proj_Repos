// src/data.ts

import { FoodCategory } from "./types";

export const foodCategories: FoodCategory[] = [
  {
    name: "Italian",
    dishes: [
      { name: "Pizza", category: "Italian", price: 10.99 },
      { name: "Pasta", category: "Italian", price: 12.99 },
    ],
    sides: [
        
    ],
  },
  {
    name: "Mexican",
    dishes: [
      { name: "Tacos", category: "Mexican", price: 10.99 },
      { name: "Burrito", category: "Mexican", price: 8.99 },
    ],
    sides: [
        
    ],
  },
  {
    name: "Latin",
    dishes: [{ name: "Arepa", category: "Latin", price: 6.99 }],
    sides: [
        
    ],
  },
  {
    name: "American",
    dishes: [{ name: "Burger", category: "American", price: 8.99 }],
    sides: [
        
    ],
  },
  {
    name: "Australian",
    dishes: [{ name: "Meat Pie", category: "Australian", price: 10.99 }],
    sides: [
        
    ],
  },
];
