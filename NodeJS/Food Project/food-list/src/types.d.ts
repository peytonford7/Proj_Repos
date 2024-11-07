// src/types.d.ts

export interface FoodCategory {
    name: string;
    dishes: Dish[];
    sides: Dish[];
  }
  
  export interface Dish {
    name: string;
    category: string;
    price: number;
  }