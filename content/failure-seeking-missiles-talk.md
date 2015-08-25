title: Testing with two failure seeking missiles: fuzzing & property based testing
Category: testing
Tags: python, testing, conferences
Date: 2015-8-5

A EuroPython 2015 talk by [Tom Viner](http://tomviner.co.uk) /
[@tomviner](http://twitter.com/tomviner)

Testing with purely random data on it's own doesn't get you very far. But
two approaches that have been around for a while have new libraries that
help you generate random input, that homes in on failing testcases.

First **[Hypothesis][1]**, a Python implementation and update of the Haskell library
QuickCheck. Known as property based testing, you specify a property of your
code that must hold, and Hypothesis does its best to find a counterexample.
It then shrinks this to find the minimal input that contradicts your
property.

Second, **[American fuzzy lop][2]** (AFL), is a young fuzzing library that's already
achieved an impressive trophy case of bug discoveries. Using
instrumentation and genetic algorithms, it generates test input that
carefully searches out as many code paths as it can find, seeking greater
functional coverage and ultimately locating crashes and hangs that no other
method has found. I'll be showing how with **[Python-AFL][3]** we can apply this
tool to our Python code.

  [1]: https://hypothesis.readthedocs.org/en/latest/
  [2]: http://lcamtuf.coredump.cx/afl/
  [3]: http://jwilk.net/software/python-afl


<iframe width="560" height="315" src="talks/failure-seeking-missiles-talk/" frameborder="0" allowfullscreen></iframe>

<a href="talks/failure-seeking-missiles-talk/" target="_blank">View slides full screen</a>

<iframe width="560" height="315" src="https://www.youtube.com/embed/5kaqOKIqX_4" frameborder="0" allowfullscreen></iframe>

Related links:

* [EuroPython2015 talk page](https://ep2015.europython.eu/conference/talks/testing-with-two-failure-seeking-missiles-fuzzing-and-property-based-testing)
* [Lanyrd page](http://lanyrd.com/2015/europython/sdqgpg/)
