// src/data.ts

import { FoodCategory } from "./types";

export const foodCategories: FoodCategory[] = [
  {
    name: "Italian",
    dishes: [
      { name: "Pizza", category: "Italian" },
      { name: "Pasta", category: "Italian" },
    ],
  },
  {
    name: "Mexican",
    dishes: [
      { name: "Tacos", category: "Mexican" },
      { name: "Burrito", category: "Mexican" },
    ],
  },
  {
    name: "Latin",
    dishes: [{ name: "Arepa", category: "Latin" }],
  },
  {
    name: "American",
    dishes: [{ name: "Burger", category: "American" }],
  },
  {
    name: "Australian",
    dishes: [{ name: "Meat Pie", category: "Australian" }],
  },
];
