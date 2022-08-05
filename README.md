# badsql-tools
The badsql-tools library in Python - use badsql from the command line

### badsql-tools docs (for version 2.2 - August 2022)

Create a badsql db by specifying headers

```
$ badsql_mkdb "Hello" "World"
| Hello | World |
| ----- | ----- |
```

Insert a row, specifying line number as first argument

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
