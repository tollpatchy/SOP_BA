FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    preview-latex-style \ 
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-lang-german \
    python3 python3-pip python3-tk \
    language-pack-de-base language-pack-de locales \
    xpdf

ENV LANG de_DE.UTF-8

RUN useradd -d /home/sopautor -m -s /bin/bash sopautor

ADD [".", "/home/sopautor/"]

RUN chown -R sopautor:sopautor /home/sopautor
RUN pip3 install -r /home/sopautor/requirements.txt

USER sopautor

WORKDIR /home/sopautor/

ENTRYPOINT ["/home/sopautor/SOP_Gui.sh"] 
