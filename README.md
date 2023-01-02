# UserInputGetter

This package provides an interface, and several implementations, of classes which continuously request command-line user input until a valid response has been attained, and parse the output as a desired type.

The input is checked for validity (for example if a date is expected, the input must match one of several supported date regular expressions), and optionally a user may specified an iterable of supported options, in which case the user input must be parsable as one of the specified options

The abstract base class is called `UserInputGetter`, and the following implementations are provided:

## Implementations

* `IntegerInputGetter`
* `CaseInsensitiveStringInputGetter`
* `DateInputGetter`
