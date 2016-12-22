# <b>Cricbuzz for Python</b>
A Pythonic interface to cricbuzz, with options to get live scores, live commentary and scorecards.

<b>Instalation</b>

<code>
pip install cricbuzz
</code>

<b>Features</b>
<ul>
<li>Get upcoming, live and recently concluded matches</li>
<li>Commentary for live matches</li>
<li>Scorecard for live and past matches</li>
</ul>

<b>Basic Usage</b>

Import the cricbuzz library.

```python
from cricbuzz import Cricbuzz
c = Cricbuzz()
```

<b>Get all the matches(live,upcoming and recently finished matches)</b>

```python
print c.matches()
```

The output is a json response containing all the matches. Each match will have an attribute 'id'. Use this 'id' to get scorecard, brief score and commentary of matches.

<b>Get scorecard of a match</b>

```python
print c.scorecard(match['id'])
```

<b>Get commentary of a match</b>

```python
print c.commentary(match['id'])
```

<b>Note</b>: All the responses will be in json format. Analyse the json response correctly. 
