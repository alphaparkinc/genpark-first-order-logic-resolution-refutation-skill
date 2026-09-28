"""First-Order Logic Robinson Syntactic Unifier.
100% Python Standard Library.
"""

class FOLUnifier:
    """Robinson's first-order logic syntactic unification algorithm with occurs check."""
    @staticmethod
    def is_var(x):
        return isinstance(x, str) and x.startswith("?")

    @staticmethod
    def apply_subst(term, theta):
        if not theta:
            return term
        if FOLUnifier.is_var(term):
            if term in theta:
                return FOLUnifier.apply_subst(theta[term], theta)
            return term
        if isinstance(term, tuple):
            return tuple(FOLUnifier.apply_subst(arg, theta) for arg in term)
        if isinstance(term, list):
            return [FOLUnifier.apply_subst(arg, theta) for arg in term]
        return term

    @staticmethod
    def unify(x, y, theta=None):
        if theta is None:
            theta = {}
        if theta is False:
            return None
        if x == y:
            return theta
        if FOLUnifier.is_var(x):
            return FOLUnifier.unify_var(x, y, theta)
        if FOLUnifier.is_var(y):
            return FOLUnifier.unify_var(y, x, theta)
        if isinstance(x, (tuple, list)) and isinstance(y, (tuple, list)) and len(x) == len(y):
            curr_theta = theta
            for a, b in zip(x, y):
                curr_theta = FOLUnifier.unify(a, b, curr_theta)
                if curr_theta is None:
                    return None
            return curr_theta
        return None

    @staticmethod
    def unify_var(var, x, theta):
        if var in theta:
            return FOLUnifier.unify(theta[var], x, theta)
        if FOLUnifier.is_var(x) and x in theta:
            return FOLUnifier.unify(var, theta[x], theta)
        x_subst = FOLUnifier.apply_subst(x, theta)
        if FOLUnifier.occurs_check(var, x_subst, theta):
            return None
        new_theta = {k: FOLUnifier.apply_subst(v, {var: x_subst}) for k, v in theta.items()}
        new_theta[var] = x_subst
        return new_theta

    @staticmethod
    def occurs_check(var, x, theta):
        if var == x:
            return True
        if FOLUnifier.is_var(x) and x in theta:
            return FOLUnifier.occurs_check(var, theta[x], theta)
        if isinstance(x, (tuple, list)):
            return any(FOLUnifier.occurs_check(var, arg, theta) for arg in x)
        return False
