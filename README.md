# stylesage-test1
Job interview test for StyleSage

Small app that takes an integer and return a string representation of that integer with commas separating groups of 3 digits.

```
In [1]: from translate import translate

In [2]: translate(1234)
Out[2]: '1,234'

In [3]: translate(123456789)
Out[3]: '123,456,789'
```

### Tests

Install pytest: `pip install pytest`

Run tests: `pytest tests.py`
