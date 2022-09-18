# PCA-GUI

## General
This program is designed to calculate and visualise principle component analysis calculations. 

The input is excel spredsheet saved in xlsx or csv format. 

* Headers for the columns is not required. To specifie the type add column 'Type' and for colour column named 'Colour'. The colour name must be string. See https://matplotlib.org/stable/gallery/color/named_colors.html for colour names. 


## Execution

Create a bash script where path to PCA-gui.py is specified and executed by python3. Then convert it to executable.  

```
export main=path/to/pca-gui/PCA-gui.py

python3 $main 
```

