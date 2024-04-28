# LIBRARY / MODULE / PUSTAKA

import streamlit as st

import os

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, classification_report

from warnings import simplefilter

simplefilter(action= "ignore", category= FutureWarning)

# DEFAULT FUNCTIONS

"""Make Space

Fungsi-fungsi untuk membuat jarak pada webpage menggunakan margin space dengan
ukuran yang bervariatif.
"""

def ms_20():
    st.markdown("<div class= \"ms-20\"></div>", unsafe_allow_html= True)

def ms_40():
    st.markdown("<div class= \"ms-40\"></div>", unsafe_allow_html= True)

def ms_60():
    st.markdown("<div class= \"ms-60\"></div>", unsafe_allow_html= True)

def ms_80():
    st.markdown("<div class= \"ms-80\"></div>", unsafe_allow_html= True)

"""Make Layout

Fungsi-fungsi untuk layouting webpage menggunakan fungsi columns() dari
Streamlit.

Returns
-------
self : object containers
    Mengembalikan layout container.
"""

def ml_center():
    left, center, right = st.columns([.3, 2.5, .3])
    return center

def ml_split():
    left, center, right = st.columns([1, .1, 1])
    return left, right

def ml_left():
    left, center, right = st.columns([2, .1, 1])
    return left, right

def ml_right():
    left, center, right = st.columns([1, .1, 2])
    return left, right

"""Cetak text

Fungsi-fungsi untuk menampilkan teks dengan berbagai gaya menggunakan method
dari Streamlit seperti title(), write(), dan caption().

Parameters
----------
text : str
    Teks yang ingin ditampilkan dalam halaman.

size : int
    Ukuran Heading untuk teks yang akan ditampilkan.

division : bool
    Kondisi yang menyatakan penambahan garis divisi teks ditampilkan.
"""

def show_title(text, division= False):
    st.title(text)
    if division:
        st.markdown("---")

def show_text(text, size= 3, division= False):
    heading = "#" if size == 1 else (
        "##" if size == 2 else (
            "###" if size == 3 else (
                "####" if size == 4 else "#####"
            )
        )
    )

    st.write(f"{heading} {text}")
    if division:
        st.markdown("---")

def show_caption(text, size= 3, division= False):
    heading = "#" if size == 1 else (
        "##" if size == 2 else (
            "###" if size == 3 else (
                "####" if size == 4 else "#####"
            )
        )
    )

    st.caption(f"{heading} {text}")
    if division:
        st.markdown("---")

def show_paragraf(text):
    st.markdown(
        f"<div class= \"paragraph\">{text}</div>", unsafe_allow_html= True
    )

"""Load file

Fungsi-fungsi untuk membaca file dalam lokal direktori.

Parameters
----------
filepath : str
    Jalur tempat data tersedia di lokal direktori.

Returns
-------
self : object DataFrame or str
    Obyek dengan informasi yang berhasil diekstrak.
"""

def get_csv(filepath):
    return pd.read_csv(filepath)

def get_excel(filepath):
    return pd.read_excel(filepath)

# ----------

def mk_dir(dirpath):
    """Buat folder
    
    Fungsi ini akan memeriksa path folder yang diberikan. Jika tidak ada
    folder sesuai path yang dimaksud, maka folder akan dibuat.

    Parameters
    ----------
    dirpath : str
        Jalur tempat folder akan dibuat.
    """
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

# CUSTOM FUNCTIONS
        
def train_model(
        X, y, test_size= None, train_size= None, random_state= None,
        shuffle: bool= True
    ):
    """Train Model

    Fungsi ini akan melatih model categorical naive bayes.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Vektor pelatihan di mana n_samples adalah jumlah sampel dan n_features
        adalah jumlah fitur. Di sini, setiap fitur X diasumsikan berasal dari
        distribusi kategori yang berbeda. Diasumsikan lebih lanjut bahwa semua
        kategori dari setiap fitur diawali oleh angka 0, ..., n-1, dimana n
        mengacu pada jumlah total kategori untuk fitur yang diberikan.

    y : array-like of shape (n_samples)
        Nilai target/label.

    test_size : float or int, default= None
        Jika float, harus antara 0,0 dan 1,0 dan merepresentasikan proporsi
        dari dataset yang akan disertakan dalam pemisahan test. Jika int,
        representasi nilai absolut dari sampel test. Jika None, nilainya
        ditetapkan sebagai pelengkap ukuran train. Jika train_size juga
        None, maka akan di set ke 0,25.

    train_size : float or int, default= None
        Jika float, harus antara 0,0 dan 1,0 dan merepresentasikan proporsi
        dari dataset yang akan disertakan dalam pemisahan train. Jika int,
        representasi nilai absolut dari sampel train. Jika None, nilainya
        secara otomatis diatur ke pelengkap ukuran test.
    
    random_state : int, RandomState instance or None, default= None
        Mengontrol pengacakan yang diterapkan pada data sebelum menerapkan
        pemisahan. Berikan nilai int untuk keluaran yang dapat
        direproduksi di beberapa panggilan fungsi.

    shuffle : bool, default= True
        Jika True, data akan di acak sebelum pemisahan. Jika False, maka
        sebaliknya.

    Returns
    -------
    model : object
        Mengembalikan model yang telah di latih.

    X_test : {array-like, sparse matrix} of shape (n_samples, n_features)
        Vektor fitur data test hasil dari pemisahan data.

    y_test : array-like of shape (n_samples)
        Nilai target/label dari data test.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size= test_size, train_size= train_size,
        random_state= random_state, shuffle= shuffle
    )

    model = CategoricalNB()
    model.fit(X_train, y_train)

    return model, X_test, y_test

def score_model(y_true, y_pred):
    """Menghitung skor model

    Parameters
    ----------
    y_test : array-like of shape (n_samples)
        Nilai target/label dari data aktual.

    y_pred : array-like of shape (n_samples)
        Nilai target/label hasil prediksi.

    Returns
    -------
    self : float
        Nilai skor model yang dihitung menggunakan accuracy_score()
    """
    return accuracy_score(y_true= y_true, y_pred= y_pred)

def clf_report(y_true, y_pred):
    """
    """
    cr = classification_report(y_true, y_pred, output_dict= True)
    return pd.DataFrame(cr).transpose()