# LIBRARY / MODULE / PUSTAKA

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit import session_state as ss

from functions import *
from warnings import simplefilter

simplefilter(action= "ignore", category= FutureWarning)

# PAGE CONFIG

st.set_page_config(
    page_title= "App", layout= "wide",
    page_icon= "globe", initial_sidebar_state= "expanded"
)

# hide menu, header, and footer
st.markdown(
    """<style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .st-emotion-cache-z5fcl4 {padding-top: 1rem;}
    </style>""",
    unsafe_allow_html= True
)

## CSS on style.css
with open("./css/style.css") as file:
    st.markdown(
        "<style>{}</style>".format(file.read()), unsafe_allow_html= True
    )

class MyApp():
    """Class dari MyApp

    Parameters
    ----------
    message : bool, default= False
        Jika False, maka pesan error tidak akan ditampilkan dalam Webpage Sistem.
        Jika True, maka akan menampilkan pesan dalam Webpage Sistem yang dapat
        dianalisis.

    Attributes
    ----------
    message : bool
        Tampilkan pesan error pada Webpage Sistem atau tidak.

    pathdata : str
        Path (jalur) data disimpan dalam lokal direktori.

    menu_ : list
        Daftar menu yang akan ditampilkan dalam Webpage Sistem.

    icons_ : list
        Daftar icon menu untuk setiap menu yang ditampilkan dalam Webpage.
    """

    def __init__(self, message= False):
        self.message = message
        self.pathdata = "./data/dataframe"
        self.menu_ = [
            "Beranda", "Data Penelitian"
        ]
        self.icons_ = [
            "house", "database"
        ]

    def _navigation(self):
        """Navigasi sistem
        
        Returns
        -------
        selected : string
            Selected menu.
        """
        with st.sidebar:
            selected = option_menu(
                menu_title= "", options= self.menu_, icons= self.icons_,
                styles= {
                    "container": {
                        "padding": "0 !important",
                        "background-color": "#E6E6EA"
                    },
                    "icon": {"color": "#020122", "font-size": "18px"},
                    "nav-link": {
                        "font-size": "16px", "text-align": "left",
                        "margin": "0px", "color": "#020122"
                    },
                    "nav-link-selected": {"background-color": "#F4F4F8"}
                }
            )

            ms_60()
            show_caption("Copyright © 2024 | Ach. Choirul Umam", size= 5)
        return selected
    
    def _exceptionMessage(self, e):
        """Tampilkan pesan galat

        Parameters
        ----------
        e : exception object
            Obyek exception yang tersimpan.
        """
        ms_20()
        with ml_center():
            st.error("Terjadi masalah...")
            if self.message:
                st.exception(e) # tampilkan keterangan galat

    def _pageBeranda(self):
        """Tab beranda
        
        Halaman ini akan menampilkan judul penelitian dan abstrak dari proyek.
        """
        try:
            ms_20()
            show_text(
                "Integrasi Sistem Pakar Rule-Based untuk Diagnosis Penyakit \
                pada Ibu Hamil", size= 2
            )
            show_caption(
                "Studi Kasus: Klinik Utama Sukma Wijaya Kabupaten Sampang",
                size= 2, division= True
            )

            ms_40()
            with ml_center():
                with open("./assets/abstract.txt", "r") as file:
                    abstract = file.read()
                show_paragraf(abstract)
        except Exception as e:
            self._exceptionMessage(e)

    def _pageDataset(self):
        """Tab dataset
        
        Halaman ini akan menampilkan data penelitian.
        """
        try:
            ms_20()
            show_text("Data Penelitian", division= True)

            df = get_csv("./data/dataframe/data.csv")
            detail_data = df.iloc[:, :3]
            label_data = df.iloc[:, -1]
            sample_data = pd.concat([detail_data, label_data], axis= 1)
            with st.expander("Dataset"):
                st.dataframe(
                    sample_data,
                    use_container_width= True, hide_index= True
                )

            ms_20()
            show_caption("Detail Data:")

            with open("./assets/data-detail.txt", "r") as file:
                detail = file.read()
            show_paragraf(detail)

            ms_20()
            left, right = ml_split()
            with left:
                show_caption("Daftar Gejala:")
                gejala_data = df.iloc[:, 3:-1].columns
                for no, gejala in enumerate(gejala_data):
                    st.write(f"{no + 1}. {gejala}")
            with right:
                show_caption("Jenis Penyakit:")
                penyakit_data = label_data.unique()
                for no, penyakit in enumerate(penyakit_data):
                    st.write(f"{no + 1}. {penyakit}")
        except Exception as e:
            self._exceptionMessage(e)

    def main(self):
        """Main program
        
        Setting session page diatur disini dan konfigurasi setiap halaman
        dipanggil disini.
        """
        with st.container():
            selected = self._navigation()

            if selected == self.menu_[0]:
                self._pageBeranda()
            elif selected == self.menu_[1]:
                self._pageDataset()

if __name__ == "__main__":
    app = MyApp(message= True)
    app.main()