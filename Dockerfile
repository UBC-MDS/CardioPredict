FROM quay.io/jupyter/minimal-notebook:2023-11-19 

RUN  conda install -y \
    altair=5.1.2 \
    matplotlib=3.8.0 \
    nb_conda_kernels=2.3.1 \
    pandas=2.1.1 \
    scikit-learn=1.3.1 \
    numpy=1.26.0 \
    pytest=7.4.3 
    #vega_datasets= 0.9.0 \
    #vegafusion=1.4.3 \
    #vegafusion-jupyter=1.4.3 \
    #vegafusion-python-embed=1.4.3 \
    #vl-convert-python=1.1.0 

RUN pip install imblearn==0.0 
