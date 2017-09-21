Title: pytest and I, time for a sprint?
Category: testing
Tags: python, testing, pytest
Date: 2016-2-20

Pytest is having a [sprint](http://pytest.org/latest/announce/sprint2016.html) this summer, in Freiburg, Germany. I've signed up myself, and so I thought I'd explain what attracted me to pytest and why you should consider [donating](https://www.indiegogo.com/projects/python-testing-sprint-mid-2016#/).

As someone who started their career coding Microsoft ASP it was a revelation to discover the Python programming language. I found the power at my fingertips greatly expanded. It was a similar feeling when I later discovered pytest. Compared to Python's built-in test framework, `unittest`, I found the barrier to getting started writing tests greatly reduced. And I started to really get in to TDD.

The top three features of pytest that attracted me were:

- your first test can be just 2 or 3 lines. No imports, classes or `self` needed - *no API is the best API*
- pytest fixtures are a concise method of pre-test arrangement, which allow sharing setup code between tests
- asserts are simple and intuitive. `unittest` really makes you do unnecessary extra work here with its `self.assertLess`, `assertGreaterEqual` etc etc

I explained some of these thoughts in my PyConUK conference talk: [Exploring unit-testing: unittest v pytest: FIGHT!](http://tomviner.co.uk/exploring-unit-testing-unittest-v-pytest-fight.html)

I first got involved in contributing to pytest, while writing another [conference talk, about the Hypothesis library](http://tomviner.co.uk/testing-with-two-failure-seeking-missiles-fuzzing-property-based-testing.html). I found a bug in the *assertion rewriting* system, which shows the value of variables involved in failed assert statements. It's very clever, it works by modifying the AST (abstract syntax tree) of your test code. It inserts a bunch of extra statements to break down the expressions you're asserting about, and makes a note of each value involved. But for developers working on these pytest internals, it's really hard to visualise what's going on with this rewritten AST, so I wrote [a plugin for viewing the modified AST back as Python source](https://github.com/tomviner/pytest-ast-back-to-python).

I got involved as a mentor in [adopt pytest month](http://pytest.org/latest/adopt.html) last April. It was really rewarding to help out [`bidict`](https://bidict.readthedocs.org/en/master/). Working with its author, we refactored and expanded the tests from solely consisting of doctests to taking advantage pytest's features. We also [incorporated](https://hypothesis.readthedocs.org/en/release/endorsements.html#id5) [Hypothesis](https://hypothesis.readthedocs.org/en/release/) for property based testing.

Now I've been using pytest on dozens of projects at work and home, and I've contributed to a number of different pytest tickets, I thought a sprint would be a great opportunity to meet everyone and get more involved. Especially as, in my experience, the pytest core devs are always so receptive and appreciative of contributions, it really helps one to feel like newcomers are welcome.

For many of us, pytest and tox are the common packages we always end up installing in all our projects, if this applies to you or your company, please consider [donating](https://www.indiegogo.com/projects/python-testing-sprint-mid-2016#/) to help improve these tools even further.