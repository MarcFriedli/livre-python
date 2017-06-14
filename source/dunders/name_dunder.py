"""Module d'exemple utilisant le dunder __name__."""


def some_function():
    """Affiche une simple phrase."""
    print("I'm a script")


if __name__ == __main__:
    """
        some_function ne s'exécute que si on lance directement le module
        et pas si on l'importe.
    """
    some_function()
