# badsql-tools
The badsql-tools library in Python - use badsql from the command line

### Setup

#### Install from pip:

```
pip install badsql-tools
```

### Documentation

for version 4.2

#### Create a badsql db by specifying headers

```
$ badsql_mkdb "Hello" "World"
| Hello | World |
| ----- | ----- |
```

Note: when using `badsql_mkdb`, the previous db is deleted and replaced with the new, empty one

#### Insert a row, specifying line number as first argument

```
$ badsql_insertrow 1 "Foo" "Bar"
| Hello | World |
| ----- | ----- |
| Foo   | Bar   |

$ badsql_insertrow 1 "val1" "val2"
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| Foo   | Bar   |

$ badsql_insertrow 2 "test1" "test2"
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| test1 | test2 |
| Foo   | Bar   |
```

#### Display the db that is currently in memory

```
$ badsql_display
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| test1 | test2 |
| Foo   | Bar   |
```

#### Select rows from the db using a condition

```
$ badsql_select "len(Hello) <= 4"
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| Foo   | Bar   |
```

The optional second parameter `save` defaults to False. If True, the selected db is saved to memory. If False, it is forgotten after displaying.

```
$ badsql_display
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| test1 | test2 |
| Foo   | Bar   |

$ badsql_select "len(Hello) <= 4"
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| Foo   | Bar   |

$ badsql_display
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| test1 | test2 |
| Foo   | Bar   |

$ badsql_select "len(Hello) <= 4" True
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| Foo   | Bar   |

$ badsql_display
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| Foo   | Bar   |
```

#### Remove row from row number

```
$ badsql_display
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| test1 | test2 |
| Foo   | Bar   |

$ badsql_removerow 2
| Hello | World |
| ----- | ----- |
| val1  | val2  |
| Foo   | Bar   |
```
