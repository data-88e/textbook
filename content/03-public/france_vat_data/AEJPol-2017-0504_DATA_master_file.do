********************************************************
*Title: AEJPol-2017-0504_DATA_master_file.do
*Date: 5 May, 2018
*Author: Dorian Carloni
********************************************************

global main "C:/Users/doria/Dropbox/AEJ EP/Files for publication/Do files"

**************
****Data******
**************

do "$main/AEJPol-2017-0504_DATA_amadeus_data.do" 
do "$main/AEJPol-2017-0504_DATA_price_data.do" 
do "$main/AEJPol-2017-0504_DATA_eec_data.do"     

**************
****Tables****
**************

*Main text
do "$main/AEJPol-2017-0504_DATA_table_1.do"  
do "$main/AEJPol-2017-0504_DATA_table_2.do"  

**************
****Figures***
**************

*Main text
do "$main/AEJPol-2017-0504_DATA_figure_1.do"
do "$main/AEJPol-2017-0504_DATA_figure_2.do"
do "$main/AEJPol-2017-0504_DATA_figure_3.do"

