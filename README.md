## Overview
This package provides a way to ask the user's home county by city. 
It reads the provided city and attempts to match with the closest county.

## Usage
The package has a single file, counties.yml. To use it you should first include the question:
```yaml
include:
  - docassemble.CountySelect:counties.yml
```
Then, you can request the variable `county` and the question will be provided. 
Since there are no mandatory blocks, you should make sure to order the code appropriately.
For example, you can say:
```yaml:
code: |
  need(some_other_variable, county)
```
You can also set the `city` value to provide a default city. 