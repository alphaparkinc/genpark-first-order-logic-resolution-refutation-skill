# First-Order Logic Unifier Skill

Robinson's syntactic Most General Unifier (MGU) algorithm with strict occurs-check for automated theorem proving.

```mermaid
flowchart TD
    Terms["Input Terms (t1, t2)"] --> Decomp["Recursive Term Decomposition"]
    Decomp --> VarCheck{"Variable in Sub-term?"}
    VarCheck -- Yes --> Occurs{"Occurs Check Passed?"}
    Occurs -- No --> Fail["Unification Failed (Cycle)"]
    Occurs -- Yes --> Bind["Bind Variable to Sub-term"]
    VarCheck -- No --> Match{"Symbols Match?"}
    Match -- Yes --> SubTerms["Unify Arguments"]
    Match -- No --> Fail
    Bind --> Accum["Accumulate Substitutions θ"]
    Accum --> MGU["Return Valid MGU"]
```

## Features
- **100% Python Standard Library**: Recursive syntactic tree traversal.
- **Strict Occurs Check**: Prevents infinite circular term expansions.
- **Composed Substitutions**: Automatic term propagation across nested expressions.
