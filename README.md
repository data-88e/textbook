# Data 88: Economic Models Textbook

This is a textbook developed for UC Berkeley's course Data 88: Economic Models. [Data 88](https://d8a-88.github.io) is a generic course listing for Data 8 connector courses.

## Contributing

To contribute to this textbook, clone it locally, make edits to the `/content` directory, and rebuild.

## Building

This Jupyter Book distribution has a custom Makefile which pulls in content from the working repository for the Fall 2019 offering of Data 88. To build the textbook, run the following:

```bash
make textbook
```

This will temporarily clone the repository into the `/content` directory, build the HTML files, and then remove the clone.