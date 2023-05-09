import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.header(":green[Aplikasi Pengolahan Data Tunggal dalam Statistika]")
    
    # Memasukkan data manual
    st.header("Masukkan Data!:point_right::point_left:")
    rows = st.number_input("Jumlah Baris Data:", min_value=1, value=1)
    cols = st.number_input("Jumlah Kolom Data, max 1 karena perhitungan data tunggal:", min_value=1, value=1)
    
    data = []
    for i in range (rows):
        row = []
        for j in range(cols):
            value = st.number_input(f"Data Baris {i+1}, Kolom {1}", value=0.00)
            row.append(value)
        data.append(row)
        
    df = pd.DataFrame(data)
    st.write("Data yang Dimasukkan:")
    st.write(df)
    
 # Menghitung nilai rata-rata, median, range, simpangan rata-rata, ragam, dan simpangan baku
    st.header("Hasil Pengolahan Data:memo:")
    st.write("Rata-rata: ", np.mean(data))
    st.write("Median: ", np.median(data))
    st.write("Ragam/Variasi: ", np.var(data))
    st.write("Simpangan Rata-rata: ", np.mean(np.abs(data - np.mean(data))))
    st.write("Jangkauan/Range: ", np.max(data)-np.min(data))
    st.write("Simpangan Baku/Standar Deviasi: ", np.std(data))
             
             
             
             
             
             
             
             
             
             
             
             
             
             
    
if __name__ == '__main__':
    main()