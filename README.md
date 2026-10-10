# Market Basket Analysis

A Python script that finds associations between items in shopping baskets (e.g., "customers who buy diapers also tend to buy beer") by calculating three standard association rule metrics, written from scratch with no external libraries.

## Metrics
- **Support**: how often an item (or pair of items) appears across all transactions
- **Confidence**: given that a customer bought item A, how likely they are to also buy item B
- **Lift**: how much more likely B is bought alongside A compared to B's baseline popularity (above 1 means a positive association, below 1 a negative one)

## How it works
- Takes a list of transactions (each one a basket of items)
- Generates every possible item pair with `itertools.combinations`
- Skips pairs that never appear together
- Prints support, confidence, and lift for each pair that does

## How to run
```bash
python market_basket.py
```

## What I learned
- The core metrics behind association rule mining and recommendation systems
- Using `itertools.combinations()` to generate all unique pairs from a set
- Using `sum()` with a generator expression to count matching baskets concisely
- Building small, single-purpose functions that reuse each other (lift builds on confidence, which builds on support)

## Dependencies
None. Uses only Python's standard library.
