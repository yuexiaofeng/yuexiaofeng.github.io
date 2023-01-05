---
layout: post
title: "Python's Implicit Booleaness"
author: "Xiaofeng"
excerpt_separator: <!--more-->
tags: [Tech]
---

> Beautiful is better<!--more--> than ugly.
> 
> Explicit is better than implicit.
> 
> ...

If that isn't the quote from the famous `The Zen of Python`, by Tim Peters. You can see the full commandments if you type:

```text
>>> import this
```

in any Python command interpreter.

As much as I want to believe these rules are coherent, they can be conflicting with each other under circumstances. This implicit booleaness / emptiness check would be a prime example: beauty clearly outweighs explicitness here.

## Context

In full disclosure, I have played with this quite some time ago but recently encountered again, so I decided to ramble a bit in a post. Here it goes.

Say if you want to check if an abject is depleted/empty or true/false to trigger some logic, it'd be naturally to do any of the following:

```python
#!/usr/bin/env python3

# An object that could be a container like list, 
# or just an object instantiated from your own class definition etc
if len(obj) == 0:
    # Do something when the obj is empty
    pass

if obj is None:
    # Do something for null
    pass

while len(obj) > 0:
    # If the length is greater than 0, which implies True
    pass

while len(obj):
    # Implies len(obj) is not 0, which is a broader case of len(obj) > 0.
    # This reminds me of the good times of ancient C, we'd actually -
    # use 0 to represent False cuz the lack of good boolean support
    pass

while not obj.is_empty():
    # If such method/api is provided
    pass
```

But a more Pythonic and elegant way is just to do:

```python
if not obj:
    # Do something if obj is empty/False/None
    pass

while obj:
    # Continue doing stuff, while obj is not_empty/True:
    pass
```

Python's built-in objects would have baked-in supports for this already. According to its documentation[^fn1], here are most of the built-in objects considered false:

1. constants defined to be false: None and False.
2. zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
3. empty sequences and collections: '', (), [], {}, set(), range(0)

But what if you want to write a class/collection of your own, and would like this groovy feature too, cuz y'all wanna hang out with the cool kids right?

## The Experiments

A helper to get started so we don't keep writing print statements:

```python
def check_bool(obj):
    """
    Emptiness should be equivalent to False
    """
    if obj:
        print('object is True or not empty, and bool(obj) is: ', bool(obj))
    else:
        # aka `not obj`. 
        print('object is False or empty!! bool(obj) is: ', bool(obj))
    print()
```

Let's begin by a dummy class without any actual implementation in it:

```python
class Dummy:
    pass
```

and do:

```python
obj = Dummy()
check_bool(obj)
```

This turned out to be True aka not empty, which is a bit counter-intuitive. That's cuz when it's evaluated for booleaness, Python would do `bool(obj)` which then triggers the built-in magic method `__bool__()` if available. So if we do the following instead:

```python
class BoolDummy(Dummy):
    def __bool__(self):
        return False


obj = BoolDummy()

# it will be False now
check_bool(obj)
```

Then this new dummy object would now be evaluated as false.

But just having `__bool__()` return True/False outright seems a bit arbitrary. We could take a step further and tie it to the emptiness, as shown in the homemade list container/collection example below (obviously there could be other boolean check use cases as well):

```python
class ContainerBase:
    """A copycat of Stack/List"""

    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        self.container.pop()

class HomemadeContainer(ContainerBase):
    def __init__(self):
        super().__init__()

    def __bool__(self):
        return len(self.container) != 0
```

Now it'll behave just like what a built-in list would do, in terms of emptiness/False:

```python
obj = HomemadeContainer()

# False since it's empty to begin with
check_bool(obj)

obj.push('a')

# True now that obj is not "empty"
check_bool(obj)

```

Alternatively, we could also resort to another implicit check for `len(obj)` that achieves the same effect, which means overriding Python's magic method of `__len__()`, here's an example:

```python
class AltHomemadeContainer(ContainerBase):
    def __init__(self):
        super().__init__()
    
    def __len__(self):
        return len(self.container)

obj = AltHomemadeContainer()

assert len(obj) == 0

# False since it's empty to begin with
check_bool(obj)

obj.push('a')

# should be 1 now
assert len(obj) == 1

# True now that obj is not "empty"
check_bool(obj)
```

Now we can totes do shorthands like `if obj` with it! Not half bad eh?

While you can get away with overriding either `__bool__()` or `__len__()`, there's absolutely no harm in doing both (I'd argue `len` is actually quite useful). Why not get the best of both worlds when you can! :D

---
[^fn1]: Python [doc](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) on Truth Value Testing
