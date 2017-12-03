# <b>Cricbuzz for Python</b>
A Pythonic interface to cricbuzz, with options to get live scores, live commentary and scorecards.

You can find detailed explaination here: <a href = "https://cricstatshub.com/2017/12/03/cricket-api-for-python/">pycricbuzz blog</a>

<b>Instalation</b>

<code>
pip install pycricbuzz
</code>

<b>Features</b>
<ul>
<li>Get upcoming, live and recently concluded matches</li>
<li>Commentary for live matches</li>
<li>Scorecard for live and past matches</li>
</ul>

<b>Basic Usage</b>

Import the pycricbuzz library.

```python
from pycricbuzz import Cricbuzz
c = Cricbuzz()
```

<b>Get all the matches(live,upcoming and recently finished matches)</b>

```python
print c.matches()
```

Each match will have an attribute 'id'. Use this 'id' to get scorecard, brief score and commentary of matches.

<b>Get brief score of a match</b>

```python
print c.livescore(match['id'])
```

<b>Get scorecard of a match</b>

```python
print c.scorecard(match['id'])
```

<b>Get commentary of a match</b>

```python
print c.commentary(match['id'])
```

