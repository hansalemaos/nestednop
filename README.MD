## Library to update nested dicts and lists

You can change the values in a flattened version of your dict that NestedNop creates for you. After you editing, NestedNop updates the original structure automatically.

```python
pip install nestednop 
```

```python
    dictoriginal=data={'level1': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}},
    'level2': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 9, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 5},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 13},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 20}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}}}

    from nestednop import NestedNop
    nest=NestedNop(dictoriginal)
    for key, item in nest.iterable_flat.items():
        if item['get_value']() == 4 and key[-1] == 'col3':
            item['set_value'](400000000000000)

    updatediter = nest.get_updated_iterable()


    updatediter
    {'level1': {'t1': {'s1': {'col1': 5,
        'col2': 4,
        'col3': 400000000000000,
        'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 8},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9}},
      't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 8},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9}},
      't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
       's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
       's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
       's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}},
     'level2': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 9, 'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 5},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 13},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 20}},
      't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 8},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9}},
      't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
       's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
       's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
       's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}}}
```
