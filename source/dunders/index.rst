.. _dunders-tutorial:

=======
Dunders
=======

Par Marc Friedli [#mf]_

Introduction
============

Le mot dunder est un raccourci de *Double UNDERscore* et représente toutes les méthodes Python qui commencent et finissent par un double underscore (par ex. ``__init__()``).

Les dunders sont des méthodes très puissantes et régulièrement utilisées en python. Un dunder est toujours une méthode privée appartenant à une classe. La particularité de ces méthodes et qu'elles ne sont jamais directement appelées mais toujours implicitement ou explicitement

par exemple :

.. code-block:: python3

    x = MyClass() #fera appel au dunder __init__() de la classe MyClass
    str(x) #fera appel au dunder __str__() de la classe MyClass
    str(12) #fera appel au dunder __str__() de la classe Integer


.. todo:: Un peu imprécis car il n'y a pas que des méthodes. ``__name__`` ou ``__file__``


Les dunders ont des méthodes raccourci qui vont directement les appeler (autre raison pour laquelle on utilise régulièrement les dunders sans s'en rendre compte) :

.. code-block:: pycon

    >>> 4 + 5
    9


fera appel au dunder ``__add__()``

.. de quelle classe? puisque c'est une méthode.

Ou bien :

.. code-block:: python3

    str("I'm a text")


fera appel au dunder ``__str__()`` de :py:class:`str`.

.. obtenir la chaine de caractère d'une chaine de caractère, n'est pas le meilleur exemple.

La grande puissance des dunders est leur universalité. En effet, Python a été programmé de manière à ce qu'une opération soit toujours relié au même *dunder*.

Par exemple, dans beaucoup de langages, si on veut connaitre la taille d'un truc, il faut d'abord savoir de quoi on parle (un tableau, une liste, un string etc.) avant de faire appel à la méthode appropriée. Dans python, on utilise toujours le dunder __len__() :


.. literalinclude:: someclass.py

.. todo:: Cet exemple n'est pas représentatif de l'usage de ``len``.

Voir: `Python and the Principle of Least Astonishment <http://lucumr.pocoo.org/2011/7/9/python-and-pola/>`_

Une autre grande utilisation des dunders consiste à les surcharger de manière à les personalisé.

Exemples
========


.. literalinclude:: main.py


Différence entre :py:class:`str` et :py:func:`repr`
---------------------------------------------------

Les deux servent à afficher l'objets mais pas de la même manière :

:str: se veut d'être lisible, il donne les informations qu'un utilisateur veut savoir et non le programme. Elle est ambigu et permet donc facilement le cast.

:repr: se veut au contraire non ambigu. Il doit représenter l'objet tel qu'il est réellement.

De base, quand on chercher à afficher un objet, à moins que la méthode ``__str__()`` soit redéfinie, c'est la méthode repr qui sera appelée.

.. code-block:: python3

    print(str(3)==str("3")) # return True car str est ambigu
    print(repr(3)==repr("3")) # return False car non-ambigu (Int != String)

.. ça vous parait clair?


Idéalement, il faudrait toujours redéfinir la méthode ``__repr__()`` et redéfinir ``__str__()`` uniquement si on a besoin de l'ambiguïté.

Conclusion
==========

Il existe beaucoup de dunders. Il faut puiser dans la doc afin de connaitre ceux dont on a l'usage et savoir quand ils sont utilisés.
Ce sont de puissants outils de Python qui permettent de facilement spécialiser le comportement d'un objet.

Documentation officielle
-------------------------

https://docs.python.org/3/reference/datamodel.html

Bibliographie
=============

- The Python Data model, extrait de Fluent Python
- http://sametmax.com/le-guide-ultime-et-definitif-sur-la-programmation-orientee-objet-en-python-a-lusage-des-debutants-qui-sont-rassures-par-les-textes-detailles-qui-prennent-le-temps-de-tout-expliquer-partie-6/
- http://www.diveintopython3.net/special-method-names.html

.. [#mf] <marc.friedli@he-arc.ch>
