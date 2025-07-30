# textbook
Textbook for Data 88E: Economic Models at UC Berkeley

Content is stored in the content folder. Order of textbook can be changed from _toc.yml file.

To build the textbook, run
```
jupyter-book build .
```

This will output HTML to `_build/html`, which can be copied to `docs` in order to be served on GitHub Pages.


# NOTE: Chapter 4 - shifts.ipynb
The figures generated in this notebook are Plotly-based javascript-enbedded html files. The script portion of each figX.html file messes with the Jupyter Books ability to render the Latex symbols. You can see I commented out the creation of the html files(e.g fig1.html, etc). Then I went into each html file and commented out the script section. Then went back to the notebook and ran the cell to display the figure. There has to be an easier way!
