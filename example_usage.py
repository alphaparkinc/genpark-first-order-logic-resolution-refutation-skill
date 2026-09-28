"""Example demonstrating Robinson First-Order Logic Unification."""
from client import FOLUnifier

def main():
    # Unify P(?x, f(?x)) with P(g(?y), ?z)
    t1 = ["P", "?x", ["f", "?x"]]
    t2 = ["P", ["g", "?y"], "?z"]
    print("Term 1:", t1)
    print("Term 2:", t2)
    mgu = FOLUnifier.unify(t1, t2)
    print("Most General Unifier:", mgu)

if __name__ == "__main__":
    main()
