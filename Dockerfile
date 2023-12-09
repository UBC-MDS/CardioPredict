FROM quay.io/jupyter/minimal-notebook:2023-11-19 

RUN  conda install -y \
    altair=5.1.2 \
    matplotlib=3.8.0 \
    nb_conda_kernels=2.3.1 \
    pandas=2.1.1 \
    scikit-learn=1.3.2 \
    numpy=1.26.0 \
    pytest=7.4.3 \
    click=8.1.7 \
    jupyter-book=0.15.1 \
    make=4.2.1

RUN pip install imblearn==0.0 
